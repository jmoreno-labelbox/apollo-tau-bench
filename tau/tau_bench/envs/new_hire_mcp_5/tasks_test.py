from tau_bench.types import Action, Task
TASKS = [

    Task(
        annotator="v5",
        user_id="task_001",
        instruction=(
            "Handle day-1 access verification for michael.anderson@example.com (start 2024-08-01): ensure all checks are recorded as passing, issue a day-1 orientation invite, and log the timestamp of the invite."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_1", "checks": [
                {"system_name": "Email",  "status": "pass"},
                {"system_name": "SSO",    "status": "pass"},
                {"system_name": "Slack",  "status": "pass"},
                {"system_name": "GitHub", "status": "pass"},
            ]}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["michael.anderson@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_1"
            }),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_1",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_002",
        instruction=(
            "Coordinate the logging of day-1 access checks for william.davis@example.com (start 2024-07-29): ensure Email=pass, SSO=pass, Slack=fail, GitHub=pass. Subsequently, send a day-1 orientation invite, log the invite timestamp as 2025-09-01T00:00:00Z, and inform IT of any access discrepancies."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_3", "checks": [
                {"system_name": "Email",  "status": "pass"},
                {"system_name": "SSO",    "status": "pass"},
                {"system_name": "Slack",  "status": "fail"},
                {"system_name": "GitHub", "status": "pass"},
            ]}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["william.davis@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_3"
            }),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_3",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"
            }),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Access Gaps",
                "candidate_id": "cand_3"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_003",
        instruction=(
            "Prepare and dispatch a basic onboarding packet for the employee at sofia.martinez@example.com with the start date of 2024-08-12."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="RenderOnboardingWelcome",
                   kwargs={"candidate_id": "cand_4", "candidate_name": "Sofia Martinez", "role_title": "UX Designer", "start_date": "2024-08-12"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md",
                           "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["sofia.martinez@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_4",
                           "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                     "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_4", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_004",
        instruction=(
            "Prepare and dispatch a basic onboarding packet for the employee at lily.zhang@example.com with the start date of 2024-08-26."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="RenderOnboardingWelcome",
                   kwargs={"candidate_id": "cand_6", "candidate_name": "Lily Zhang", "role_title": "Marketing Specialist",
                           "start_date": "2024-08-26"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/welcome_Emily_Chen.md", "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["lily.zhang@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_6",
                                               "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                                         "/onboarding/Emily_Chen/welcome_Emily_Chen.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_6", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_005",
        instruction=(
            "Craft and dispatch a basic onboarding packet for the employee at raj.patel@example.com, whose start date is 2024-09-02. Customize the template, include the policy/benefits, send the email, and record the welcome email id."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="RenderOnboardingWelcome",
                   kwargs={"candidate_id": "cand_7", "candidate_name": "Raj Patel", "role_title": "Senior Software Engineer",
                           "start_date": "2024-09-02"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/welcome_Robert_Singh.md", "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["raj.patel@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_7",
                                               "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                                         "/onboarding/Robert_Singh/welcome_Robert_Singh.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_7", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_006",
        instruction=(
            "Formulate and forward an equipment provisioning request for the employee at michael.anderson@example.com, beginning on 2024-08-01. Utilize asset type Standard-Laptop, send to email it-assets@example.com, afterwards mark the request as Sent and tag the email Asset-Request."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_007",
        instruction=(
            "Coordinate the creation and dispatch of an equipment provisioning request for the employee at sofia.martinez@example.com with start date 2024-08-12. Utilize the existing request, email it-assets@example.com, then mark the request as Sent and tag the email Asset-Request."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_008",
        instruction=(
            "Handle the creation and sending of an equipment provisioning request for the employee at william.davis@example.com, with the start date 2024-07-29. Work on the existing request, email it-assets@example.com, then mark the request as Sent and categorize the email as Asset-Request."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_009",
        instruction=(
            "Handle the task of sending and labeling a one-week checklist reminder to emma.thompson@example.com (start 2024-08-05, cutoff 2024-08-12). Ensure pending items are marked as reminded with the associated reminder email id, and log the follow-up timestamp."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_010",
        instruction=(
            "Coordinate the creation and dispatch of an equipment provisioning request for the employee at raj.patel@example.com starting from 2024-09-02. Utilize the current request, communicate with email it-assets@example.com, then update the request status to Sent and label the email Asset-Request."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_011",
        instruction=(
            "Prepare and dispatch a fundamental onboarding packet to the employee at michael.anderson@example.com with the start date of 2024-08-01."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_012",
        instruction=(
            "Prepare and dispatch a fundamental onboarding packet to the employee at william.davis@example.com with the start date of 2024-07-29."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="RenderOnboardingWelcome",
                   kwargs={"candidate_id": "cand_3", "candidate_name": "William Davis", "role_title": "Data Scientist", "start_date": "2024-07-29"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md", "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail", kwargs={"to_emails": ["william.davis@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_3",
                                               "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                                         "/onboarding/Peter_Jones/welcome_Peter_Jones.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_3", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=[]
    ),


    Task(
        annotator="v5",
        user_id="task_013",
        instruction=(
            "Check initial access for the employee at sofia.martinez@example.com (commencing 2024-08-12). Dispatch orientation and manager-introduction invites; inform IT of any access issues."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_014",
        instruction=(
            "Confirm day-1 access for the employee at michael.anderson@example.com (starting 2024-08-01). Send out orientation and manager-introduction invitations; alert IT if any problems arise."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_115",
        instruction=(
            "Handle and classify a one-week checklist reminder for sofia.martinez@example.com (start 2024-08-12, cutoff 2024-08-19), tag the pending items as reminded with the reminder email id, and document the follow-up timestamp."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_016",
        instruction=(
            "Coordinate a one-week onboarding checklist reminder for the employee at michael.anderson@example.com (cutoff 2024-08-08). You include the pending tasks summary, classify the email, and document the follow-up timestamp."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_017",
        instruction=(
            "Handle sending a one-week onboarding checklist reminder for the employee at william.davis@example.com (cutoff 2024-08-05). Attach the pending tasks summary, apply label, and record the follow-up timestamp."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_018",
        instruction=(
            "Coordinate sending a one-week onboarding checklist reminder for the employee at sofia.martinez@example.com (cutoff 2024-08-19). Attach the pending tasks summary, label the email, record the follow-up timestamp, and mark pending items as reminded."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_019",
        instruction=(
            "Handle a one-week onboarding checklist reminder for the employee at lily.zhang@example.com (cutoff 2024-09-02). Include the pending tasks summary as an attachment, appropriately label the email, and log the follow-up timestamp."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_020",
        instruction=(
            "Coordinate the sending of a one-week onboarding checklist reminder for the employee starting on 2024-09-02 at raj.patel@example.com. Add the pending tasks summary as an attachment, label the email, note the follow-up timestamp, and indicate that pending items have been reminded."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_021",
        instruction=(
            "Handle the creation and dispatch of a basic onboarding packet for the employee at emma.thompson@example.com, whose start date is 2024-08-05. Tailor the onboarding template, append standard documents, dispatch the email, then update the status to 'Packet Sent' and preserve the welcome email id."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_022",
        instruction=(
            "Handle the creation and dispatch of a basic onboarding packet for the employee at jordan.williams@example.com, whose start date is 2024-08-19. Tailor the onboarding template, append standard documents, dispatch the email, then update the status to 'Packet Sent' and preserve the welcome email id."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="RenderOnboardingWelcome", kwargs={"candidate_id": "cand_5", "candidate_name": "Jordan Williams", "role_title": "DevOps Engineer",
                                                             "start_date": "2024-08-19"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md",
                "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "onboarding",
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Welcome to the Team",
                "candidate_id": "cand_5",
                "attachment_file_paths": [
                    "/library/Company-Policies.pdf",
                    "/library/Benefits-Guide.pdf",
                    "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_5", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_023",
        instruction=(
            "Handle the creation and dispatch of an equipment provisioning request for the employee at emma.thompson@example.com, starting on 2024-08-05. Engage with the existing request, send an email to it-assets@example.com, then update the request status to Sent and assign the label Asset-Request to the email."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_024",
        instruction=(
            "Facilitate the setting up and sending of an equipment provisioning request for the employee at jordan.williams@example.com, with a start date of 2024-08-19. Proceed with the existing request, contact it-assets@example.com, then change the request's status to Sent and apply the email label Asset-Request."
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
                "candidate_id": "cand_5", "subject": "Asset Provisioning – Jordan Williams",
                "add_names": ["Asset-Request"]})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_025",
        instruction=(
            "Handle the verification of day-1 access for the employee at emma.thompson@example.com (start 2024-08-05). Coordinate the sending of an orientation invite and inform IT if any checks are unsuccessful."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_2", "checks": [{"system_name": "Email", "status": "pass"},
                                                                                             {"system_name": "SSO", "status": "pass"},
                                                                                             {"system_name": "Slack", "status": "pass"},
                                                                                             {"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite", "to_emails": ["emma.thompson@example.com"], "subject": "Day-1 Orientation",
                                               "candidate_id": "cand_2"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_2", "orientation_invite_ts": "2025-09-01T00:00:00Z", "message_id": "msg_15"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_026",
        instruction=(
            "Ensure the verification of day-1 access for the employee at jordan.williams@example.com (start 2024-08-19). Dispatch an orientation invite and notify IT if any checks do not pass."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_027",
        instruction=(
            "Handle sending a one-week onboarding checklist reminder to the employee at emma.thompson@example.com (cutoff 2024-08-12). Attach the summary of pending tasks, label the email appropriately, log the follow-up timestamp, and note pending items as reminded."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_028",
        instruction=(
            "Coordinate sending a one-week onboarding checklist reminder to the employee at jordan.williams@example.com (cutoff 2024-08-26). Include the pending tasks summary, categorize the email with a label, capture the follow-up timestamp, and indicate pending items as reminded."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_029",
        instruction=(
            "Handle the current asset request associated with emma.thompson@example.com (start 2024-08-05)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {"request_id": "asset_req_1", "asset_type": "Laptop", "status": "Requested"}}),
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

            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_1", "status": "allocated"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_030",
        instruction=(
            "Coordinate the equipment provisioning for the employee at william.davis@example.com (start 2024-07-29) by processing the existing request. Dispatch the provisioning email, record its message id on the request, tag the email as Asset-Request, and log an allocation receipt in the database."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_2"}),
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_031",
        instruction=(
            "Handle equipment provisioning completion for sofia.martinez@example.com (start 2024-08-12) according to policy: construct the request artifact and send an email to IT with the subject 'Asset Provisioning – Sofia Martinez' and include the mandatory 'Asset-Request' label; document the email id and label the request as Sent; assign the next available inventory and note down the allocation receipt."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_032",
        instruction=(
            "Manage finalization of equipment provisioning for jordan.williams@example.com (start 2024-08-19) in line with policy: assemble the request artifact and notify IT via email using 'Asset Provisioning – Jordan Williams' including the mandated 'Asset-Request' label; log the email id and categorize the request as Sent; allocate the nearest available inventory, draft an allocation receipt, and finalize the request."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                "payload": {"request_id": "asset_req_4"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Jordan Williams",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_4",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                "payload": {
                    "request_id": "asset_req_4",
                    "status": "Sent",
                    "email_message_id": "msg_15",
                    "inventory_checked_flag": True,
                    "asset_tag": "LT-DELL-001"}}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_4",
                "status": "Completed",
                "email_message_id": "msg_15"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_033",
        instruction=(
            "Handle the equipment provisioning for the employee at raj.patel@example.com (start 2024-09-02) by managing the existing request and assigning inventory. Dispatch the provisioning email, record its message id on the request, label the email Asset-Request, assign the first available tag for the requested type, and log an allocation receipt to the database."
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
        outputs=[]

    ),

    Task(
        annotator="v5",
        user_id="task_034",
        instruction=(
            "Coordinate equipment provisioning for william.davis@example.com (start 2024-07-29) following the Equipment Provisioning policy: draft the request artifact, email IT with the fixed subject 'Asset Provisioning – William Davis' including the mandatory 'Asset-Request' label, document the provisioning email id and update the request to Sent, assign the first available inventory, and document an allocation receipt."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_035",
        instruction=(
            "Ensure equipment provisioning for william.davis@example.com (start 2024-07-29) according to the Equipment Provisioning policy: compile the request artifact, contact IT through email using 'Asset Provisioning – William Davis' as the subject, ensuring the JSON is attached and the 'Asset-Request' label is applied; document the email id and classify the request as Sent; assign the first available inventory and note the allocation; generate an allocation receipt and dispatch a confirmation to the employee along with the receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/asset_request.json",
                "payload": {"request_id": "asset_req_2", "asset_type": "Laptop", "status": "Requested"}}),
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
                "payload": {"request_id": "asset_req_2", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["william.davis@example.com"],
                "candidate_id": "cand_3",
                "attachment_file_paths": ["/onboarding/Peter_Jones/allocation_receipt.json"]}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_036",
        instruction=(
            "Coordinate the distribution and labeling of a one-week checklist reminder for jordan.williams@example.com (start 2024-08-19, cutoff 2024-08-26), ensure pending items are marked as reminded with the reminder email id, and log the timestamp for follow-up."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_037",
        instruction=(
            "Handle the verification of day-1 access for jordan.williams@example.com (start 2024-08-19) and issue an orientation invitation, afterwards, finalize provisioning by dispatching and labeling the request, assigning inventory, auditing attachments, and confirming labels."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_5", "checks": [{"system_name": "Email", "status": "pass"},
                                                                                             {"system_name": "SSO", "status": "pass"},
                                                                                             {"system_name": "Slack", "status": "pass"},
                                                                                             {"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "orientation_invite", "to_emails": ["jordan.williams@example.com"], "subject": "Day-1 Orientation",
                           "candidate_id": "cand_5"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_5", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                                                            "payload": {"request_id": "asset_req_4"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jordan Williams", "candidate_id": "cand_5",
                            "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus",
                   kwargs={"request_id": "asset_req_4", "status": "Sent", "candidate_id": "cand_5", "subject": "Asset Provisioning – Jordan Williams",
                            }),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_5", "subject": "Asset Provisioning – Jordan Williams",
                           "add_names": ["Asset-Request"]}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4", }),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json",
                                                         "mime_type": "application/json"}),
            Action(name="AuditAttachmentsForEmail",
                   kwargs={"candidate_id": "cand_5", "subject": "Asset Provisioning – Jordan Williams"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_038",
        instruction=(
            "Ensure the verification of day-1 access for raj.patel@example.com (start 2024-09-02), issue an orientation invitation, then finalize provisioning by dispatching and labeling the request, assigning inventory, and responding to the provisioning thread to confirm receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="RecordAccessChecks", kwargs={
                "candidate_id": "cand_7",
                "checks": [
                    {"system_name": "Email", "status": "pass"},
                    {"system_name": "SSO", "status": "pass"},
                    {"system_name": "Slack", "status": "pass"},
                    {"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "orientation_invite", "to_emails": ["raj.patel@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_7", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/asset_request.json",
                "payload": {"request_id": "asset_req_5", "candidate_id": "cand_7", "status": "Requested"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Raj Patel", "candidate_id": "cand_7",
                 "attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_5", "status": "Sent",
                "candidate_id": "cand_7", "subject": "Asset Provisioning – Raj Patel",
                }),
            Action(name="ModifyEmailLabels", kwargs={
                "candidate_id": "cand_7", "subject": "Asset Provisioning – Raj Patel",
                "add_names": ["Asset-Request"]}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5", }),
            Action(name="ReplyToEmailThread", kwargs={
                "candidate_id": "cand_7", "subject": "Asset Provisioning – Raj Patel",  "task": "acknowledge"})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_039",
        instruction=(
            "Handle the personalization and dispatch of the onboarding packet for michael.anderson@example.com (start 2024-08-01) including policy/benefits, and afterwards, send and tag a reminder for the one-week checklist (cutoff 2024-08-08)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_1",
                "file_path": "/onboarding/John_Doe/welcome_John_Doe.md",
                "mime_type": "text/markdown",
                "content_text": "# Welcome, Michael Anderson!\n\nRole: Software Engineer\nStart date: 2024-08-01\n\nWe’re excited to have you on board. Please review the attached policy and benefits guides."}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["michael.anderson@example.com"],
                "subject": "Welcome to the Team",
                "candidate_id": "cand_1",
                "attachment_file_paths": [
                    "/library/Company-Policies.pdf",
                    "/library/Benefits-Guide.pdf",
                    "/onboarding/John_Doe/welcome_John_Doe.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_1",
                "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="WritePendingTasksFile", kwargs={
                "candidate_id": "cand_1",
                "file_path": "/onboarding/John_Doe/pending_tasks.md",
                "due_date_lte": "2024-08-08"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["michael.anderson@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_1",
                "attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_1",
                "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_040",
        instruction=(
            "Coordinate the sending of a day-1 orientation invitation for lily.zhang@example.com (start 2024-08-26), followed by sending and tagging a reminder for the checklist (cutoff 2024-09-01)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "orientation_invite", "to_emails": ["lily.zhang@example.com"], "subject": "Day-1 Orientation",
                "candidate_id": "cand_6"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_6", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-01"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "checklist_reminder", "to_emails": ["lily.zhang@example.com"], "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_6",
                "attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={
                "candidate_id": "cand_6", "subject": "Pending Onboarding Tasks",
                "add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_6", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_041",
        instruction=(
            "Draft an access summary for emma.thompson@example.com (start 2024-08-05), dispatch an orientation invite, then transmit and tag a one-week checklist reminder with a cutoff of 2024-08-12, confirming the label is applied."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/access_summary.md",
                "mime_type": "text/markdown",
                "content_text": "# Access Summary (Day 1)\n\nCandidate: Emma Thompson\nStart date: 2024-08-05\n"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["emma.thompson@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_2"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_2",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="WritePendingTasksFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/pending_tasks.md",
                "due_date_lte": "2024-08-12"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["emma.thompson@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_2",
                "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"]}),
            Action(name="SearchChecklistItems", kwargs={
                "candidate_id": "cand_2",
                "status": "Pending",
                "due_date_lte": "2024-08-12"}),
            Action(name="MarkChecklistItemsReminded", kwargs={
                "item_ids": ["item_4", "item_5", "item_6", "item_7"],
                "reminder_email_message_id": "msg_16"}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_2",
                "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_042",
        instruction=(
            "Deliver day-1 orientation and manager-intro invitations for raj.patel@example.com (start 2024-09-02). Next, send out the provisioning email and verify the Asset-Request label is attached."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["raj.patel@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_7"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["raj.patel@example.com", "rachel.taylor@example.com"],
                "subject": "Manager Intro",
                "candidate_id": "cand_7"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_7",
                "orientation_invite_ts": "2025-09-01T00:00:00Z",
                "manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
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
                "email_message_id": "msg_17"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_043",
        instruction=(
            "Handle the distribution of the onboarding packet to michael.anderson@example.com (beginning 2024-08-01) followed by dispatching and marking a checklist reminder (deadline 2024-08-08)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_1",
                "file_path": "/onboarding/John_Doe/welcome_John_Doe.md",
                "mime_type": "text/markdown",
                "content_text": "# Welcome, Michael Anderson!\n\nRole: Software Engineer\nStart date: 2024-08-01\n\nWe’re excited to have you on board. Please review the attached policy and benefits guides."}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["michael.anderson@example.com"],
                "subject": "Welcome to the Team",
                "candidate_id": "cand_1",
                "attachment_file_paths": [
                    "/library/Company-Policies.pdf",
                    "/library/Benefits-Guide.pdf",
                    "/onboarding/John_Doe/welcome_John_Doe.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_1",
                "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="WritePendingTasksFile", kwargs={
                "candidate_id": "cand_1",
                "file_path": "/onboarding/John_Doe/pending_tasks.md",
                "due_date_lte": "2024-08-08"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["michael.anderson@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_1",
                "attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"]}),
            Action(name="SearchChecklistItems", kwargs={
                "candidate_id": "cand_1",
                "status": "Pending",
                "due_date_lte": "2024-08-08"}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_1",
                "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_044",
        instruction=(
            "Coordinate the mailing of the onboarding packet for jordan.williams@example.com (beginning 2024-08-19), send an orientation invitation, followed by sending and tagging a checklist reminder for one week (deadline 2024-08-26)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md",
                "mime_type": "text/markdown",
                "content_text": "# Welcome, Jordan Williams!\n\nRole: DevOps Engineer\nStart date: 2024-08-19\n\nPlease review the attached policy and benefits guides."}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Welcome to the Team",
                "candidate_id": "cand_5",
                "attachment_file_paths": [
                    "/library/Company-Policies.pdf",
                    "/library/Benefits-Guide.pdf",
                    "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_5",
                "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_5"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_5",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="WritePendingTasksFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/pending_tasks.md",
                "due_date_lte": "2024-08-26"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"] }),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_5",
                "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_045",
        instruction=(
            "Complete provisioning for raj.patel@example.com (start 2024-09-02) by dispatching the 'Asset Provisioning – Raj Patel' email, ensuring the request JSON is attached, documenting its message id within the request, tagging it with the 'Asset-Request' label, distributing inventory, and saving /onboarding/Robert_Singh/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/asset_request.json",
                "payload": {"request_id": "asset_req_5", "candidate_id": "cand_7"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Raj Patel",
                "candidate_id": "cand_7",
                "label_names": ["Asset-Request"],
                "attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_5",
                "status": "Sent",
                "email_message_id": "msg_15" }),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_046",
        instruction=(
            "Customize and send out the onboarding packet for lily.zhang@example.com (start 2024-08-26) including the policy/benefits attachment, then issue a day-1 orientation invitation and log the timestamp of the invite."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_6",
                "file_path": "/onboarding/Emily_Chen/welcome_Emily_Chen.md",
                "mime_type": "text/markdown"}),
                Action(name="GenerateAndSendEmail",
                   kwargs={"task": "onboarding", "to_emails": ["lily.zhang@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_6",
                           "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                     "/onboarding/Emily_Chen/welcome_Emily_Chen.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_6", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),

            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite", "to_emails": ["lily.zhang@example.com"], "subject": "Day-1 Orientation",
                                               "candidate_id": "cand_6"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_6", "orientation_invite_ts": "2025-09-01T00:00:00Z"})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_047",
        instruction=(
            "Handle the closure of finished checklist items for lily.zhang@example.com (start 2024-08-26), then proceed to dispatch and categorize a one-week checklist reminder with cutoff 2024-09-02."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_6", "due_date_lte": "2024-09-02"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["lily.zhang@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_6",
                           "attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_6", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded",
                   kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02", "subject": "Pending Onboarding Tasks",
                            "item_ids": []}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_6", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_048",
        instruction=(
            "Coordinate provisioning for sofia.martinez@example.com (start 2024-08-12) by dispatching and categorizing the request, assigning inventory and saving a receipt to /onboarding/Maria_Rodriguez/allocation_receipt.json, followed by sending an allocation confirmation email with subject 'Asset Allocation – Sofia Martinez'."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                "payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Sofia Martinez",
                "candidate_id": "cand_4",
                "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_3",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["sofia.martinez@example.com"],
                "subject": "Asset Allocation – Sofia Martinez",
                "candidate_id": "cand_4",
                "attachment_file_paths": ["/onboarding/Maria_Rodriguez/allocation_receipt.json"]}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_049",
        instruction=(
            "Handle a one-week checklist follow-up for jordan.williams@example.com (commencing 2024-08-19) according to the checklist policy: prepare the pending-tasks artifact for items due by 2024-08-26, dispatch a labeled reminder to the employee, tag those items as reminded using the reminder email's id, and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/pending_tasks.md",
                "due_date_lte": "2024-08-26"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={
                "item_ids": ["item_13", "item_14"],
                "reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_5",
                "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_050",
        instruction=(
            "Coordinate the existing asset request for raj.patel@example.com (beginning 2024-09-02): send the 'Asset Provisioning – Raj Patel' email, record its message id on the request, and affix the 'Asset-Request' label."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_5"}),
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
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_051",
        instruction=(
            "Close the checklist items that have been completed for lily.zhang@example.com starting on 2024-08-26, then proceed to send and label a checklist reminder with a deadline of 2024-09-02 and log the follow-up time."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_6", "due_date_lte": "2024-09-02"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02"}),
            Action(name="WritePendingTasksFile", kwargs={
                "candidate_id": "cand_6",
                "file_path": "/onboarding/Emily_Chen/pending_tasks.md",
                "due_date_lte": "2024-09-02"
            }),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["lily.zhang@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_6",
                "attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"]
            }),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_6",
                "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}
            }),
        ],

        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_052",
        instruction=(
            "Finish Emma Thompson’s provisioning by dispatching and tagging the request, distributing inventory and documenting a receipt, and respond to the provisioning thread to confirm."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_053",
        instruction=(
            "Handle the personalization and distribution of the onboarding packet for william.davis@example.com, including the attachment of policy/benefits documents (start 2024-07-29), and afterward dispatch and categorize a checklist reminder (cutoff 2024-08-05)."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md", "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "onboarding", "to_emails": ["william.davis@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_3",

                           "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                     "/onboarding/Peter_Jones/welcome_Peter_Jones.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_3", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),

            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_3", "status": "Pending", "due_date_lte": "2024-08-05"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["william.davis@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_3",
                           "attachment_file_paths": ["/onboarding/Peter_Jones/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_3", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_3", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=[]
    ),


    Task(
        annotator="v5",
        user_id="task_054",
        instruction=(
            "Coordinate the validation of day-1 access for michael.anderson@example.com (start 2024-08-01), issue an orientation invitation, send a notice regarding Access Gaps, and respond to the gaps thread to confirm receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_1", "checks": [
                {"system_name": "Email", "status": "pass"}, {"system_name": "SSO", "status": "pass"},
                {"system_name": "Slack", "status": "pass"}, {"system_name": "GitHub", "status": "fail"}]}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite", "to_emails": ["michael.anderson@example.com"], "subject": "Day-1 Orientation",
                                               "candidate_id": "cand_1"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_1", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "access_gaps", "to_emails": ["it-assets@example.com", "rachel.taylor@example.com"],
                                               "subject": "Access Gaps", "candidate_id": "cand_1"}),
            Action(name="ReplyToEmailThread",
                   kwargs={"candidate_id": "cand_1", "subject": "Access Gaps",  "task": "acknowledge"})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_055",
        instruction=(
            "You customize and dispatch the onboarding packet for michael.anderson@example.com (start 2024-08-01) including the policy/benefits, review its attachments, afterward send and tag a one-week checklist reminder (cutoff 2024-08-08) making sure the label is applied."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/welcome_John_Doe.md", "mime_type": "text/markdown"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "onboarding", "to_emails": ["michael.anderson@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_1",
                           "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                     "/onboarding/John_Doe/welcome_John_Doe.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_1", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="AuditAttachmentsForEmail",
                   kwargs={"candidate_id": "cand_1", "subject": "Welcome to the Team"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="WritePendingTasksFile",
                   kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md", "due_date_lte": "2024-08-08"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["michael.anderson@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_1",
                           "attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"],
                           "label_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ]
        ,
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_056",
        instruction=(
            "You dispatch a one-week onboarding checklist reminder for emma.thompson@example.com (cutoff 2024-08-12), tag it, identify pending items as reminded with the reminder email id, and log the follow-up timestamp."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_057",
        instruction=(
            "Dispatch and tag a one-week checklist reminder for raj.patel@example.com (start 2024-09-02, cutoff 2024-09-09), indicate pending items as reminded using the reminder email id, document the follow-up timestamp, and finalize any completed items that lack timestamps."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_058",
        instruction=(
            "Dispatch and tag a one-week checklist reminder for raj.patel@example.com (start 2024-09-02, cutoff 2024-09-09), indicate pending items as reminded using the reminder email id, document the follow-up timestamp, and finalize any completed items that lack timestamps."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_059",
        instruction=(
            "Confirm that the Asset-Request label is included in the previously dispatched provisioning email (message_id 'msg_4') for william.davis@example.com (start 2024-07-29), and update the existing asset request with this email id."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="UpdateAssetRequestStatus",
                   kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4", }),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Asset-Request"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_4", "add_names": ["Asset-Request"]})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_060",
        instruction=(
            "Dispatch day-1 orientation and manager-intro invitations for sofia.martinez@example.com (start 2024-08-12), then send her provisioning email, labeling it as Asset-Request and conduct an attachments audit."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "orientation_invite",
                "to_emails": ["sofia.martinez@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_4"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "manager_intro",
                "to_emails": ["sofia.martinez@example.com", "daniel.lee@example.com"],
                "subject": "Manager Intro",
                "candidate_id": "cand_4"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_4",
                "orientation_invite_ts": "2025-09-01T00:00:00Z",
                "manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                "payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Sofia Martinez",
                "candidate_id": "cand_4",
                "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_3",
                "status": "Sent",
                "email_message_id": "msg_17"}),
            Action(name="AuditAttachmentsForEmail", kwargs={
                "candidate_id": "cand_4",
                "subject": "Asset Provisioning – Sofia Martinez"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_061",
        instruction=(
            "Handle the sending and labeling of a one-week onboarding checklist reminder for sofia.martinez@example.com (cutoff 2024-08-19), ensure pending items are marked as reminded with the reminder email id, and note the follow-up timestamp."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_062",
        instruction=(
            "Coordinate the completion of provisioning for jordan.williams@example.com (start 2024-08-19) by dispatching and tagging the request, assigning inventory and documenting a receipt, followed by forwarding an allocation confirmation that includes the receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                "payload": {"request_id": "asset_req_4", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Jordan Williams",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_4",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Asset Allocation – Jordan Williams",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/allocation_receipt.json"]}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_063",
        instruction=(
            "Handle the creation of an access summary for jordan.williams@example.com (start 2024-08-19), proceed to send and label a one-week checklist reminder with deadline 2024-08-26, tag pending items as reminded using the reminder email id, and document the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="SummarizeAccessChecks", kwargs={"candidate_id": "cand_5"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["jordan.williams@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_5", "label_names": ["Onboarding-Reminder"],
                           "attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_13", "item_14"], "reminder_email_message_id": "msg_15",}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_064",
        instruction=(
            "Coordinate the completion of provisioning for sofia.martinez@example.com (start 2024-08-12) by sending and labeling the request, allotting inventory and generating a receipt in /onboarding/Maria_Rodriguez/allocation_receipt.json, then send out an allocation confirmation that incorporates the receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                "payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Sofia Martinez",
                "candidate_id": "cand_4",
                "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_3",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["sofia.martinez@example.com"],
                "subject": "Asset Allocation – Sofia Martinez",
                "candidate_id": "cand_4",
                "attachment_file_paths": ["/onboarding/Maria_Rodriguez/allocation_receipt.json"]}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_065",
        instruction=(
            "Complete the equipment provisioning for jordan.williams@example.com (starting on 2024-08-19) as specified by the Equipment Provisioning policy: organize the request artifact and send an email to IT using ‘Asset Provisioning – Jordan Williams’ with the mandatory ‘Asset-Request’ label; note the email ID and denote the request as Sent; assign the earliest available inventory and log the allocation receipt."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_066",
        instruction=(
            "Handle the allocation process for raj.patel@example.com (starting 2024-09-02) in accordance with the policy: assign the initial available inventory, document the allocation on the request, produce an allocation receipt, and email the employee ‘Asset Allocation – Raj Patel’ attaching the receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["raj.patel@example.com"],
                "subject": "Asset Allocation – Raj Patel",
                "candidate_id": "cand_7",
                "attachment_file_paths": ["/onboarding/Robert_Singh/allocation_receipt.json"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_5",
                "status": "Completed",
                "email_message_id": "msg_15"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_067",
        instruction=(
            "Handle equipment provisioning for emma.thompson@example.com (commencing 2024-08-05) in compliance with the Equipment Provisioning policy: assemble the request artifact, communicate with IT using 'Asset Provisioning – Emma Thompson' and make sure to include the 'Asset-Request' label; note the email ID and label the request as Sent; allocate from the first available inventory and document the allocation; produce an allocation receipt and dispatch a confirmation to the employee including the receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/asset_request.json",
                                                            "payload": {"request_id": "asset_req_1"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Emma Thompson", "candidate_id": "cand_2",
                           "attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/allocation_receipt.json", "mime_type": "application/json",
                           "payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["emma.thompson@example.com"], "subject": "Asset Allocation – Emma Thompson", "candidate_id": "cand_2",
                           "attachment_file_paths": ["/onboarding/Jane_Smith/allocation_receipt.json"]}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_068",
        instruction=(
            "Coordinate provisioning for jordan.williams@example.com (beginning 2024-08-19) by sending and labeling the request, allocating inventory and documenting a receipt to /onboarding/Alex_Thompson/allocation_receipt.json, then email an allocation confirmation to jordan.williams@example.com with subject 'Asset Allocation – Jordan Williams' and attach the receipt file."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                                                            "payload": {"request_id": "asset_req_4"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jordan Williams", "candidate_id": "cand_5",
                           "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json",
                                                         "mime_type": "application/json",
                                                         "payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001",
                                                                     "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["jordan.williams@example.com"], "subject": "Asset Allocation – Jordan Williams", "candidate_id": "cand_5",
                           "attachment_file_paths": ["/onboarding/Alex_Thompson/allocation_receipt.json"]}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_069",
        instruction=(
            "Handle the current asset request for emma.thompson@example.com (start 2024-08-05). Dispatch the 'Asset Provisioning – Emma Thompson' email, record its message id with the request, tag with 'Asset-Request', assign an available asset, draft /onboarding/Jane_Smith/allocation_receipt.json, and dispatch 'Asset Allocation – Emma Thompson' with the attached receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/asset_request.json",
                                                            "payload": {"request_id": "asset_req_1"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Emma Thompson", "candidate_id": "cand_2",
                           "attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/allocation_receipt.json", "mime_type": "application/json",
                           "payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["emma.thompson@example.com"], "subject": "Asset Allocation – Emma Thompson", "candidate_id": "cand_2",
                           "attachment_file_paths": ["/onboarding/Jane_Smith/allocation_receipt.json"]}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_070",
        instruction=(
            "Manage the ongoing asset request for william.davis@example.com (start 2024-07-29). Send out the 'Asset Provisioning – William Davis' email, capture its message id on the request, apply the 'Asset-Request' label, assign a free asset, generate /onboarding/Peter_Jones/allocation_receipt.json, and transmit 'Asset Allocation – William Davis' with the receipt attached."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_071",
        instruction=(
            "Handle the existing asset request for sofia.martinez@example.com (start 2024-08-12). Prepare the request and email IT using 'Asset Provisioning – Sofia Martinez' with the necessary 'Asset-Request' label; document the email id and mark the request Sent; assign the first available inventory and create /onboarding/Maria_Rodriguez/allocation_receipt.json; afterward, deliver an allocation confirmation email to sofia.martinez@example.com with the subject 'Asset Allocation – Sofia Martinez' including the receipt."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_072",
        instruction=(
            "Coordinate the handling of the current asset request for jordan.williams@example.com (start 2024-08-19). Dispatch the 'Asset Provisioning – Jordan Williams' email with the request JSON attached, save its message id on the request, apply the 'Asset-Request' label, allocate a suitable asset, and generate /onboarding/Alex_Thompson/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                                                            "payload": {"request_id": "asset_req_4"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jordan Williams", "candidate_id": "cand_5",
                           "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json",
                                                         "mime_type": "application/json",
                                                         "payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001",
                                                                     "asset_type": "Laptop"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_073",
        instruction=(
            "Manage the current asset request for raj.patel@example.com (start 2024-09-02). Dispatch the 'Asset Provisioning – Raj Patel' email, log its message id on the request, tag it with the 'Asset-Request' label, assign a free asset, create /onboarding/Robert_Singh/allocation_receipt.json, and dispatch the 'Asset Allocation – Raj Patel' confirmation with the receipt included."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/asset_request.json",
                                                            "payload": {"request_id": "asset_req_5"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Raj Patel", "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"], "label_names": ["Asset-Request"],
                           "date_ts": "2025-09-01T00:00:00Z"}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_5", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_5"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/allocation_receipt.json", "mime_type": "application/json",
                           "payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["raj.patel@example.com"], "subject": "Asset Allocation – Raj Patel", "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/allocation_receipt.json"]}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_074",
        instruction=(
            "Administer the current asset request for emma.thompson@example.com (start 2024-08-05). Transmit the 'Asset Provisioning – Emma Thompson' email, record its message id on the request, tag it with the 'Asset-Request' label, assign a free asset, and produce /onboarding/Jane_Smith/allocation_receipt.json."
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
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001"}
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_075",
        instruction=(
            "Manage the current asset request for william.davis@example.com (start 2024-07-29). Dispatch the 'Asset Provisioning – William Davis' email, record its message id on the request, assign the 'Asset-Request' label, and document /onboarding/Peter_Jones/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json",
                                                            "payload": {"request_id": "asset_req_2"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – William Davis", "candidate_id": "cand_3",
                           "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="WriteOnboardingFile",
                   kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/allocation_receipt.json", "mime_type": "application/json",
                           "payload": {"request_id": "asset_req_2"}}),
        ]
        ,
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_076",
        instruction=(
            "Dispatch the 'Asset Provisioning – Emma Thompson' email for emma.thompson@example.com (start 2024-08-05), record its message id on the request, and assign the 'Asset-Request' label."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {"request_id": "asset_req_1"}
            }),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Emma Thompson",
                "candidate_id": "cand_2",
                "attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"],
                "label_names": ["Asset-Request"]
            }),
            Action(name="UpdateAssetRequestStatus", kwargs={
                "request_id": "asset_req_1",
                "status": "Sent",
                "email_message_id": "msg_15"
            }),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_077",
        instruction=(
            "Handle the fulfillment of the 'Asset-Request' in 'Asset Provisioning – William Davis' for william.davis@example.com (start 2024-07-29) and respond to the provisioning thread to confirm receipt."
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
            Action(name="ReplyToEmailThread", kwargs={
                "candidate_id": "cand_3",
                "thread_id": "msg_15",
                "subject": "Asset Provisioning – William Davis",
                "task": "acknowledge"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_078",
        instruction=(
            "Finalize closed checklist items for jordan.williams@example.com (start 2024-08-19), then dispatch and categorize a checklist alert (cutoff 2024-08-26) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_5", "due_date_lte": "2024-08-26"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md", "due_date_lte": "2024-08-26"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "checklist_reminder","to_emails": ["jordan.williams@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_13", "item_14"], "reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_079",
        instruction=(
            "Handle the sending of the 'Asset Provisioning – Sofia Martinez' email to sofia.martinez@example.com (start 2024-08-12), record its message id in the request, and attach the 'Asset-Request' label."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                                                            "payload": {"request_id": "asset_req_3"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Sofia Martinez", "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                                                            "payload": {"request_id": "asset_req_3", "status": "Sent",
                                                                        "email_message_id": "msg_15"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_080",
        instruction=(
            "Coordinate the dispatch and labeling of a one-week checklist reminder for michael.anderson@example.com (start 2024-08-01, cutoff 2024-08-08) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["michael.anderson@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_1", "label_names": ["Onboarding-Reminder"],
                           "attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_081",
        instruction=(
            "Dispatch a day-1 orientation invite to michael.anderson@example.com (start 2024-08-01), subsequently dispatch and tag a one-week checklist reminder (cutoff 2024-08-08) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "michael.anderson@example.com", "start_date": "2024-08-01"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "orientation_invite", "to_emails": ["michael.anderson@example.com"], "subject": "Day-1 Orientation",
                                               "candidate_id": "cand_1"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_1", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["michael.anderson@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_1",
                           "attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels",
                   kwargs={"candidate_id": "cand_1", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_082",
        instruction=(
            "Customize and send the onboarding packet for lily.zhang@example.com (start 2024-08-26) with attached policy/benefits, then dispatch and tag a one-week checklist reminder (cutoff 2024-09-02) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_6",
                "file_path": "/onboarding/Emily_Chen/welcome_Emily_Chen.md",
                "mime_type": "text/markdown",
                "content_text": "# Welcome, Lily Zhang!\n\nRole: Marketing Specialist\nStart date: 2024-08-26\n\nWe’re excited to have you onboard. Please review the attached policy and benefits guides to prepare for Day 1."}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["lily.zhang@example.com"],
                "subject": "Welcome to the Team",
                "candidate_id": "cand_6",
                "attachment_file_paths": [
                    "/library/Company-Policies.pdf",
                    "/library/Benefits-Guide.pdf",
                    "/onboarding/Emily_Chen/welcome_Emily_Chen.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_6",
                "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="WritePendingTasksFile", kwargs={
                "candidate_id": "cand_6",
                "file_path": "/onboarding/Emily_Chen/pending_tasks.md",
                "due_date_lte": "2024-09-02"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["lily.zhang@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_6",
                "attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_6",
                "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_083",
        instruction=(
            "Handle the current asset request for sofia.martinez@example.com (start 2024-08-12): dispatch the 'Asset Provisioning – Sofia Martinez' email, register its id on the request, apply the 'Asset-Request' label, allocate an available asset, and create /onboarding/Maria_Rodriguez/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_3"}),
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
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_084",
        instruction=(
            "Customize and send the onboarding packet for emma.thompson@example.com (start 2024-08-05) with the standard policy and benefits attachments, log the welcome email id, and tag the candidate as 'Packet Sent'. Afterwards, send a day-1 orientation invite."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md",
                "mime_type": "text/markdown",
                "content_text": "# Welcome, Emma Thompson!\n\nRole: Product Manager\nStart date: 2024-08-05\n\nWe’re excited to have you join us. Please review the attached policy and benefits guides to prepare for Day 1."}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["emma.thompson@example.com"],
                "subject": "Welcome to the Team",
                "candidate_id": "cand_2",
                "attachment_file_paths": [
                    "/library/Company-Policies.pdf",
                    "/library/Benefits-Guide.pdf",
                    "/onboarding/Jane_Smith/welcome_Jane_Smith.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_2",
                "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"} }),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["emma.thompson@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_2"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_2",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_085",
        instruction=(
            "Handle the dispatch of a one-week checklist reminder to william.davis@example.com (start 2024-07-29, cutoff 2024-08-05) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_3", "status": "Pending", "due_date_lte": "2024-08-05"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={"task": "checklist_reminder", "to_emails": ["william.davis@example.com"],
                        "subject": "Pending Onboarding Tasks", "candidate_id": "cand_3",  "attachment_file_paths": ["/onboarding/Peter_Jones/pending_tasks.md"]}),
            Action(name="ModifyEmailLabels", kwargs={"candidate_id": "cand_3", "subject": "Pending Onboarding Tasks",  "add_names": ["Onboarding-Reminder"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={"candidate_id": "cand_3", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_086",
        instruction=(
            "Coordinate the sending of day-1 orientation and manager-intro invites to raj.patel@example.com (start 2024-09-02) and log the invite timestamps."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "raj.patel@example.com", "start_date": "2024-09-02"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["raj.patel@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_7"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_7",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["raj.patel@example.com", "rachel.taylor@example.com"],
                "subject": "Manager Intro",
                "candidate_id": "cand_7"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_7",
                "manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_087",
        instruction=(
            "Handle the 'Asset Provisioning – Jordan Williams' email for jordan.williams@example.com (start 2024-08-19), ensure its id is stored on the request, attach the 'Asset-Request' label, and record /onboarding/Alex_Thompson/allocation_receipt.json."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                                                            "payload": {"request_id": "asset_req_4"}}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jordan Williams", "candidate_id": "cand_5",
                           "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"], "add_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json",
                                                         "mime_type": "application/json", "payload": {"request_id": "asset_req_4"}}),
        ],
    outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_088",
        instruction=(
            "Make sure the 'Asset-Request' label is applied to the 'Asset Provisioning – Emma Thompson' email for emma.thompson@example.com (start 2024-08-05), then respond to the provisioning thread to confirm receipt."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_1"}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Asset-Request"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_3", "add_names": ["Asset-Request"]}),
            Action(name="ReplyToEmailThread",
                   kwargs={"candidate_id": "cand_2", "thread_id": "msg_3", "subject": "Asset Provisioning – Emma Thompson"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_089",
        instruction=(
            "You should close completed checklist items for sofia.martinez@example.com (start 2024-08-12), then handle sending and labeling a checklist reminder (cutoff 2024-08-19) and record the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="CloseCompletedChecklistItems", kwargs={"candidate_id": "cand_4", "due_date_lte": "2024-08-19"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "checklist_reminder", "to_emails": ["sofia.martinez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4", "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"],
                           "label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ]
        ,
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_090",
        instruction=(
            "Please send and label a one-week checklist reminder for jordan.williams@example.com (start 2024-08-19, cutoff 2024-08-26) and ensure the follow-up timestamp is recorded."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "checklist_reminder",
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={
                "item_ids": ["item_13", "item_14"],
                "reminder_email_message_id": "msg_15"}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_091",
        instruction=(
            "Handle the recording of day-1 access checks for lily.zhang@example.com (start 2024-08-26) with results: Email=pass, SSO=fail, Slack=pass, GitHub=pass. Dispatch a day-1 orientation invite, then inform IT about any access discrepancies."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "lily.zhang@example.com", "start_date": "2024-08-26"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_6", "checks": [
                {"system_name": "Email", "status": "pass"},
                {"system_name": "SSO", "status": "fail"},
                {"system_name": "Slack", "status": "pass"},
                {"system_name": "GitHub", "status": "pass"}
            ]}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["lily.zhang@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_6"
            }),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_6",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"
            }),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Access Gaps",
                "candidate_id": "cand_6"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_092",
        instruction=(
            "Document day-1 access checks for emma.thompson@example.com (start 2024-08-05): Email=pass, SSO=fail, Slack=pass, GitHub=pass. Next, send out a day-1 orientation invite and log the invite's timestamp, notifying IT about any access issues."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_2", "checks": [
                {"system_name": "Email", "status": "pass"},
                {"system_name": "SSO", "status": "fail"},
                {"system_name": "Slack", "status": "pass"},
                {"system_name": "GitHub", "status": "pass"}]}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["emma.thompson@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_2"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_2",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Access Gaps",
                "candidate_id": "cand_2"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_093",
        instruction=(
            "Handle the inclusion of the 'Asset-Request' label on 'Asset Provisioning – William Davis' for william.davis@example.com (start 2024-07-29), amend the current request by adding the provisioning email id, and document an attachments audit."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_2"}),
            Action(name="GetOrCreateEmailLabel", kwargs={"name": "Asset-Request"}),
            Action(name="ModifyEmailLabels", kwargs={"message_id": "msg_4", "add_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4"}),
            Action(name="WriteAssetRequestFile", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json",
                                                            "payload": {"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4"}}),
            Action(name="AuditAttachmentsForEmail", kwargs={"candidate_id": "cand_3", "subject": "Asset Provisioning – William Davis"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_094",
        instruction=(
            "Coordinate the dispatch of day-1 orientation and manager-intro invites for sofia.martinez@example.com (start 2024-08-12) and log the timestamps for both invitations."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "sofia.martinez@example.com", "start_date": "2024-08-12"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "orientation_invite", "to_emails": ["sofia.martinez@example.com"], "subject": "Day-1 Orientation",
                           "candidate_id": "cand_4"}),
            Action(name="GenerateAndSendEmail",
                   kwargs={"task": "manager_intro", "to_emails": ["sofia.martinez@example.com", "daniel.lee@example.com"], "subject": "Manager Intro",
                           "candidate_id": "cand_4"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={"candidate_id": "cand_4", "orientation_invite_ts": "2025-09-01T00:00:00Z",
                                                                      "manager_intro_invite_ts": "2025-09-01T00:00:00Z"})
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_095",
        instruction=(
            "Handle the review and emailing of the asset request for 'Asset Provisioning – Jordan Williams' addressed to jordan.williams@example.com (start 2024-08-19), and allocate an available asset."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="ReadAssetRequest", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteAssetRequestFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                "payload": {"request_id": "asset_req_4", "asset_type": "Laptop", "status": "Completed"}
            }),
            Action(name="GenerateAndSendEmail",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jordan Williams", "candidate_id": "cand_5",
                           "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="UpdateAssetRequestStatus", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="AllocateFirstAvailableAsset", kwargs={"request_id": "asset_req_4"}),
            Action(name="WriteOnboardingFile", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json",
                                                         "mime_type": "application/json",
                                                         "payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001",
                                                                     "asset_type": "Laptop"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_096",
        instruction=(
            "Dispatch and annotate a one-week checklist reminder to emma.thompson@example.com (start 2024-08-05, cutoff 2024-08-12) and log the follow-up timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "emma.thompson@example.com", "start_date": "2024-08-05"}),
            Action(name="SearchChecklistItems", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="WritePendingTasksFile", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "checklist_reminder",
                "to_emails": ["emma.thompson@example.com"],
                "subject": "Pending Onboarding Tasks",
                "candidate_id": "cand_2",
                "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"],
                "label_names": ["Onboarding-Reminder"]}),
            Action(name="MarkChecklistItemsReminded", kwargs={
                "item_ids": ["item_4", "item_5", "item_6", "item_7"],
                "reminder_email_message_id": "msg_15",
                "updated_ts": "2025-09-01T00:00:00Z"}),
            Action(name="UpdateCandidateStatusFields",
                   kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_097",
        instruction=(
            "Handle the day-1 access verification for william.davis@example.com (start 2024-07-29): Email=pass, SSO=pass, Slack=pass, GitHub=pass. Afterwards, dispatch a day-1 orientation invite and log the invite timestamp."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "william.davis@example.com", "start_date": "2024-07-29"}),
            Action(name="RecordAccessChecks", kwargs={"candidate_id": "cand_3", "checks": [
                {"system_name": "Email", "status": "pass"},
                {"system_name": "SSO", "status": "pass"},
                {"system_name": "Slack", "status": "pass"},
                {"system_name": "GitHub", "status": "pass"}
            ]}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "orientation_invite",
                "to_emails": ["william.davis@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_3"
            }),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_3",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_098",
        instruction=(
            "Manage the current asset request for sofia.martinez@example.com (start 2024-08-12): verify that the 'Asset-Request' label appears on the existing provisioning email (msg_9), update the request with that email_message_id and change its status to Sent, assign the first available asset, and review the attachments of the provisioning email."
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
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_099",
        instruction=(
            "Handle personalizing and dispatching the onboarding packet for jordan.williams@example.com (start 2024-08-19) with policy/benefits enclosed, then send a day-1 orientation invitation and document the necessary updates."
        ),
        actions=[
            Action(name="FindCandidateByEmail", kwargs={"candidate_email": "jordan.williams@example.com", "start_date": "2024-08-19"}),
            Action(name="ReadOnboardingFile", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="WriteOnboardingFile", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md",
                "mime_type": "text/markdown",
                "content_text":
                    "# Welcome, Jordan Williams!\n\n"
                    "Role: DevOps Engineer\n"
                    "Start date: 2024-08-19\n\n"
"## Initial Setup\n"
                    "- Review the attached Company Policies and Benefits Guide.\n"
                    "- Bring a valid photo ID for security badging.\n"
                    "- Your laptop pickup will be coordinated by IT on Day 1.\n\n"
"## Agenda for Day 1\n"
                    "- Orientation session\n"
                    "- Account setup (SSO, email, Slack)\n"
                    "- Team introductions\n\n"
                    "If you have any questions before your start date, reply to this email and HR will assist."
            }),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "onboarding",
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Welcome to the Team",
                "candidate_id": "cand_5",
                "attachment_file_paths": [
                    "/library/Company-Policies.pdf",
                    "/library/Benefits-Guide.pdf",
                    "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="UpdateCandidateStatusFields", kwargs={
                "candidate_id": "cand_5",
                "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="GenerateAndSendEmail", kwargs={
                "task": "orientation_invite",
                "to_emails": ["jordan.williams@example.com"],
                "subject": "Day-1 Orientation",
                "candidate_id": "cand_5"}),
            Action(name="UpdateCandidateInviteTimestamps", kwargs={
                "candidate_id": "cand_5",
                "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="task_100",
        instruction=(
            "Organize and tag a one-week checklist reminder for raj.patel@example.com (start 2024-09-02, cutoff 2024-09-09). Note the pending items as reminded using the reminder email id, and log the follow-up timestamp."
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
        outputs=[]
    ),

]