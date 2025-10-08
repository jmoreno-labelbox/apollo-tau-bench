from tau_bench.types import Action, Task
TASKS = [

    Task(
        annotator="0",
        user_id="V4_Task_001",
        instruction=(
            "Handle the closure of completed checklist items for lily.zhang@example.com (start 2024-08-26), then proceed to send and label a one-week checklist reminder with cutoff 2024-09-02."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_6", "due_date_lte": "2024-09-02"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "checklist_reminder", "to_emails": ["lily.zhang@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_6","attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",kwargs={"candidate_id": "cand_6", "subject": "Pending Onboarding Tasks","add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02", "subject": "Pending Onboarding Tasks","item_ids": []}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_6", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_002",
        instruction=(
            "Coordinate the finalization of the allocation for raj.patel@example.com (start 2024-09-02) in accordance with policy: allocate the first available inventory, record the allocation on the request, generate an allocation receipt, and email the employee ‘Asset Allocation – Raj Patel’ with the receipt attached."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["raj.patel@example.com"],"subject": "Asset Allocation – Raj Patel","candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/allocation_receipt.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_5","status": "Completed","email_message_id": "msg_15"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_003",
        instruction=(
            "Handle the finalization of equipment provisioning for emma.thompson@example.com (beginning 2024-08-05) following the Equipment Provisioning policy: assemble the request artifact, reach out to IT via email using 'Asset Provisioning – Emma Thompson' and ensure the inclusion of the required 'Asset-Request' label; log the email ID and mark the request as Sent; assign the first available inventory and document the allocation; produce an allocation receipt and send a confirmation with the receipt to the employee."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Emma Thompson", "candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteOnboardingFile",kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/allocation_receipt.json", "mime_type": "application/json","payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["emma.thompson@example.com"], "subject": "Asset Allocation – Emma Thompson", "candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/allocation_receipt.json"]}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_004",
        instruction=(
            "Coordinate day-1 access checks for lily.zhang@example.com (starting 2024-08-26) with results: Email=pass, SSO=fail, Slack=pass, GitHub=pass; then send a day-1 orientation invitation and inform IT about any access discrepancies."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_6", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "fail"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["lily.zhang@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_6"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_6","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_6"}),
        ],
        outputs=['"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_005",
        instruction=(
            "Manage the existing asset request associated with emma.thompson@example.com (start 2024-08-05). Dispatch the 'Asset Provisioning – Emma Thompson' email and record its message id with the request, label it with 'Asset-Request', assign a suitable asset, save to /onboarding/Jane_Smith/allocation_receipt.json, and deliver 'Asset Allocation – Emma Thompson' with the receipt included."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Emma Thompson", "candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteOnboardingFile",kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/allocation_receipt.json", "mime_type": "application/json","payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["emma.thompson@example.com"], "subject": "Asset Allocation – Emma Thompson", "candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/allocation_receipt.json"]}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_006",
        instruction=(
            "Customize and distribute the onboarding packet for william.davis@example.com (start 2024-07-29) complete with policy/benefits, followed by sending and tagging a checklist reminder (cutoff 2024-08-05)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile",kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md", "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "onboarding", "to_emails": ["william.davis@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_3","attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Peter_Jones/welcome_Peter_Jones.md"]}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_3", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_3", "status": "Pending", "due_date_lte": "2024-08-05"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "checklist_reminder", "to_emails": ["william.davis@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",kwargs={"candidate_id": "cand_3", "subject": "Pending Onboarding Tasks","add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_3", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_007",
        instruction=(
            "Handle the distribution of day-1 orientation and manager-intro invitations for sofia.martinez@example.com (start 2024-08-12) and log the timestamps for both invites."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "orientation_invite", "to_emails": ["sofia.martinez@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_4"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "manager_intro", "to_emails": ["sofia.martinez@example.com", "daniel.lee@example.com"], "subject": "Manager Intro","candidate_id": "cand_4"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_4", "orientation_invite_ts": "2025-09-01T00:00:00Z","manager_intro_invite_ts": "2025-09-01T00:00:00Z"})
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
    annotator="0",
    user_id="V4_Task_008",
        instruction=(
            "Ensure day-1 access is verified for sofia.martinez@example.com (start 2024-08-12), subsequently dispatch the 'Welcome to the Team' packet (attach Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown) and document the welcome email id."
        ),
    actions=[
        Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
        Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_4", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "pass"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
        Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
        Action(name="RenderOnboardingWelcome", kwargs={"candidate_id": "cand_4", "candidate_name": "Sofia Martinez", "role_title": "UX Designer", "start_date": "2024-08-12"}),
        Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md","mime_type": "text/markdown"}),
        Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["sofia.martinez@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_4","attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md"]}),
        Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_4", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_4"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
),
 Task(
        annotator="0",
        user_id="V4_Task_009",
        instruction=(
            "Confirm day‑1 access for jordan.williams@example.com (start 2024‑08‑19); dispatch 'Day‑1 Orientation' and 'Welcome to the Team' (policy PDFs + personalized markdown); subsequently manage the one‑week checklist follow‑up (cutoff 2024‑08‑26): deliver 'Pending Onboarding Tasks' labeled 'Onboarding‑Reminder' with pending_tasks.md, document the welcome message id, assign the follow‑up timestamp, and indicate the reminded items. Deliver the 'Day-1 Orientation' invite, provide the 'Welcome to the Team' packet (Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown), and finalize the one‑week checklist follow‑up: distribute 'Pending Onboarding Tasks' (cutoff 2024-08-26) labeled 'Onboarding-Reminder' with pending_tasks.md; note the welcome email message id and onboarding status, assign the checklist follow-up timestamp, and tag the reminded items with the email's message id."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_5", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "pass"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["jordan.williams@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_5"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md","mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["jordan.williams@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_5","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5","status": "Pending","due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["jordan.williams@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_5","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_16", "checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_13", "item_14"],"reminder_email_message_id": "msg_17","updated_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_010",
        instruction=(
            "Confirm day-1 access for raj.patel@example.com (start 2024-09-02), dispatch an orientation invite, then finalize provisioning by sending and labeling the request, allocating inventory, and responding to the provisioning thread to acknowledge."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_7","checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "pass"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite", "to_emails": ["raj.patel@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_7", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5", "candidate_id": "cand_7", "status": "Requested"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Raj Patel", "candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_5", "status": "Sent","candidate_id": "cand_7", "subject": "Asset Provisioning – Raj Patel",}),
            Action(name="ModifyEmailLabels", kwargs={"candidate_id": "cand_7", "subject": "Asset Provisioning – Raj Patel","add_names": ["Asset-Request"]}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5", }),
            Action(name="ReplyToEmailThread", kwargs={"candidate_id": "cand_7", "subject": "Asset Provisioning – Raj Patel",  "task": "acknowledge"})
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
 Task(
    annotator="0",
    user_id="V4_Task_011",
        instruction=(
            "Handle provisioning for jordan.williams@example.com (start 2024-08-19): send an email to IT with the subject 'Asset Provisioning – Jordan Williams' tagged 'Asset-Request' and attach /onboarding/Alex_Thompson/asset_request.json; mark asset_req_4 as Sent using the email's message id; assign the first available asset; save the receipt in /onboarding/Alex_Thompson/allocation_receipt.json; afterwards, email the employee a confirmation with the subject 'Asset Allocation – Jordan Williams' including the receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/asset_request.json","payload": {"request_id": "asset_req_4", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Jordan Williams","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_4","status": "Sent","email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["jordan.williams@example.com"],"subject": "Asset Allocation – Jordan Williams","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/allocation_receipt.json"]}),
            ],
            outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
            ),

    Task(
        annotator="0",
        user_id="V4_Task_012",
        instruction=(
            "Prepare an access summary for jordan.williams@example.com (start 2024-08-19), afterwards send and tag a one-week checklist reminder with the deadline of 2024-08-26, mark any pending items as reminded with the reminder email id, and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="SummarizeAccessChecks", kwargs={"candidate_id": "cand_5"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "checklist_reminder", "to_emails": ["jordan.williams@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_5", "label_names": ["Onboarding-Reminder"],"attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"]}),
            Action(name="MarkChecklistItemsReminded",kwargs={"item_ids": ["item_13", "item_14"], "reminder_email_message_id": "msg_15",}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_013",
        instruction=(
            "Handle provisioning for sofia.martinez@example.com (start 2024-08-12) by sending and labeling the request, allocating inventory, and writing a receipt to /onboarding/Maria_Rodriguez/allocation_receipt.json, followed by sending an allocation confirmation that includes the receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Sofia Martinez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_3","status": "Sent","email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["sofia.martinez@example.com"],"subject": "Asset Allocation – Sofia Martinez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/allocation_receipt.json"]}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_014",
        instruction=(
            "Coordinate the completion of equipment provisioning for jordan.williams@example.com (start 2024-08-19) according to the Equipment Provisioning policy: prepare the request artifact and email IT using ‘Asset Provisioning – Jordan Williams’ with the required ‘Asset-Request’ label; record the email id and mark the request as Sent; allocate the first available inventory and record the allocation receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                "payload": {"request_id": "asset_req_4", "asset_type": "Laptop", "status": "Requested"}
            }),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Jordan Williams",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"],
                "label_names": ["Asset-Request"]
            }),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_4",
                "status": "Sent",
                "email_message_id": "msg_15"
            }),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={
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
            "Send and tag a one-week checklist reminder to emma.thompson@example.com (start 2024-08-05, cutoff 2024-08-12), ensuring the follow-up timestamp is recorded."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "checklist_reminder","to_emails": ["emma.thompson@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"],"reminder_email_message_id": "msg_15","updated_ts": "2025-09-01T00:00:00Z"}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),

    

    Task(
        annotator="0",
        user_id="V4_Task_016",
        instruction=(
            "Dispatch a one-week onboarding checklist reminder to the employee using michael.anderson@example.com (cutoff 2024-08-08). Include the pending tasks summary, label the message, and ensure the follow-up timestamp is noted."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["michael.anderson@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_1",
                           "attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_017",
        instruction=(
            "Handle the task of sending a one-week onboarding checklist reminder to the employee at william.davis@example.com (cutoff 2024-08-05). Attach the pending tasks summary, apply the appropriate label, and document the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_3", "status": "Pending", "due_date_lte": "2024-08-05"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["william.davis@example.com"], "subject": "Pending Onboarding Tasks", "candidate_id": "cand_3",
                           "attachment_file_paths": ["/onboarding/Peter_Jones/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_3", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}
                           })
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_3"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_018",
        instruction=(
            "Coordinate the sending of a one-week onboarding checklist reminder to the employee at sofia.martinez@example.com (cutoff 2024-08-19). Attach the pending tasks summary, label the email accordingly, document the follow-up timestamp, and mark the pending items as reminded."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["sofia.martinez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"]}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15", }),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_019",
        instruction=(
            "Ensure a one-week onboarding checklist reminder is dispatched to the employee at lily.zhang@example.com (cutoff 2024-09-02). Include the summary of pending tasks, label the email, and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["lily.zhang@example.com"], "subject": "Pending Onboarding Tasks", "candidate_id": "cand_6",
                           "attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"]}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_6", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}
                           })
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_020",
        instruction=(
            "Coordinate day-1 orientation and manager-intro invites for raj.patel@example.com (start 2024-09-02) and document the timestamps for both invitations."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["raj.patel@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_7"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_7","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["raj.patel@example.com", "rachel.taylor@example.com"],"subject": "Manager Intro","candidate_id": "cand_7"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_7","manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_021",
        instruction=(
            "Handle the sending of the 'Asset Provisioning – Jordan Williams' email to jordan.williams@example.com (start 2024-08-19), save its id on the request, attach the 'Asset-Request' label, and record /onboarding/Alex_Thompson/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/asset_request.json","payload": {"request_id": "asset_req_4"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jordan Williams", "candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"], "add_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json","mime_type": "application/json", "payload": {"request_id": "asset_req_4"}}),
        ],
    outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_022",
        instruction=(
            "Confirm that the 'Asset-Request' label is on the 'Asset Provisioning – Emma Thompson' email sent to emma.thompson@example.com (start 2024-08-05), and subsequently reply to the provisioning thread to acknowledge."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Asset-Request"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_3", "add_names": ["Asset-Request"]}),
            Action(name="ReplyToEmailThread",kwargs={"candidate_id": "cand_2", "thread_id": "msg_3", "subject": "Asset Provisioning – Emma Thompson"}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_023",
        instruction=(
            "Complete the task of closing the checklist items finalized for sofia.martinez@example.com (start 2024-08-12), afterwards send and label a checklist reminder (cutoff 2024-08-19) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_4", "due_date_lte": "2024-08-19"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "checklist_reminder", "to_emails": ["sofia.martinez@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_4", "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_024",
        instruction=(
            "Initiate the process of sending and labeling a checklist reminder for one week for jordan.williams@example.com (start 2024-08-19, cutoff 2024-08-26) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "checklist_reminder","to_emails": ["jordan.williams@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_13", "item_14"],"reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_025",
        instruction=(
            "Handle sending and labeling of a one-week checklist reminder for michael.anderson@example.com (start 2024-08-01, cutoff 2024-08-08) and document the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "checklist_reminder", "to_emails": ["michael.anderson@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_1", "label_names": ["Onboarding-Reminder"],"attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"]}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_1"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_026",
        instruction=(
            "Coordinate sending a day-1 orientation invite for michael.anderson@example.com (start 2024-08-01), then send and label a one-week checklist reminder (cutoff 2024-08-08) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite", "to_emails": ["michael.anderson@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_1"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_1", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "checklist_reminder", "to_emails": ["michael.anderson@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_1","attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",kwargs={"candidate_id": "cand_1", "subject": "Pending Onboarding Tasks","add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_1"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_027",
        instruction=(
            "Handle the personalization and dispatch of the onboarding packet for lily.zhang@example.com (start 2024-08-26) with the policy/benefits included, then send a one-week checklist reminder (cutoff 2024-09-02) and label it, followed by recording the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_6","file_path": "/onboarding/Emily_Chen/welcome_Emily_Chen.md","mime_type": "text/markdown","content_text": " Welcome, Lily Zhang!\n\nRole: Marketing Specialist\nStart date: 2024-08-26\n\nWe’re excited to have you onboard. Please review the attached policy and benefits guides to prepare for Day 1."}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["lily.zhang@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_6","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Emily_Chen/welcome_Emily_Chen.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_6","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_6","file_path": "/onboarding/Emily_Chen/pending_tasks.md","due_date_lte": "2024-09-02"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["lily.zhang@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_6","attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_6","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_028",
        instruction=(
            "Coordinate the current asset request for sofia.martinez@example.com (start 2024-08-12): dispatch the 'Asset Provisioning – Sofia Martinez' email, log its id on the request, apply the 'Asset-Request' label, allocate an available asset, and save to /onboarding/Maria_Rodriguez/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Sofia Martinez", "candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001","asset_type": "Laptop"}}),
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_029",
        instruction=(
            "Customize and dispatch the onboarding packet to emma.thompson@example.com (start 2024-08-05), including the standard policy and benefits attachments, and log the welcome email id by marking the candidate 'Packet Sent'. Afterward, send a day-1 orientation invitation."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md","mime_type": "text/markdown","content_text": " Welcome, Emma Thompson!\n\nRole: Product Manager\nStart date: 2024-08-05\n\nWe’re excited to have you join us. Please review the attached policy and benefits guides to prepare for Day 1."}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["emma.thompson@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_2","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Jane_Smith/welcome_Jane_Smith.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_2","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"} }),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["emma.thompson@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_2"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_2","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_030",
        instruction=(
            "Log the day-1 access checks for william.davis@example.com (start 2024-07-29): Email=pass, SSO=pass, Slack=fail, GitHub=pass. Next, issue a day-1 orientation invite, noting the invite timestamp as 2025-09-01T00:00:00Z, and alert IT about the access discrepancies."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_3", "checks": [{"system_name": "Email",  "status": "pass"},{"system_name": "SSO",    "status": "pass"},{"system_name": "Slack",  "status": "fail"},{"system_name": "GitHub", "status": "pass"},]}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["william.davis@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_3"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_3","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_3"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_3"'],
    ),
    Task(
    annotator="0",
    user_id="V4_Task_031",
        instruction=(
            "Ensure day-1 access for sofia.martinez@example.com (start 2024-08-12) is confirmed, then distribute the 'Welcome to the Team' packet (include Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown) and log the welcome email id."
        ),
    actions=[
        Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
        Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_4", "checks": [
            {"system_name": "Email", "status": "pass"},
            {"system_name": "SSO", "status": "pass"},
            {"system_name": "Slack", "status": "pass"},
            {"system_name": "GitHub", "status": "pass"}
        ]}),
        Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
        Action(name="RenderOnboardingWelcome", kwargs={"candidate_id": "cand_4", "candidate_name": "Sofia Martinez", "role_title": "UX Designer", "start_date": "2024-08-12"}),
        Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md","mime_type": "text/markdown"}),
        Action(name="GenerateAndSendEmail", kwargs={
            "to_emails": ["sofia.martinez@example.com"],
            "subject": "Welcome to the Team",
            "candidate_id": "cand_4",
            "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md"]
        }),
        Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_4", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_4"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
),
Task(
    annotator="0",
    user_id="V4_Task_032",
        instruction=(
            "Confirm day-1 access for lily.zhang@example.com (start 2024-08-26) and distribute a 'Day-1 Orientation' invitation, documenting the orientation_invite_ts."
        ),
    actions=[
        Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
        Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_6","checks": [
            {"system_name": "Email", "status": "pass"},
            {"system_name": "SSO", "status": "pass"},
            {"system_name": "Slack", "status": "pass"},
            {"system_name": "GitHub", "status": "pass"}
        ]}),
        Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["lily.zhang@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_6"}),
        Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_6", "orientation_invite_ts": "2025-09-01T00:00:00Z"})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
),
Task(
    annotator="0",
    user_id="V4_Task_033",
        instruction=(
            "Handle day-1 access verification for raj.patel@example.com (start 2024-09-02), customize and dispatch the 'Welcome to the Team' packet (attach Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown), and maintain record of the welcome email id."
        ),
    actions=[
        Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
        Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_7", "checks": [
            {"system_name": "Email", "status": "pass"},
            {"system_name": "SSO", "status": "pass"},
            {"system_name": "Slack", "status": "pass"},
            {"system_name": "GitHub", "status": "pass"}
        ]}),
        Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
        Action(name="RenderOnboardingWelcome", kwargs={"candidate_id": "cand_7", "candidate_name": "Raj Patel", "role_title": "Senior Software Engineer","start_date": "2024-09-02"}),
        Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/welcome_Robert_Singh.md","mime_type": "text/markdown"}),
        Action(name="GenerateAndSendEmail", kwargs={
            "to_emails": ["raj.patel@example.com"],
            "subject": "Welcome to the Team",
            "candidate_id": "cand_7",
            "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Robert_Singh/welcome_Robert_Singh.md"]
        }),
        Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_7", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_7"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
),
    Task(
        annotator="0",
        user_id="V4_Task_034",
        instruction=(
            "Coordinate the existing asset request for william.davis@example.com (start 2024-07-29). Dispatch the 'Asset Provisioning – William Davis' email, document its message id on the request, assign the 'Asset-Request' label, allocate a suitable asset, create /onboarding/Peter_Jones/allocation_receipt.json, and distribute 'Asset Allocation – William Davis' with the attached receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json",
                                                            "payload": {"request_id": "asset_req_2"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – William Davis", "candidate_id": "cand_3",
                           "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_2"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/allocation_receipt.json", "mime_type": "application/json",
                           "payload": {"request_id": "asset_req_2", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["william.davis@example.com"], "subject": "Asset Allocation – William Davis", "candidate_id": "cand_3",
                           "attachment_file_paths": ["/onboarding/Peter_Jones/allocation_receipt.json"]}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_035",
        instruction=(
            "Handle the day-1 orientation and manager-intro invites for sofia.martinez@example.com (start 2024-08-12), then proceed to send and tag her provisioning email as Asset-Request and draft an attachments audit."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite","to_emails": ["sofia.martinez@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_4"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "manager_intro","to_emails": ["sofia.martinez@example.com", "daniel.lee@example.com"],"subject": "Manager Intro","candidate_id": "cand_4"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_4","orientation_invite_ts": "2025-09-01T00:00:00Z","manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Sofia Martinez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_3","status": "Sent","email_message_id": "msg_17"}),
            Action(name="AuditAttachmentsForEmail", kwargs={"candidate_id": "cand_4","subject": "Asset Provisioning – Sofia Martinez"}),
        ],
        outputs=['"candidate_id":"cand_4"', "/onboarding/Maria_Rodriguez/attachments_audit.json"],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_036",
        instruction=(
            "Coordinate sending and labeling a one-week onboarding checklist reminder for sofia.martinez@example.com (cutoff 2024-08-19), highlight pending items as reminded using the reminder email id, and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["sofia.martinez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"]}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_4", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_037",
        instruction=(
            "Customize and dispatch the onboarding packet for michael.anderson@example.com (commencing 2024-08-01) including policy/benefits, followed by sending and marking a one-week checklist reminder (deadline 2024-08-08)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_1","file_path": "/onboarding/John_Doe/welcome_John_Doe.md","mime_type": "text/markdown","content_text": " Welcome, Michael Anderson!\n\nRole: Software Engineer\nStart date: 2024-08-01\n\nWe’re excited to have you on board. Please review the attached policy and benefits guides."}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["michael.anderson@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_1","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/John_Doe/welcome_John_Doe.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_1","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_1","file_path": "/onboarding/John_Doe/pending_tasks.md","due_date_lte": "2024-08-08"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["michael.anderson@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_1","attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_1","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_1"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_038",
        instruction=(
            "Deliver a day-1 orientation invitation for lily.zhang@example.com (starting 2024-08-26), then proceed to send and tag a checklist reminder (deadline 2024-09-01)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite", "to_emails": ["lily.zhang@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_6"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_6", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-01"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "checklist_reminder", "to_emails": ["lily.zhang@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_6","attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={"candidate_id": "cand_6", "subject": "Pending Onboarding Tasks","add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_6", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_039",
        instruction=(
            "Ensure the employee at sofia.martinez@example.com has day-1 access ready (start 2024-08-12). Dispatch orientation and manager-intro invites and inform IT of any issues encountered."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_4", "checks": [{"system_name": "Email", "status": "pass"},
                                                                                             {"system_name": "SSO", "status": "pass"},
                                                                                             {"system_name": "Slack", "status": "pass"},
                                                                                             {"system_name": "VPN", "status": "fail"}]}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "orientation_invite", "to_emails": ["sofia.martinez@example.com"], "subject": "Day-1 Orientation",
                           "candidate_id": "cand_4"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "manager_intro", "to_emails": ["sofia.martinez@example.com", "daniel.lee@example.com"],
                                               "subject": "Manager Intro", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_4", "orientation_invite_ts": "2025-09-01T00:00:00Z",
                                                                      "manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "access_gaps", "to_emails": ["it-assets@example.com", "daniel.lee@example.com"], "subject": "Access Gaps",
                           "candidate_id": "cand_4"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_040",
        instruction=(
            "Ensure the employee at michael.anderson@example.com has day-1 access ready (start 2024-08-01). Dispatch orientation and manager-intro invites and inform IT of any issues encountered."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_1", "checks": [
                {"system_name": "Email", "status": "pass"},
                {"system_name": "SSO", "status": "pass"},
                {"system_name": "Slack", "status": "fail"},
                {"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "orientation_invite", "to_emails": ["michael.anderson@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_1"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "manager_intro", "to_emails": ["michael.anderson@example.com", "rachel.taylor@example.com"], "subject": "Manager Intro",
                "candidate_id": "cand_1"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_1", "orientation_invite_ts": "2025-09-01T00:00:00Z",
                                                                      "manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "access_gaps", "to_emails": ["it-assets@example.com"], "subject": "Access Gaps", "candidate_id": "cand_1"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_041",
        instruction=(
            "Handle the dispatch and labeling of a one-week checklist reminder for sofia.martinez@example.com (start 2024-08-12, cutoff 2024-08-19), ensure the pending items are marked as reminded with the reminder email id, and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["sofia.martinez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4", "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_4", "subject": "Pending Onboarding Tasks", "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15", "updated_ts": "2025-09-01T00:00:00Z"}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_042",
        instruction=(
            "Coordinate the recording of day-1 access checks for william.davis@example.com (start 2024-07-29): Email=pass, SSO=pass, Slack=pass, GitHub=pass. Next, dispatch a day-1 orientation invite and log the invite timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_3", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "pass"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite","to_emails": ["william.davis@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_3"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_3","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_043",
        instruction=(
            "Manage the current asset request for sofia.martinez@example.com (start 2024-08-12): verify the inclusion of the 'Asset-Request' label on the existing provisioning email (msg_9), incorporate the email_message_id into the request and flag it as Sent, assign the first available asset, and review the attachments in the provisioning email for auditing."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Asset-Request"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_9", "add_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={ "request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_9"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_3"}),
            Action(name="AuditAttachmentsForEmail", kwargs={ "candidate_id": "cand_4", "subject": "Asset Provisioning – Sofia Martinez"}),
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_044",
        instruction=(
            "Customize and dispatch the onboarding packet for jordan.williams@example.com (start 2024-08-19) ensuring the inclusion of policy/benefits, then distribute a day-1 orientation invite while documenting necessary updates."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md","mime_type": "text/markdown","content_text":" Welcome, Jordan Williams!\n\n""Role: DevOps Engineer\n""Start date: 2024-08-19\n\n"" Getting Started\n""- Review the attached Company Policies and Benefits Guide.\n""- Bring a valid photo ID for security badging.\n""- Your laptop pickup will be coordinated by IT on Day 1.\n\n"" Day 1 Agenda\n""- Orientation session\n""- Account setup (SSO, email, Slack)\n""- Team introductions\n\n""If you have any questions before your start date, reply to this email and HR will assist."}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "onboarding","to_emails": ["jordan.williams@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_5","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_5","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite","to_emails": ["jordan.williams@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_5"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_5","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_045",
        instruction=(
            "Handle and categorize a checklist reminder for one week for raj.patel@example.com (beginning 2024-09-02, ending 2024-09-09), label any uncompleted items as reminded with the corresponding reminder email id, and log the timestamp for follow-up."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email":"raj.patel@example.com","start_date":"2024-09-02"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id":"cand_7","status":"Pending","due_date_lte":"2024-09-09"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id":"cand_7","file_path":"/onboarding/Robert_Singh/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"task":"checklist_reminder","to_emails":["raj.patel@example.com"],"subject":"Pending Onboarding Tasks","candidate_id":"cand_7","attachment_file_paths":["/onboarding/Robert_Singh/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={"candidate_id":"cand_7","subject":"Pending Onboarding Tasks","add_names":["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids":["item_15","item_16"],"reminder_email_message_id":"msg_15","updated_ts":"2025-09-01T00:00:00Z"}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id":"cand_7","fields":{"checklist_follow_up_ts_nullable":"2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
    Task(
annotator="0",
user_id="V4_Task_046",
        instruction=(
            "Confirm day-1 access for the employee at emma.thompson@example.com (beginning 2024-08-05). Send out an invitation for orientation and alert IT if any verification fails."
        ),
actions=[
Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_2", "checks": [
{"system_name": "Email", "status": "pass"},
{"system_name": "SSO", "status": "pass"},
{"system_name": "Slack", "status": "pass"},
{"system_name": "GitHub", "status": "pass"}
]}),
Action(name="GenerateAndSendEmail", kwargs={
"to_emails": ["emma.thompson@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_2"
}),
Action(name="UpdateCandidateInviteTimestamps", kwargs={
"candidate_id": "cand_2", "orientation_invite_ts": "2025-09-01T00:00:00Z", "message_id": "msg_15"
})
],
outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
),
    Task(
        annotator="0",
        user_id="V4_Task_047",
        instruction=(
            "Handle day-1 access verification for lily.zhang@example.com (start 2024-08-26) on Email=pass, SSO=fail, Slack=pass, GitHub=pass; send a day-1 orientation invite, and subsequently notify IT about access gaps."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_6", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "fail"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["lily.zhang@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_6"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_6","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_6"}),
        ],
        outputs=['"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_048",
        instruction=(
            "Conduct day-1 access checks for emma.thompson@example.com (start 2024-08-05): Email=pass, SSO=fail, Slack=pass, GitHub=pass. Next, dispatch a day-1 orientation invite and log the invite timestamp, subsequently informing IT of the access gaps."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_2", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "fail"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["emma.thompson@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_2"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_2","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_2"}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_049",
        instruction=(
            "Ensure the 'Asset-Request' label is included on 'Asset Provisioning – William Davis' for william.davis@example.com (start 2024-07-29), update the existing request with the provisioning email id, and document an attachments audit."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_2"}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Asset-Request"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_4", "add_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json","payload": {"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4"}}),Action(name="AuditAttachmentsForEmail", kwargs={"candidate_id": "cand_3", "subject": "Asset Provisioning – William Davis"}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_050",
        instruction=(
            "Send day-1 orientation and manager-intro invitations for sofia.martinez@example.com (start 2024-08-12) and log the timestamps for both invites."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "orientation_invite", "to_emails": ["sofia.martinez@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_4"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "manager_intro", "to_emails": ["sofia.martinez@example.com", "daniel.lee@example.com"], "subject": "Manager Intro","candidate_id": "cand_4"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_4", "orientation_invite_ts": "2025-09-01T00:00:00Z","manager_intro_invite_ts": "2025-09-01T00:00:00Z"})
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_051",
        instruction=(
            "Handle the assessment of the asset request and send an email for 'Asset Provisioning – Jordan Williams' directed to jordan.williams@example.com (start 2024-08-19), and assign an available asset."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/asset_request.json","payload": {"request_id": "asset_req_4", "asset_type": "Laptop", "status": "Completed"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jordan Williams", "candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001","asset_type": "Laptop"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    
    

    Task(
        annotator="0",
        user_id="V4_Task_052",
        instruction=(
            "Coordinate the completion of Emma Thompson’s provisioning by dispatching and tagging the request, distributing inventory, issuing a receipt, and responding to the provisioning thread for confirmation."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {"request_id": "asset_req_1"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Emma Thompson",
                "candidate_id": "cand_2",
                "attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_1",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {
                    "request_id": "asset_req_1",
                    "status": "Sent",
                    "email_message_id": "msg_15",
                    "inventory_checked_flag": True,
                    "asset_tag": "LT-DELL-001"}}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="ReplyToEmailThread", kwargs={
                "candidate_id": "cand_2",
                "thread_id": "msg_15",
                "subject": "Asset Provisioning – Emma Thompson",
                "task": "acknowledge"
            }),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_053",
        instruction=(
            "Initiate and dispatch an equipment provisioning request for the employee at michael.anderson@example.com with start date 2024-08-01. Utilize asset type Standard-Laptop, send it to it-assets@example.com, then mark the request as Sent and tag the email Asset-Request."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="CreateAssetRequest", kwargs={"candidate_id": "cand_1", "asset_type": "Standard-Laptop", "status": "Requested"
                                                        }),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/asset_request.json",
                                                            "payload": {"candidate_name": "Michael Anderson", "asset_type": "Standard-Laptop"}
                                                            }),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Michael Anderson", "candidate_id": "cand_1",
                           "attachment_file_paths": ["/onboarding/John_Doe/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus",
                   kwargs={"candidate_id": "cand_1", "asset_type": "Standard-Laptop", "status": "Sent", "email_message_id": "msg_15"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"', '"message_id":"msg_15"', '"request_status":"Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_054",
        instruction=(
            "Initiate and dispatch an equipment provisioning request for the employee at sofia.martinez@example.com with start date 2024-08-12. Operate on the existing request, send it to it-assets@example.com, then mark the request as Sent and tag the email Asset-Request."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                                                            "payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Sofia Martinez", "candidate_id": "cand_4",
                          "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_4", "subject": "Asset Provisioning – Sofia Martinez",
                           "add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"', '"request_id":"asset_req_3"', '"request_status":"Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_055",
        instruction=(
            "Handle and dispatch an equipment provisioning request for the employee at william.davis@example.com with a commencement date of 2024-07-29. Work with the existing request, email it-assets@example.com, then update the request status to Sent and tag the email Asset-Request."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_2"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json",
                                                            "payload": {"request_id": "asset_req_2"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – William Davis", "candidate_id": "cand_3",
                          "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus",
                   kwargs={"request_id": "asset_req_2", "status": "Sent", "candidate_id": "cand_3", "subject": "Asset Provisioning – William Davis",
                           }),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Asset-Request"}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_3", "subject": "Asset Provisioning – William Davis",
                           "add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_3"', '"request_id":"asset_req_2"', '"request_status":"Sent"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_056",
        instruction=(
            "Coordinate the sending of a one-week onboarding checklist reminder for emma.thompson@example.com (cutoff 2024-08-12), categorize it, mark ongoing tasks as reminded using the reminder email id, and note the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["emma.thompson@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_2",
                           "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_2", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"], "reminder_email_message_id": "msg_15",
                           }),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_057",
        instruction=(
            "Dispatch and tag a one-week checklist reminder to raj.patel@example.com (commencing 2024-09-02, deadline 2024-09-09), mark any outstanding items as reminded using the reminder email id, log the follow-up timestamp, and finalize any completed items that lack timestamps."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_7", "status": "Pending", "due_date_lte": "2024-09-09"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["raj.patel@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_7", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_15", "item_16"], "reminder_email_message_id": "msg_15", }),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_7", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_7", "due_date_lte": "2024-09-09"})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_058",
        instruction=(
            "Dispatch and tag a one-week checklist reminder to raj.patel@example.com (commencing 2024-09-02, deadline 2024-09-09), mark any outstanding items as reminded using the reminder email id, log the follow-up timestamp, and finalize any completed items that lack timestamps."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_7", "status": "Pending", "due_date_lte": "2024-09-09"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["raj.patel@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/pending_tasks.md"], "label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_15", "item_16"], "reminder_email_message_id": "msg_15", }),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_7", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_7", "due_date_lte": "2024-09-09"})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_059",
        instruction=(
            "Make sure the Asset-Request label is attached to the previously dispatched provisioning email (message_id 'msg_4') for william.davis@example.com (start 2024-07-29), and update the current asset request using that email id."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="UpdateAssetRequestStatus",
                   kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4", }),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Asset-Request"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_4", "add_names": ["Asset-Request"]})
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_060",
        instruction=(
            "Dispatch and tag a one-week checklist reminder for william.davis@example.com (start 2024-07-29, cutoff 2024-08-05) and log the time of follow-up."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_3", "status": "Pending", "due_date_lte": "2024-08-05"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "checklist_reminder", "to_emails": ["william.davis@example.com"],"subject": "Pending Onboarding Tasks", "candidate_id": "cand_3",  "attachment_file_paths": ["/onboarding/Peter_Jones/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={"candidate_id": "cand_3", "subject": "Pending Onboarding Tasks",  "add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_3", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_061",
        instruction=(
            "Handle equipment provisioning completion for sofia.martinez@example.com (beginning 2024-08-12) according to policy: prepare the request documentation and email IT using 'Asset Provisioning – Sofia Martinez' with the necessary 'Asset-Request' tag; log the email id and label the request as Sent; assign the earliest available inventory and document the allocation receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                "payload": {"request_id": "asset_req_3", "asset_type": "Laptop", "status": "Pending"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Sofia Martinez",
                "candidate_id": "cand_4",
                "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_3",
                "status": "Sent",
                "email_message_id": "msg_15" }),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="WriteAssetRequestFile", kwargs={
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
            "Coordinate and dispatch an equipment provisioning request for the employee at michael.anderson@example.com with a start date on 2024-08-01. Utilize asset type Standard-Laptop, email it-assets@example.com, then record the request as Sent and tag the email Asset-Request."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="CreateAssetRequest", kwargs={"candidate_id": "cand_1", "asset_type": "Standard-Laptop", "status": "Requested"
                                                        }),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/asset_request.json",
                                                            "payload": {"candidate_name": "Michael Anderson", "asset_type": "Standard-Laptop"}
                                                            }),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Michael Anderson", "candidate_id": "cand_1",
                           "attachment_file_paths": ["/onboarding/John_Doe/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus",
                   kwargs={"candidate_id": "cand_1", "asset_type": "Standard-Laptop", "status": "Sent", "email_message_id": "msg_15"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"', '"message_id":"msg_15"', '"request_status":"Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_063",
        instruction=(
            "Handle the equipment provisioning for the employee at raj.patel@example.com (start 2024-09-02) by utilizing the existing request and assigning inventory. Dispatch the provisioning email, save its message id on the request, mark the email with 'Asset-Request', assign the first available tag for the requested type, and log an allocation receipt into the database."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/asset_request.json",
                "payload": {"request_id": "asset_req_5"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Raj Patel",
                "candidate_id": "cand_7",
                "attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_5",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/asset_request.json",
                "payload": {
                    "request_id": "asset_req_5",
                    "status": "Sent",
                    "email_message_id": "msg_15",
                    "inventory_checked_flag": True,
                    "asset_tag": "LT-DELL-001"}}),
            Action(name="UpdateAssetRequestStatus", kwargs={
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
            "Complete the equipment provisioning for william.davis@example.com (start 2024-07-29) following the Equipment Provisioning policy: prepare the request artifact, send an email to IT using the predetermined subject 'Asset Provisioning – William Davis' with the necessary 'Asset-Request' label, document the provisioning email id and mark the request as Sent, allocate the first available inventory, and document an allocation receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/asset_request.json",
                "payload": {"request_id": "asset_req_2"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – William Davis",
                "candidate_id": "cand_3",
                "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_2",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_2"}),
            Action(name="WriteOnboardingFile", kwargs={
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
            "Handle the closing of completed checklist items for jordan.williams@example.com (start 2024-08-19), then coordinate the sending and labeling of a checklist reminder (cutoff 2024-08-26) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_5", "due_date_lte": "2024-08-26"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md", "due_date_lte": "2024-08-26"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "checklist_reminder","to_emails": ["jordan.williams@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_13", "item_14"], "reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_066",
        instruction=(
            "Dispatch the 'Asset Provisioning – Sofia Martinez' email for sofia.martinez@example.com (start 2024-08-12), retain its message id on the request, and affix the 'Asset-Request' label."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Sofia Martinez", "candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3", "status": "Sent","email_message_id": "msg_15"}}),
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_067",
        instruction=(
            "Handle the current asset request for sofia.martinez@example.com starting on 2024-08-12. Coordinate the preparation of the request and communicate with IT by emailing them with 'Asset Provisioning – Sofia Martinez' while ensuring the 'Asset-Request' label is used. Document the email ID and indicate the request as Sent. Allocate the initial available inventory and draft the receipt at /onboarding/Maria_Rodriguez/allocation_receipt.json. Afterwards, dispatch an allocation confirmation email to sofia.martinez@example.com, with the subject line 'Asset Allocation – Sofia Martinez', including the receipt as an attachment."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                                                            "payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Sofia Martinez", "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json",
                                                         "mime_type": "application/json",
                                                         "payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001",
                                                                     "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["sofia.martinez@example.com"], "subject": "Asset Allocation – Sofia Martinez", "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/allocation_receipt.json"]}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
 Task(
        annotator="0",
        user_id="V4_Task_068",
        instruction=(
            "Complete the equipment provisioning process for william.davis@example.com, whose start date is 2024-07-29, following the Equipment Provisioning policy. Organize the preparation of the request artifact and send an email to IT using 'Asset Provisioning – William Davis', ensuring the JSON is attached and the 'Asset-Request' label is included. Log the email ID and label the request as Sent. Allocate the initial available inventory, document the allocation, generate an allocation receipt, and then send a confirmation to the employee, including the receipt with the subject 'Equipment Allocation Receipt'."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3","file_path": "/onboarding/Peter_Jones/asset_request.json","payload": {"request_id": "asset_req_2", "asset_type": "Laptop", "status": "Requested"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – William Davis","candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_2","status": "Sent","email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_2"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_3","file_path": "/onboarding/Peter_Jones/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_2", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["william.davis@example.com"],"subject": "Equipment Allocation Receipt","candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/allocation_receipt.json"]}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_069",
        instruction=(
            "Handle sending and labeling a checklist reminder for the week to jordan.williams@example.com (start 2024-08-19, cutoff 2024-08-26). Mark the pending items as reminded using the reminder email id, and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email":"jordan.williams@example.com","start_date":"2024-08-19"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id":"cand_5","status":"Pending","due_date_lte":"2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id":"cand_5","file_path":"/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"task":"checklist_reminder","to_emails":["jordan.williams@example.com"],"subject":"Pending Onboarding Tasks","candidate_id":"cand_5","attachment_file_paths":["/onboarding/Alex_Thompson/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={"candidate_id":"cand_5","subject":"Pending Onboarding Tasks","add_names":["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids":["item_13","item_14"],"reminder_email_message_id":"msg_15","updated_ts":"2025-09-01T00:00:00Z"}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id":"cand_5","fields":{"checklist_follow_up_ts_nullable":"2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_070",
        instruction=(
            "Coordinate the sending and labeling of a one-week checklist reminder for emma.thompson@example.com (start 2024-08-05, cutoff 2024-08-12). Ensure pending items are marked as reminded with the reminder email id, and document the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["emma.thompson@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_2", "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_2", "subject": "Pending Onboarding Tasks", "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"], "reminder_email_message_id": "msg_15",
                           "updated_ts": "2025-09-01T00:00:00Z"}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_071",
        instruction=(
            "Handle the creation and dispatch of an equipment provisioning request for the employee at raj.patel@example.com with a start date of 2024-09-02. Manage the existing request, contact email it-assets@example.com, and subsequently mark the request as Sent, labeling the email Asset-Request."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/asset_request.json",
                                                            "payload": {"request_id": "asset_req_5"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Raj Patel", "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus",
                   kwargs={"request_id": "asset_req_5", "status": "Sent", "candidate_id": "cand_7", "subject": "Asset Provisioning – Raj Patel",
                           }),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_15", "add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"', '"request_id":"asset_req_5"', '"request_status":"Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_072",
        instruction=(
            "Coordinate the creation and delivery of a basic onboarding packet for the employee at michael.anderson@example.com with a starting date of 2024-08-01."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="RenderOnboardingWelcome",
                   kwargs={"candidate_id": "cand_1", "candidate_name": "Michael Anderson", "role_title": "Software Engineer", "start_date": "2024-08-01"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/welcome_John_Doe.md", "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["michael.anderson@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_1",
                                               "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                                         "/onboarding/John_Doe/welcome_John_Doe.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_1", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
    ),
    Task(
    annotator="0",
    user_id="V4_Task_073",
        instruction=(
            "Handle the verification of day-1 access for raj.patel@example.com (start 2024-09-02), customize and dispatch the 'Welcome to the Team' packet (include Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown), and save the welcome email id."
        ),
    actions=[
        Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
        Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_7", "checks": [
            {"system_name": "Email", "status": "pass"},
            {"system_name": "SSO", "status": "pass"},
            {"system_name": "Slack", "status": "pass"},
            {"system_name": "GitHub", "status": "pass"}
        ]}),
        Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
        Action(name="RenderOnboardingWelcome", kwargs={"candidate_id": "cand_7", "candidate_name": "Raj Patel", "role_title": "Senior Software Engineer","start_date": "2024-09-02"}),
        Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/welcome_Robert_Singh.md","mime_type": "text/markdown"}),
        Action(name="GenerateAndSendEmail", kwargs={
            "to_emails": ["raj.patel@example.com"],
            "subject": "Welcome to the Team",
            "candidate_id": "cand_7",
            "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Robert_Singh/welcome_Robert_Singh.md"]
        }),
        Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_7", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_7"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
),
 Task(
        annotator="0",
        user_id="V4_Task_074",
        instruction=(
            "Coordinate the sending of the 'Asset Provisioning – Emma Thompson' email for emma.thompson@example.com (start 2024-08-05), record its message id on the request, and assign the 'Asset-Request' label."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Emma Thompson","candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_1","status": "Sent","email_message_id": "msg_15"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_075",
        instruction=(
            "Handle the completion of 'Asset-Request' for 'Asset Provisioning – William Davis' at william.davis@example.com (start 2024-07-29) and respond to the provisioning email thread to confirm receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3","file_path": "/onboarding/Peter_Jones/asset_request.json","payload": {"request_id": "asset_req_2"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – William Davis","candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_2","status": "Sent","email_message_id": "msg_15"}),
            Action(name="ReplyToEmailThread", kwargs={"candidate_id": "cand_3","thread_id": "msg_15","subject": "Asset Provisioning – William Davis","task": "acknowledge"}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    

    Task(
        annotator="0",
        user_id="V4_Task_076",
        instruction=(
            "Manage the current asset request for jordan.williams@example.com (start 2024-08-19). Dispatch the 'Asset Provisioning – Jordan Williams' email including the request JSON as an attachment, save its message id on the request, use the 'Asset-Request' label, assign an available asset, and create /onboarding/Alex_Thompson/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/asset_request.json","payload": {"request_id": "asset_req_4"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jordan Williams", "candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001","asset_type": "Laptop"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_077",
        instruction=(
            "Manage the current asset request for emma.thompson@example.com (start 2024-08-05). Dispatch the 'Asset Provisioning – Emma Thompson' email, record its message id on the request, apply the 'Asset-Request' label, allocate an available asset, and document /onboarding/Jane_Smith/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Emma Thompson","candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_1","status": "Sent","email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_078",
        instruction=(
            "Handle the ongoing asset request for william.davis@example.com (start 2024-07-29). Send the 'Asset Provisioning – William Davis' email, log its message id on the request, affix the 'Asset-Request' label, and write /onboarding/Peter_Jones/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json","payload": {"request_id": "asset_req_2"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – William Davis", "candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="WriteOnboardingFile",kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/allocation_receipt.json", "mime_type": "application/json","payload": {"request_id": "asset_req_2"}}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_079",
        instruction=(
            "Handle the current asset request for raj.patel@example.com (start 2024-09-02). Dispatch the 'Asset Provisioning – Raj Patel' email, log its message id on the request, apply the 'Asset-Request' label, allocate an available asset, create /onboarding/Robert_Singh/allocation_receipt.json, and send out the 'Asset Allocation – Raj Patel' confirmation with the attached receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Raj Patel", "candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"], "label_names": ["Asset-Request"],"date_ts": "2025-09-01T00:00:00Z"}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_5", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteOnboardingFile",kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/allocation_receipt.json", "mime_type": "application/json","payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",kwargs={"to_emails": ["raj.patel@example.com"], "subject": "Asset Allocation – Raj Patel", "candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/allocation_receipt.json"]}),
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_080",
        instruction=(
            "Ensure day-1 access for the employee at jordan.williams@example.com (start 2024-08-19). Issue an orientation invite and alert IT if any checks fail."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_5", "checks": [{"system_name": "Email", "status": "pass"},
                                                                                             {"system_name": "SSO", "status": "fail"},
                                                                                             {"system_name": "Slack", "status": "pass"},
                                                                                             {"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "orientation_invite", "to_emails": ["jordan.williams@example.com"], "subject": "Day-1 Orientation",
                           "candidate_id": "cand_5"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_5", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "access_gaps", "to_emails": ["it-assets@example.com"], "subject": "Access Gaps", "candidate_id": "cand_5"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_081",
        instruction=(
            "Handle the sending of a one-week onboarding checklist reminder to the employee at emma.thompson@example.com (cutoff 2024-08-12). Attach the pending tasks summary, label the email, log the follow-up timestamp, and ensure pending items are marked as reminded."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["emma.thompson@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_2",
                           "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_2", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_4", "item_5","item_6", "item_7"], "reminder_email_message_id": "msg_15", }),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_082",
        instruction=(
            "Coordinate the sending of a one-week onboarding checklist reminder for the employee at jordan.williams@example.com (cutoff 2024-08-26). Attach the pending tasks summary, apply a label to the email, document the follow-up timestamp, and update pending items as reminded."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["jordan.williams@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_5", "attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"]}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_5", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_13", "item_14"], "reminder_email_message_id": "msg_15", }),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),
Task(
        annotator="0",
        user_id="V4_Task_083",
        instruction=(
            "Coordinate checklist follow-up for emma.thompson@example.com (start 2024-08-05) utilizing the existing asset request as reference. Implement the one-week cutoff (2024-08-12) to identify unresolved items and send a 'Pending Onboarding Tasks' email to the candidate with the label 'Onboarding-Reminder' attaching the generated pending_tasks.md. Update the records to indicate the reminder: set checklist_follow_up_ts to 2025-09-01T00:00:00Z and mark the relevant items as reminded, saving message_id msg_15."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["emma.thompson@example.com"], "subject": "Pending Onboarding Tasks", "candidate_id": "cand_2", "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"], "label_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"], "reminder_email_message_id": "msg_15", "updated_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"', '"request_id":"asset_req_1"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_084",
        instruction=(
            "Carry out the equipment provisioning for the employee at william.davis@example.com (start 2024-07-29) by utilizing the existing request. Dispatch the provisioning email, log its message id on the request, tag the email Asset-Request, and record an allocation receipt to the database."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_2"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/asset_request.json",
                "payload": {"request_id": "asset_req_2"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – William Davis",
                "candidate_id": "cand_3",
                "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_2",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/asset_request.json",
                "payload": {"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_15"}}),
            Action(name="WriteOnboardingFile", kwargs={
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
            "Handle a one-week onboarding checklist reminder for the employee at raj.patel@example.com, whose start date is 2024-09-02. Attach the summary of pending tasks, categorize the email, log the follow-up timestamp, and indicate pending items as reminded."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_7", "status": "Pending", "due_date_lte": "2024-09-09"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["raj.patel@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_15", "item_16"], "reminder_email_message_id": "msg_15", }),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_7", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_086",
        instruction=(
            "Coordinate the creation and dispatch of a basic onboarding packet for the employee at emma.thompson@example.com with the start date 2024-08-05. Customize the onboarding template, include standard docs, deliver the email, then update the status to 'Packet Sent' and save the welcome email ID."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="RenderOnboardingWelcome",
                   kwargs={"candidate_id": "cand_2", "candidate_name": "Emma Thompson", "role_title": "Product Manager", "start_date": "2024-08-05"}),

            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md", "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "onboarding", "to_emails": ["emma.thompson@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_2",
                           "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                     "/onboarding/Jane_Smith/welcome_Jane_Smith.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_2", "fields": {"onboarding_status": "Packet Sent",
                                                                                                       "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"', '"status":"Packet Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_087",
        instruction=(
            "Handle the first-day access verifications for william.davis@example.com (beginning 2024-07-29): Email=pass, SSO=pass, Slack=fail, GitHub=pass. Subsequently, dispatch an orientation invitation for the first day, document the invite timestamp as 2025-09-01T00:00:00Z, and alert IT about the access discrepancies."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_3", "checks": [{"system_name": "Email",  "status": "pass"},{"system_name": "SSO",    "status": "pass"},{"system_name": "Slack",  "status": "fail"},{"system_name": "GitHub", "status": "pass"},]}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["william.davis@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_3"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_3","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_3"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_088",
        instruction=(
            "Coordinate and dispatch an equipment provisioning request for the employee with email emma.thompson@example.com starting on 2024-08-05. Proceed with the existing request by emailing it-assets@example.com, then designate the request as Sent and tag the email with Asset-Request."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {"request_id": "asset_req_1", "candidate_id": "cand_2", "status": "Completed"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Emma Thompson",
                "candidate_id": "cand_2",
                "attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15", }),
            Action(name="ModifyEmailLabels", kwargs={
                "candidate_id": "cand_2", "subject": "Asset Provisioning – Emma Thompson",
                "add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"', '"request_id":"asset_req_1"', '"request_status":"Sent"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_089",
        instruction=(
            "Handle the creation and dispatch of an equipment provisioning request for the employee at jordan.williams@example.com with the start date of 2024-08-19. Manage the existing request, communicate with email it-assets@example.com, then mark the request as Sent and label the email Asset-Request."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                "payload": {"request_id": "asset_req_4", "candidate_id": "cand_5", "status": "Completed"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Jordan Williams",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15", }),
            Action(name="ModifyEmailLabels", kwargs={
                "candidate_id": "cand_5", "subject": "Asset Provisioning – Jordan Williams","add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"', '"request_id":"asset_req_4"', '"request_status":"Sent"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_090",
        instruction=(
            "Customize and transmit the onboarding packet for lily.zhang@example.com (start date 2024-08-26) with policy/benefits attached, then issue a day-1 orientation invite and log the invite timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_6","file_path": "/onboarding/Emily_Chen/welcome_Emily_Chen.md","mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail",kwargs={"task": "onboarding", "to_emails": ["lily.zhang@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_6","attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Emily_Chen/welcome_Emily_Chen.md"]}),
            Action(name="UpdateCandidateStatusFields",kwargs={"candidate_id": "cand_6", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite", "to_emails": ["lily.zhang@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_6"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_6", "orientation_invite_ts": "2025-09-01T00:00:00Z"})
        ],
        outputs=['"candidate_id":"cand_6"'],
    ),
Task(
        annotator="0",
        user_id="V4_Task_091",
        instruction=(
            "Verify day-1 access for michael.anderson@example.com (start 2024-08-01): note all checks passed, dispatch a day-1 orientation invite, and log the invite's timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_1", "checks": [{"system_name": "Email",  "status": "pass"},{"system_name": "SSO",    "status": "pass"},{"system_name": "Slack",  "status": "pass"},{"system_name": "GitHub", "status": "pass"},]}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["michael.anderson@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_1"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_1","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_092",
        instruction=(
            "Complete provisioning for sofia.martinez@example.com (start 2024-08-12) by sending and marking the request, assigning inventory, documenting the receipt in /onboarding/Maria_Rodriguez/allocation_receipt.json, and emailing an allocation confirmation with the subject 'Asset Allocation – Sofia Martinez'."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Sofia Martinez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_3","status": "Sent","email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["sofia.martinez@example.com"],"subject": "Asset Allocation – Sofia Martinez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/allocation_receipt.json"]}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_093",
        instruction=(
            "Handle a one-week checklist follow-up for jordan.williams@example.com (start 2024-08-19) in accordance with the checklist policy: prepare the pending-tasks artifact for items due by 2024-08-26, dispatch a labeled reminder to the employee, denote those items as reminded using the reminder email’s id, and note the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/pending_tasks.md","due_date_lte": "2024-08-26"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["jordan.williams@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_13", "item_14"],"reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_5","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_5"', '"reminder_message_id":"msg_15"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_094",
        instruction=(
            "Administer the current asset request for raj.patel@example.com (start 2024-09-02): dispatch the 'Asset Provisioning – Raj Patel' email, record its message id on the request, and attach the 'Asset-Request' label."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Raj Patel","candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_5","status": "Sent","email_message_id": "msg_15"}),
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_095",
        instruction=(
            "Handle the closure of completed checklist items for lily.zhang@example.com (start 2024-08-26), then transmit and tag a checklist reminder with cutoff 2024-09-02 and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_6", "due_date_lte": "2024-09-02"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_6","file_path": "/onboarding/Emily_Chen/pending_tasks.md","due_date_lte": "2024-09-02"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["lily.zhang@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_6","attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_6","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_096",
        instruction=(
            "Coordinate writing an access summary for emma.thompson@example.com (start 2024-08-05), dispatch an orientation invite, then send and label a one-week checklist reminder with cutoff 2024-08-12 and verify the label's presence."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/access_summary.md","mime_type": "text/markdown","content_text": " Access Summary (Day 1)\n\nCandidate: Emma Thompson\nStart date: 2024-08-05\n"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["emma.thompson@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_2"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_2","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/pending_tasks.md","due_date_lte": "2024-08-12"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["emma.thompson@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_2","status": "Pending","due_date_lte": "2024-08-12"}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"],"reminder_email_message_id": "msg_16"}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_2","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_097",
        instruction=(
            "Initiate the sending of day-1 orientation and manager-intro invites for raj.patel@example.com (start 2024-09-02). Following that, dispatch the provisioning email and apply the Asset-Request label."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["raj.patel@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_7"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["raj.patel@example.com", "rachel.taylor@example.com"],"subject": "Manager Intro","candidate_id": "cand_7"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_7","orientation_invite_ts": "2025-09-01T00:00:00Z","manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Raj Patel","candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_5","status": "Sent","email_message_id": "msg_17"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_098",
        instruction=(
            "Send out a one-week onboarding checklist reminder for the employee at sofia.martinez@example.com (cutoff 2024-08-19). Ensure to attach the pending tasks summary, label the email, log the follow-up timestamp, and label pending items as reminded."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["sofia.martinez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"]}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15", }),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_099",
        instruction=(
            "Handle the dispatch of the onboarding packet for jordan.williams@example.com (start 2024-08-19), coordinate an orientation invite afterward, and then send and mark a one-week checklist reminder (cutoff 2024-08-26)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md","mime_type": "text/markdown","content_text": " Welcome, Jordan Williams!\n\nRole: DevOps Engineer\nStart date: 2024-08-19\n\nPlease review the attached policy and benefits guides."}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["jordan.williams@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_5","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_5","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["jordan.williams@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_5"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_5","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/pending_tasks.md","due_date_lte": "2024-08-26"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["jordan.williams@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"] }),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_5","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_100",
        instruction=(
            "Complete the provisioning process for raj.patel@example.com (start 2024-09-02) by dispatching the 'Asset Provisioning – Raj Patel' email with the request JSON attached, recording its message id on the request, applying the 'Asset-Request' label, assigning inventory, and generating /onboarding/Robert_Singh/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5", "candidate_id": "cand_7"}}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Raj Patel","candidate_id": "cand_7","label_names": ["Asset-Request"],"attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_5","status": "Sent","email_message_id": "msg_15" }),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
]