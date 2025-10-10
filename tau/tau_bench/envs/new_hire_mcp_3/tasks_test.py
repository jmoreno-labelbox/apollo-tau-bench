from tau_bench.types import Action, Task

TASKS = [

    Task(
        annotator="R",
        user_id="onboarding_ds_002",
        instruction=(
            "Handle the approval of candidate cand_2's asset requests req_201 and req_202, allocate assets LT-002 and PH-002, finalize checklist check_201, check onboarding file offer_letter.pdf, tag email email_201 with 'Ready', and record all actions. Update the candidate record to indicate completion."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-005B", "candidate_id": "cand_5"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_502", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/Benefits-Guide.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_502", "label_id": "label_Ready"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Assets assigned for cand_5", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_003",
        instruction=(
            "You handle the release of old assets LT-003 and PH-003 for candidate cand_3, allocate new laptop LT-003B, finish checklist items check_301 and check_302, incorporate onboarding file id_scan.pdf, attach email label 'AssetUpdate' to email email_301, document all changes, and revise the candidate record."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_401", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_402", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-004", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-004", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-005", "candidate_id": "cand_4"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide_cand4.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan_cand4.pdf", "updates": {"verified": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_401", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_402", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_401", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_401", "label_id": "label_Welcome"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_402", "label_id": "label_Policy"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_401 and req_402 approved", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, and mouse assigned", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome' and 'Policy'", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_004",
        instruction=(
            "You endorse asset requests req_401 for candidate cand_4, allocate laptop LT-004 and phone PH-004, fulfill checklist item check_401, incorporate onboarding file welcome_guide.pdf, attach email label 'Onboarded' to email email_401, document all actions, and designate candidate record as completed."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_401", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_402", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-004", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-004", "candidate_id": "cand_4"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/cand_4_onboarding.json",
                                                          "updates": {"laptop_assigned": True,
                                                                      "phone_assigned": True}}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Requests req_401 and req_402 approved",
                           "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "PH-LAPTOP-004 assigned",
                           "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-004 assigned",
                           "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_005",
        instruction=(
            "Handle asset reassignment for candidate cand_5: release old laptop LT-005, assign new laptop LT-005B, ensure completion of checklist item check_501, verify the onboarding file id_scan.pdf, apply email label 'AssetUpdate' to email email_501, log all updates, and update the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-OLD-001"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-NEW-006", "candidate_id": "cand_6"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-NEW-006", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_602", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_601"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_602"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_604", "status": "Pending"}}),
            Action(name="AddAttachment",
                   kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="AddAttachment", kwargs={
                "attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_601", "label_id": "label_AssetChange"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_006",
        instruction=(
            "Manage the onboarding of candidate cand_7 through approval of asset requests req_501, req_502, assign a laptop LT-DELL-010, a phone PH-SAMSUNG-005, and provide accessories ACC-MOUSE-001. Checklist tasks check_701, check_702 are fulfilled, onboarding documents welcome_guide.pdf and id_scan.pdf are confirmed, and access validations access_901, access_902 are sanctioned. An email email_701 has the label 'Welcome'. Final state: assets are assigned and approved; documents are verified; checklist and access validations completed; terminal logs are available; candidate's onboarding status is revised."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_5", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-003", "candidate_id": "cand_5"}),
            Action(name="UpdateAsset", kwargs={"asset_tag": "PH-IPHONE-003", "updates": {"status": "Assigned"}}),
            Action(name="UpdateOnboardingFile", kwargs={"candidate_id": "cand_5", "updates": {"phone_assigned": True}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "PHONE_ASSIGNED", "message": "Phone assigned to cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_5 approved"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_007",
        instruction=(
            "Authorize the laptop and phone requests for candidate cand_7, allocate the assets, and make sure the onboarding documents indicate the asset allocation. Desired outcome: asset requests are indicated as 'Approved'; assets PH-LAPTOP-007 and PH-IPHONE-007 are allocated to cand_7; onboarding documents display phone_assigned=True and laptop_assigned=True; terminal logs record the assignment and authorization activities."
        ),
        actions=[
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="RemoveAttachment", kwargs={"attachment_id": "attach_3"}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_4", "file_name": "Training-Guide.pdf"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_card.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_202", "label_id": "label_Training"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_202", "status": "Pending"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop assigned for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist item completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"training_status": "InProgress"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_008",
        instruction=(
            "Authorize the laptop and phone requests for candidate cand_7, allocate the assets, revise onboarding documents for asset allocation, finalize checklist tasks, sanction access verifications, and categorize emails. Desired outcome: asset requests are marked 'Approved'; assets PH-LAPTOP-010, PH-IPHONE-005, and ACC-MOUSE-001 are assigned; checklist tasks marked 'Completed'; access verifications approved; onboarding documents reflect assigned assets; the email is categorized as 'Welcome'; terminal logs record all operations."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_301", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_302", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-003", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-003", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-004", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-KEYBOARD-003", "candidate_id": "cand_3"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide_cand3.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan_cand3.pdf", "updates": {"verified": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/policy_ack_cand3.pdf", "updates": {"acknowledged": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_301", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_302", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_301", "label_id": "label_Welcome"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_302", "label_id": "label_Policy"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_301 and req_302 approved", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, mouse, and keyboard assigned", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome' and 'Policy'", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_010",
        instruction=(
            "Authorize candidate cand_7's request for a phone, allocate the asset, revise onboarding files to reflect the phone assignment, finalize checklist items, authorize access checks, assign email tags, and log the records. End state: phone request authorized; asset PH-IPHONE-005 allocated; onboarding files indicate phone_assigned=True; checklist items finalized; access checks authorized; email tagged 'Welcome'; terminal logs document all activities."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_103", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-002", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "MON-LG-001", "candidate_id": "cand_3"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Peter_Jones/asset_request.json",
                                                          "updates": {"laptop_assigned": True,
                                                                      "monitor_assigned": True}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED",
                                                       "message": "Asset requests req_102 and req_103 approved",
                                                       "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "LT-DELL-002 assigned",
                           "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "MONITOR_ASSIGNED", "message": "MON-LG-001 assigned",
                           "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_011",
        instruction=(
            "Handle the complete onboarding process for candidate cand_7: approve every asset request (laptop, phone, accessories), allocate assets, finalize all checklist items, give approval for all access checks, update several onboarding files, apply numerous email labels, and document terminal logs for each step. End state: all assets allocated; checklist items finalized; access checks approved; onboarding files updated; emails labeled; logs document all actions; candidate status indicates full onboarding."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-001B", "candidate_id": "cand_1"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_101"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_102"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_105", "status": "Pending"}}),
            Action(name="AddAttachment",
                   kwargs={"attachment": {"attachment_id": "attach_3", "file_name": "Company-Policies.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_101", "label_id": "label_AssetChange"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_1",
                           "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_1",
                           "candidate_id": "cand_1"}),
            Action(name="UpdateOnboardingFile",
                   kwargs={"file_path": "files/Passport.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_1", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_012",
        instruction=(
            "Coordinate full onboarding for candidate cand_1: approve all asset requests (laptop, phone, accessories), allocate assets, complete all checklist items, authorize all access checks, revise multiple onboarding files, apply email labels, and document terminal logs for each step. Final condition: all assets are allocated; checklist items are completed; access checks are authorized; onboarding files are updated; emails have labels; logs document all activities; candidate status shows full onboarding."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-004A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-004B", "candidate_id": "cand_4"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_401", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_401"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_402"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_405", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_406", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Company-Policies.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_401", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/ID-Card.pdf", "updates": {"status": "Verified"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_013",
        instruction=(
            "Coordinate the completion of onboarding for candidate cand_6: approve asset requests req_601, req_602, assign laptop LT-HP-006, phone PH-IP-006. Handle checklist items check_601, check_602, verify onboarding files offer_letter.pdf and id_scan.pdf. Approve access checks access_601, access_602. Label email email_601 as 'OnboardingReady' and log all updates accordingly."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_601", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_602", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-HP-006", "candidate_id": "cand_6"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IP-006", "candidate_id": "cand_6"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_601", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_602", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_601", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_602", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_601", "label_id": "label_OnboardingReady"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Candidate cand_6 onboarding completed", "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_6", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_014",
        instruction=(
            "For candidate cand_2, substitute temporary laptop LT-Temp02 with permanent laptop LT-002C, finish security induction checklist items check_221 and check_222, verify background_verification.pdf, update access check access_207 to 'Approved', add a new access check access_208, apply email label 'SecurityClearance' to email_221, record all updates, and revise candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-Temp02"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002C", "candidate_id": "cand_2"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_221", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_222", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/background_verification.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_207", "updates": {"status": "Approved"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_208", "status": "Pending"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_221", "label_id": "label_SecurityClearance"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "SECURITY_CHECK", "message": "Security induction completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATE", "message": "Access updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"security_clearance": "Granted"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_015",
        instruction=(
            "For candidate cand_4, distribute mobile device MB-004X, relinquish the old tablet TB-004Z, finalize orientation checklist items check_410 and check_411, confirm the signed_policy.pdf, attach the team_structure.pdf, tag email_410 with the 'Orientation' label, record the changes, and refresh the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "TB-004Z"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "MB-004X", "candidate_id": "cand_4"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_410", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_411", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/signed_policy.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_9", "file_name": "team_structure.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_410", "label_id": "label_Orientation"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "DEVICE_UPDATE", "message": "Mobile assigned to cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Orientation tasks done for cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "FILE_VERIFIED", "message": "Signed policy verified for cand_4", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"orientation_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_016",
        instruction=(
            "Oversee the entire multi-step onboarding for candidate cand_1: authorize all asset requests, allocate all assets, finalize all checklist items, authorize all access checks, update all onboarding files, apply multiple email labels, and document detailed terminal logs for each step. End state: all assets allocated, onboarding files revised, checklist items finalized, access checks authorized, emails labeled, and candidate status indicates full completion."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-001X"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-001Y", "candidate_id": "cand_1"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Closed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_103", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/confidentiality_agreement.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_105", "status": "Pending"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_106"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_103", "label_id": "label_TrainingUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New permanent laptop assigned to cand_1", "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"training_status": "Completed"}})
        ],
        outputs=[]
    ),


    Task(
        annotator="R",
        user_id="onboarding_ds_017",
        instruction=(
            "Handle the comprehensive multi-step onboarding for candidate cand_2: approve every pending asset request, assign all applicable assets, finalize each checklist item, authorize access checks, refresh onboarding files with asset and policy information, utilize suitable email labels, and meticulously log terminal activities throughout the process. Final goal: candidate cand_2 is fully assigned assets, checklist is finalized, access checks are authorized, onboarding files are updated, emails bear appropriate labels, and the candidate's status reads as fully completed."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_201", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_201"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_202"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_206", "status": "Pending"}}),
            Action(name="AddAttachment",
                   kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_201", "label_id": "label_AssetChange"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_2",
                           "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_2",
                           "candidate_id": "cand_2"}),
            Action(name="UpdateOnboardingFile",
                   kwargs={"file_path": "files/ID-Proof.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_019",
        instruction=(
            "Manage the release of the old monitor MON-202A and designate the new monitor MON-202B for candidate cand_2. Finalize checklist check_202, attach NDA-Form.pdf, revoke access check access_202, implement new access check access_204, and apply the 'HR' label to email email_202. Record updates and amend the candidate HR record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "MON-202A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "MON-202B", "candidate_id": "cand_2"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_12", "file_name": "NDA-Form.pdf"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_202"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_204", "status": "Pending"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_202", "label_id": "label_HR"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "MONITOR_UPDATED", "message": "Monitor swapped for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"hr_status": "Updated"}}),
            Action(name="SendEmail", kwargs={"email_id": "email_202", "updates": {"status": "Sent"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_021",
        instruction=(
            "For candidate cand_4, handle decommissioning of the old phone PH-404A, assign the smartphone PH-404B, remove access check access_404, add access check access_405, attach Orientation-Schedule.pdf, update checklist check_404, apply label 'Orientation' to email email_404, log the activities, and mark candidate orientation complete."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "PH-404A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-404B", "candidate_id": "cand_4"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_404"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_405", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_14", "file_name": "Orientation-Schedule.pdf"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_404", "updates": {"status": "Completed"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_404", "label_id": "label_Orientation"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "PHONE_UPDATED", "message": "Smartphone assigned to cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"orientation_status": "Completed"}}),
            Action(name="SendEmail", kwargs={"email_id": "email_404", "updates": {"status": "Sent"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_091",
        instruction=(
            "Manage the transition for candidate cand_3 by releasing headset HS-003A, allocating headset HS-003B, finalizing asset request req_301, withdrawing access check access_301, instituting new access check access_305, attaching Security-Guidelines.pdf, applying email label 'SecurityDocs' to email email_305, fulfilling checklist item check_305, recording updates for assets and access, and refreshing the candidate record."
        ),
        actions=[
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-001B"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-001D", "candidate_id": "cand_1"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-001D", "candidate_id": "cand_1"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_105", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_106", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_103"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_108", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={
                "attachment": {"attachment_id": "attach_welcome_jane", "file_name": "welcome_Jane_Smith.md"}}),
            Action(name="ApplyLabelToEmail",
                   kwargs={"email_id": "email_101", "label_id": "label_OnboardingComplete"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_1",
                           "candidate_id": "cand_1"})
        ],
        outputs=[]
    ),
    Task(
        annotator="R",
        user_id="onboarding_ds_092",
        instruction=(
            "Coordinate activities for candidate cand_5 by releasing tablet TB-005A, assigning tablet TB-005B, concluding asset request req_501, removing access check access_501, implementing access check access_506, attaching Training-Plan.pdf, applying email label 'Learning' to email email_506, completing checklist item check_506, documenting updates for assets and access, and revising the candidate record."
        ),
        actions=[
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_403"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_404"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_407", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_408", "status": "Pending"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-004D", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-004D", "candidate_id": "cand_4"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_407", "updates": {"status": "Completed"}}),
            Action(name="AddAttachment",
                   kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Company-Policies.pdf"}}),
            Action(name="UpdateOnboardingFile",
                   kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "DEVICE_ASSIGNED", "message": "Devices assigned for cand_4",
                           "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_4",
                           "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_094",
        instruction=(
            "For candidate cand_7, designate the laptop LT-007C and phone PH-007C, manage the completion of asset requests req_701 and req_702. Discard old access checks access_701 and access_702, insert new access checks access_703 and access_704, include welcome_Robert_Singh.md, assign the 'OnboardingComplete' label to email email_701, document all modifications, and update the candidate record."
        ),
        actions=[
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-007C", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-007C", "candidate_id": "cand_7"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_702", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_701"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_702"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_703", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_704", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={
                "attachment": {"attachment_id": "attach_welcome_robert", "file_name": "welcome_Robert_Singh.md"}}),
            Action(name="ApplyLabelToEmail",
                   kwargs={"email_id": "email_701", "label_id": "label_OnboardingComplete"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_7",
                           "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),
    Task(
        annotator="R",
        user_id="onboarding_ds_095",
        instruction=(
            "With respect to candidate cand_6, handle checklist items check_603 and check_604. Release the old laptop LT-006B, assign the new laptop LT-006C and phone PH-006C, and update asset requests req_603 and req_604. Remove the access check access_603, add the access check access_605, attach Benefits-Guide.pdf, log all changes, and update the candidate record."
        ),
        actions=[
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_603", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_604", "updates": {"status": "Completed"}}),
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-006B"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-006C", "candidate_id": "cand_6"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-006C", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_603", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_604", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_603"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_605", "status": "Pending"}}),
            Action(name="AddAttachment",
                   kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_096",
        instruction=(
            "Referring to candidate cand_2, coordinate the release of their old laptop LT-002A and the assignment of a new laptop LT-002B and phone PH-002B. Ensure asset requests req_203 and req_204 are completed. Remove previous access checks access_203 and access_204, and add new access checks access_205 and access_206. Attach the document Company-Policies.pdf, log all updates, and update the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_203", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_204", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_203"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_204"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_205", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_206", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_3", "file_name": "Company-Policies.pdf"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REASSIGNED", "message": "Assets reassigned for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_098",
        instruction=(
            "Ensure that candidate cand_3 is assigned the retired laptop LT-003B, along with the new laptop LT-003C and phone PH-003C, while asset requests req_303 and req_304 are updated. You need to remove access checks access_303 and access_304, incorporate access checks access_305 and access_306, append offer_letter.pdf, document all changes, and revise the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-003B"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-003C", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-003C", "candidate_id": "cand_3"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_303", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_304", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_303"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_304"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_305", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_306", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_offer_letter", "file_name": "offer_letter.pdf"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_3", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_099",
        instruction=(
            "The assignment for candidate cand_7 involves providing laptop LT-007D and phone PH-007D, finalizing asset requests req_705 and req_706, eliminating outdated access checks access_705 and access_706, setting up new access checks access_707 and access_708, appending welcome_Maria_Rodriguez.md, recording all updates, and revising the candidate record."
        ),
        actions=[
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-007D", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-007D", "candidate_id": "cand_7"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_705", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_706", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_705"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_706"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_707", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_708", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_welcome_maria", "file_name": "welcome_Maria_Rodriguez.md"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),
    Task(
        annotator="R",
        user_id="onboarding_ds_100",
        instruction=(
            "Candidate cand_6 must return the old laptop LT-006C. You are to allocate the new laptop LT-006D and phone PH-006D, finalize asset requests req_607 and req_608, revoke access check access_605, grant access check access_606, include Benefits-Guide.pdf, document all changes, and revise the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-006C"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-006D", "candidate_id": "cand_6"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-006D", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_607", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_608", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_605"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_606", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_303",
        instruction=(
            "For candidate cand_3, retrieve the old laptop LT-003A, allocate the new laptop LT-003B, address checklist items check_303 and check_304, confirm the onboarding file offer_letter.pdf, assign email label 'AssetUpdate' to email email_303, record all modifications, update the candidate record, and append Company-Policies.pdf."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-003A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_303", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_304", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_303", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New assets assigned for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_3", "candidate_id": "cand_3"}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_3", "file_name": "Company-Policies.pdf"}}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_305",
        instruction=(
            "Regarding candidate cand_5, handle the release of the old laptop LT-005A, assign the new laptop LT-005B, fulfill asset requests req_501 and req_502, eliminate access checks access_501, introduce new access check access_507, attach Benefits-Guide.pdf, apply the label 'AssetChange' to email email_501, document the changes, update the candidate record, and confirm the onboarding file Driving-License.pdf."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-005A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_501"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_507", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_501", "label_id": "label_AssetChange"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_5", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"asset_update_status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/Driving-License.pdf", "updates": {"status": "Verified"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_306",
        instruction=(
            "Regarding candidate cand_6, manage the release of the old laptop LT-006A, assign the new laptop LT-006B, fulfill asset request req_601, remove access check access_601, introduce new access checks access_603 and access_604, attach Company-Policies.pdf, affix the label 'AssetUpdate' to email email_601, register the changes, update the candidate record, and confirm the onboarding file Passport.pdf."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-006A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-006B", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_601"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_604", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Company-Policies.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_601", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/Passport.pdf", "updates": {"status": "Verified"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_307",
        instruction=(
            "Handle candidate cand_7 by releasing the old laptop LT-007A, assigning the new laptop LT-007B, completing checklist items check_701 and check_702, removing access check access_701, adding new access check access_705, attaching Benefits-Guide.pdf, applying the label 'AssetUpdate' to email email_701, logging the changes, updating the candidate record, and verifying the onboarding file ID-Proof.pdf."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-007A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-007B", "candidate_id": "cand_7"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_701"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_705", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/ID-Proof.pdf", "updates": {"status": "Verified"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_201",
        instruction=(
            "Coordinate tasks for candidate cand_1 by releasing the old asset LT-001A, assigning the new asset LT-001B, updating asset request req_101 to Completed, marking checklist items check_101 and check_102 as Completed, verifying the onboarding file offer_letter.pdf, applying the label 'OnboardingUpdate' to email email_101, removing access check access_101, adding access check access_105, attaching Handbook.pdf, logging the updates, and marking the candidate onboarding as Completed."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-001B", "candidate_id": "cand_1"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_101", "label_id": "label_OnboardingUpdate"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_101"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_105", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Handbook.pdf"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_progress": "Completed"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_203",
        instruction=(
            "Regarding candidate cand_3, release asset LT-003A, assign LT-003B, update checklist items check_301 and check_302, verify tax_form.pdf, attach label 'Finance' to email email_303, revoke access check access_303, grant access check access_304, detach Benefits.pdf, attach Payroll-Form.pdf, document changes, and refresh payroll_status."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-003A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/tax_form.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_303", "label_id": "label_Finance"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_303"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_304", "status": "Pending"}}),
            Action(name="RemoveAttachment", kwargs={"attachment_id": "attach_5"}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_6", "file_name": "Payroll-Form.pdf"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "FINANCE_UPDATE", "message": "Payroll forms updated for cand_3", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"payroll_status": "Active"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_204",
        instruction=(
            "In reference to candidate cand_2, release laptop LT-002A, assign laptop LT-002B, update asset request req_201, finalize checklist items check_201 and check_202, remove onboarding file id_proof.pdf, include onboarding file nda.pdf, label email email_201 with 'OnboardingComplete', record all updates, and designate candidate record as fully onboarded."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_201", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="RemoveOnboardingFile", kwargs={"file_path": "files/id_proof.pdf"}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/nda.pdf", "status": "Pending"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_201", "label_id": "label_OnboardingComplete"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"status": "Onboarded"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_205",
        instruction=(
            "For candidate cand_5, handle the release of asset LT-005A, allocate asset LT-005B, modify asset request req_501, eliminate access verification access_501, incorporate new access verification access_502, finalize checklist check_502, refresh email email_501 content, apply the label 'AccessUpdate' to the same email, document the changes, and revise the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-005A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_501"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_502", "status": "Pending"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_502", "updates": {"status": "Completed"}}),
            Action(name="UpdateEmail", kwargs={"email_id": "email_501", "updates": {"subject": "Access Updated"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_501", "label_id": "label_AccessUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_5", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist item completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"access_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_206",
        instruction=(
            "For candidate cand_7, manage the release of asset LT-007A, allocate asset LT-007B, finalize checklist items check_701 and check_702, update the onboarding file tax_form.pdf, attach Employee-Handbook.pdf, refresh email email_701, apply the label 'PolicyUpdate', document changes, and change the candidate onboarding phase to 'Finalized'."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-007A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-007B", "candidate_id": "cand_7"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/tax_form.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Employee-Handbook.pdf"}}),
            Action(name="UpdateEmail", kwargs={"email_id": "email_701", "updates": {"subject": "Onboarding Policy Updated"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_PolicyUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_UPDATED", "message": "Onboarding finalized for cand_7", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "All checklist items completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"phase": "Finalized"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_207",
        instruction=(
            "Handle candidate cand_1 by releasing asset LT-001A, assigning LT-001C, finalizing checklist items check_101 and check_102, eliminating access check access_101, including access check access_103, revising onboarding file offer_letter.pdf, incorporating file signed_contract.pdf, amending email email_101 with subject 'Final Contract Signed', applying label 'ContractComplete', documenting the updates, and designating candidate as confirmed."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-001C", "candidate_id": "cand_1"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_101"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_103", "status": "Pending"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/signed_contract.pdf", "status": "Pending"}}),
            Action(name="UpdateEmail", kwargs={"email_id": "email_101", "updates": {"subject": "Final Contract Signed"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_101", "label_id": "label_ContractComplete"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CANDIDATE_CONFIRMED", "message": "cand_1 fully confirmed", "candidate_id": "cand_1"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"status": "Confirmed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_208",
        instruction=(
            "Coordinate candidate cand_3 by releasing asset LT-003A, assigning LT-003B, updating asset request req_301, completing checklist check_301, modifying onboarding file id_proof.pdf, adding onboarding file medical_form.pdf, altering email email_301 with subject 'Onboarding Medical Cleared', applying label 'MedicalUpdate', removing attachment attach_3, adding attachment Training-Schedule.pdf, recording updates, and setting candidate stage to 'ReadyForTraining'."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-003A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_301", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_proof.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/medical_form.pdf", "status": "Pending"}}),
            Action(name="UpdateEmail", kwargs={"email_id": "email_301", "updates": {"subject": "Onboarding Medical Cleared"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_301", "label_id": "label_MedicalUpdate"}),
            Action(name="RemoveAttachment", kwargs={"attachment_id": "attach_3"}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_3_new", "file_name": "Training-Schedule.pdf"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_READY", "message": "Medical cleared and training scheduled for cand_3", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"stage": "ReadyForTraining"}})
        ],
        outputs=[]
    ),


    Task(
        annotator="R",
        user_id="onboarding_ds_209",
        instruction=(
            "Handle the tasks for candidate cand_4 by releasing LT-004A, assigning LT-004B, updating request req_401, fulfilling checklist items check_401 and check_402, adding access check access_404, removing the onboarding file old_resume.pdf, including the new file updated_resume.pdf, updating email email_401 with the subject 'Resume Verified', applying the label 'ResumeCheck', logging the actions, and setting the candidate profile to 'Verified'."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-004A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-004B", "candidate_id": "cand_4"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_401", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_401", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_402", "updates": {"status": "Completed"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_404", "status": "Pending"}}),
            Action(name="RemoveOnboardingFile", kwargs={"file_path": "files/old_resume.pdf"}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/updated_resume.pdf", "status": "Pending"}}),
            Action(name="UpdateEmail", kwargs={"email_id": "email_401", "updates": {"subject": "Resume Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_401", "label_id": "label_ResumeCheck"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "PROFILE_VERIFIED", "message": "Resume verified for cand_4", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"profile_status": "Verified"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_210",
        instruction=(
            "Coordinate the steps for candidate cand_6 by releasing LT-006A, assigning LT-006B, updating request req_601, completing checklist item check_601, adding access check access_606, updating the onboarding file training_doc.pdf, adding the file signed_training.pdf, updating email email_601 with the subject 'Training Completed', applying the label 'TrainingDone', logging the actions, and marking the candidate status as 'Trained'."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-006A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-006B", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_601", "updates": {"status": "Completed"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_606", "status": "Pending"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/training_doc.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/signed_training.pdf", "status": "Pending"}}),
            Action(name="UpdateEmail", kwargs={"email_id": "email_601", "updates": {"subject": "Training Completed"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_601", "label_id": "label_TrainingDone"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "TRAINING_COMPLETED", "message": "cand_6 training completed", "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_6", "updates": {"status": "Trained"}})
        ],
        outputs=[]
    ),


    Task(
        annotator="R",
        user_id="onboarding_ds_211",
        instruction=(
            "Handle the release of LT-002B and assign LT-002C for candidate cand_2. Update asset request req_202, finalize checklist items check_203 and check_204, insert access verification access_205, revise onboarding document nda.pdf, append attachment Code-Of-Conduct.pdf, amend email email_202 including the subject 'Code of Conduct Signed', apply the label 'PolicySigned', record updates, and alter the candidate phase to 'ActiveEmployee'."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-002B"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002C", "candidate_id": "cand_2"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_204", "updates": {"status": "Completed"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_205", "status": "Pending"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/nda.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_2_new", "file_name": "Code-Of-Conduct.pdf"}}),
            Action(name="UpdateEmail", kwargs={"email_id": "email_202", "updates": {"subject": "Code of Conduct Signed"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_202", "label_id": "label_PolicySigned"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "POLICY_ACCEPTED", "message": "Code of conduct signed for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"phase": "ActiveEmployee"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_086",
        instruction=(
            "Coordinate the release of old laptop LT-002A and the assignment of new laptop LT-002B for candidate cand_2. Fulfill asset request req_202, remove access verification access_202, incorporate new access check access_205, attach Code-of-Conduct.pdf, assign the email label 'PolicyUpdate' to email email_205, finalize checklist item check_205, document updates for both assets and access, and revise the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_202"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_205", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_11", "file_name": "Code-of-Conduct.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_205", "label_id": "label_PolicyUpdate"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_205", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Laptop updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access changes applied for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_087",
        instruction=(
            "For candidate cand_1, handle the release of the old laptop LT-001A, assign laptop LT-001B, finalize asset request req_101, remove access check access_101, add new access check access_103, attach Employee-Handbook.pdf, apply email label 'OnboardingDocs' to email email_103, fulfill checklist item check_103, log updates for assets and access, and update the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-001B", "candidate_id": "cand_1"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_101"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_103", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_12", "file_name": "Employee-Handbook.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_103", "label_id": "label_OnboardingDocs"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_103", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Laptop updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_088",
        instruction=(
            "For candidate cand_4, manage the release of monitor MN-004A, assign monitor MN-004B, finalize asset request req_401, eliminate access check access_401, add access check access_402, attach Health-Safety.pdf, apply email label 'HealthPolicy' to email email_402, accomplish checklist item check_402, log changes for assets and access, and update the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "MN-004A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "MN-004B", "candidate_id": "cand_4"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_401", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_401"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_402", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_13", "file_name": "Health-Safety.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_402", "label_id": "label_HealthPolicy"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_402", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Monitor updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_089",
        instruction=(
            "For candidate cand_6, handle the release of phone PH-006A, assign phone PH-006B, finalize asset request req_601, remove access check access_601, add access check access_603, attach Compliance-Report.pdf, apply the email label 'Compliance' to email email_603, complete checklist item check_603, record changes for assets and access, and update the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "PH-006A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-006B", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_601"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_14", "file_name": "Compliance-Report.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_603", "label_id": "label_Compliance"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_603", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Phone updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_090",
        instruction=(
            "For candidate cand_2, coordinate the release of desktop DT-002A, assign desktop DT-002B, finalize asset request req_201, remove access check access_201, add new access check access_204, attach Payroll-Guide.pdf, apply the email label 'FinanceDocs' to email email_204, complete checklist item check_204, document changes for assets and access, and update the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "DT-002A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "DT-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_201", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_201"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_204", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_15", "file_name": "Payroll-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_204", "label_id": "label_FinanceDocs"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_204", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Desktop updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_091",
        instruction=(
            "Manage the transition for candidate cand_3 by releasing headset HS-003A, allocating headset HS-003B, finalizing asset request req_301, withdrawing access check access_301, instituting new access check access_305, attaching Security-Guidelines.pdf, applying email label 'SecurityDocs' to email email_305, fulfilling checklist item check_305, recording updates for assets and access, and refreshing the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "HS-003A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "HS-003B", "candidate_id": "cand_3"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_301", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_301"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_305", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_16", "file_name": "Security-Guidelines.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_305", "label_id": "label_SecurityDocs"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_305", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Headset updated for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_3", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_092",
        instruction=(
            "Coordinate activities for candidate cand_5 by releasing tablet TB-005A, assigning tablet TB-005B, concluding asset request req_501, removing access check access_501, implementing access check access_506, attaching Training-Plan.pdf, applying email label 'Learning' to email email_506, completing checklist item check_506, documenting updates for assets and access, and revising the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "TB-005A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "TB-005B", "candidate_id": "cand_5"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_501"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_506", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_17", "file_name": "Training-Plan.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_506", "label_id": "label_Learning"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_506", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Tablet updated for cand_5", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_5", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_093",
        instruction=(
            "For candidate cand_7, handle the release of docking station DS-007A, assign docking station DS-007B, carry out asset request req_701, eliminate access check access_701, incorporate new access check access_707, attach Onboarding-Schedule.pdf, apply the email label 'Onboarding' to email email_707, complete the checklist item check_707, document changes for assets and access, and refresh the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "DS-007A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "DS-007B", "candidate_id": "cand_7"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_701", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_701"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_707", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_18", "file_name": "Onboarding-Schedule.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_707", "label_id": "label_Onboarding"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_707", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Docking station updated for cand_7", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access updated for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_081",
        instruction=(
            "For candidate cand_1, manage the release of old laptop LT-001A, allocate new laptop LT-001B, fulfill asset requests req_101 and req_102, delete access check access_101, introduce new access check access_103, attach Benefits-Guide.pdf, document changes, and revise the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-001A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-001B", "candidate_id": "cand_1"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_101"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_103", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_1", "candidate_id": "cand_1"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_082",
        instruction=(
            "For candidate cand_4, handle the release of the old laptop LT-004A, allocate the new laptop LT-004B and phone PH-004, finalize asset request req_401, eliminate access check access_401, incorporate new access check access_403, include Company-Policies.pdf, record all modifications, and refresh the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-004A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-004B", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-004", "candidate_id": "cand_4"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_401", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_401"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_403", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_7", "file_name": "Company-Policies.pdf"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_083",
        instruction=(
            "For candidate cand_6, handle the release of the old laptop LT-006A, allocate the new laptop LT-006B, finalize asset request req_601, eliminate access check access_601, incorporate new access check access_603, include Benefits-Guide.pdf, apply email label 'AssetUpdate' to email email_603, accomplish checklist item check_603, record changes, and refresh the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-006A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-006B", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_601"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="AddAttachment",
                   kwargs={"attachment": {"attachment_id": "attach_8", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_603", "label_id": "label_AssetUpdate"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_603", "updates": {"status": "Completed"}}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_6",
                           "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_071",
        instruction=(
            "Handle the reassignment of assets for candidate cand_6: release the old laptop LT-006, allocate the new laptop LT-006B and phone PH-006B, update asset requests req_601 and req_602 with the status 'Completed', remove access checks access_601 and access_602, implement new access checks access_603 and access_604, attach Company-Policies.pdf and Benefits-Guide.pdf, apply the label 'AssetChange' to email email_601, ensure all changes are logged, and mark the candidate record as updated."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-006"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-006B", "candidate_id": "cand_6"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-006B", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_601", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_602", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_601"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_602"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_603", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_604", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_601", "label_id": "label_AssetChange"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_6", "candidate_id": "cand_6"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_072",
        instruction=(
            "Coordinate the assignment for candidate cand_7 with laptop LT-007 and phone PH-007, approve the asset requests req_701 and req_702, complete the checklist items check_701 and check_702, confirm the onboarding files welcome.pdf and id_scan.pdf are verified, apply the email label 'Ready' to email email_701, ensure all changes are logged, and mark the candidate record as updated."
        ),
        actions=[
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-007", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-007", "candidate_id": "cand_7"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_701", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_702", "updates": {"status": "Approved"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_Ready"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_073",
        instruction=(
            "For candidate cand_3, handle the release of the old laptop LT-003A, assign the new laptop LT-003B, finish checklist items check_303 and check_304, confirm the onboarding file offer_letter.pdf, attach Company-Policies.pdf, use the email label 'AssetUpdate' for email email_303, document all modifications, and amend the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-003A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_303", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_304", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_303", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New assets assigned for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_3", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_041",
        instruction=(
            "Authorize laptop asset requests for candidates Emma Thompson (cand_2) and William Davis (cand_3), allocate the correct laptops, and revise onboarding files to indicate laptop assignment. Final status: asset requests are 'Approved'; laptops LT-DELL-003 and LT-DELL-002 are allocated; onboarding files reflect laptop_assigned=True; terminal logs record assignment and approval processes."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_Jane_Laptop", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_Peter_Laptop", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-003", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-002", "candidate_id": "cand_3"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Jane_Smith/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Peter_Jones/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_REQUEST_APPROVED", "message": "Laptop requests approved and assigned", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_REQUEST_APPROVED", "message": "Laptop requests approved and assigned", "candidate_id": "cand_3"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_075",
        instruction=(
            "Handle the reassignment of candidate cand_2's assets: release laptop LT-002A, assign new laptop LT-002B and phone PH-002B, complete checklist items check_203 and check_204, verify onboarding file Company-Policies.pdf, apply email label 'AssetUpdate' to email email_203, document all steps, and refresh the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_204", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/Company-Policies.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_203", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New assets assigned for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_077",
        instruction=(
            "Coordinate the asset reassignment for candidate cand_4: release laptop LT-004A, assign new laptop LT-004B and phone PH-004B, complete checklist item check_404, verify onboarding file offer_letter.pdf, add attachment Company-Policies.pdf, apply email label 'AssetUpdate' to email email_404, record all actions, and refresh the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-004A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-004B", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-004B", "candidate_id": "cand_4"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_404", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_404", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist item completed for cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email labeled for cand_4", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_078",
        instruction=(
            "Regarding candidate cand_5, allocate laptop LT-005B and phone PH-005B, finish checklist tasks check_505 and check_506, confirm onboarding documents resume.pdf and security_form.pdf, include attachment Company-Policies.pdf, place email label 'Welcome' on email email_505, record all modifications, and revise candidate record."
        ),
        actions=[
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-005B", "candidate_id": "cand_5"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_505", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_506", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/resume.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/security_form.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_505", "label_id": "label_Welcome"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_079",
        instruction=(
            "As for candidate cand_2, decommission old laptop LT-002A, allocate new laptop LT-002B and phone PH-002B, complete checklist items check_202 and check_203, confirm onboarding document offer_letter.pdf, attach Company-Policies.pdf, assign email label 'AssetChange' to email email_202, document all operations, and amend candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_202", "label_id": "label_AssetChange"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_UPDATED", "message": "Assets updated for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_005",# It seems there was an error with your request. Please provide the comment you'd like paraphrased.
        instruction=(
            "Handle asset reassignment for candidate cand_5: release old laptop LT-005, assign new laptop LT-005B, ensure completion of checklist item check_501, verify the onboarding file id_scan.pdf, apply email label 'AssetUpdate' to email email_501, log all updates, and update the candidate record."
        ),
        actions=[
            # Modify several email tags.
            Action(name="UpdateEmailLabel", kwargs={"label_id": "label_2", "updates": {"priority": "Urgent"}}),
            Action(name="UpdateEmailLabel", kwargs={"label_id": "label_3", "updates": {"priority": "High"}}),

            # Handle several email messages.
            Action(name="UpdateEmail", kwargs={"email_id": "email_101", "updates": {"processed": True}}),
            Action(name="UpdateEmail", kwargs={"email_id": "email_102", "updates": {"processed": True}}),

            # Assign tags to emails.
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_101", "label_id": "label_2"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_102", "label_id": "label_3"}),

            # Revise onboarding documents.
            Action(name="UpdateOnboardingFile",
                   kwargs={"candidate_id": "cand_6", "updates": {"email_label_applied": True}}),
            Action(name="AddOnboardingFile", kwargs={"candidate_id": "cand_6", "file_name": "Email Confirmation",
                                                       "file_path": "/onboarding/email_confirmation.pdf"}),

            # Allocate an asset
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MAC-001", "candidate_id": "cand_6"}),
            Action(name="UpdateAsset", kwargs={"asset_tag": "LT-MAC-001", "updates": {"status": "Assigned"}}),

                # Console output logs
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "EMAIL_LABEL_UPDATED", "message": "Email labels 'Urgent' and 'High' applied for cand_6"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ONBOARDING_FILE_UPDATED", "message": "Onboarding files updated for cand_6"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop assigned to cand_6"}),

                # Revise the onboarding status of the candidate.
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_6", "updates": {"onboarding_status": "Ready"}})
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
            "Manage the onboarding of candidate cand_7 through approval of asset requests req_501, req_502, assign a laptop LT-DELL-010, a phone PH-SAMSUNG-005, and provide accessories ACC-MOUSE-001. Checklist tasks check_701, check_702 are fulfilled, onboarding documents welcome_guide.pdf and id_scan.pdf are confirmed, and access validations access_901, access_902 are sanctioned. An email email_701 has the label 'Welcome'. Final state: assets are assigned and approved; documents are verified; checklist and access validations completed; terminal logs are available; candidate's onboarding status is revised."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-010", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-SAMSUNG-005", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-001", "candidate_id": "cand_7"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop, phone, and accessory assigned to cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_501 and req_502 approved"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email labeled 'Welcome' for cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_007",# It seems you've entered a single letter "p." Could you please provide a specific comment to paraphrase?
        instruction=(
            "Authorize the laptop and phone requests for candidate cand_7, allocate the assets, and make sure the onboarding documents indicate the asset allocation. Desired outcome: asset requests are indicated as 'Approved'; assets PH-LAPTOP-007 and PH-IPHONE-007 are allocated to cand_7; onboarding documents display phone_assigned=True and laptop_assigned=True; terminal logs record the assignment and authorization activities."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_701", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_702", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-007", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-007", "candidate_id": "cand_7"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/cand_7_onboarding.json", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_701 and req_702 approved", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-007 assigned", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "PH-LAPTOP-007 assigned", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_008",#p
        instruction=(
            "Authorize the laptop and phone requests for candidate cand_7, allocate the assets, revise onboarding documents for asset allocation, finalize checklist tasks, sanction access verifications, and categorize emails. Desired outcome: asset requests are marked 'Approved'; assets PH-LAPTOP-010, PH-IPHONE-005, and ACC-MOUSE-001 are assigned; checklist tasks marked 'Completed'; access verifications approved; onboarding documents reflect assigned assets; the email is categorized as 'Welcome'; terminal logs record all operations."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-010", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-005", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-001", "candidate_id": "cand_7"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True, "accessory_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_501 and req_502 approved", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "PH-LAPTOP-010, PH-IPHONE-005, and ACC-MOUSE-001 assigned", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items check_701 and check_702 completed", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks access_901 and access_902 approved", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email email_701 labeled Welcome", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_009",#p
        instruction=(
            "Authorize candidate cand_7's request for a laptop, allocate the asset, revise onboarding files to reflect the laptop assignment, and log the records. End state: laptop request authorized; laptop PH-LAPTOP-010 allocated; onboarding files indicate laptop_assigned=True; terminal logs document assignment and authorization."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-010", "candidate_id": "cand_7"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_501 approved", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "PH-LAPTOP-010 assigned", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "LaptopAssigned"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_010",#p
        instruction=(
            "Authorize candidate cand_7's request for a phone, allocate the asset, revise onboarding files to reflect the phone assignment, finalize checklist items, authorize access checks, assign email tags, and log the records. End state: phone request authorized; asset PH-IPHONE-005 allocated; onboarding files indicate phone_assigned=True; checklist items finalized; access checks authorized; email tagged 'Welcome'; terminal logs document all activities."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-005", "candidate_id": "cand_7"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"phone_assigned": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_502 approved", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-005 assigned", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items check_701 and check_702 completed", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks access_901 and access_902 approved", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email email_701 labeled Welcome", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "AssetsAndChecksReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_011",
        instruction=(
            "Handle the complete onboarding process for candidate cand_7: approve every asset request (laptop, phone, accessories), allocate assets, finalize all checklist items, give approval for all access checks, update several onboarding files, apply numerous email labels, and document terminal logs for each step. End state: all assets allocated; checklist items finalized; access checks approved; onboarding files updated; emails labeled; logs document all actions; candidate status indicates full onboarding."
        ),
        actions=[
            # Approval for asset requests
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),

            # Allocate resources
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-010", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-005", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-001", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-KEYBOARD-002", "candidate_id": "cand_7"}),

            # Revise onboarding documentation.
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide.pdf",
                                                          "updates": {"laptop_assigned": True,
                                                                      "phone_assigned": True}}),
            Action(name="UpdateOnboardingFile",
                   kwargs={"file_path": "files/id_scan.pdf", "updates": {"verified": True}}),
            Action(name="UpdateOnboardingFile",
                   kwargs={"file_path": "files/policy_acknowledgment.pdf", "updates": {"acknowledged": True}}),

            # Checklist finalized.
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_703", "updates": {"status": "Completed"}}),

            # Permission validations
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_903", "updates": {"status": "Approved"}}),

            # Email tags
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_702", "label_id": "label_Policy"}),

            # Command line output logs
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED",
                                                       "message": "Asset requests req_501 and req_502 approved",
                                                       "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, mouse, and keyboard assigned",
                           "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED",
                                                       "message": "Checklist items check_701, check_702, check_703 completed",
                                                       "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED",
                                                       "message": "Access checks access_901, access_902, access_903 approved",
                                                       "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Emails email_701 and email_702 labeled",
                           "candidate_id": "cand_7"}),

            # Update on candidate status
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_055",
        instruction=(
            "Authorize candidate cand_5's laptop request req_105, allocate LT-MBP-003, confirm onboarding files verified, finalize checklist items check_207, check_208, authorize access checks access_306, access_307, and document all terminal logs. End state: candidate assets allocated and onboarding prepared."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_105", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MBP-003", "candidate_id": "cand_5"}),
            Action(name="UpdateOnboardingFile",
                   kwargs={"file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md",
                           "updates": {"laptop_assigned": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_207", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_208", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_306", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_307", "updates": {"status": "Approved"}}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop LT-MBP-003 assigned to cand_5"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_105 approved"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_5"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_5"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_042",
        instruction=(
            "Authorize and allocate laptops to several candidates (Emma Thompson cand_2, William Davis cand_3, Sofia Martinez cand_4) according to asset requests. Choose suitable laptops that meet the specifications and check availability, update the onboarding files accordingly, and create terminal logs for each allocation. End state: asset requests marked 'Approved'; laptops LT-DELL-003, LT-DELL-002, LT-MBP-001 assigned; onboarding files show laptop_assigned=True; logs capture all approvals and assignments."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_Jane_Laptop", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_Peter_Laptop", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_Maria_Laptop", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-003", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-002", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_4"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Jane_Smith/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Peter_Jones/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Maria_Rodriguez/asset_request.json", "updates": {"laptop_assigned": True}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "Laptops assigned to Jane, Peter, Maria", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "Laptops assigned to Jane, Peter, Maria", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "Laptops assigned to Jane, Peter, Maria", "candidate_id": "cand_4"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_043",
        instruction=(
            "Authorize and allocate both a laptop and phone to candidate Jordan Williams (cand_5). Update the onboarding file to reflect laptop_assigned=True and phone_assigned=True, make terminal log entries, and set the candidate's onboarding status to 'AssetsReady'. End state: asset requests marked 'Approved'; laptop LT-MBP-002 and phone PH-IPHONE-001 assigned; onboarding file updated; candidate status updated."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_Alex_Laptop", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_Alex_Phone", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MBP-002", "candidate_id": "cand_5"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_5"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Alex_Thompson/asset_request.json", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Laptop and phone approved for Jordan Williams", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "LT-MBP-002 assigned", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-001 assigned", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_044",
        instruction=(
            "Authorize cand_2's laptop request, allocate the laptop, and modify the onboarding file to display the laptop assignment. Final condition: asset request authorized; LT-DELL-003 allocated to cand_2; onboarding file indicates laptop_assigned=True; terminal logs record approval and allocation events."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-003", "candidate_id": "cand_2"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Jane_Smith/asset_request.json",
                                                          "updates": {"laptop_assigned": True}}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_101 approved",
                           "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "LT-DELL-003 assigned",
                           "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_046",
        instruction=(
            "Authorize cand_4's requests for a laptop and phone, allocate the necessary assets, resolve any pending access problems, and amend the onboarding files. Final condition: asset requests authorized; LT-MBP-001 and PH-IPHONE-002 allocated; onboarding files reflect laptop_assigned=True, phone_assigned=True; access problems logged as resolved."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_104", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_105", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-002", "candidate_id": "cand_4"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Maria_Rodriguez/asset_request.json", "updates": {"laptop_assigned": True, "phone_assigned": True, "access_issues_resolved": True}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_104 and req_105 approved", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "LT-MBP-001 assigned", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "PHONE_ASSIGNED", "message": "PH-IPHONE-002 assigned", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_033",
        instruction=(
            "Endorse candidate cand_7's laptop request, allocate the asset, update onboarding documentation reflecting the laptop allocation, finalize checklist tasks, authorize access checks, categorize emails, and document logs. Final state: laptop request endorsed; laptop PH-LAPTOP-010 allocated; onboarding documentation indicates laptop_assigned=True; checklist tasks completed; access checks authorized; email tagged 'Welcome'; terminal logs record all activities."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-010", "candidate_id": "cand_7"}),
            Action(name="UpdateOnboardingFile",
                   kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_Welcome"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_501 approved",
                           "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "LAPTOP_ASSIGNED", "message": "PH-LAPTOP-010 assigned",
                           "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED",
                                                       "message": "Checklist items check_701 and check_702 completed",
                                                       "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED",
                                                       "message": "Access checks access_901 and access_902 approved",
                                                       "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "EMAIL_LABEL_APPLIED", "message": "Email email_701 labeled Welcome",
                           "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "AssetsAndChecksReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_001",
        instruction=(
            "Authorize asset requests req_101, req_102 for candidate cand_1, allocate laptop LT-001 and phone PH-001, finalize checklist tasks check_101 and check_102, confirm onboarding documents welcome.pdf and id_scan.pdf, label email email_101 with 'Welcome,' and register all modifications. Ensure the candidate record confirms completion."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-001", "candidate_id": "cand_1"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-001", "candidate_id": "cand_1"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_101", "label_id": "label_Welcome"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Onboarding completed for cand_1", "candidate_id": "cand_1"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_002",
        instruction=(
            "Handle the approval of candidate cand_2's asset requests req_201 and req_202, allocate assets LT-002 and PH-002, finalize checklist check_201, check onboarding file offer_letter.pdf, tag email email_201 with 'Ready', and record all actions. Update the candidate record to indicate completion."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_201", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_202", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-002", "candidate_id": "cand_2"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_201", "label_id": "label_Ready"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Assets assigned to cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_2", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'Ready' for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_003",
        instruction=(
            "You handle the release of old assets LT-003 and PH-003 for candidate cand_3, allocate new laptop LT-003B, finish checklist items check_301 and check_302, incorporate onboarding file id_scan.pdf, attach email label 'AssetUpdate' to email email_301, document all changes, and revise the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-003"}),
            Action(name="ReleaseAsset", kwargs={"asset_tag": "PH-003"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/id_scan.pdf", "status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_301", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'AssetUpdate' for cand_3", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_003",
        instruction=(
            "You handle the release of old assets LT-003 and PH-003 for candidate cand_3, allocate new laptop LT-003B, finish checklist items check_301 and check_302, incorporate onboarding file id_scan.pdf, attach email label 'AssetUpdate' to email email_301, document all changes, and revise the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-003"}),
            Action(name="ReleaseAsset", kwargs={"asset_tag": "PH-003"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-003B", "candidate_id": "cand_3"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/id_scan.pdf", "status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_301", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_3", "candidate_id": "cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'AssetUpdate' for cand_3", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_004",
        instruction=(
            "You endorse asset requests req_401 for candidate cand_4, allocate laptop LT-004 and phone PH-004, fulfill checklist item check_401, incorporate onboarding file welcome_guide.pdf, attach email label 'Onboarded' to email email_401, document all actions, and designate candidate record as completed."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_401", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-004", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-004", "candidate_id": "cand_4"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_401", "updates": {"status": "Completed"}}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/welcome_guide.pdf", "status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_401", "label_id": "label_Onboarded"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Assets assigned for cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_4", "candidate_id": "cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'Onboarded' for cand_4", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_005",
        instruction=(
            "Handle asset reassignment for candidate cand_5: release old laptop LT-005, assign new laptop LT-005B, ensure completion of checklist item check_501, verify the onboarding file id_scan.pdf, apply email label 'AssetUpdate' to email email_501, log all updates, and update the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-005"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_501", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_501", "label_id": "label_AssetUpdate"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_RELEASED", "message": "Old assets released for cand_5", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "New assets assigned for cand_5", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist completed for cand_5", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELED", "message": "Email labeled 'AssetUpdate' for cand_5", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_068",
        instruction=(
            "Handle the onboarding of candidate cand_7: approve asset requests req_701 and req_702, assign laptop LT-HP-007, phone PH-IP-007, and accessory ACC-KEY-007. Complete checklist items check_801 and check_802. Verify onboarding files resume.pdf and id_scan.pdf. Approve access checks access_901 and access_902. Tag email email_701 with 'OnboardingComplete' and record all actions."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_401", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_402", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-004", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-SAMSUNG-004", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-004", "candidate_id": "cand_4"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_401", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_402", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_401", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_402", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_401", "label_id": "label_OnboardingReady"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Candidate cand_4 onboarding completed", "candidate_id": "cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_065",
        instruction=(
            "Candidate cand_7 is tasked with cleaning up emails and reallocating assets. You eliminate email email_701, discard attachment attach_701, incorporate the new onboarding document policies_cand7.pdf, mark checklist item check_701 as Completed, and authorize access check access_701. Log terminal activities for each action performed."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-OLD-007"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-NEW-007", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-NEW-007", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-HEADSET-007", "candidate_id": "cand_7"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_702", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_701"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_702"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_703", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_704", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_AssetChange"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_7", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),


    Task(
        annotator="R",
        user_id="onboarding_ds_064",
        instruction=(
            "Candidate cand_6 has several assets and emails awaiting action. You approve asset request req_601, allocate laptop LT-LENOVO-006. Dispatch a welcome email ('Welcome!', 'Hello cand_6') email_601, attach the file welcome_attach.pdf, and apply the label 'Onboarding' to email_601. Release the outdated asset LT-OLD-001. Document all terminal logs for the executed tasks. The final state should be: new asset assigned, email dispatched with label, old asset released."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-HP-001", "candidate_id": "cand_1"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IP-001", "candidate_id": "cand_1"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_101", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_102", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_101", "label_id": "label_OnboardingReady"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Candidate cand_1 onboarding completed", "candidate_id": "cand_1"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_062",
        instruction=(
            "Handle the onboarding of candidate cand_3 by endorsing laptop request req_203 and accessory requests req_204, allocate LT-DELL-003, monitor MON-LG-002, keyboard ACC-KEYBOARD-001, finalize checklist items check_303, check_304, sanction access checks access_403, access_404, update onboarding files, and register terminal logs. End state: all assets assigned and approved, files verified, checklist and access checks completed, candidate status updated."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_301", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_302", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-HP-003", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IP-003", "candidate_id": "cand_3"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_301", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_302", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_301", "label_id": "label_OnboardingReady"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Candidate cand_3 onboarding completed", "candidate_id": "cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_061",
        instruction=(
            "Coordinate candidate cand_2's onboarding by authorizing asset requests req_201, req_202, assigning laptop LT-MBP-004, phone PH-IPHONE-002, and accessory ACC-HEADSET-001. Fulfill checklist items check_301, check_302, endorse access verifications access_401, access_402, revise onboarding documents welcome_Jane_Smith.md and asset_request.json, and log terminal records. Completion state: assets allocated and approved, documents verified, checklist and access finalized, candidate onboarding status refreshed."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_201", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_202", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MBP-004", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-002", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-HEADSET-001", "candidate_id": "cand_2"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_301", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_302", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_401", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_402", "updates": {"status": "Approved"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Jane_Smith/asset_request.json", "updates": {"assigned_assets": ["LT-MBP-004", "PH-IPHONE-002", "ACC-HEADSET-001"]}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop, phone, and headset assigned to cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_201 and req_202 approved"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_062",
        instruction=(
            "Handle the onboarding of candidate cand_3 by endorsing laptop request req_203 and accessory requests req_204, allocate LT-DELL-003, monitor MON-LG-002, keyboard ACC-KEYBOARD-001, finalize checklist items check_303, check_304, sanction access checks access_403, access_404, update onboarding files, and register terminal logs. End state: all assets assigned and approved, files verified, checklist and access checks completed, candidate status updated."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_203", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_204", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-003", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "MON-LG-002", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-KEYBOARD-001", "candidate_id": "cand_3"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_303", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_304", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_403", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_404", "updates": {"status": "Approved"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md", "updates": {"laptop_assigned": True, "monitor_assigned": True, "keyboard_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Peter_Jones/asset_request.json", "updates": {"assigned_assets": ["LT-DELL-003","MON-LG-002","ACC-KEYBOARD-001"]}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop, monitor, and keyboard assigned to cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_203 and req_204 approved"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_3"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_3"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_063",
        instruction=(
            "Coordinate the onboarding of candidate cand_4 by endorsing laptop request req_205, phone request req_206, accessory request req_207, allocate LT-MBP-005, PH-IPHONE-003, ACC-MOUSE-002, finalize checklist items check_305, check_306, authorize access checks access_405, access_406, update onboarding files welcome and asset_request.json, and document all actions. End state: all assets assigned, files verified, checklist and access completed, candidate status updated."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_205", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_206", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_207", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MBP-005", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-003", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-002", "candidate_id": "cand_4"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_305", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_306", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_405", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_406", "updates": {"status": "Approved"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md", "updates": {"laptop_assigned": True, "phone_assigned": True, "accessory_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Maria_Rodriguez/asset_request.json", "updates": {"assigned_assets": ["LT-MBP-005","PH-IPHONE-003","ACC-MOUSE-002"]}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop, phone, and accessory assigned to cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_205, req_206, req_207 approved"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_4"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_064",
        instruction=(
            "Candidate cand_6 has several assets and emails awaiting action. You approve asset request req_601, allocate laptop LT-LENOVO-006. Dispatch a welcome email ('Welcome!', 'Hello cand_6') email_601, attach the file welcome_attach.pdf, and apply the label 'Onboarding' to email_601. Release the outdated asset LT-OLD-001. Document all terminal logs for the executed tasks. The final state should be: new asset assigned, email dispatched with label, old asset released."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_601", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-LENOVO-006", "candidate_id": "cand_6"}),
            Action(name="SendEmail", kwargs={"email": {"message_id": "email_601", "subject": "Welcome!", "body": "Hello cand_6"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_601", "file_name": "welcome_attach.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_601", "label_id": "label_Onboarding"}),
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-OLD-001"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED", "message": "LT-LENOVO-006 assigned to cand_6", "candidate_id": "cand_6"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_SENT", "message": "Welcome email sent to cand_6", "candidate_id": "cand_6"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_RELEASED", "message": "LT-OLD-001 released from cand_6", "candidate_id": "cand_6"})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_065",
        instruction=(
            "Candidate cand_7 is tasked with cleaning up emails and reallocating assets. You eliminate email email_701, discard attachment attach_701, incorporate the new onboarding document policies_cand7.pdf, mark checklist item check_701 as Completed, and authorize access check access_701. Log terminal activities for each action performed."
        ),
        actions=[
            Action(name="DeleteEmail", kwargs={"message_id": "email_701"}),
            Action(name="RemoveAttachment", kwargs={"attachment_id": "attach_701"}),
            Action(name="AddOnboardingFile", kwargs={"file": {"file_path": "files/policies_cand7.pdf", "status": "Uploaded"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_701", "updates": {"status": "Approved"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_DELETED", "message": "email_701 deleted for cand_7", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ATTACHMENT_REMOVED", "message": "attach_701 removed for cand_7", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_FILE_ADDED", "message": "policies_cand7.pdf uploaded", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_UPDATED", "message": "check_701 completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_APPROVED", "message": "access_701 approved for cand_7", "candidate_id": "cand_7"})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_407",
        instruction=(
            "For candidate cand_7, handle the release of the old laptop LT-007A, allocate the new laptop LT-007B, complete asset requests req_701 and req_702, eliminate access checks access_701 and access_702, introduce new access checks access_703 and access_704, include Company-Policies.pdf and Benefits-Guide.pdf as attachments, apply the label 'AssetUpdate' to emails email_701 and email_702, update checklist items check_701 and check_702, ensure the verification of onboarding files ID-Card.pdf and Passport.pdf, record all modifications, and refresh the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-007A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-007B", "candidate_id": "cand_7"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_702", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_701"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_702"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_703", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_704", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_13", "file_name": "Company-Policies.pdf"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_14", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_AssetUpdate"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_702", "label_id": "label_AssetUpdate"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/ID-Card.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/Passport.pdf", "updates": {"status": "Verified"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Full asset and checklist update for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_067",
        instruction=(
            "Coordinate candidate cand_7's offboarding: manage the release of assets LT-OLD-007 and PH-OLD-007, erase checklist items check_701 and check_702, revoke access checks access_701 and access_702, remove onboarding files farewell.pdf and exit_form.pdf, and document the events."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-OLD-007"}),
            Action(name="ReleaseAsset", kwargs={"asset_tag": "PH-OLD-007"}),
            Action(name="RemoveChecklistItem", kwargs={"item_id": "check_701"}),
            Action(name="RemoveChecklistItem", kwargs={"item_id": "check_702"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_701"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_702"}),
            Action(name="RemoveOnboardingFile", kwargs={"file_path": "files/farewell.pdf"}),
            Action(name="RemoveOnboardingFile", kwargs={"file_path": "files/exit_form.pdf"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "OFFBOARDING_ASSETS_RELEASED", "message": "Assets released for cand_7", "candidate_id": "cand_7"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "OFFBOARDING_COMPLETED", "message": "Checklist, access, and files removed for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"offboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_068",
        instruction=(
            "Handle the onboarding of candidate cand_7: approve asset requests req_701 and req_702, assign laptop LT-HP-007, phone PH-IP-007, and accessory ACC-KEY-007. Complete checklist items check_801 and check_802. Verify onboarding files resume.pdf and id_scan.pdf. Approve access checks access_901 and access_902. Tag email email_701 with 'OnboardingComplete' and record all actions."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_701", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_702", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-HP-007", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IP-007", "candidate_id": "cand_7"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-KEY-007", "candidate_id": "cand_7"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_801", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_802", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/resume.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_901", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_902", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_701", "label_id": "label_OnboardingComplete"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "All onboarding steps completed for cand_7", "candidate_id": "cand_7"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_7", "updates": {"onboarding_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_069",
        instruction=(
            "Coordinate the reassignment of assets for candidate cand_6: release old phone PH-OLD-006, assign new laptop LT-NEW-006 and new phone PH-NEW-006. Update asset requests req_603 and req_604 to 'Completed'. Remove access checks access_603, add new access checks access_605 and access_606. Attach Company-Policies.pdf and Benefits-Guide.pdf, set label 'AssetChange' for email email_602, and document all changes."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "PH-OLD-006"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-NEW-006", "candidate_id": "cand_6"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-NEW-006", "candidate_id": "cand_6"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_603", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_604", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_603"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_605", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_606", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_1", "file_name": "Company-Policies.pdf"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_2", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_602", "label_id": "label_AssetChange"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REASSIGNMENT", "message": "Assets reassigned for cand_6", "candidate_id": "cand_6"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_UPDATED", "message": "Access checks updated for cand_6", "candidate_id": "cand_6"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_6", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_070",
        instruction=(
            "Handle the finalization of onboarding for candidate cand_5: approve asset requests req_501 and req_502, allocate laptop LT-DELL-005, phone PH-SAMSUNG-005, and mouse ACC-MOUSE-005. Mark checklist items check_701 and check_702 as completed. Confirm onboarding files offer_letter.pdf and id_scan.pdf. Approve access checks access_801 and access_802. Dispatch email email_501 with label 'OnboardingReady' and document terminal logs for all updates."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-005", "candidate_id": "cand_5"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-SAMSUNG-005", "candidate_id": "cand_5"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-005", "candidate_id": "cand_5"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_701", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_702", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/offer_letter.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_801", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_802", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_501", "label_id": "label_OnboardingReady"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_FINALIZED", "message": "Candidate cand_5 onboarding finalized", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "Ready"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_052",
        instruction=(
            "Coordinate the approval of candidate cand_2's laptop request req_101, assign laptop LT-MBP-001, update onboarding files to set laptop_assigned=True, fulfill checklist items check_201 and check_202, approve access checks access_301, and log all terminal records. Final condition: laptop assigned and approved, files, checklist, and access checks completed, onboarding status of candidate updated."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_2"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md",
                                                        "updates": {"laptop_assigned": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_301", "updates": {"status": "Approved"}}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_ASSIGNED", "message": "Laptop LT-MBP-001 assigned to cand_2"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_101 approved"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_2"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_2"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_405",
        instruction=(
            "Handle candidate cand_5 by relinquishing the old laptop LT-005A, assigning the new laptop LT-005B, fulfilling asset requests req_501 and req_502, discontinuing access checks access_501 and access_502, adding access checks access_503, access_504, attaching Company-Policies.pdf, attaching Benefits-Guide.pdf, applying label 'AssetChange' to the email email_501, updating checklist items check_501, check_502, ensuring verification of onboarding files ID-Card.pdf and Passport.pdf, logging all changes, and updating the candidate record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-005A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-005B", "candidate_id": "cand_5"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_501"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_502"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_503", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_504", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_9", "file_name": "Company-Policies.pdf"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_10", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_501", "label_id": "label_AssetChange"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_501", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_502", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/ID-Card.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/Passport.pdf", "updates": {"status": "Verified"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Full asset and checklist update for cand_5", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_053",
        instruction=(
            "Coordinate the onboarding of candidate cand_3 by sanctioning laptop request req_102, assigning the laptop LT-DELL-002 and monitor MON-LG-001, marking files as verified in the onboarding, completing checklist items check_203, check_204, and endorsing access checks access_302, access_303. Document terminal logs and update the candidate onboarding status."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-DELL-002", "candidate_id": "cand_3"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "MON-LG-001", "candidate_id": "cand_3"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md",
                                                        "updates": {"laptop_assigned": True,
                                                                    "monitor_assigned": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_204", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_302", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_303", "updates": {"status": "Approved"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED",
                                                     "message": "Laptop LT-DELL-002 and Monitor MON-LG-001 assigned to cand_3"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset request req_102 approved"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_3"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_3"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_3", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_054",
        instruction=(
            "Handle onboarding for candidate cand_4 by approving the laptop request req_103 and phone request req_104, allocating LT-MBP-002 and PH-IPHONE-001, verifying onboarding files, fulfilling checklist items check_205, check_206, approving access checks access_304, access_305, and logging all activities."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_103", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_104", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-MBP-002", "candidate_id": "cand_4"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_4"}),
            Action(name="UpdateOnboardingFile",
                   kwargs={"file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md",
                           "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_205", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_206", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_304", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_305", "updates": {"status": "Approved"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_ASSIGNED",
                                                     "message": "Laptop LT-MBP-002 and Phone PH-IPHONE-001 assigned to cand_4"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED",
                                                     "message": "Asset requests req_103 and req_104 approved"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed for cand_4"}),
            Action(name="RecordTerminalLog",
                   kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved for cand_4"}),
            Action(name="UpdateCandidate",
                   kwargs={"candidate_id": "cand_4", "updates": {"onboarding_status": "AssetsReady"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_012",
        instruction=(
            "Coordinate full onboarding for candidate cand_1: approve all asset requests (laptop, phone, accessories), allocate assets, complete all checklist items, authorize all access checks, revise multiple onboarding files, apply email labels, and document terminal logs for each step. Final condition: all assets are allocated; checklist items are completed; access checks are authorized; onboarding files are updated; emails have labels; logs document all activities; candidate status shows full onboarding."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-001", "candidate_id": "cand_1"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_1"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-002", "candidate_id": "cand_1"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"verified": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_101", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_101", "label_id": "label_Welcome"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_101 and req_102 approved", "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, and mouse assigned", "candidate_id": "cand_1"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_017",
        instruction=(
            "Handle the comprehensive multi-step onboarding for candidate cand_2: approve every pending asset request, assign all applicable assets, finalize each checklist item, authorize access checks, refresh onboarding files with asset and policy information, utilize suitable email labels, and meticulously log terminal activities throughout the process. Final goal: candidate cand_2 is fully assigned assets, checklist is finalized, access checks are authorized, onboarding files are updated, emails bear appropriate labels, and the candidate's status reads as fully completed."
        ),
        actions=[
            # Approval for asset requests
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_201", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_202", "updates": {"status": "Approved"}}),

            # Allocation of assets
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-002", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-002", "candidate_id": "cand_2"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-003", "candidate_id": "cand_2"}),

            # Updates to onboarding documents
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide_cand2.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan_cand2.pdf", "updates": {"verified": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/policy_ack_cand2.pdf", "updates": {"acknowledged": True}}),

            # Completion of checklist items
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_203", "updates": {"status": "Completed"}}),

            # Authorization for access verification
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_201", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_202", "updates": {"status": "Approved"}}),

            # Email tags
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_201", "label_id": "label_Welcome"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_202", "label_id": "label_Policy"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_203", "label_id": "label_Onboarding"}),

            # Command line logs
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_201 and req_202 approved", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, and mouse assigned", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_2"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome', 'Policy', 'Onboarding'", "candidate_id": "cand_2"}),

            # Update on the candidate
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_402",
        instruction=(
            "For candidate cand_2, coordinate the release of old laptop LT-002A, allocate new laptop LT-002B, fulfill asset requests req_201 and req_202, eliminate access checks access_201, access_202, introduce new access checks access_203, access_204, attach Company-Policies.pdf, append Benefits-Guide.pdf, apply the label 'AssetUpdate' to email email_201, update checklist items check_201, check_202, confirm onboarding files ID-Card.pdf and Driving-License.pdf, document all modifications, and refresh the candidate's record."
        ),
        actions=[
            Action(name="ReleaseAsset", kwargs={"asset_tag": "LT-002A"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "LT-002B", "candidate_id": "cand_2"}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_201", "updates": {"status": "Completed"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_202", "updates": {"status": "Completed"}}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_201"}),
            Action(name="RemoveAccessCheck", kwargs={"check_id": "access_202"}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_203", "status": "Pending"}}),
            Action(name="AddAccessCheck", kwargs={"check": {"check_id": "access_204", "status": "Pending"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_3", "file_name": "Company-Policies.pdf"}}),
            Action(name="AddAttachment", kwargs={"attachment": {"attachment_id": "attach_4", "file_name": "Benefits-Guide.pdf"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_201", "label_id": "label_AssetUpdate"}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_201", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_202", "updates": {"status": "Completed"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/ID-Card.pdf", "updates": {"status": "Verified"}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/Driving-License.pdf", "updates": {"status": "Verified"}}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ONBOARDING_COMPLETED", "message": "Full asset and checklist update for cand_2", "candidate_id": "cand_2"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_2", "updates": {"asset_update_status": "Completed"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_020",
        instruction=(
            "Handle onboarding for candidate cand_5: authorize asset requests, allocate assets such as laptop, phone, and accessories, finalize checklist items, authorize access checks, revise onboarding files, label emails, and document terminal logs."
        ),
        actions=[
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_501", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_502", "updates": {"status": "Approved"}}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-005", "candidate_id": "cand_5"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-005", "candidate_id": "cand_5"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-006", "candidate_id": "cand_5"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-KEYBOARD-004", "candidate_id": "cand_5"}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide_cand5.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan_cand5.pdf", "updates": {"verified": True}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_501", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_502", "updates": {"status": "Completed"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_501", "updates": {"status": "Approved"}}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_501", "label_id": "label_Welcome"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_502", "label_id": "label_Policy"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_501 and req_502 approved", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, mouse, and keyboard assigned", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_5"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome' and 'Policy'", "candidate_id": "cand_5"}),
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_5", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="R",
        user_id="onboarding_ds_016",# It seems you entered a single letter, which does not provide enough context for paraphrasing. Please provide a complete comment for me to paraphrase.
        instruction=(
            "Oversee the entire multi-step onboarding for candidate cand_1: authorize all asset requests, allocate all assets, finalize all checklist items, authorize all access checks, update all onboarding files, apply multiple email labels, and document detailed terminal logs for each step. End state: all assets allocated, onboarding files revised, checklist items finalized, access checks authorized, emails labeled, and candidate status indicates full completion."
        ),
        actions=[
            # Approval for asset requests
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_101", "updates": {"status": "Approved"}}),
            Action(name="UpdateAssetRequest", kwargs={"request_id": "req_102", "updates": {"status": "Approved"}}),

            # Asset allocations
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-LAPTOP-001", "candidate_id": "cand_1"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_1"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-MOUSE-002", "candidate_id": "cand_1"}),
            Action(name="AssignAsset", kwargs={"asset_tag": "ACC-KEYBOARD-002", "candidate_id": "cand_1"}),

            # Updates to onboarding files
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/welcome_guide.pdf", "updates": {"laptop_assigned": True, "phone_assigned": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/id_scan.pdf", "updates": {"verified": True}}),
            Action(name="UpdateOnboardingFile", kwargs={"file_path": "files/policy_acknowledgment.pdf", "updates": {"acknowledged": True}}),

            # Completion of checklist items
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_101", "updates": {"status": "Completed"}}),
            Action(name="UpdateChecklistItem", kwargs={"item_id": "check_102", "updates": {"status": "Completed"}}),

            # Authorization for access verification
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_101", "updates": {"status": "Approved"}}),
            Action(name="UpdateAccessCheck", kwargs={"check_id": "access_102", "updates": {"status": "Approved"}}),

            # Email tags
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_101", "label_id": "label_Welcome"}),
            Action(name="ApplyLabelToEmail", kwargs={"email_id": "email_102", "label_id": "label_Policy"}),

            # Console logs
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSET_REQUEST_APPROVED", "message": "Asset requests req_101 and req_102 approved", "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ASSETS_ASSIGNED", "message": "Laptop, phone, mouse, and keyboard assigned", "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "CHECKLIST_COMPLETED", "message": "Checklist items completed", "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "ACCESS_CHECK_APPROVED", "message": "Access checks approved", "candidate_id": "cand_1"}),
            Action(name="RecordTerminalLog", kwargs={"event_type": "EMAIL_LABELS_APPLIED", "message": "Emails labeled 'Welcome' and 'Policy'", "candidate_id": "cand_1"}),

            # Update on the candidate
            Action(name="UpdateCandidate", kwargs={"candidate_id": "cand_1", "updates": {"onboarding_status": "OnboardingCompleted"}})
        ],
        outputs=[]
    ),
]
