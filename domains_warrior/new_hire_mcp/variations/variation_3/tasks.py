from domains.dto import Task, Action

TASKS = [

    Task(
        annotator="R",
        user_id="onboarding_ds_002",
        instruction=(
            "You approve candidate cand_5 asset requests req_501 and req_502, assign assets LT-005B and PH-005B, complete checklist item check_502, "
            "verify onboarding file Benefits-Guide.pdf, apply label 'Ready' to email email_502, log all actions, and update candidate record."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-005B", "candidate_id": "cand_5"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_502", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/Benefits-Guide.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_502", "label_id": "label_Ready"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Assets assigned for cand_5", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.LT-005B.status=Assigned | asset.PH-005B.status=Assigned | checklist_item.check_502.status=Completed | onboarding_files.Benefits-Guide.pdf.status=Verified | email.email_502.labels=label_Ready | log.ASSET_ASSIGNED.message=Assets assigned for cand_5 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_5 | candidate.cand_5.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_003",
        instruction=(
            "You complete full onboarding for candidate cand_4 with multi-step workflow: approve asset requests, assign multiple assets, "
            "complete checklist items, approve access checks, update onboarding files, label emails, record terminal logs, "
            "and ensure candidate status reflects full completion."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_401", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_402", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-004", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-004", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-005", "candidate_id": "cand_4"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide_cand4.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan_cand4.pdf", "updates": {"verified": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_401", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_402", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_401", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_401", "label_id": "label_Welcome"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_402", "label_id": "label_Policy"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_401 and req_402 approved", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, and mouse assigned", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome' and 'Policy'", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[
            "asset_request.req_401.status=Approved | asset_request.req_402.status=Approved | asset.PH-LAPTOP-004.status=Assigned | asset.PH-IPHONE-004.status=Assigned | asset.ACC-MOUSE-005.status=Assigned | onboarding_files.welcome_guide_cand4.laptop_assigned=True | onboarding_files.welcome_guide_cand4.phone_assigned=True | onboarding_files.id_scan_cand4.verified=True | checklist.check_401.status=Completed | checklist.check_402.status=Completed | access_check.access_401.status=Approved | email.email_401.labels=label_Welcome | email.email_402.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_401 and req_402 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, and mouse assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome' and 'Policy' | candidate.cand_4.onboarding_status=OnboardingCompleted"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_004",
        instruction=(
            "You process both laptop and phone requests for candidate cand_4, approve them, assign the corresponding assets, "
            "and update the onboarding file to reflect both device assignments. You also update the candidate’s status "
            "to 'AssetsReady' and ensure logs capture approval and assignment events for each device."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_401", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_402", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-004", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-004", "candidate_id": "cand_4"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/cand_4_onboarding.json",
                                                          "updates": {"laptop_assigned": True,
                                                                      "phone_assigned": True}}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Requests req_401 and req_402 approved",
                           "candidate_id": "cand_4"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "PH-LAPTOP-004 assigned",
                           "candidate_id": "cand_4"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-004 assigned",
                           "candidate_id": "cand_4"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_401.status=Approved | asset_request.req_402.status=Approved | asset.PH-LAPTOP-004.status=Assigned | asset.PH-IPHONE-004.status=Assigned | onboarding_files.cand_4.laptop_assigned=True | onboarding_files.cand_4.phone_assigned=True | log.ASSET_REQUEST_APPROVED.message=Requests req_401 and req_402 approved | log.LAPTOP_ASSIGNED.message=PH-LAPTOP-004 assigned | log.PHONE_ASSIGNED.message=PH-IPHONE-004 assigned | candidate.cand_4.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_005",
        instruction=(
            "You reassign assets for candidate cand_6: release the old laptop LT-OLD-001, and assign the new laptop LT-NEW-006 along with the new phone PH-NEW-006. "
            "Update asset requests req_601 and req_602 to 'Completed'. Remove the old access checks access_601 and access_602, and add new access checks access_603 and access_604. "
            "Attach the documents Company-Policies.pdf and Benefits-Guide.pdf. Apply the label 'AssetChange' to email email_601, and record terminal logs for all these changes."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-OLD-001"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-NEW-006", "candidate_id": "cand_6"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-NEW-006", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_602", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_601"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_602"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_604", "status": "Pending"}}),
            Action(name="add_attachment",
                   kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="add_attachment", kwargs={
                "attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_601", "label_id": "label_AssetChange"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-OLD-001.status=Available | asset.LT-NEW-006.status=Assigned | asset.PH-NEW-006.status=Assigned | asset_request.req_601.status=Completed | asset_request.req_602.status=Completed | access_check.access_601=Removed | access_check.access_602=Removed | access_check.access_603.status=Pending | access_check.access_604.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_601.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_6 | log.ACCESS_UPDATED.message=Access checks updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_006",
        instruction=(
            "You update candidate cand_5's asset requests and onboard phone devices. End state: "
            "asset requests marked 'Approved'; phones assigned; terminal logs 'PHONE_ASSIGNED' and 'ASSET_REQUEST_APPROVED' exist."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_5", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-003", "candidate_id": "cand_5"}),
            Action(name="update_asset", kwargs={"asset_tag": "PH-IPHONE-003", "updates": {"status": "Assigned"}}),
            Action(name="update_onboarding_file", kwargs={"candidate_id": "cand_5", "updates": {"phone_assigned": True}}),
            Action(name="record_terminal_log", kwargs={"event_type": "PHONE_ASSIGNED", "message": "Phone assigned to cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_5 approved"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_5.status=Approved | asset.PH-IPHONE-003.status=Assigned | onboarding_files.phone_assigned=True | log.PHONE_ASSIGNED.message=Phone assigned to cand_5 | log.ASSET_REQUEST_APPROVED.message=Asset request req_5 approved | candidate.cand_5.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_007",
        instruction=(
            "For candidate cand_2, you assign laptop LT-002B, complete asset request req_202, update checklist check_202 to Completed, "
            "remove attachment Policies.pdf, add Training-Guide.pdf, verify file id_card.pdf, "
            "apply email label 'Training' to email email_202, add access check access_202, "
            "log updates, and set candidate training_status to InProgress."
        ),
        actions=[
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="remove_attachment", kwargs={"attachment_id": "attach_3"}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_4", "file_name": "Training-Guide.pdf"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_card.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_202", "label_id": "label_Training"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_202", "status": "Pending"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop assigned for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist item completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"training_status": "InProgress"}}),
        ],
        outputs=[
            "asset.LT-002B.status=Assigned | asset_request.req_202.status=Completed | checklist_item.check_202.status=Completed | attachment.Policies.pdf.removed=True | attachment.Training-Guide.pdf.added=True | onboarding_files.id_card.pdf.status=Verified | email.email_202.labels=label_Training | access_check.access_202.status=Pending | log.ASSET_ASSIGNED.message=Laptop assigned for cand_2 | log.CHECKLIST_COMPLETED.message=Checklist item completed for cand_2 | candidate.cand_2.training_status=InProgress"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_008",
        instruction=(
            "You complete multi-step onboarding for candidate cand_3: approve all asset requests, assign assets including laptop, phone, and peripherals, "
            "complete checklist items, approve access checks, update onboarding files, apply multiple email labels, and record terminal logs. "
            "End state: all tasks completed and candidate status updated."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_301", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_302", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-003", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-003", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-004", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-KEYBOARD-003", "candidate_id": "cand_3"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide_cand3.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan_cand3.pdf", "updates": {"verified": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/policy_ack_cand3.pdf", "updates": {"acknowledged": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_301", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_302", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_301", "label_id": "label_Welcome"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_302", "label_id": "label_Policy"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_301 and req_302 approved", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, mouse, and keyboard assigned", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome' and 'Policy'", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[
            "asset_request.req_301.status=Approved | asset_request.req_302.status=Approved | asset.PH-LAPTOP-003.status=Assigned | asset.PH-IPHONE-003.status=Assigned | asset.ACC-MOUSE-004.status=Assigned | asset.ACC-KEYBOARD-003.status=Assigned | onboarding_files.welcome_guide_cand3.laptop_assigned=True | onboarding_files.welcome_guide_cand3.phone_assigned=True | onboarding_files.id_scan_cand3.verified=True | onboarding_files.policy_ack_cand3.acknowledged=True | checklist.check_301.status=Completed | checklist.check_302.status=Completed | access_check.access_301.status=Approved | access_check.access_302.status=Approved | email.email_301.labels=label_Welcome | email.email_302.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_301 and req_302 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, mouse, and keyboard assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome' and 'Policy' | candidate.cand_3.onboarding_status=OnboardingCompleted"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_010",
        instruction=(
            "You approve cand_3's laptop and monitor requests, assign assets, update onboarding files to reflect assignments, and log events."
            "End state: requests approved; LT-DELL-002 and MON-LG-001 assigned; onboarding file shows laptop_assigned=True and monitor_assigned=True; logs capture all events."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_103", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-002", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "MON-LG-001", "candidate_id": "cand_3"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Peter_Jones/asset_request.json",
                                                          "updates": {"laptop_assigned": True,
                                                                      "monitor_assigned": True}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED",
                                                       "message": "Asset requests req_102 and req_103 approved",
                                                       "candidate_id": "cand_3"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "LT-DELL-002 assigned",
                           "candidate_id": "cand_3"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "MONITOR_ASSIGNED", "message": "MON-LG-001 assigned",
                           "candidate_id": "cand_3"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_102.status=Approved | asset_request.req_103.status=Approved | asset.LT-DELL-002.status=Assigned | asset.MON-LG-001.status=Assigned | onboarding_files.cand_3.laptop_assigned=True | onboarding_files.cand_3.monitor_assigned=True | log.ASSET_REQUEST_APPROVED.message=Asset requests req_102 and req_103 approved | log.LAPTOP_ASSIGNED.message=LT-DELL-002 assigned | log.MONITOR_ASSIGNED.message=MON-LG-001 assigned | candidate.cand_3.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_011",
        instruction=(
            "For candidate cand_1, you release old laptop LT-001A, assign new laptop LT-001B, complete asset requests req_101 and req_102, "
            "remove access checks access_101 and access_102, add new access check access_105, attach Company-Policies.pdf, "
            "apply label 'AssetChange' to email email_101, log all changes, update candidate record, and verify onboarding file Passport.pdf."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-001B", "candidate_id": "cand_1"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_101"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_102"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_105", "status": "Pending"}}),
            Action(name="add_attachment",
                   kwargs={"attachment": {"attachment_id": "attach_3", "file_name": "Company-Policies.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_101", "label_id": "label_AssetChange"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_1",
                           "candidate_id": "cand_1"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_1",
                           "candidate_id": "cand_1"}),
            Action(name="update_onboarding_file",
                   kwargs={"file_path": "files/Passport.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_1", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-001A.status=Available | asset.LT-001B.status=Assigned | asset_request.req_101.status=Completed | asset_request.req_102.status=Completed | access_check.access_101=Removed | access_check.access_102=Removed | access_check.access_105.status=Pending | attachment.Company-Policies.pdf.added=True | email.email_101.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_1 | log.ACCESS_UPDATED.message=Access checks updated for cand_1 | onboarding_files.Passport.pdf.status=Verified | candidate.cand_1.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_012",
        instruction=(
            "For candidate cand_4, you release old laptop LT-004A, assign new laptop LT-004B, complete asset request req_401, "
            "remove access checks access_401 and access_402, add new access checks access_405 and access_406, "
            "attach Company-Policies.pdf, apply email label 'AssetUpdate' to email email_401, log changes, update candidate record, "
            "and verify onboarding file ID-Card.pdf."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-004A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-004B", "candidate_id": "cand_4"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_401", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_401"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_402"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_405", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_406", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Company-Policies.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_401", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/ID-Card.pdf", "updates": {"status": "Verified"}})
        ],
        outputs=[
            "asset.LT-004A.status=Available | asset.LT-004B.status=Assigned | asset_request.req_401.status=Completed | access_check.access_401=Removed | access_check.access_402=Removed | access_check.access_405.status=Pending | access_check.access_406.status=Pending | attachment.Company-Policies.pdf.added=True | email.email_401.labels=label_AssetUpdate | log.ASSET_UPDATED.message=Assets updated for cand_4 | onboarding_files.ID-Card.pdf.status=Verified | candidate.cand_4.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_013",
        instruction=(
            "You finalize onboarding for candidate cand_6: approve asset requests req_601, req_602, assign laptop LT-HP-006, phone PH-IP-006. "
            "Complete checklist items check_601, check_602, verify onboarding files offer_letter.pdf and id_scan.pdf. Approve access checks access_601, access_602. "
            "Label email email_601 as 'OnboardingReady' and log all updates."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_601", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_602", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-HP-006", "candidate_id": "cand_6"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IP-006", "candidate_id": "cand_6"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_601", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_602", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_601", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_602", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_601", "label_id": "label_OnboardingReady"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Candidate cand_6 onboarding completed", "candidate_id": "cand_6"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_6", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_601.status=Approved | asset_request.req_602.status=Approved | asset.LT-HP-006.status=Assigned | asset.PH-IP-006.status=Assigned | checklist_item.check_601.status=Completed | checklist_item.check_602.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_601.status=Approved | access_check.access_602.status=Approved | email.email_601.labels=label_OnboardingReady | log.ONBOARDING_COMPLETED.message=Candidate cand_6 onboarding completed | candidate.cand_6.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_014",
        instruction=(
            "For candidate cand_2, you replace temporary laptop LT-Temp02 with permanent laptop LT-002C, complete security induction checklist items "
            "check_221 and check_222, verify background_verification.pdf, update access check access_207 to 'Approved', add a new access check access_208, "
            "apply email label 'SecurityClearance' to email_221, log all updates, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-Temp02"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002C", "candidate_id": "cand_2"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_221", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_222", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/background_verification.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_207", "updates": {"status": "Approved"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_208", "status": "Pending"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_221", "label_id": "label_SecurityClearance"}),
            Action(name="record_terminal_log", kwargs={"event_type": "SECURITY_CHECK", "message": "Security induction completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATE", "message": "Access updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"security_clearance": "Granted"}})
        ],
        outputs=[
            "asset.LT-Temp02.status=Available | asset.LT-002C.status=Assigned | checklist_item.check_221.status=Completed | checklist_item.check_222.status=Completed | onboarding_files.background_verification.pdf.status=Verified | access_check.access_207.status=Approved | access_check.access_208.status=Pending | email.email_221.labels=label_SecurityClearance | log.SECURITY_CHECK.message=Security induction completed for cand_2 | log.ACCESS_UPDATE.message=Access updated for cand_2 | candidate.cand_2.security_clearance=Granted"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_015",
        instruction=(
            "For candidate cand_4, you assign mobile device MB-004X, release old tablet TB-004Z, complete orientation checklist items check_410 and check_411, "
            "verify signed_policy.pdf, add attachment with team_structure.pdf, apply 'Orientation' label to email_410, log the changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "TB-004Z"}),
            Action(name="assign_asset", kwargs={"asset_tag": "MB-004X", "candidate_id": "cand_4"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_410", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_411", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/signed_policy.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_9", "file_name": "team_structure.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_410", "label_id": "label_Orientation"}),
            Action(name="record_terminal_log", kwargs={"event_type": "DEVICE_UPDATE", "message": "Mobile assigned to cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Orientation tasks done for cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "FILE_VERIFIED", "message": "Signed policy verified for cand_4", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"orientation_status": "Completed"}})
        ],
        outputs=[
            "asset.TB-004Z.status=Available | asset.MB-004X.status=Assigned | checklist_item.check_410.status=Completed | checklist_item.check_411.status=Completed | onboarding_files.signed_policy.pdf.status=Verified | attachment.team_structure.pdf.added=True | email.email_410.labels=label_Orientation | log.DEVICE_UPDATE.message=Mobile assigned to cand_4 | log.CHECKLIST_COMPLETED.message=Orientation tasks done for cand_4 | log.FILE_VERIFIED.message=Signed policy verified for cand_4 | candidate.cand_4.orientation_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_016",
        instruction=(
            "For candidate cand_1, you release temporary laptop LT-001X, assign permanent laptop LT-001Y, close asset request req_102, complete training checklist check_103, "
            "verify confidentiality_agreement.pdf, add access check access_105, remove outdated access check access_106, label email email_103 as 'TrainingUpdate', "
            "log updates, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-001X"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-001Y", "candidate_id": "cand_1"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Closed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_103", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/confidentiality_agreement.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_105", "status": "Pending"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_106"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_103", "label_id": "label_TrainingUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New permanent laptop assigned to cand_1", "candidate_id": "cand_1"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"training_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-001X.status=Available | asset.LT-001Y.status=Assigned | asset_request.req_102.status=Closed | checklist_item.check_103.status=Completed | onboarding_files.confidentiality_agreement.pdf.status=Verified | access_check.access_105.status=Pending | access_check.access_106=Removed | email.email_103.labels=label_TrainingUpdate | log.ASSET_ASSIGNED.message=New permanent laptop assigned to cand_1 | log.ACCESS_UPDATED.message=Access checks updated for cand_1 | candidate.cand_1.training_status=Completed"
        ],
    ),


    Task(
        annotator="R",
        user_id="onboarding_ds_017",
        instruction=(
            "For candidate cand_2, you release old laptop LT-002A, assign new laptop LT-002B, complete asset requests req_201 and req_202, "
            "remove access checks access_201 and access_202, add new access check access_206, attach Benefits-Guide.pdf, "
            "apply label 'AssetChange' to email email_201, log all changes, update candidate record, and verify onboarding file ID-Proof.pdf."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_201", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_201"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_202"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_206", "status": "Pending"}}),
            Action(name="add_attachment",
                   kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_201", "label_id": "label_AssetChange"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_2",
                           "candidate_id": "cand_2"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_2",
                           "candidate_id": "cand_2"}),
            Action(name="update_onboarding_file",
                   kwargs={"file_path": "files/ID-Proof.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset_request.req_201.status=Completed | asset_request.req_202.status=Completed | access_check.access_201=Removed | access_check.access_202=Removed | access_check.access_206.status=Pending | attachment.Benefits-Guide.pdf.added=True | email.email_201.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_2 | log.ACCESS_UPDATED.message=Access checks updated for cand_2 | onboarding_files.ID-Proof.pdf.status=Verified | candidate.cand_2.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_019",
        instruction=(
            "For candidate cand_2, you release old monitor MON-202A, assign new monitor MON-202B, complete checklist check_202, "
            "attach NDA-Form.pdf, remove access check access_202, add new access check access_204, "
            "apply 'HR' label to email email_202, log updates, and update candidate HR record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "MON-202A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "MON-202B", "candidate_id": "cand_2"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_12", "file_name": "NDA-Form.pdf"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_202"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_204", "status": "Pending"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_202", "label_id": "label_HR"}),
            Action(name="record_terminal_log", kwargs={"event_type": "MONITOR_UPDATED", "message": "Monitor swapped for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"hr_status": "Updated"}}),
            Action(name="send_email", kwargs={"email_id": "email_202", "updates": {"status": "Sent"}})
        ],
        outputs=[
            "asset.MON-202A.status=Available | asset.MON-202B.status=Assigned | checklist_item.check_202.status=Completed | attachment.NDA-Form.pdf.added=True | access_check.access_202=Removed | access_check.access_204.status=Pending | email.email_202.labels=label_HR | log.MONITOR_UPDATED.message=Monitor swapped for cand_2 | log.ACCESS_UPDATED.message=Access updated for cand_2 | candidate.cand_2.hr_status=Updated | email.email_202.status=Sent"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_021",
        instruction=(
            "For candidate cand_4, you decommission old phone PH-404A, assign smartphone PH-404B, "
            "remove access check access_404, add access check access_405, attach Orientation-Schedule.pdf, "
            "update checklist check_404, apply label 'Orientation' to email email_404, log activities, "
            "and mark candidate orientation complete."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "PH-404A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-404B", "candidate_id": "cand_4"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_404"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_405", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_14", "file_name": "Orientation-Schedule.pdf"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_404", "updates": {"status": "Completed"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_404", "label_id": "label_Orientation"}),
            Action(name="record_terminal_log", kwargs={"event_type": "PHONE_UPDATED", "message": "Smartphone assigned to cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"orientation_status": "Completed"}}),
            Action(name="send_email", kwargs={"email_id": "email_404", "updates": {"status": "Sent"}})
        ],
        outputs=[
            "asset.PH-404A.status=Available | asset.PH-404B.status=Assigned | access_check.access_404=Removed | access_check.access_405.status=Pending | attachment.Orientation-Schedule.pdf.added=True | checklist_item.check_404.status=Completed | email.email_404.labels=label_Orientation | log.PHONE_UPDATED.message=Smartphone assigned to cand_4 | log.ACCESS_UPDATED.message=Access updated for cand_4 | candidate.cand_4.orientation_status=Completed | email.email_404.status=Sent"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_091",
        instruction=(
            "For candidate cand_1, you complete the pending tasks check_101 and check_102. "
            "Release the old laptop LT-001B, assign the new laptop LT-001D and phone PH-001D. "
            "Update asset requests req_105 and req_106, remove access check access_103, add access check access_108. "
            "Attach welcome_Jane_Smith.md, apply the 'OnboardingComplete' label to email email_101, log completion, and update the candidate record."
        ),
        actions=[
            Action(name="update_checklist_item", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="release_asset", kwargs={"asset_tag": "LT-001B"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-001D", "candidate_id": "cand_1"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-001D", "candidate_id": "cand_1"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_105", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_106", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_103"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_108", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={
                "attachment": {"attachment_id": "attach_welcome_jane", "file_name": "welcome_Jane_Smith.md"}}),
            Action(name="apply_label_to_email",
                   kwargs={"email_id": "email_101", "label_id": "label_OnboardingComplete"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_1",
                           "candidate_id": "cand_1"})
        ],
        outputs=[
            "checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | asset.LT-001B.status=Available | asset.LT-001D.status=Assigned | asset.PH-001D.status=Assigned | asset_request.req_105.status=Completed | asset_request.req_106.status=Completed | access_check.access_103=Removed | access_check.access_108.status=Pending | attachment.welcome_Jane_Smith.md.added=True | email.email_101.labels=label_OnboardingComplete | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_1"
        ]
    ),
    Task(
        annotator="R",
        user_id="onboarding_ds_092",
        instruction=(
            "For candidate cand_4, you remove old access checks access_403 and access_404, and add new access checks access_407 and access_408. "
            "Assign laptop LT-004D and phone PH-004D, complete asset request req_407, attach Company-Policies.pdf, and verify onboarding file offer_letter.pdf. "
            "Log all changes and update the candidate record."
        ),
        actions=[
            Action(name="remove_access_check", kwargs={"check_id": "access_403"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_404"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_407", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_408", "status": "Pending"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-004D", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-004D", "candidate_id": "cand_4"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_407", "updates": {"status": "Completed"}}),
            Action(name="add_attachment",
                   kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Company-Policies.pdf"}}),
            Action(name="update_onboarding_file",
                   kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "DEVICE_ASSIGNED", "message": "Devices assigned for cand_4",
                           "candidate_id": "cand_4"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_4",
                           "candidate_id": "cand_4"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "access_check.access_403=Removed | access_check.access_404=Removed | access_check.access_407.status=Pending | access_check.access_408.status=Pending | asset.LT-004D.status=Assigned | asset.PH-004D.status=Assigned | asset_request.req_407.status=Completed | attachment.Company-Policies.pdf.added=True | onboarding_files.offer_letter.pdf.status=Verified | log.DEVICE_ASSIGNED.message=Devices assigned for cand_4 | log.ACCESS_UPDATED.message=Access updated for cand_4 | candidate.cand_4.asset_update_status=Completed"
        ]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_094",
        instruction=(
            "For candidate cand_7, you assign the laptop LT-007C and phone PH-007C, complete asset requests req_701 and req_702. "
            "Remove old access checks access_701 and access_702, add new access checks access_703 and access_704, attach welcome_Robert_Singh.md, "
            "apply the 'OnboardingComplete' label to email email_701, log all changes, and update the candidate record."
        ),
        actions=[
            Action(name="assign_asset", kwargs={"asset_tag": "LT-007C", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-007C", "candidate_id": "cand_7"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_701", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_702", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_701"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_702"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_703", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_704", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={
                "attachment": {"attachment_id": "attach_welcome_robert", "file_name": "welcome_Robert_Singh.md"}}),
            Action(name="apply_label_to_email",
                   kwargs={"email_id": "email_701", "label_id": "label_OnboardingComplete"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_7",
                           "candidate_id": "cand_7"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-007C.status=Assigned | asset.PH-007C.status=Assigned | asset_request.req_701.status=Completed | asset_request.req_702.status=Completed | access_check.access_701=Removed | access_check.access_702=Removed | access_check.access_703.status=Pending | access_check.access_704.status=Pending | attachment.welcome_Robert_Singh.md.added=True | email.email_701.labels=label_OnboardingComplete | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ]
    ),
    Task(
        annotator="R",
        user_id="onboarding_ds_095",
        instruction=(
            "For candidate cand_6, you complete checklist items check_603 and check_604. "
            "Release old laptop LT-006B, assign new laptop LT-006C and phone PH-006C, update asset requests req_603 and req_604. "
            "Remove access check access_603, add access check access_605, attach Benefits-Guide.pdf, log all changes, and update the candidate record."
        ),
        actions=[
            Action(name="update_checklist_item", kwargs={"item_id": "check_603", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_604", "updates": {"status": "Completed"}}),
            Action(name="release_asset", kwargs={"asset_tag": "LT-006B"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-006C", "candidate_id": "cand_6"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-006C", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_603", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_604", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_603"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_605", "status": "Pending"}}),
            Action(name="add_attachment",
                   kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "checklist_item.check_603.status=Completed | checklist_item.check_604.status=Completed | asset.LT-006B.status=Available | asset.LT-006C.status=Assigned | asset.PH-006C.status=Assigned | asset_request.req_603.status=Completed | asset_request.req_604.status=Completed | access_check.access_603=Removed | access_check.access_605.status=Pending | attachment.Benefits-Guide.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_096",
        instruction=(
            "For candidate cand_2 you should have their old laptop LT-002A released and a new laptop LT-002B and phone PH-002B assigned. "
            "Asset requests req_203 and req_204 are to be completed. Old access checks access_203 and access_204 should be removed, "
            "and new access checks access_205 and access_206 should be added. Attach Company-Policies.pdf, log all updates, "
            "and update the candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-002B", "candidate_id": "cand_2"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_203", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_204", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_203"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_204"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_205", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_206", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_3", "file_name": "Company-Policies.pdf"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REASSIGNED", "message": "Assets reassigned for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset.PH-002B.status=Assigned | asset_request.req_203.status=Completed | asset_request.req_204.status=Completed | access_check.access_203=Removed | access_check.access_204=Removed | access_check.access_205.status=Pending | access_check.access_206.status=Pending | attachment.Company-Policies.pdf.added=True | log.ASSET_REASSIGNED.message=Assets reassigned for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_098",
        instruction=(
            "Candidate cand_3 should have old laptop LT-003B released, new laptop LT-003C and phone PH-003C assigned, "
            "and asset requests req_303 and req_304 updated. You remove access checks access_303 and access_304, add access checks access_305 and access_306, "
            "attach offer_letter.pdf, log all changes, and update the candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-003B"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-003C", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-003C", "candidate_id": "cand_3"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_303", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_304", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_303"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_304"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_305", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_306", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_offer_letter", "file_name": "offer_letter.pdf"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_3", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-003B.status=Available | asset.LT-003C.status=Assigned | asset.PH-003C.status=Assigned | asset_request.req_303.status=Completed | asset_request.req_304.status=Completed | access_check.access_303=Removed | access_check.access_304=Removed | access_check.access_305.status=Pending | access_check.access_306.status=Pending | attachment.offer_letter.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_3 | candidate.cand_3.asset_update_status=Completed"
        ]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_099",
        instruction=(
            "Candidate cand_7 must have laptop LT-007D and phone PH-007D assigned, you complete asset requests req_705 and req_706, "
            "remove old access checks access_705 and access_706, add new access checks access_707 and access_708, "
            "attach welcome_Maria_Rodriguez.md, log all updates, and update the candidate record."
        ),
        actions=[
            Action(name="assign_asset", kwargs={"asset_tag": "LT-007D", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-007D", "candidate_id": "cand_7"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_705", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_706", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_705"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_706"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_707", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_708", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_welcome_maria", "file_name": "welcome_Maria_Rodriguez.md"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-007D.status=Assigned | asset.PH-007D.status=Assigned | asset_request.req_705.status=Completed | asset_request.req_706.status=Completed | access_check.access_705=Removed | access_check.access_706=Removed | access_check.access_707.status=Pending | access_check.access_708.status=Pending | attachment.welcome_Maria_Rodriguez.md.added=True | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ]
    ),
    Task(
        annotator="R",
        user_id="onboarding_ds_100",
        instruction=(
            "Candidate cand_6 should release old laptop LT-006C, you assign new laptop LT-006D and phone PH-006D, "
            "complete asset requests req_607 and req_608, remove access check access_605, add access check access_606, "
            "attach Benefits-Guide.pdf, log all updates, and update the candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-006C"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-006D", "candidate_id": "cand_6"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-006D", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_607", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_608", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_605"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_606", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-006C.status=Available | asset.LT-006D.status=Assigned | asset.PH-006D.status=Assigned | asset_request.req_607.status=Completed | asset_request.req_608.status=Completed | access_check.access_605=Removed | access_check.access_606.status=Pending | attachment.Benefits-Guide.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_6 | log.ACCESS_UPDATED.message=Access updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_303",
        instruction=(
            "For candidate cand_3, you release old laptop LT-003A, assign new laptop LT-003B, complete checklist items check_303 and check_304, "
            "verify onboarding file offer_letter.pdf, apply email label 'AssetUpdate' to email email_303, log all changes, update candidate record, "
            "and attach Company-Policies.pdf."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-003A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_303", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_304", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_303", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New assets assigned for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_3", "candidate_id": "cand_3"}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_3", "file_name": "Company-Policies.pdf"}}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-003A.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_303.status=Completed | checklist_item.check_304.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | email.email_303.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_3 | log.ASSET_ASSIGNED.message=New assets assigned for cand_3 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_3 | attachment.Company-Policies.pdf.added=True | candidate.cand_3.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_305",
        instruction=(
            "For candidate cand_5, you release old laptop LT-005A, assign new laptop LT-005B, complete asset requests req_501 and req_502, "
            "remove access checks access_501, add new access check access_507, attach Benefits-Guide.pdf, apply label 'AssetChange' to email email_501, "
            "log changes, update candidate record, and verify onboarding file Driving-License.pdf."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-005A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_501"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_507", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_501", "label_id": "label_AssetChange"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_5", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"asset_update_status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/Driving-License.pdf", "updates": {"status": "Verified"}})
        ],
        outputs=[
            "asset.LT-005A.status=Available | asset.LT-005B.status=Assigned | asset_request.req_501.status=Completed | asset_request.req_502.status=Completed | access_check.access_501=Removed | access_check.access_507.status=Pending | attachment.Benefits-Guide.pdf.added=True | email.email_501.labels=label_AssetChange | log.ASSET_UPDATED.message=Assets updated for cand_5 | onboarding_files.Driving-License.pdf.status=Verified | candidate.cand_5.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_306",
        instruction=(
            "For candidate cand_6, you release old laptop LT-006A, assign new laptop LT-006B, complete asset requests req_601, remove access check access_601, "
            "add new access checks access_603 and access_604, attach Company-Policies.pdf, apply label 'AssetUpdate' to email email_601, "
            "log changes, update candidate record, and verify onboarding file Passport.pdf."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-006A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-006B", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_601"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_604", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Company-Policies.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_601", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/Passport.pdf", "updates": {"status": "Verified"}})
        ],
        outputs=[
            "asset.LT-006A.status=Available | asset.LT-006B.status=Assigned | asset_request.req_601.status=Completed | access_check.access_601=Removed | access_check.access_603.status=Pending | access_check.access_604.status=Pending | attachment.Company-Policies.pdf.added=True | email.email_601.labels=label_AssetUpdate | log.ASSET_UPDATED.message=Assets updated for cand_6 | onboarding_files.Passport.pdf.status=Verified | candidate.cand_6.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_307",
        instruction=(
            "For candidate cand_7, you release old laptop LT-007A, assign new laptop LT-007B, complete checklist items check_701 and check_702, "
            "remove access check access_701, add new access check access_705, attach Benefits-Guide.pdf, apply label 'AssetUpdate' to email email_701, "
            "log changes, update candidate record, and verify onboarding file ID-Proof.pdf."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-007A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-007B", "candidate_id": "cand_7"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_701"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_705", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/ID-Proof.pdf", "updates": {"status": "Verified"}})
        ],
        outputs=[
            "asset.LT-007A.status=Available | asset.LT-007B.status=Assigned | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | access_check.access_701=Removed | access_check.access_705.status=Pending | attachment.Benefits-Guide.pdf.added=True | email.email_701.labels=label_AssetUpdate | log.ASSET_UPDATED.message=Assets updated for cand_7 | onboarding_files.ID-Proof.pdf.status=Verified | candidate.cand_7.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_201",
        instruction=(
            "For candidate cand_1, you release old asset LT-001A, assign new asset LT-001B, update asset request req_101 to Completed, "
            "mark checklist items check_101 and check_102 as Completed, verify onboarding file offer_letter.pdf, "
            "apply label 'OnboardingUpdate' to email email_101, remove access check access_101, add access check access_105, "
            "attach Handbook.pdf, log updates, and mark candidate onboarding as Completed."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-001B", "candidate_id": "cand_1"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_101", "label_id": "label_OnboardingUpdate"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_101"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_105", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Handbook.pdf"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_progress": "Completed"}}),
        ],
        outputs=[
            "asset.LT-001A.status=Available | asset.LT-001B.status=Assigned | asset_request.req_101.status=Completed | checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | email.email_101.labels=label_OnboardingUpdate | access_check.access_101=Removed | access_check.access_105.status=Pending | attachment.Handbook.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_1 | candidate.cand_1.onboarding_progress=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_203",
        instruction=(
            "For candidate cand_3, you release asset LT-003A, assign LT-003B, update checklist items check_301 and check_302, "
            "verify tax_form.pdf, add label 'Finance' to email email_303, remove access check access_303, add access check access_304, "
            "remove attachment Benefits.pdf, add attachment Payroll-Form.pdf, log changes, and update payroll_status."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-003A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/tax_form.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_303", "label_id": "label_Finance"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_303"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_304", "status": "Pending"}}),
            Action(name="remove_attachment", kwargs={"attachment_id": "attach_5"}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_6", "file_name": "Payroll-Form.pdf"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "FINANCE_UPDATE", "message": "Payroll forms updated for cand_3", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"payroll_status": "Active"}}),
        ],
        outputs=[
            "asset.LT-003A.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | onboarding_files.tax_form.pdf.status=Verified | email.email_303.labels=label_Finance | access_check.access_303=Removed | access_check.access_304.status=Pending | attachment.Benefits.pdf.removed=True | attachment.Payroll-Form.pdf.added=True | log.FINANCE_UPDATE.message=Payroll forms updated for cand_3 | candidate.cand_3.payroll_status=Active"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_204",
        instruction=(
            "For candidate cand_2, you release laptop LT-002A, assign laptop LT-002B, update asset request req_201, "
            "complete checklist items check_201 and check_202, remove onboarding file id_proof.pdf, "
            "add onboarding file nda.pdf, apply email label 'OnboardingComplete' to email email_201, "
            "log all updates, and mark candidate record as fully onboarded."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_201", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="remove_onboarding_file", kwargs={"file_path": "files/id_proof.pdf"}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/nda.pdf", "status": "Pending"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_201", "label_id": "label_OnboardingComplete"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"status": "Onboarded"}})
        ],
        outputs=[
            "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset_request.req_201.status=Completed | checklist_item.check_201.status=Completed | checklist_item.check_202.status=Completed | onboarding_files.id_proof.pdf=Removed | onboarding_files.nda.pdf.status=Pending | email.email_201.labels=label_OnboardingComplete | log.ASSET_UPDATED.message=Assets updated for cand_2 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_2 | candidate.cand_2.status=Onboarded"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_205",
        instruction=(
            "For candidate cand_5, you release asset LT-005A, assign LT-005B, update asset request req_501, "
            "remove access check access_501, add new access check access_502, complete checklist check_502, "
            "update email email_501 content, apply label 'AccessUpdate' to the same email, "
            "log the changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-005A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_501"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_502", "status": "Pending"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_502", "updates": {"status": "Completed"}}),
            Action(name="update_email", kwargs={"email_id": "email_501", "updates": {"subject": "Access Updated"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_501", "label_id": "label_AccessUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_5", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist item completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"access_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-005A.status=Available | asset.LT-005B.status=Assigned | asset_request.req_501.status=Completed | access_check.access_501=Removed | access_check.access_502.status=Pending | checklist_item.check_502.status=Completed | email.email_501.subject=Access Updated | email.email_501.labels=label_AccessUpdate | log.ACCESS_UPDATED.message=Access updated for cand_5 | log.CHECKLIST_COMPLETED.message=Checklist item completed for cand_5 | candidate.cand_5.access_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_206",
        instruction=(
            "For candidate cand_7, you release asset LT-007A, assign asset LT-007B, complete checklist items check_701 and check_702, "
            "update onboarding file tax_form.pdf, add attachment Employee-Handbook.pdf, update email email_701, "
            "apply label 'PolicyUpdate', log changes, and set candidate onboarding phase to 'Finalized'."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-007A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-007B", "candidate_id": "cand_7"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/tax_form.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Employee-Handbook.pdf"}}),
            Action(name="update_email", kwargs={"email_id": "email_701", "updates": {"subject": "Onboarding Policy Updated"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_PolicyUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_UPDATED", "message": "Onboarding finalized for cand_7", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "All checklist items completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"phase": "Finalized"}})
        ],
        outputs=[
            "asset.LT-007A.status=Available | asset.LT-007B.status=Assigned | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.tax_form.pdf.status=Verified | attachment.Employee-Handbook.pdf.added=True | email.email_701.subject=Onboarding Policy Updated | email.email_701.labels=label_PolicyUpdate | log.ONBOARDING_UPDATED.message=Onboarding finalized for cand_7 | log.CHECKLIST_COMPLETED.message=All checklist items completed for cand_7 | candidate.cand_7.phase=Finalized"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_207",
        instruction=(
            "For candidate cand_1, you release asset LT-001A, assign LT-001C, complete checklist items check_101 and check_102, "
            "remove access check access_101, add access check access_103, update onboarding file offer_letter.pdf, "
            "add file signed_contract.pdf, update email email_101 with subject 'Final Contract Signed', "
            "apply label 'ContractComplete', log the updates, and mark candidate as confirmed."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-001C", "candidate_id": "cand_1"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_101"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_103", "status": "Pending"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/signed_contract.pdf", "status": "Pending"}}),
            Action(name="update_email", kwargs={"email_id": "email_101", "updates": {"subject": "Final Contract Signed"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_101", "label_id": "label_ContractComplete"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CANDIDATE_CONFIRMED", "message": "cand_1 fully confirmed", "candidate_id": "cand_1"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"status": "Confirmed"}})
        ],
        outputs=[
            "asset.LT-001A.status=Available | asset.LT-001C.status=Assigned | checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | access_check.access_101=Removed | access_check.access_103.status=Pending | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.signed_contract.pdf.status=Pending | email.email_101.subject=Final Contract Signed | email.email_101.labels=label_ContractComplete | log.CANDIDATE_CONFIRMED.message=cand_1 fully confirmed | candidate.cand_1.status=Confirmed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_208",
        instruction=(
            "For candidate cand_3, you release asset LT-003A, assign LT-003B, update asset request req_301, "
            "complete checklist check_301, update onboarding file id_proof.pdf, add onboarding file medical_form.pdf, "
            "update email email_301 with subject 'Onboarding Medical Cleared', apply label 'MedicalUpdate', "
            "remove attachment attach_3, add attachment Training-Schedule.pdf, log updates, and set candidate stage to 'ReadyForTraining'."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-003A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_301", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_proof.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/medical_form.pdf", "status": "Pending"}}),
            Action(name="update_email", kwargs={"email_id": "email_301", "updates": {"subject": "Onboarding Medical Cleared"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_301", "label_id": "label_MedicalUpdate"}),
            Action(name="remove_attachment", kwargs={"attachment_id": "attach_3"}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_3_new", "file_name": "Training-Schedule.pdf"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_READY", "message": "Medical cleared and training scheduled for cand_3", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"stage": "ReadyForTraining"}})
        ],
        outputs=[
            "asset.LT-003A.status=Available | asset.LT-003B.status=Assigned | asset_request.req_301.status=Completed | checklist_item.check_301.status=Completed | onboarding_files.id_proof.pdf.status=Verified | onboarding_files.medical_form.pdf.status=Pending | email.email_301.subject=Onboarding Medical Cleared | email.email_301.labels=label_MedicalUpdate | attachment.attach_3=Removed | attachment.Training-Schedule.pdf.added=True | log.ONBOARDING_READY.message=Medical cleared and training scheduled for cand_3 | candidate.cand_3.stage=ReadyForTraining"
        ],
    ),


    Task(
        annotator="R",
        user_id="onboarding_ds_209",
        instruction=(
            "For candidate cand_4, you release LT-004A, assign LT-004B, update request req_401, "
            "complete checklist items check_401 and check_402, add access check access_404, "
            "remove onboarding file old_resume.pdf, add new file updated_resume.pdf, "
            "update email email_401 with subject 'Resume Verified', apply label 'ResumeCheck', "
            "log actions, and set candidate profile as 'Verified'."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-004A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-004B", "candidate_id": "cand_4"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_401", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_401", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_402", "updates": {"status": "Completed"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_404", "status": "Pending"}}),
            Action(name="remove_onboarding_file", kwargs={"file_path": "files/old_resume.pdf"}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/updated_resume.pdf", "status": "Pending"}}),
            Action(name="update_email", kwargs={"email_id": "email_401", "updates": {"subject": "Resume Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_401", "label_id": "label_ResumeCheck"}),
            Action(name="record_terminal_log", kwargs={"event_type": "PROFILE_VERIFIED", "message": "Resume verified for cand_4", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"profile_status": "Verified"}})
        ],
        outputs=[
            "asset.LT-004A.status=Available | asset.LT-004B.status=Assigned | asset_request.req_401.status=Completed | checklist_item.check_401.status=Completed | checklist_item.check_402.status=Completed | access_check.access_404.status=Pending | onboarding_files.old_resume.pdf=Removed | onboarding_files.updated_resume.pdf.status=Pending | email.email_401.subject=Resume Verified | email.email_401.labels=label_ResumeCheck | log.PROFILE_VERIFIED.message=Resume verified for cand_4 | candidate.cand_4.profile_status=Verified"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_210",
        instruction=(
            "For candidate cand_6, you release LT-006A, assign LT-006B, update request req_601, "
            "complete checklist item check_601, add access check access_606, "
            "update onboarding file training_doc.pdf, add file signed_training.pdf, "
            "update email email_601 with subject 'Training Completed', apply label 'TrainingDone', "
            "log actions, and mark candidate status 'Trained'."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-006A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-006B", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_601", "updates": {"status": "Completed"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_606", "status": "Pending"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/training_doc.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/signed_training.pdf", "status": "Pending"}}),
            Action(name="update_email", kwargs={"email_id": "email_601", "updates": {"subject": "Training Completed"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_601", "label_id": "label_TrainingDone"}),
            Action(name="record_terminal_log", kwargs={"event_type": "TRAINING_COMPLETED", "message": "cand_6 training completed", "candidate_id": "cand_6"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_6", "updates": {"status": "Trained"}})
        ],
        outputs=[
            "asset.LT-006A.status=Available | asset.LT-006B.status=Assigned | asset_request.req_601.status=Completed | checklist_item.check_601.status=Completed | access_check.access_606.status=Pending | onboarding_files.training_doc.pdf.status=Verified | onboarding_files.signed_training.pdf.status=Pending | email.email_601.subject=Training Completed | email.email_601.labels=label_TrainingDone | log.TRAINING_COMPLETED.message=cand_6 training completed | candidate.cand_6.status=Trained"
        ],
    ),


    Task(
        annotator="R",
        user_id="onboarding_ds_211",
        instruction=(
            "For candidate cand_2, you release LT-002B, assign LT-002C, update asset request req_202, "
            "complete checklist items check_203 and check_204, add access check access_205, "
            "update onboarding file nda.pdf, add attachment Code-Of-Conduct.pdf, "
            "update email email_202 with subject 'Code of Conduct Signed', apply label 'PolicySigned', "
            "log updates, and update candidate phase to 'ActiveEmployee'."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-002B"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002C", "candidate_id": "cand_2"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_204", "updates": {"status": "Completed"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_205", "status": "Pending"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/nda.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_2_new", "file_name": "Code-Of-Conduct.pdf"}}),
            Action(name="update_email", kwargs={"email_id": "email_202", "updates": {"subject": "Code of Conduct Signed"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_202", "label_id": "label_PolicySigned"}),
            Action(name="record_terminal_log", kwargs={"event_type": "POLICY_ACCEPTED", "message": "Code of conduct signed for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"phase": "ActiveEmployee"}})
        ],
        outputs=[
            "asset.LT-002B.status=Available | asset.LT-002C.status=Assigned | asset_request.req_202.status=Completed | checklist_item.check_203.status=Completed | checklist_item.check_204.status=Completed | access_check.access_205.status=Pending | onboarding_files.nda.pdf.status=Verified | attachment.Code-Of-Conduct.pdf.added=True | email.email_202.subject=Code of Conduct Signed | email.email_202.labels=label_PolicySigned | log.POLICY_ACCEPTED.message=Code of conduct signed for cand_2 | candidate.cand_2.phase=ActiveEmployee"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_086",
        instruction=(
            "For candidate cand_2, you release old laptop LT-002A, assign new laptop LT-002B, complete asset request req_202, "
            "remove access check access_202, add new access check access_205, attach Code-of-Conduct.pdf, "
            "apply email label 'PolicyUpdate' to email email_205, complete checklist item check_205, "
            "log updates for both assets and access, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_202"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_205", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_11", "file_name": "Code-of-Conduct.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_205", "label_id": "label_PolicyUpdate"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_205", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Laptop updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access changes applied for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset_request.req_202.status=Completed | access_check.access_202=Removed | access_check.access_205.status=Pending | attachment.Code-of-Conduct.pdf.added=True | email.email_205.labels=label_PolicyUpdate | checklist_item.check_205.status=Completed | log.ASSET_UPDATED.message=Laptop updated for cand_2 | log.ACCESS_UPDATED.message=Access changes applied for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_087",
        instruction=(
            "For candidate cand_1, you release old laptop LT-001A, assign laptop LT-001B, complete asset request req_101, "
            "remove access check access_101, add new access check access_103, attach Employee-Handbook.pdf, "
            "apply email label 'OnboardingDocs' to email email_103, complete checklist item check_103, "
            "log updates for assets and access, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-001B", "candidate_id": "cand_1"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_101"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_103", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_12", "file_name": "Employee-Handbook.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_103", "label_id": "label_OnboardingDocs"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_103", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Laptop updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-001A.status=Available | asset.LT-001B.status=Assigned | asset_request.req_101.status=Completed | access_check.access_101=Removed | access_check.access_103.status=Pending | attachment.Employee-Handbook.pdf.added=True | email.email_103.labels=label_OnboardingDocs | checklist_item.check_103.status=Completed | log.ASSET_UPDATED.message=Laptop updated for cand_1 | log.ACCESS_UPDATED.message=Access updated for cand_1 | candidate.cand_1.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_088",
        instruction=(
            "For candidate cand_4, you release monitor MN-004A, assign monitor MN-004B, complete asset request req_401, "
            "remove access check access_401, add access check access_402, attach Health-Safety.pdf, "
            "apply email label 'HealthPolicy' to email email_402, complete checklist item check_402, "
            "log changes for assets and access, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "MN-004A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "MN-004B", "candidate_id": "cand_4"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_401", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_401"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_402", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_13", "file_name": "Health-Safety.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_402", "label_id": "label_HealthPolicy"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_402", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Monitor updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.MN-004A.status=Available | asset.MN-004B.status=Assigned | asset_request.req_401.status=Completed | access_check.access_401=Removed | access_check.access_402.status=Pending | attachment.Health-Safety.pdf.added=True | email.email_402.labels=label_HealthPolicy | checklist_item.check_402.status=Completed | log.ASSET_UPDATED.message=Monitor updated for cand_4 | log.ACCESS_UPDATED.message=Access updated for cand_4 | candidate.cand_4.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_089",
        instruction=(
            "For candidate cand_6, you release phone PH-006A, assign phone PH-006B, complete asset request req_601, "
            "remove access check access_601, add access check access_603, attach Compliance-Report.pdf, "
            "apply email label 'Compliance' to email email_603, complete checklist item check_603, "
            "log changes for assets and access, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "PH-006A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-006B", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_601"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_14", "file_name": "Compliance-Report.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_603", "label_id": "label_Compliance"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_603", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Phone updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.PH-006A.status=Available | asset.PH-006B.status=Assigned | asset_request.req_601.status=Completed | access_check.access_601=Removed | access_check.access_603.status=Pending | attachment.Compliance-Report.pdf.added=True | email.email_603.labels=label_Compliance | checklist_item.check_603.status=Completed | log.ASSET_UPDATED.message=Phone updated for cand_6 | log.ACCESS_UPDATED.message=Access updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_090",
        instruction=(
            "For candidate cand_2, you release desktop DT-002A, assign desktop DT-002B, complete asset request req_201, "
            "remove access check access_201, add new access check access_204, attach Payroll-Guide.pdf, "
            "apply email label 'FinanceDocs' to email email_204, complete checklist item check_204, "
            "log changes for assets and access, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "DT-002A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "DT-002B", "candidate_id": "cand_2"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_201", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_201"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_204", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_15", "file_name": "Payroll-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_204", "label_id": "label_FinanceDocs"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_204", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Desktop updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.DT-002A.status=Available | asset.DT-002B.status=Assigned | asset_request.req_201.status=Completed | access_check.access_201=Removed | access_check.access_204.status=Pending | attachment.Payroll-Guide.pdf.added=True | email.email_204.labels=label_FinanceDocs | checklist_item.check_204.status=Completed | log.ASSET_UPDATED.message=Desktop updated for cand_2 | log.ACCESS_UPDATED.message=Access updated for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_091",
        instruction=(
            "For candidate cand_3, you release headset HS-003A, assign headset HS-003B, complete asset request req_301, "
            "remove access check access_301, add new access check access_305, attach Security-Guidelines.pdf, "
            "apply email label 'SecurityDocs' to email email_305, complete checklist item check_305, "
            "log updates for assets and access, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "HS-003A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "HS-003B", "candidate_id": "cand_3"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_301", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_301"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_305", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_16", "file_name": "Security-Guidelines.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_305", "label_id": "label_SecurityDocs"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_305", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Headset updated for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_3", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.HS-003A.status=Available | asset.HS-003B.status=Assigned | asset_request.req_301.status=Completed | access_check.access_301=Removed | access_check.access_305.status=Pending | attachment.Security-Guidelines.pdf.added=True | email.email_305.labels=label_SecurityDocs | checklist_item.check_305.status=Completed | log.ASSET_UPDATED.message=Headset updated for cand_3 | log.ACCESS_UPDATED.message=Access updated for cand_3 | candidate.cand_3.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_092",
        instruction=(
            "For candidate cand_5, you release tablet TB-005A, assign tablet TB-005B, complete asset request req_501, "
            "remove access check access_501, add access check access_506, attach Training-Plan.pdf, "
            "apply email label 'Learning' to email email_506, complete checklist item check_506, "
            "log updates for assets and access, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "TB-005A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "TB-005B", "candidate_id": "cand_5"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_501"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_506", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_17", "file_name": "Training-Plan.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_506", "label_id": "label_Learning"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_506", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Tablet updated for cand_5", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_5", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.TB-005A.status=Available | asset.TB-005B.status=Assigned | asset_request.req_501.status=Completed | access_check.access_501=Removed | access_check.access_506.status=Pending | attachment.Training-Plan.pdf.added=True | email.email_506.labels=label_Learning | checklist_item.check_506.status=Completed | log.ASSET_UPDATED.message=Tablet updated for cand_5 | log.ACCESS_UPDATED.message=Access updated for cand_5 | candidate.cand_5.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_093",
        instruction=(
            "For candidate cand_7, you release docking station DS-007A, assign docking station DS-007B, complete asset request req_701, "
            "remove access check access_701, add new access check access_707, attach Onboarding-Schedule.pdf, "
            "apply email label 'Onboarding' to email email_707, complete checklist item check_707, "
            "log changes for assets and access, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "DS-007A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "DS-007B", "candidate_id": "cand_7"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_701", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_701"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_707", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_18", "file_name": "Onboarding-Schedule.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_707", "label_id": "label_Onboarding"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_707", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Docking station updated for cand_7", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.DS-007A.status=Available | asset.DS-007B.status=Assigned | asset_request.req_701.status=Completed | access_check.access_701=Removed | access_check.access_707.status=Pending | attachment.Onboarding-Schedule.pdf.added=True | email.email_707.labels=label_Onboarding | checklist_item.check_707.status=Completed | log.ASSET_UPDATED.message=Docking station updated for cand_7 | log.ACCESS_UPDATED.message=Access updated for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_081",
        instruction=(
            "For candidate cand_1, you release old laptop LT-001A, assign new laptop LT-001B, complete asset requests req_101 and req_102, "
            "remove access check access_101, add new access check access_103, attach Benefits-Guide.pdf, log changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-001B", "candidate_id": "cand_1"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_101"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_103", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-001A.status=Available | asset.LT-001B.status=Assigned | asset_request.req_101.status=Completed | asset_request.req_102.status=Completed | access_check.access_101=Removed | access_check.access_103.status=Pending | attachment.Benefits-Guide.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_1 | log.ACCESS_UPDATED.message=Access checks updated for cand_1 | candidate.cand_1.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_082",
        instruction=(
            "For candidate cand_4, you release old laptop LT-004A, assign new laptop LT-004B and phone PH-004, complete asset request req_401, "
            "remove access check access_401, add new access check access_403, attach Company-Policies.pdf, log all changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-004A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-004B", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-004", "candidate_id": "cand_4"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_401", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_401"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_403", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Company-Policies.pdf"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-004A.status=Available | asset.LT-004B.status=Assigned | asset.PH-004.status=Assigned | asset_request.req_401.status=Completed | access_check.access_401=Removed | access_check.access_403.status=Pending | attachment.Company-Policies.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_4 | log.ACCESS_UPDATED.message=Access checks updated for cand_4 | candidate.cand_4.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_083",
        instruction=(
            "For candidate cand_6, you release old laptop LT-006A, assign new laptop LT-006B, complete asset request req_601, remove access check access_601, "
            "add new access check access_603, attach Benefits-Guide.pdf, apply email label 'AssetUpdate' to email email_603, complete checklist item check_603, "
            "log changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-006A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-006B", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_601"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="add_attachment",
                   kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_603", "label_id": "label_AssetUpdate"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_603", "updates": {"status": "Completed"}}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-006A.status=Available | asset.LT-006B.status=Assigned | asset_request.req_601.status=Completed | access_check.access_601=Removed | access_check.access_603.status=Pending | attachment.Benefits-Guide.pdf.added=True | email.email_603.labels=label_AssetUpdate | checklist_item.check_603.status=Completed | log.ASSET_UPDATED.message=Assets updated for cand_6 | log.ACCESS_UPDATED.message=Access checks updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_071",
        instruction=(
            "You reassign assets for candidate cand_6: release old laptop LT-006, assign new laptop LT-006B and phone PH-006B, "
            "update asset requests req_601 and req_602 to 'Completed', remove access checks access_601, access_602, add new access checks access_603, access_604, "
            "attach Company-Policies.pdf and Benefits-Guide.pdf, apply label 'AssetChange' to email email_601, log all changes, and mark candidate record updated."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-006"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-006B", "candidate_id": "cand_6"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-006B", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_602", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_601"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_602"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_604", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_601", "label_id": "label_AssetChange"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_6", "candidate_id": "cand_6"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-006.status=Available | asset.LT-006B.status=Assigned | asset.PH-006B.status=Assigned | asset_request.req_601.status=Completed | asset_request.req_602.status=Completed | access_check.access_601=Removed | access_check.access_602=Removed | access_check.access_603.status=Pending | access_check.access_604.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_601.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_6 | log.ACCESS_UPDATED.message=Access checks updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_072",
        instruction=(
            "You assign candidate cand_7 laptop LT-007 and phone PH-007, approve asset requests req_701, req_702, "
            "complete checklist items check_701 and check_702, verify onboarding files welcome.pdf and id_scan.pdf, "
            "apply email label 'Ready' to email email_701, log all changes, and mark candidate record updated."
        ),
        actions=[
            Action(name="assign_asset", kwargs={"asset_tag": "LT-007", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-007", "candidate_id": "cand_7"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_701", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_702", "updates": {"status": "Approved"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_Ready"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-007.status=Assigned | asset.PH-007.status=Assigned | asset_request.req_701.status=Approved | asset_request.req_702.status=Approved | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.welcome.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | email.email_701.labels=label_Ready | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_7 | candidate.cand_7.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_073",
        instruction=(
            "For candidate cand_3, you release old laptop LT-003A, assign new laptop LT-003B, complete checklist items check_303 and check_304, "
            "verify onboarding file offer_letter.pdf, attach Company-Policies.pdf, apply email label 'AssetUpdate' to email email_303, log all changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-003A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_303", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_304", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_303", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New assets assigned for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_3", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-003A.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_303.status=Completed | checklist_item.check_304.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | attachment.Company-Policies.pdf.added=True | email.email_303.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_3 | log.ASSET_ASSIGNED.message=New assets assigned for cand_3 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_3 | candidate.cand_3.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_041",
        instruction=(
            "You approve laptop asset requests for candidates Jane Smith (cand_2) and Peter Jones (cand_3), assign the appropriate laptops, "
            "and update onboarding files to reflect laptop assignment. "
            "End state: asset requests marked 'Approved'; laptops LT-DELL-003 and LT-DELL-002 assigned; onboarding files show laptop_assigned=True; terminal logs capture assignment and approval events."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_Jane_Laptop", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_Peter_Laptop", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-003", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-002", "candidate_id": "cand_3"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Jane_Smith/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Peter_Jones/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_REQUEST_APPROVED", "message": "Laptop requests approved and assigned", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_REQUEST_APPROVED", "message": "Laptop requests approved and assigned", "candidate_id": "cand_3"}),
        ],
        outputs=[
            "asset_request.req_Jane_Laptop.status=Approved | asset_request.req_Peter_Laptop.status=Approved | asset.LT-DELL-003.status=Assigned | asset.LT-DELL-002.status=Assigned | onboarding_files.Jane_Smith.laptop_assigned=True | onboarding_files.Peter_Jones.laptop_assigned=True | log.LAPTOP_REQUEST_APPROVED.message=Laptop requests approved and assigned"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_075",
        instruction=(
            "You reassign candidate cand_2's assets: release laptop LT-002A, assign new laptop LT-002B and phone PH-002B, "
            "complete checklist items check_203 and check_204, verify onboarding file Company-Policies.pdf, apply email label 'AssetUpdate' to email email_203, "
            "log all steps, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-002B", "candidate_id": "cand_2"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_204", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/Company-Policies.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_203", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New assets assigned for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset.PH-002B.status=Assigned | checklist_item.check_203.status=Completed | checklist_item.check_204.status=Completed | onboarding_files.Company-Policies.pdf.status=Verified | email.email_203.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_2 | log.ASSET_ASSIGNED.message=New assets assigned for cand_2 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_077",
        instruction=(
            "For candidate cand_4, you release laptop LT-004A, assign new laptop LT-004B and phone PH-004B, complete checklist item check_404, "
            "verify onboarding file offer_letter.pdf, add attachment Company-Policies.pdf, apply email label 'AssetUpdate' to email email_404, log all actions, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-004A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-004B", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-004B", "candidate_id": "cand_4"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_404", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_404", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist item completed for cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email labeled for cand_4", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-004A.status=Available | asset.LT-004B.status=Assigned | asset.PH-004B.status=Assigned | checklist_item.check_404.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | attachment.Company-Policies.pdf.added=True | email.email_404.labels=label_AssetUpdate | log.ASSET_UPDATED.message=Assets updated for cand_4 | log.CHECKLIST_COMPLETED.message=Checklist item completed for cand_4 | log.EMAIL_LABEL_APPLIED.message=Email labeled for cand_4 | candidate.cand_4.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_078",
        instruction=(
            "For candidate cand_5, you assign laptop LT-005B, phone PH-005B, complete checklist items check_505 and check_506, "
            "verify onboarding files resume.pdf and security_form.pdf, add attachment Company-Policies.pdf, apply email label 'Welcome' to email email_505, log changes, and update candidate record."
        ),
        actions=[
            Action(name="assign_asset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-005B", "candidate_id": "cand_5"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_505", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_506", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/resume.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/security_form.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_505", "label_id": "label_Welcome"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-005B.status=Assigned | asset.PH-005B.status=Assigned | checklist_item.check_505.status=Completed | checklist_item.check_506.status=Completed | onboarding_files.resume.pdf.status=Verified | onboarding_files.security_form.pdf.status=Verified | attachment.Company-Policies.pdf.added=True | email.email_505.labels=label_Welcome | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_5 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_5 | candidate.cand_5.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_079",
        instruction=(
            "For candidate cand_2, you release old laptop LT-002A, assign new laptop LT-002B and phone PH-002B, complete checklist items check_202 and check_203, "
            "verify onboarding file offer_letter.pdf, add attachment Company-Policies.pdf, apply email label 'AssetChange' to email email_202, log all actions, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-002B", "candidate_id": "cand_2"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_202", "label_id": "label_AssetChange"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset.PH-002B.status=Assigned | checklist_item.check_202.status=Completed | checklist_item.check_203.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | attachment.Company-Policies.pdf.added=True | email.email_202.labels=label_AssetChange | log.ASSET_UPDATED.message=Assets updated for cand_2 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_005",#p
        instruction=(
            "You prioritize multiple email labels for cand_6, process multiple emails, update related onboarding files, "
            "assign a laptop, and record terminal events. End state: "
            "email labels show priorities 'Urgent' and 'High'; emails are marked processed; onboarding files updated; "
            "assets assigned; terminal logs 'EMAIL_LABEL_UPDATED', 'ONBOARDING_FILE_UPDATED', and 'ASSET_ASSIGNED' exist."
        ),
        actions=[
            # Update multiple email labels
            Action(name="update_email_label", kwargs={"label_id": "label_2", "updates": {"priority": "Urgent"}}),
            Action(name="update_email_label", kwargs={"label_id": "label_3", "updates": {"priority": "High"}}),

            # Process multiple emails
            Action(name="update_email", kwargs={"email_id": "email_101", "updates": {"processed": True}}),
            Action(name="update_email", kwargs={"email_id": "email_102", "updates": {"processed": True}}),

            # Apply labels to emails
            Action(name="apply_label_to_email", kwargs={"email_id": "email_101", "label_id": "label_2"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_102", "label_id": "label_3"}),

            # Update onboarding files
            Action(name="update_onboarding_file",
                   kwargs={"candidate_id": "cand_6", "updates": {"email_label_applied": True}}),
            Action(name="add_onboarding_file", kwargs={"candidate_id": "cand_6", "file_name": "Email Confirmation",
                                                       "file_path": "/onboarding/email_confirmation.pdf"}),

            # Assign an asset
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MAC-001", "candidate_id": "cand_6"}),
            Action(name="update_asset", kwargs={"asset_tag": "LT-MAC-001", "updates": {"status": "Assigned"}}),

                # Terminal logs
            Action(name="record_terminal_log",
                   kwargs={"event_type": "EMAIL_LABEL_UPDATED", "message": "Email labels 'Urgent' and 'High' applied for cand_6"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ONBOARDING_FILE_UPDATED", "message": "Onboarding files updated for cand_6"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop assigned to cand_6"}),

                # Update candidate onboarding status
            Action(name="update_candidate", kwargs={"candidate_id": "cand_6", "updates": {"onboarding_status": "Ready"}})
            ],
            outputs = [
                "email_label.label_2.priority=Urgent | email_label.label_3.priority=High | "
                "email.email_101.processed=True | email.email_102.processed=True | "
                "onboarding_files.email_label_applied=True | onboarding_files.Email Confirmation.file_path=/onboarding/email_confirmation.pdf | "
                "asset.LT-MAC-001.status=Assigned | "
                "log.EMAIL_LABEL_UPDATED.message=Email labels 'Urgent' and 'High' applied for cand_6 | "
                "log.ONBOARDING_FILE_UPDATED.message=Onboarding files updated for cand_6 | "
                "log.ASSET_ASSIGNED.message=Laptop assigned to cand_6 | "
                "candidate.cand_6.onboarding_status=Ready"
            ],
            ),

    Task(
        annotator="R",
        user_id="onboarding_ds_006",#p
        instruction=(
            "You onboard candidate cand_7 by approving asset requests req_501, req_502, assigning laptop LT-DELL-010, phone PH-SAMSUNG-005, and accessories ACC-MOUSE-001. "
            "Checklist items check_701, check_702 are completed, onboarding files welcome_guide.pdf and id_scan.pdf verified, and access checks access_901, access_902 approved. "
            "Email email_701 labeled 'Welcome'. End state: assets assigned and approved; files verified; checklist and access checks completed; terminal logs exist; candidate onboarding status updated."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-010", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-SAMSUNG-005", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-001", "candidate_id": "cand_7"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop, phone, and accessory assigned to cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_501 and req_502 approved"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email labeled 'Welcome' for cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.LT-DELL-010.status=Assigned | asset.PH-SAMSUNG-005.status=Assigned | asset.ACC-MOUSE-001.status=Assigned | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.welcome_guide.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_Welcome | log.ASSET_ASSIGNED.message=Laptop, phone, and accessory assigned to cand_7 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_501 and req_502 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_7 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_7 | log.EMAIL_LABEL_APPLIED.message=Email labeled 'Welcome' for cand_7 | candidate.cand_7.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_007",#p
        instruction=(
            "You approve candidate cand_7's laptop and phone requests, assign the assets, and ensure onboarding files reflect asset assignment. "
            "End state: asset requests marked 'Approved'; assets PH-LAPTOP-007 and PH-IPHONE-007 assigned to cand_7; onboarding files show phone_assigned=True and laptop_assigned=True; terminal logs capture assignment and approval events."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_701", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_702", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-007", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-007", "candidate_id": "cand_7"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/cand_7_onboarding.json", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_701 and req_702 approved", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-007 assigned", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "PH-LAPTOP-007 assigned", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_701.status=Approved | asset_request.req_702.status=Approved | asset.PH-LAPTOP-007.status=Assigned | asset.PH-IPHONE-007.status=Assigned | onboarding_files.cand_7.laptop_assigned=True | onboarding_files.cand_7.phone_assigned=True | log.ASSET_REQUEST_APPROVED.message=Asset requests req_701 and req_702 approved | log.PHONE_ASSIGNED.message=PH-IPHONE-007 assigned | log.LAPTOP_ASSIGNED.message=PH-LAPTOP-007 assigned | candidate.cand_7.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_008",#p
        instruction=(
            "You approve candidate cand_7's laptop and phone requests, assign the assets, "
            "update onboarding files for asset assignment, complete checklist items, approve access checks, and label emails. "
            "End state: asset requests marked 'Approved'; assets PH-LAPTOP-010, PH-IPHONE-005, and ACC-MOUSE-001 assigned; "
            "checklist items marked 'Completed'; access checks approved; onboarding files reflect assigned assets; "
            "email labeled 'Welcome'; terminal logs capture all actions."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-010", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-005", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-001", "candidate_id": "cand_7"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True, "accessory_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_501 and req_502 approved", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "PH-LAPTOP-010, PH-IPHONE-005, and ACC-MOUSE-001 assigned", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items check_701 and check_702 completed", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks access_901 and access_902 approved", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email email_701 labeled Welcome", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.PH-LAPTOP-010.status=Assigned | asset.PH-IPHONE-005.status=Assigned | asset.ACC-MOUSE-001.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | onboarding_files.welcome_guide.phone_assigned=True | onboarding_files.welcome_guide.accessory_assigned=True | onboarding_files.id_scan.status=Verified | checklist.check_701.status=Completed | checklist.check_702.status=Completed | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_Welcome | candidate.cand_7.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_009",#p
        instruction=(
            "You approve candidate cand_7's laptop request, assign the asset, update onboarding files for laptop assignment, and record logs. "
            "End state: laptop request approved; laptop PH-LAPTOP-010 assigned; onboarding files show laptop_assigned=True; terminal logs capture assignment and approval."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-010", "candidate_id": "cand_7"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_501 approved", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "PH-LAPTOP-010 assigned", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "LaptopAssigned"}})
        ],
        outputs=[
            "asset_request.req_501.status=Approved | asset.PH-LAPTOP-010.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | log.ASSET_REQUEST_APPROVED.message=Asset request req_501 approved | log.LAPTOP_ASSIGNED.message=PH-LAPTOP-010 assigned | candidate.cand_7.onboarding_status=LaptopAssigned"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_010",#p
        instruction=(
            "You approve candidate cand_7's phone request, assign the asset, update onboarding files for phone assignment, complete checklist items, "
            "approve access checks, apply email labels, and record logs. "
            "End state: phone request approved; asset PH-IPHONE-005 assigned; onboarding files show phone_assigned=True; checklist items completed; access checks approved; email labeled 'Welcome'; terminal logs capture all actions."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-005", "candidate_id": "cand_7"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"phone_assigned": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_502 approved", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-005 assigned", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items check_701 and check_702 completed", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks access_901 and access_902 approved", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email email_701 labeled Welcome", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "AssetsAndChecksReady"}})
        ],
        outputs=[
            "asset_request.req_502.status=Approved | asset.PH-IPHONE-005.status=Assigned | onboarding_files.welcome_guide.phone_assigned=True | checklist.check_701.status=Completed | checklist.check_702.status=Completed | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_Welcome | log.ASSET_REQUEST_APPROVED.message=Asset request req_502 approved | log.PHONE_ASSIGNED.message=PH-IPHONE-005 assigned | log.CHECKLIST_COMPLETED.message=Checklist items check_701 and check_702 completed | log.ACCESS_CHECK_APPROVED.message=Access checks access_901 and access_902 approved | log.EMAIL_LABEL_APPLIED.message=Email email_701 labeled Welcome | candidate.cand_7.onboarding_status=AssetsAndChecksReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_011",
        instruction=(
            "You complete full onboarding for candidate cand_7: approve all asset requests (laptop, phone, accessories), assign assets, "
            "complete all checklist items, approve all access checks, update multiple onboarding files, apply multiple email labels, "
            "and record terminal logs for each step. "
            "End state: all assets assigned; checklist items completed; access checks approved; onboarding files updated; emails labeled; logs capture all actions; candidate status reflects full onboarding."
        ),
        actions=[
            # Asset requests approval
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),

            # Assign assets
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-010", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-005", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-001", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-KEYBOARD-002", "candidate_id": "cand_7"}),

            # Update onboarding files
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide.pdf",
                                                          "updates": {"laptop_assigned": True,
                                                                      "phone_assigned": True}}),
            Action(name="update_onboarding_file",
                   kwargs={"file_path": "files/id_scan.pdf", "updates": {"verified": True}}),
            Action(name="update_onboarding_file",
                   kwargs={"file_path": "files/policy_acknowledgment.pdf", "updates": {"acknowledged": True}}),

            # Checklist completion
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_703", "updates": {"status": "Completed"}}),

            # Access checks
            Action(name="update_access_check", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_903", "updates": {"status": "Approved"}}),

            # Email labels
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_702", "label_id": "label_Policy"}),

            # Terminal logs
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED",
                                                       "message": "Asset requests req_501 and req_502 approved",
                                                       "candidate_id": "cand_7"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, mouse, and keyboard assigned",
                           "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED",
                                                       "message": "Checklist items check_701, check_702, check_703 completed",
                                                       "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED",
                                                       "message": "Access checks access_901, access_902, access_903 approved",
                                                       "candidate_id": "cand_7"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Emails email_701 and email_702 labeled",
                           "candidate_id": "cand_7"}),

            # Candidate status update
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[
            "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.PH-LAPTOP-010.status=Assigned | asset.PH-IPHONE-005.status=Assigned | asset.ACC-MOUSE-001.status=Assigned | asset.ACC-KEYBOARD-002.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | onboarding_files.welcome_guide.phone_assigned=True | onboarding_files.id_scan.verified=True | onboarding_files.policy_acknowledgment.acknowledged=True | checklist.check_701.status=Completed | checklist.check_702.status=Completed | checklist.check_703.status=Completed | access_check.access_901.status=Approved | access_check.access_902.status=Approved | access_check.access_903.status=Approved | email.email_701.labels=label_Welcome | email.email_702.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_501 and req_502 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, mouse, and keyboard assigned | log.CHECKLIST_COMPLETED.message=Checklist items check_701, check_702, check_703 completed | log.ACCESS_CHECK_APPROVED.message=Access checks access_901, access_902, access_903 approved | log.EMAIL_LABEL_APPLIED.message=Emails email_701 and email_702 labeled | candidate.cand_7.onboarding_status=OnboardingCompleted"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_055",
        instruction=(
            "You approve candidate cand_5's laptop request req_105, assign LT-MBP-003, mark onboarding files verified, complete checklist items check_207, check_208, "
            "approve access checks access_306, access_307, and record all terminal logs. End state: candidate assets assigned and onboarding ready."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_105", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MBP-003", "candidate_id": "cand_5"}),
            Action(name="update_onboarding_file",
                   kwargs={"file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md",
                           "updates": {"laptop_assigned": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_207", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_208", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_306", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_307", "updates": {"status": "Approved"}}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop LT-MBP-003 assigned to cand_5"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_105 approved"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_5"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_5"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_105.status=Approved | asset.LT-MBP-003.status=Assigned | onboarding_files.Alex_Thompson.laptop_assigned=True | checklist_item.check_207.status=Completed | checklist_item.check_208.status=Completed | access_check.access_306.status=Approved | access_check.access_307.status=Approved | log.ASSET_ASSIGNED.message=Laptop LT-MBP-003 assigned to cand_5 | log.ASSET_REQUEST_APPROVED.message=Asset request req_105 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_5 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_5 | candidate.cand_5.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_042",
        instruction=(
            "You approve and assign laptops to multiple candidates (Jane Smith cand_2, Peter Jones cand_3, Maria Rodriguez cand_4) based on asset requests. "
            "Select appropriate laptops based on specifications and availability, update onboarding files, and generate terminal logs for each assignment. "
            "End state: asset requests marked 'Approved'; laptops LT-DELL-003, LT-DELL-002, LT-MBP-001 assigned; onboarding files show laptop_assigned=True; logs capture all approvals and assignments."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_Jane_Laptop", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_Peter_Laptop", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_Maria_Laptop", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-003", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-002", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_4"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Jane_Smith/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Peter_Jones/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Maria_Rodriguez/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "Laptops assigned to Jane, Peter, Maria", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "Laptops assigned to Jane, Peter, Maria", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "Laptops assigned to Jane, Peter, Maria", "candidate_id": "cand_4"}),
        ],
        outputs=[
            "asset_request.req_Jane_Laptop.status=Approved | asset_request.req_Peter_Laptop.status=Approved | asset_request.req_Maria_Laptop.status=Approved | asset.LT-DELL-003.status=Assigned | asset.LT-DELL-002.status=Assigned | asset.LT-MBP-001.status=Assigned | onboarding_files.Jane_Smith.laptop_assigned=True | onboarding_files.Peter_Jones.laptop_assigned=True | onboarding_files.Maria_Rodriguez.laptop_assigned=True | log.LAPTOP_ASSIGNED.message=Laptops assigned to Jane, Peter, Maria"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_043",
        instruction=(
            "You approve and assign both laptop and phone for candidate Alex Thompson (cand_5). "
            "Update onboarding file to reflect laptop_assigned=True and phone_assigned=True, record terminal logs, and update candidate onboarding status to 'AssetsReady'. "
            "End state: asset requests marked 'Approved'; laptop LT-MBP-002 and phone PH-IPHONE-001 assigned; onboarding file updated; candidate status updated."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_Alex_Laptop", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_Alex_Phone", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MBP-002", "candidate_id": "cand_5"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_5"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Alex_Thompson/asset_request.json", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Laptop and phone approved for Alex Thompson", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "LT-MBP-002 assigned", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-001 assigned", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_Alex_Laptop.status=Approved | asset_request.req_Alex_Phone.status=Approved | asset.LT-MBP-002.status=Assigned | asset.PH-IPHONE-001.status=Assigned | onboarding_files.Alex_Thompson.laptop_assigned=True | onboarding_files.Alex_Thompson.phone_assigned=True | log.ASSET_REQUEST_APPROVED.message=Laptop and phone approved for Alex Thompson | log.LAPTOP_ASSIGNED.message=LT-MBP-002 assigned | log.PHONE_ASSIGNED.message=PH-IPHONE-001 assigned | candidate.cand_5.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_044",
        instruction=(
            "You approve cand_2's laptop request, assign the laptop, and update onboarding file to reflect laptop assignment. "
            "End state: asset request approved; LT-DELL-003 assigned to cand_2; onboarding file shows laptop_assigned=True; terminal logs capture approval and assignment events."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-003", "candidate_id": "cand_2"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Jane_Smith/asset_request.json",
                                                          "updates": {"laptop_assigned": True}}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_101 approved",
                           "candidate_id": "cand_2"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "LT-DELL-003 assigned",
                           "candidate_id": "cand_2"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_101.status=Approved | asset.LT-DELL-003.status=Assigned | onboarding_files.cand_2.laptop_assigned=True | log.ASSET_REQUEST_APPROVED.message=Asset request req_101 approved | log.LAPTOP_ASSIGNED.message=LT-DELL-003 assigned | candidate.cand_2.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_046",
        instruction=(
            "You approve cand_4's laptop and phone requests, assign assets, resolve pending access issues, and update onboarding files."
            "End state: asset requests approved; LT-MBP-001 and PH-IPHONE-002 assigned; onboarding files show laptop_assigned=True, phone_assigned=True; access issues logged as resolved."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_104", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_105", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-002", "candidate_id": "cand_4"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Maria_Rodriguez/asset_request.json", "updates": {"laptop_assigned": True, "phone_assigned": True, "access_issues_resolved": True}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_104 and req_105 approved", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "LT-MBP-001 assigned", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-002 assigned", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_104.status=Approved | asset_request.req_105.status=Approved | asset.LT-MBP-001.status=Assigned | asset.PH-IPHONE-002.status=Assigned | onboarding_files.cand_4.laptop_assigned=True | onboarding_files.cand_4.phone_assigned=True | onboarding_files.cand_4.access_issues_resolved=True | log.ASSET_REQUEST_APPROVED.message=Asset requests req_104 and req_105 approved | log.LAPTOP_ASSIGNED.message=LT-MBP-001 assigned | log.PHONE_ASSIGNED.message=PH-IPHONE-002 assigned | candidate.cand_4.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_033",
        instruction=(
            "You approve candidate cand_7's laptop request, assign the asset, update onboarding files for laptop assignment, complete checklist items, "
            "approve access checks, apply email labels, and record logs. "
            "End state: laptop request approved; laptop PH-LAPTOP-010 assigned; onboarding files show laptop_assigned=True; checklist items completed; access checks approved; email labeled 'Welcome'; terminal logs capture all actions."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-010", "candidate_id": "cand_7"}),
            Action(name="update_onboarding_file",
                   kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_501 approved",
                           "candidate_id": "cand_7"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "PH-LAPTOP-010 assigned",
                           "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED",
                                                       "message": "Checklist items check_701 and check_702 completed",
                                                       "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED",
                                                       "message": "Access checks access_901 and access_902 approved",
                                                       "candidate_id": "cand_7"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email email_701 labeled Welcome",
                           "candidate_id": "cand_7"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "AssetsAndChecksReady"}})
        ],
        outputs=[
            "asset_request.req_501.status=Approved | asset.PH-LAPTOP-010.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | checklist.check_701.status=Completed | checklist.check_702.status=Completed | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_Welcome | log.ASSET_REQUEST_APPROVED.message=Asset request req_501 approved | log.LAPTOP_ASSIGNED.message=PH-LAPTOP-010 assigned | log.CHECKLIST_COMPLETED.message=Checklist items check_701 and check_702 completed | log.ACCESS_CHECK_APPROVED.message=Access checks access_901 and access_902 approved | log.EMAIL_LABEL_APPLIED.message=Email email_701 labeled Welcome | candidate.cand_7.onboarding_status=AssetsAndChecksReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_001",
        instruction=(
            "You approve asset requests req_101, req_102 for candidate cand_1, assign laptop LT-001 and phone PH-001, "
            "complete checklist items check_101 and check_102, verify onboarding files welcome.pdf and id_scan.pdf, "
            "apply label 'Welcome' to email email_101, and log all changes. Ensure candidate record reflects completion."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-001", "candidate_id": "cand_1"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-001", "candidate_id": "cand_1"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_101", "label_id": "label_Welcome"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_1", "candidate_id": "cand_1"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_101.status=Approved | asset_request.req_102.status=Approved | asset.LT-001.status=Assigned | asset.PH-001.status=Assigned | checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | onboarding_files.welcome.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | email.email_101.labels=label_Welcome | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_1 | candidate.cand_1.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_002",
        instruction=(
            "You approve candidate cand_2's asset requests req_201 and req_202, assign assets LT-002 and PH-002, "
            "complete checklist check_201, verify onboarding file offer_letter.pdf, apply label 'Ready' to email email_201, "
            "and log all steps. Update candidate record to mark completion."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_201", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_202", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-002", "candidate_id": "cand_2"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_201", "label_id": "label_Ready"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Assets assigned to cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'Ready' for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_201.status=Approved | asset_request.req_202.status=Approved | asset.LT-002.status=Assigned | asset.PH-002.status=Assigned | checklist_item.check_201.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | email.email_201.labels=label_Ready | log.ASSET_ASSIGNED.message=Assets assigned to cand_2 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_2 | log.EMAIL_LABELED.message=Email labeled 'Ready' for cand_2 | candidate.cand_2.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_003",
        instruction=(
            "You release old assets LT-003 and PH-003 for candidate cand_3, assign new laptop LT-003B, "
            "complete checklist items check_301 and check_302, add onboarding file id_scan.pdf, "
            "apply email label 'AssetUpdate' to email email_301, log all changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-003"}),
            Action(name="release_asset", kwargs={"asset_tag": "PH-003"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/id_scan.pdf", "status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_301", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'AssetUpdate' for cand_3", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-003.status=Available | asset.PH-003.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | onboarding_files.id_scan.pdf.status=Verified | email.email_301.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_3 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_3 | log.EMAIL_LABELED.message=Email labeled 'AssetUpdate' for cand_3 | candidate.cand_3.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_003",
        instruction=(
            "You release old assets LT-003 and PH-003 for candidate cand_3, assign new laptop LT-003B, "
            "complete checklist items check_301 and check_302, add onboarding file id_scan.pdf, "
            "apply email label 'AssetUpdate' to email email_301, log all changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-003"}),
            Action(name="release_asset", kwargs={"asset_tag": "PH-003"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/id_scan.pdf", "status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_301", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_3", "candidate_id": "cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'AssetUpdate' for cand_3", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-003.status=Available | asset.PH-003.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | onboarding_files.id_scan.pdf.status=Verified | email.email_301.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_3 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_3 | log.EMAIL_LABELED.message=Email labeled 'AssetUpdate' for cand_3 | candidate.cand_3.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_004",
        instruction=(
            "You approve asset requests req_401 for candidate cand_4, assign laptop LT-004 and phone PH-004, "
            "complete checklist item check_401, add onboarding file welcome_guide.pdf, "
            "apply email label 'Onboarded' to email email_401, log all actions, and mark candidate record completed."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_401", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-004", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-004", "candidate_id": "cand_4"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_401", "updates": {"status": "Completed"}}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/welcome_guide.pdf", "status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_401", "label_id": "label_Onboarded"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Assets assigned for cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_4", "candidate_id": "cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'Onboarded' for cand_4", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_401.status=Approved | asset.LT-004.status=Assigned | asset.PH-004.status=Assigned | checklist_item.check_401.status=Completed | onboarding_files.welcome_guide.pdf.status=Verified | email.email_401.labels=label_Onboarded | log.ASSET_ASSIGNED.message=Assets assigned for cand_4 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_4 | log.EMAIL_LABELED.message=Email labeled 'Onboarded' for cand_4 | candidate.cand_4.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_005",
        instruction=(
            "You reassign assets for candidate cand_5: release old laptop LT-005, assign new laptop LT-005B, "
            "complete checklist item check_501, verify onboarding file id_scan.pdf, apply email label 'AssetUpdate' to email email_501, "
            "log all updates, and mark candidate record updated."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-005"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_501", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_501", "label_id": "label_AssetUpdate"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_5", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New assets assigned for cand_5", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'AssetUpdate' for cand_5", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-005.status=Available | asset.LT-005B.status=Assigned | checklist_item.check_501.status=Completed | onboarding_files.id_scan.pdf.status=Verified | email.email_501.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_5 | log.ASSET_ASSIGNED.message=New assets assigned for cand_5 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_5 | log.EMAIL_LABELED.message=Email labeled 'AssetUpdate' for cand_5 | candidate.cand_5.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_068",
        instruction=(
            "You finalize onboarding for candidate cand_4: approve asset requests req_401, req_402, assign laptop LT-DELL-004, phone PH-SAMSUNG-004, and mouse ACC-MOUSE-004. "
            "Complete checklist items check_401, check_402, verify onboarding files welcome_guide.pdf and id_scan.pdf. Approve access checks access_401, access_402. "
            "Label email email_401 as 'OnboardingReady' and log all updates."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_401", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_402", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-004", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-SAMSUNG-004", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-004", "candidate_id": "cand_4"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_401", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_402", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_401", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_402", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_401", "label_id": "label_OnboardingReady"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Candidate cand_4 onboarding completed", "candidate_id": "cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_401.status=Approved | asset_request.req_402.status=Approved | asset.LT-DELL-004.status=Assigned | asset.PH-SAMSUNG-004.status=Assigned | asset.ACC-MOUSE-004.status=Assigned | checklist_item.check_401.status=Completed | checklist_item.check_402.status=Completed | onboarding_files.welcome_guide.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_401.status=Approved | access_check.access_402.status=Approved | email.email_401.labels=label_OnboardingReady | log.ONBOARDING_COMPLETED.message=Candidate cand_4 onboarding completed | candidate.cand_4.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_065",
        instruction=(
            "You update assets for candidate cand_7: release laptop LT-OLD-007, assign new laptop LT-NEW-007, phone PH-NEW-007, and headset ACC-HEADSET-007. "
            "Complete asset requests req_701, req_702, remove access checks access_701, access_702, add access checks access_703, access_704. "
            "Attach Company-Policies.pdf, apply label 'AssetChange' to email email_701, and log all updates."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-OLD-007"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-NEW-007", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-NEW-007", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-HEADSET-007", "candidate_id": "cand_7"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_701", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_702", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_701"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_702"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_703", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_704", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_AssetChange"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_7", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-OLD-007.status=Available | asset.LT-NEW-007.status=Assigned | asset.PH-NEW-007.status=Assigned | asset.ACC-HEADSET-007.status=Assigned | asset_request.req_701.status=Completed | asset_request.req_702.status=Completed | access_check.access_701=Removed | access_check.access_702=Removed | access_check.access_703.status=Pending | access_check.access_704.status=Pending | attachment.Company-Policies.pdf.added=True | email.email_701.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_7 | log.ACCESS_UPDATED.message=Access checks updated for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ],
    ),


    Task(
        annotator="R",
        user_id="onboarding_ds_064",
        instruction=(
            "You finalize onboarding for candidate cand_1: approve asset requests req_101, req_102, assign laptop LT-HP-001, phone PH-IP-001. "
            "Complete checklist items check_101, check_102, verify files offer_letter.pdf and id_scan.pdf. Approve access checks access_101, access_102. "
            "Label email email_101 as 'OnboardingReady' and log all updates."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-HP-001", "candidate_id": "cand_1"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IP-001", "candidate_id": "cand_1"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_101", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_102", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_101", "label_id": "label_OnboardingReady"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Candidate cand_1 onboarding completed", "candidate_id": "cand_1"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_101.status=Approved | asset_request.req_102.status=Approved | asset.LT-HP-001.status=Assigned | asset.PH-IP-001.status=Assigned | checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_101.status=Approved | access_check.access_102.status=Approved | email.email_101.labels=label_OnboardingReady | log.ONBOARDING_COMPLETED.message=Candidate cand_1 onboarding completed | candidate.cand_1.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_062",
        instruction=(
            "You finalize onboarding for candidate cand_3: approve asset requests req_301, req_302, assign laptop LT-HP-003, phone PH-IP-003. "
            "Complete checklist items check_301, check_302, verify onboarding files offer_letter.pdf and id_scan.pdf. Approve access checks access_301, access_302. "
            "Label email email_301 as 'OnboardingReady' and log all updates."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_301", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_302", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-HP-003", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IP-003", "candidate_id": "cand_3"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_301", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_302", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_301", "label_id": "label_OnboardingReady"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Candidate cand_3 onboarding completed", "candidate_id": "cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_301.status=Approved | asset_request.req_302.status=Approved | asset.LT-HP-003.status=Assigned | asset.PH-IP-003.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_301.status=Approved | access_check.access_302.status=Approved | email.email_301.labels=label_OnboardingReady | log.ONBOARDING_COMPLETED.message=Candidate cand_3 onboarding completed | candidate.cand_3.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_061",
        instruction=(
            "You onboard candidate cand_2 by approving asset requests req_201, req_202, assign laptop LT-MBP-004, phone PH-IPHONE-002, "
            "and accessory ACC-HEADSET-001. Complete checklist items check_301, check_302, approve access checks access_401, access_402, "
            "update onboarding files welcome_Jane_Smith.md and asset_request.json, and record terminal logs. "
            "End state: assets assigned and approved, files verified, checklist and access completed, candidate onboarding status updated."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_201", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_202", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MBP-004", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-002", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-HEADSET-001", "candidate_id": "cand_2"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_401", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_402", "updates": {"status": "Approved"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Jane_Smith/asset_request.json", "updates": {"assigned_assets": ["LT-MBP-004", "PH-IPHONE-002", "ACC-HEADSET-001"]}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop, phone, and headset assigned to cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_201 and req_202 approved"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_201.status=Approved | asset_request.req_202.status=Approved | asset.LT-MBP-004.status=Assigned | asset.PH-IPHONE-002.status=Assigned | asset.ACC-HEADSET-001.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | access_check.access_401.status=Approved | access_check.access_402.status=Approved | onboarding_files.Jane_Smith.laptop_assigned=True | onboarding_files.Jane_Smith.phone_assigned=True | onboarding_files.Jane_Smith.asset_request.assigned_assets=['LT-MBP-004','PH-IPHONE-002','ACC-HEADSET-001'] | log.ASSET_ASSIGNED.message=Laptop, phone, and headset assigned to cand_2 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_201 and req_202 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_2 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_2 | candidate.cand_2.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_062",
        instruction=(
            "You onboard candidate cand_3 by approving laptop request req_203 and accessory requests req_204, assign LT-DELL-003, monitor MON-LG-002, "
            "keyboard ACC-KEYBOARD-001, complete checklist items check_303, check_304, approve access checks access_403, access_404, update onboarding files, "
            "and record terminal logs. End state: all assets assigned and approved, files verified, checklist and access checks completed, candidate status updated."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_203", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_204", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-003", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "MON-LG-002", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-KEYBOARD-001", "candidate_id": "cand_3"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_303", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_304", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_403", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_404", "updates": {"status": "Approved"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md", "updates": {"laptop_assigned": True, "monitor_assigned": True, "keyboard_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Peter_Jones/asset_request.json", "updates": {"assigned_assets": ["LT-DELL-003","MON-LG-002","ACC-KEYBOARD-001"]}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop, monitor, and keyboard assigned to cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_203 and req_204 approved"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_3"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_3"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_203.status=Approved | asset_request.req_204.status=Approved | asset.LT-DELL-003.status=Assigned | asset.MON-LG-002.status=Assigned | asset.ACC-KEYBOARD-001.status=Assigned | checklist_item.check_303.status=Completed | checklist_item.check_304.status=Completed | access_check.access_403.status=Approved | access_check.access_404.status=Approved | onboarding_files.Peter_Jones.laptop_assigned=True | onboarding_files.Peter_Jones.monitor_assigned=True | onboarding_files.Peter_Jones.keyboard_assigned=True | onboarding_files.Peter_Jones.asset_request.assigned_assets=['LT-DELL-003','MON-LG-002','ACC-KEYBOARD-001'] | log.ASSET_ASSIGNED.message=Laptop, monitor, and keyboard assigned to cand_3 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_203 and req_204 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_3 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_3 | candidate.cand_3.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_063",
        instruction=(
            "You onboard candidate cand_4 by approving laptop request req_205, phone request req_206, accessory request req_207, assign LT-MBP-005, "
            "PH-IPHONE-003, ACC-MOUSE-002, complete checklist items check_305, check_306, approve access checks access_405, access_406, update onboarding files "
            "welcome and asset_request.json, and log all actions. End state: all assets assigned, files verified, checklist and access completed, candidate status updated."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_205", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_206", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_207", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MBP-005", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-003", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-002", "candidate_id": "cand_4"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_305", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_306", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_405", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_406", "updates": {"status": "Approved"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md", "updates": {"laptop_assigned": True, "phone_assigned": True, "accessory_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Maria_Rodriguez/asset_request.json", "updates": {"assigned_assets": ["LT-MBP-005","PH-IPHONE-003","ACC-MOUSE-002"]}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop, phone, and accessory assigned to cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_205, req_206, req_207 approved"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_4"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_205.status=Approved | asset_request.req_206.status=Approved | asset_request.req_207.status=Approved | asset.LT-MBP-005.status=Assigned | asset.PH-IPHONE-003.status=Assigned | asset.ACC-MOUSE-002.status=Assigned | checklist_item.check_305.status=Completed | checklist_item.check_306.status=Completed | access_check.access_405.status=Approved | access_check.access_406.status=Approved | onboarding_files.Maria_Rodriguez.laptop_assigned=True | onboarding_files.Maria_Rodriguez.phone_assigned=True | onboarding_files.Maria_Rodriguez.accessory_assigned=True | onboarding_files.Maria_Rodriguez.asset_request.assigned_assets=['LT-MBP-005','PH-IPHONE-003','ACC-MOUSE-002'] | log.ASSET_ASSIGNED.message=Laptop, phone, and accessory assigned to cand_4 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_205, req_206, req_207 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_4 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_4 | candidate.cand_4.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_064",
        instruction=(
            "Candidate cand_6 has multiple pending assets and emails. You approve asset request req_601, assign laptop LT-LENOVO-006. "
            "Send a welcome email ('Welcome!', 'Hello cand_6') email_601, attach file welcome_attach.pdf, apply label 'Onboarding' to email_601. "
            "Release old asset LT-OLD-001. Record all terminal logs for actions. End state: new asset assigned, email sent with label, old asset released."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_601", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-LENOVO-006", "candidate_id": "cand_6"}),
            Action(name="send_email", kwargs={"email": {"message_id": "email_601", "subject": "Welcome!", "body": "Hello cand_6"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_601", "file_name": "welcome_attach.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_601", "label_id": "label_Onboarding"}),
            Action(name="release_asset", kwargs={"asset_tag": "LT-OLD-001"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED", "message": "LT-LENOVO-006 assigned to cand_6", "candidate_id": "cand_6"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_SENT", "message": "Welcome email sent to cand_6", "candidate_id": "cand_6"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_RELEASED", "message": "LT-OLD-001 released from cand_6", "candidate_id": "cand_6"})
        ],
        outputs=[
            "asset_request.req_601.status=Approved | asset.LT-LENOVO-006.status=Assigned | email.email_601.labels=label_Onboarding | attachment.attach_601.file_name=welcome_attach.pdf | asset.LT-OLD-001.status=Available | log.ASSET_ASSIGNED.message=LT-LENOVO-006 assigned to cand_6 | log.EMAIL_SENT.message=Welcome email sent to cand_6 | log.ASSET_RELEASED.message=LT-OLD-001 released from cand_6"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_065",
        instruction=(
            "Candidate cand_7 has email cleanup and asset reassignment tasks. You delete email email_701, remove attachment attach_701, add new onboarding file policies_cand7.pdf, "
            "update checklist item check_701 as Completed, approve access check access_701. Record terminal logs for each step."
        ),
        actions=[
            Action(name="delete_email", kwargs={"message_id": "email_701"}),
            Action(name="remove_attachment", kwargs={"attachment_id": "attach_701"}),
            Action(name="add_onboarding_file", kwargs={"file": {"file_path": "files/policies_cand7.pdf", "status": "Uploaded"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_701", "updates": {"status": "Approved"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_DELETED", "message": "email_701 deleted for cand_7", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ATTACHMENT_REMOVED", "message": "attach_701 removed for cand_7", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_FILE_ADDED", "message": "policies_cand7.pdf uploaded", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_UPDATED", "message": "check_701 completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_APPROVED", "message": "access_701 approved for cand_7", "candidate_id": "cand_7"})
        ],
        outputs=[
            "email.email_701.status=Deleted | attachment.attach_701.status=Removed | onboarding_files.policies_cand7.pdf.status=Uploaded | checklist_item.check_701.status=Completed | access_check.access_701.status=Approved | log.EMAIL_DELETED.message=email_701 deleted for cand_7 | log.ATTACHMENT_REMOVED.message=attach_701 removed for cand_7 | log.ONBOARDING_FILE_ADDED.message=policies_cand7.pdf uploaded | log.CHECKLIST_UPDATED.message=check_701 completed for cand_7 | log.ACCESS_APPROVED.message=access_701 approved for cand_7"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_407",
        instruction=(
            "For candidate cand_7, you release old laptop LT-007A, assign new laptop LT-007B, complete asset requests req_701, req_702, "
            "remove access checks access_701, access_702, add new access checks access_703, access_704, attach Company-Policies.pdf and Benefits-Guide.pdf, "
            "apply label 'AssetUpdate' to emails email_701, email_702, update checklist items check_701, check_702, verify onboarding files ID-Card.pdf and Passport.pdf, "
            "log all changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-007A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-007B", "candidate_id": "cand_7"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_701", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_702", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_701"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_702"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_703", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_704", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_13", "file_name": "Company-Policies.pdf"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_14", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_AssetUpdate"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_702", "label_id": "label_AssetUpdate"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/ID-Card.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/Passport.pdf", "updates": {"status": "Verified"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Full asset and checklist update for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-007A.status=Available | asset.LT-007B.status=Assigned | asset_request.req_701.status=Completed | asset_request.req_702.status=Completed | access_check.access_701=Removed | access_check.access_702=Removed | access_check.access_703.status=Pending | access_check.access_704.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_701.labels=label_AssetUpdate | email.email_702.labels=label_AssetUpdate | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.ID-Card.pdf.status=Verified | onboarding_files.Passport.pdf.status=Verified | log.ONBOARDING_COMPLETED.message=Full asset and checklist update for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_067",
        instruction=(
            "You process candidate cand_7's offboarding: release assets LT-OLD-007 and PH-OLD-007, remove checklist items check_701, check_702, revoke access checks access_701 and access_702, delete onboarding files farewell.pdf and exit_form.pdf, and log events."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-OLD-007"}),
            Action(name="release_asset", kwargs={"asset_tag": "PH-OLD-007"}),
            Action(name="remove_checklist_item", kwargs={"item_id": "check_701"}),
            Action(name="remove_checklist_item", kwargs={"item_id": "check_702"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_701"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_702"}),
            Action(name="remove_onboarding_file", kwargs={"file_path": "files/farewell.pdf"}),
            Action(name="remove_onboarding_file", kwargs={"file_path": "files/exit_form.pdf"}),
            Action(name="record_terminal_log", kwargs={"event_type": "OFFBOARDING_ASSETS_RELEASED", "message": "Assets released for cand_7", "candidate_id": "cand_7"}),
            Action(name="record_terminal_log", kwargs={"event_type": "OFFBOARDING_COMPLETED", "message": "Checklist, access, and files removed for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"offboarding_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-OLD-007.status=Available | asset.PH-OLD-007.status=Available | checklist_item.check_701=Removed | checklist_item.check_702=Removed | access_check.access_701=Removed | access_check.access_702=Removed | onboarding_files.farewell.pdf=Removed | onboarding_files.exit_form.pdf=Removed | log.OFFBOARDING_ASSETS_RELEASED.message=Assets released for cand_7 | log.OFFBOARDING_COMPLETED.message=Checklist, access, and files removed for cand_7 | candidate.cand_7.offboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_068",
        instruction=(
            "You onboard candidate cand_7: approve asset requests req_701 and req_702, assign laptop LT-HP-007, phone PH-IP-007, and accessory ACC-KEY-007. "
            "Complete checklist items check_801 and check_802. Verify onboarding files resume.pdf and id_scan.pdf. Approve access checks access_901 and access_902. "
            "Label email email_701 as 'OnboardingComplete' and log all actions."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_701", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_702", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-HP-007", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IP-007", "candidate_id": "cand_7"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-KEY-007", "candidate_id": "cand_7"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_801", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_802", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/resume.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_701", "label_id": "label_OnboardingComplete"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "All onboarding steps completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[
            "asset_request.req_701.status=Approved | asset_request.req_702.status=Approved | asset.LT-HP-007.status=Assigned | asset.PH-IP-007.status=Assigned | asset.ACC-KEY-007.status=Assigned | checklist_item.check_801.status=Completed | checklist_item.check_802.status=Completed | onboarding_files.resume.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_OnboardingComplete | log.ONBOARDING_COMPLETED.message=All onboarding steps completed for cand_7 | candidate.cand_7.onboarding_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_069",
        instruction=(
            "You reassign assets for candidate cand_6: release old phone PH-OLD-006, assign new laptop LT-NEW-006 and new phone PH-NEW-006. "
            "Update asset requests req_603 and req_604 to 'Completed'. Remove access checks access_603, add new access checks access_605 and access_606. "
            "Add attachments Company-Policies.pdf and Benefits-Guide.pdf, apply label 'AssetChange' to email email_602, and log all changes."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "PH-OLD-006"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-NEW-006", "candidate_id": "cand_6"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-NEW-006", "candidate_id": "cand_6"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_603", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_604", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_603"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_605", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_606", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_602", "label_id": "label_AssetChange"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_6", "candidate_id": "cand_6"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.PH-OLD-006.status=Available | asset.LT-NEW-006.status=Assigned | asset.PH-NEW-006.status=Assigned | asset_request.req_603.status=Completed | asset_request.req_604.status=Completed | access_check.access_603=Removed | access_check.access_605.status=Pending | access_check.access_606.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_602.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_6 | log.ACCESS_UPDATED.message=Access checks updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_070",
        instruction=(
            "You finalize onboarding for candidate cand_5: approve asset requests req_501 and req_502, assign laptop LT-DELL-005, phone PH-SAMSUNG-005, and mouse ACC-MOUSE-005. "
            "Mark checklist items check_701 and check_702 as completed. Verify onboarding files offer_letter.pdf and id_scan.pdf. Approve access checks access_801 and access_802. "
            "Send email email_501 with label 'OnboardingReady' and record terminal logs for all updates."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-005", "candidate_id": "cand_5"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-SAMSUNG-005", "candidate_id": "cand_5"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-005", "candidate_id": "cand_5"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_801", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_802", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_501", "label_id": "label_OnboardingReady"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_FINALIZED", "message": "Candidate cand_5 onboarding finalized", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "Ready"}})
        ],
        outputs=[
            "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.LT-DELL-005.status=Assigned | asset.PH-SAMSUNG-005.status=Assigned | asset.ACC-MOUSE-005.status=Assigned | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_801.status=Approved | access_check.access_802.status=Approved | email.email_501.labels=label_OnboardingReady | log.ONBOARDING_FINALIZED.message=Candidate cand_5 onboarding finalized | candidate.cand_5.onboarding_status=Ready"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_052",
        instruction=(
            "You approve candidate cand_2's laptop request req_101, assign laptop LT-MBP-001, update onboarding files to mark laptop_assigned=True, "
            "complete checklist items check_201 and check_202, approve access checks access_301, and record all terminal logs. "
            "End state: laptop assigned and approved, files, checklist, and access checks completed, candidate onboarding status updated."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_2"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md",
                                                        "updates": {"laptop_assigned": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_301", "updates": {"status": "Approved"}}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop LT-MBP-001 assigned to cand_2"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_101 approved"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_2"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_2"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_101.status=Approved | asset.LT-MBP-001.status=Assigned | onboarding_files.Jane_Smith.laptop_assigned=True | checklist_item.check_201.status=Completed | checklist_item.check_202.status=Completed | access_check.access_301.status=Approved | log.ASSET_ASSIGNED.message=Laptop LT-MBP-001 assigned to cand_2 | log.ASSET_REQUEST_APPROVED.message=Asset request req_101 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_2 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_2 | candidate.cand_2.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_405",
        instruction=(
            "For candidate cand_5, you release old laptop LT-005A, assign new laptop LT-005B, complete asset requests req_501 and req_502, "
            "remove access checks access_501 and access_502, add access checks access_503, access_504, attach Company-Policies.pdf, "
            "attach Benefits-Guide.pdf, apply label 'AssetChange' to email email_501, update checklist items check_501, check_502, "
            "verify onboarding files ID-Card.pdf and Passport.pdf, log all changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-005A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_501"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_502"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_503", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_504", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_9", "file_name": "Company-Policies.pdf"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_10", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_501", "label_id": "label_AssetChange"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_501", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_502", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/ID-Card.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/Passport.pdf", "updates": {"status": "Verified"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Full asset and checklist update for cand_5", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-005A.status=Available | asset.LT-005B.status=Assigned | asset_request.req_501.status=Completed | asset_request.req_502.status=Completed | access_check.access_501=Removed | access_check.access_502=Removed | access_check.access_503.status=Pending | access_check.access_504.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_501.labels=label_AssetChange | checklist_item.check_501.status=Completed | checklist_item.check_502.status=Completed | onboarding_files.ID-Card.pdf.status=Verified | onboarding_files.Passport.pdf.status=Verified | log.ONBOARDING_COMPLETED.message=Full asset and checklist update for cand_5 | candidate.cand_5.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_053",
        instruction=(
            "You onboard candidate cand_3 by approving laptop request req_102, assigning laptop LT-DELL-002 and monitor MON-LG-001, "
            "marking files verified in onboarding, completing checklist items check_203, check_204, and approving access checks access_302, access_303. "
            "Record terminal logs and update candidate onboarding status."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-DELL-002", "candidate_id": "cand_3"}),
            Action(name="assign_asset", kwargs={"asset_tag": "MON-LG-001", "candidate_id": "cand_3"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md",
                                                        "updates": {"laptop_assigned": True,
                                                                    "monitor_assigned": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_204", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_302", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_303", "updates": {"status": "Approved"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED",
                                                     "message": "Laptop LT-DELL-002 and Monitor MON-LG-001 assigned to cand_3"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_102 approved"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_3"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_3"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_102.status=Approved | asset.LT-DELL-002.status=Assigned | asset.MON-LG-001.status=Assigned | onboarding_files.Peter_Jones.laptop_assigned=True | onboarding_files.Peter_Jones.monitor_assigned=True | checklist_item.check_203.status=Completed | checklist_item.check_204.status=Completed | access_check.access_302.status=Approved | access_check.access_303.status=Approved | log.ASSET_ASSIGNED.message=Laptop LT-DELL-002 and Monitor MON-LG-001 assigned to cand_3 | log.ASSET_REQUEST_APPROVED.message=Asset request req_102 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_3 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_3 | candidate.cand_3.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_054",
        instruction=(
            "You onboard candidate cand_4 by approving laptop request req_103 and phone request req_104, assigning LT-MBP-002 and PH-IPHONE-001, "
            "verify onboarding files, complete checklist items check_205, check_206, approve access checks access_304, access_305, and log all actions."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_103", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_104", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-MBP-002", "candidate_id": "cand_4"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_4"}),
            Action(name="update_onboarding_file",
                   kwargs={"file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md",
                           "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_205", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_206", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_304", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_305", "updates": {"status": "Approved"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_ASSIGNED",
                                                     "message": "Laptop LT-MBP-002 and Phone PH-IPHONE-001 assigned to cand_4"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED",
                                                     "message": "Asset requests req_103 and req_104 approved"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_4"}),
            Action(name="record_terminal_log",
                   kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_4"}),
            Action(name="update_candidate",
                   kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[
            "asset_request.req_103.status=Approved | asset_request.req_104.status=Approved | asset.LT-MBP-002.status=Assigned | asset.PH-IPHONE-001.status=Assigned | onboarding_files.Maria_Rodriguez.laptop_assigned=True | onboarding_files.Maria_Rodriguez.phone_assigned=True | checklist_item.check_205.status=Completed | checklist_item.check_206.status=Completed | access_check.access_304.status=Approved | access_check.access_305.status=Approved | log.ASSET_ASSIGNED.message=Laptop LT-MBP-002 and Phone PH-IPHONE-001 assigned to cand_4 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_103 and req_104 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_4 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_4 | candidate.cand_4.onboarding_status=AssetsReady"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_012",
        instruction=(
            "You complete full onboarding for candidate cand_1: approve all asset requests (laptop, phone, accessories), assign assets, "
            "complete all checklist items, approve all access checks, update multiple onboarding files, apply email labels, "
            "and record terminal logs for each step. End state: all assets assigned; checklist items completed; access checks approved; onboarding files updated; emails labeled; logs capture all actions; candidate status reflects full onboarding."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-001", "candidate_id": "cand_1"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_1"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-002", "candidate_id": "cand_1"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"verified": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_101", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_101", "label_id": "label_Welcome"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_101 and req_102 approved", "candidate_id": "cand_1"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, and mouse assigned", "candidate_id": "cand_1"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[
            "asset_request.req_101.status=Approved | asset_request.req_102.status=Approved | asset.PH-LAPTOP-001.status=Assigned | asset.PH-IPHONE-001.status=Assigned | asset.ACC-MOUSE-002.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | onboarding_files.welcome_guide.phone_assigned=True | onboarding_files.id_scan.verified=True | checklist.check_101.status=Completed | access_check.access_101.status=Approved | email.email_101.labels=label_Welcome | log.ASSET_REQUEST_APPROVED.message=Asset requests req_101 and req_102 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, and mouse assigned | candidate.cand_1.onboarding_status=OnboardingCompleted"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_017",
        instruction=(
            "You perform full multi-step onboarding for candidate cand_2: approve all pending asset requests, assign all relevant assets, "
            "complete all checklist items, approve access checks, update onboarding files with asset and policy info, "
            "apply appropriate email labels, and record detailed terminal logs at every step. "
            "End state: candidate cand_2 has all assets assigned, checklist completed, access checks approved, onboarding files updated, emails labeled, "
            "and candidate status reflects full completion."
        ),
        actions=[
            # Asset requests approval
            Action(name="update_asset_request", kwargs={"request_id": "req_201", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_202", "updates": {"status": "Approved"}}),

            # Asset assignments
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-002", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-002", "candidate_id": "cand_2"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-003", "candidate_id": "cand_2"}),

            # Onboarding files updates
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide_cand2.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan_cand2.pdf", "updates": {"verified": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/policy_ack_cand2.pdf", "updates": {"acknowledged": True}}),

            # Checklist items completion
            Action(name="update_checklist_item", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),

            # Access checks approval
            Action(name="update_access_check", kwargs={"check_id": "access_201", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_202", "updates": {"status": "Approved"}}),

            # Email labels
            Action(name="apply_label_to_email", kwargs={"email_id": "email_201", "label_id": "label_Welcome"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_202", "label_id": "label_Policy"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_203", "label_id": "label_Onboarding"}),

            # Terminal logs
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_201 and req_202 approved", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, and mouse assigned", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_2"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome', 'Policy', 'Onboarding'", "candidate_id": "cand_2"}),

            # Candidate update
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[
            "asset_request.req_201.status=Approved | asset_request.req_202.status=Approved | asset.PH-LAPTOP-002.status=Assigned | asset.PH-IPHONE-002.status=Assigned | asset.ACC-MOUSE-003.status=Assigned | onboarding_files.welcome_guide_cand2.laptop_assigned=True | onboarding_files.welcome_guide_cand2.phone_assigned=True | onboarding_files.id_scan_cand2.verified=True | onboarding_files.policy_ack_cand2.acknowledged=True | checklist.check_201.status=Completed | checklist.check_202.status=Completed | checklist.check_203.status=Completed | access_check.access_201.status=Approved | access_check.access_202.status=Approved | email.email_201.labels=label_Welcome | email.email_202.labels=label_Policy | email.email_203.labels=label_Onboarding | log.ASSET_REQUEST_APPROVED.message=Asset requests req_201 and req_202 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, and mouse assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome', 'Policy', 'Onboarding' | candidate.cand_2.onboarding_status=OnboardingCompleted"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_402",
        instruction=(
            "For candidate cand_2, you release old laptop LT-002A, assign new laptop LT-002B, complete asset requests req_201 and req_202, "
            "remove access checks access_201, access_202, add new access checks access_203, access_204, attach Company-Policies.pdf, "
            "attach Benefits-Guide.pdf, apply label 'AssetUpdate' to email email_201, update checklist items check_201, check_202, "
            "verify onboarding files ID-Card.pdf and Driving-License.pdf, log all changes, and update candidate record."
        ),
        actions=[
            Action(name="release_asset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="assign_asset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="update_asset_request", kwargs={"request_id": "req_201", "updates": {"status": "Completed"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="remove_access_check", kwargs={"check_id": "access_201"}),
            Action(name="remove_access_check", kwargs={"check_id": "access_202"}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_203", "status": "Pending"}}),
            Action(name="add_access_check", kwargs={"check": {"check_id": "access_204", "status": "Pending"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_3", "file_name": "Company-Policies.pdf"}}),
            Action(name="add_attachment", kwargs={"attachment": {"attachment_id": "attach_4", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_201", "label_id": "label_AssetUpdate"}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/ID-Card.pdf", "updates": {"status": "Verified"}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/Driving-License.pdf", "updates": {"status": "Verified"}}),
            Action(name="record_terminal_log", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Full asset and checklist update for cand_2", "candidate_id": "cand_2"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[
            "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset_request.req_201.status=Completed | asset_request.req_202.status=Completed | access_check.access_201=Removed | access_check.access_202=Removed | access_check.access_203.status=Pending | access_check.access_204.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_201.labels=label_AssetUpdate | checklist_item.check_201.status=Completed | checklist_item.check_202.status=Completed | onboarding_files.ID-Card.pdf.status=Verified | onboarding_files.Driving-License.pdf.status=Verified | log.ONBOARDING_COMPLETED.message=Full asset and checklist update for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_020",
        instruction=(
            "You complete onboarding for candidate cand_5: approve asset requests, assign assets including laptop, phone, and accessories, "
            "complete checklist items, approve access checks, update onboarding files, label emails, and record terminal logs."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-005", "candidate_id": "cand_5"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-005", "candidate_id": "cand_5"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-006", "candidate_id": "cand_5"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-KEYBOARD-004", "candidate_id": "cand_5"}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide_cand5.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan_cand5.pdf", "updates": {"verified": True}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_501", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_502", "updates": {"status": "Completed"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_501", "updates": {"status": "Approved"}}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_501", "label_id": "label_Welcome"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_502", "label_id": "label_Policy"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_501 and req_502 approved", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, mouse, and keyboard assigned", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_5"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome' and 'Policy'", "candidate_id": "cand_5"}),
            Action(name="update_candidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[
            "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.PH-LAPTOP-005.status=Assigned | asset.PH-IPHONE-005.status=Assigned | asset.ACC-MOUSE-006.status=Assigned | asset.ACC-KEYBOARD-004.status=Assigned | onboarding_files.welcome_guide_cand5.laptop_assigned=True | onboarding_files.welcome_guide_cand5.phone_assigned=True | onboarding_files.id_scan_cand5.verified=True | checklist.check_501.status=Completed | checklist.check_502.status=Completed | access_check.access_501.status=Approved | email.email_501.labels=label_Welcome | email.email_502.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_501 and req_502 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, mouse, and keyboard assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome' and 'Policy' | candidate.cand_5.onboarding_status=OnboardingCompleted"
        ],
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_016",#p
        instruction=(
            "You complete full multi-step onboarding for candidate cand_1: approve all asset requests, assign all assets, "
            "complete all checklist items, approve all access checks, update all onboarding files, apply multiple email labels, "
            "and record detailed terminal logs for every step. End state: all assets assigned, onboarding files updated, "
            "checklist items completed, access checks approved, emails labeled, and candidate status reflects full completion."
        ),
        actions=[
            # Asset requests approval
            Action(name="update_asset_request", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="update_asset_request", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),

            # Asset assignments
            Action(name="assign_asset", kwargs={"asset_tag": "PH-LAPTOP-001", "candidate_id": "cand_1"}),
            Action(name="assign_asset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_1"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-MOUSE-002", "candidate_id": "cand_1"}),
            Action(name="assign_asset", kwargs={"asset_tag": "ACC-KEYBOARD-002", "candidate_id": "cand_1"}),

            # Onboarding files updates
            Action(name="update_onboarding_file", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/id_scan.pdf", "updates": {"verified": True}}),
            Action(name="update_onboarding_file", kwargs={"file_path": "files/policy_acknowledgment.pdf", "updates": {"acknowledged": True}}),

            # Checklist items completion
            Action(name="update_checklist_item", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),

            # Access checks approval
            Action(name="update_access_check", kwargs={"check_id": "access_101", "updates": {"status": "Approved"}}),
            Action(name="update_access_check", kwargs={"check_id": "access_102", "updates": {"status": "Approved"}}),

            # Email labels
            Action(name="apply_label_to_email", kwargs={"email_id": "email_101", "label_id": "label_Welcome"}),
            Action(name="apply_label_to_email", kwargs={"email_id": "email_102", "label_id": "label_Policy"}),

            # Terminal logs
            Action(name="record_terminal_log", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_101 and req_102 approved", "candidate_id": "cand_1"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, mouse, and keyboard assigned", "candidate_id": "cand_1"}),
            Action(name="record_terminal_log", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_1"}),
            Action(name="record_terminal_log", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_1"}),
            Action(name="record_terminal_log", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome' and 'Policy'", "candidate_id": "cand_1"}),

            # Candidate update
            Action(name="update_candidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[
            "asset_request.req_101.status=Approved | asset_request.req_102.status=Approved | asset.PH-LAPTOP-001.status=Assigned | asset.PH-IPHONE-001.status=Assigned | asset.ACC-MOUSE-002.status=Assigned | asset.ACC-KEYBOARD-002.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | onboarding_files.welcome_guide.phone_assigned=True | onboarding_files.id_scan.verified=True | onboarding_files.policy_acknowledgment.acknowledged=True | checklist.check_101.status=Completed | checklist.check_102.status=Completed | access_check.access_101.status=Approved | access_check.access_102.status=Approved | email.email_101.labels=label_Welcome | email.email_102.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_101 and req_102 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, mouse, and keyboard assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome' and 'Policy' | candidate.cand_1.onboarding_status=OnboardingCompleted"
        ],
    ),
]
