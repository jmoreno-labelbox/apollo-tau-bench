# Copyright Sierra

tasks = [
    {
        "annotator": R,
        "user_id": "onboarding_ds_002",
        "instruction": "Handle the approval of candidate cand_2's asset requests req_201 and req_202, allocate assets LT-002 and PH-002, finalize checklist check_201, check onboarding file offer_letter.pdf, tag email email_201 with 'Ready', and record all actions. Update the candidate record to indicate completion.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_502",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/Benefits-Guide.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_502",
                    "label_id": "label_Ready"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Assets assigned for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.LT-005B.status=Assigned | asset.PH-005B.status=Assigned | checklist_item.check_502.status=Completed | onboarding_files.Benefits-Guide.pdf.status=Verified | email.email_502.labels=label_Ready | log.ASSET_ASSIGNED.message=Assets assigned for cand_5 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_5 | candidate.cand_5.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_003",
        "instruction": "You handle the release of old assets LT-003 and PH-003 for candidate cand_3, allocate new laptop LT-003B, finish checklist items check_301 and check_302, incorporate onboarding file id_scan.pdf, attach email label 'AssetUpdate' to email email_301, document all changes, and revise the candidate record.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_401",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_402",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-005",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide_cand4.pdf",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan_cand4.pdf",
                    "updates": {
                        "verified": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_401",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_402",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_401",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_401",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_402",
                    "label_id": "label_Policy"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_401 and req_402 approved",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSETS_ASSIGNED",
                    "message": "Laptop, phone, and mouse assigned",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELS_APPLIED",
                    "message": "Emails labeled 'Welcome' and 'Policy'",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "onboarding_status": "OnboardingCompleted"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_401.status=Approved | asset_request.req_402.status=Approved | asset.PH-LAPTOP-004.status=Assigned | asset.PH-IPHONE-004.status=Assigned | asset.ACC-MOUSE-005.status=Assigned | onboarding_files.welcome_guide_cand4.laptop_assigned=True | onboarding_files.welcome_guide_cand4.phone_assigned=True | onboarding_files.id_scan_cand4.verified=True | checklist.check_401.status=Completed | checklist.check_402.status=Completed | access_check.access_401.status=Approved | email.email_401.labels=label_Welcome | email.email_402.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_401 and req_402 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, and mouse assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome' and 'Policy' | candidate.cand_4.onboarding_status=OnboardingCompleted"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_004",
        "instruction": "You endorse asset requests req_401 for candidate cand_4, allocate laptop LT-004 and phone PH-004, fulfill checklist item check_401, incorporate onboarding file welcome_guide.pdf, attach email label 'Onboarded' to email email_401, document all actions, and designate candidate record as completed.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_401",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_402",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/cand_4_onboarding.json",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Requests req_401 and req_402 approved",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "PH-LAPTOP-004 assigned",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "PHONE_ASSIGNED",
                    "message": "PH-IPHONE-004 assigned",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_401.status=Approved | asset_request.req_402.status=Approved | asset.PH-LAPTOP-004.status=Assigned | asset.PH-IPHONE-004.status=Assigned | onboarding_files.cand_4.laptop_assigned=True | onboarding_files.cand_4.phone_assigned=True | log.ASSET_REQUEST_APPROVED.message=Requests req_401 and req_402 approved | log.LAPTOP_ASSIGNED.message=PH-LAPTOP-004 assigned | log.PHONE_ASSIGNED.message=PH-IPHONE-004 assigned | candidate.cand_4.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_005",
        "instruction": "Handle asset reassignment for candidate cand_5: release old laptop LT-005, assign new laptop LT-005B, ensure completion of checklist item check_501, verify the onboarding file id_scan.pdf, apply email label 'AssetUpdate' to email email_501, log all updates, and update the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-OLD-001"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-NEW-006",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-NEW-006",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_601",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_602",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_601"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_602"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_603",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_604",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_1",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_2",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_601",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REASSIGNMENT",
                    "message": "Assets reassigned for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-OLD-001.status=Available | asset.LT-NEW-006.status=Assigned | asset.PH-NEW-006.status=Assigned | asset_request.req_601.status=Completed | asset_request.req_602.status=Completed | access_check.access_601=Removed | access_check.access_602=Removed | access_check.access_603.status=Pending | access_check.access_604.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_601.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_6 | log.ACCESS_UPDATED.message=Access checks updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_006",
        "instruction": "Manage the onboarding of candidate cand_7 through approval of asset requests req_501, req_502, assign a laptop LT-DELL-010, a phone PH-SAMSUNG-005, and provide accessories ACC-MOUSE-001. Checklist tasks check_701, check_702 are fulfilled, onboarding documents welcome_guide.pdf and id_scan.pdf are confirmed, and access validations access_901, access_902 are sanctioned. An email email_701 has the label 'Welcome'. Final state: assets are assigned and approved; documents are verified; checklist and access validations completed; terminal logs are available; candidate's onboarding status is revised.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_5",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-003",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-003",
                    "updates": {
                        "status": "Assigned"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "PHONE_ASSIGNED",
                    "message": "Phone assigned to cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset request req_5 approved"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_5.status=Approved | asset.PH-IPHONE-003.status=Assigned | onboarding_files.phone_assigned=True | log.PHONE_ASSIGNED.message=Phone assigned to cand_5 | log.ASSET_REQUEST_APPROVED.message=Asset request req_5 approved | candidate.cand_5.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_007",
        "instruction": "Authorize the laptop and phone requests for candidate cand_7, allocate the assets, and make sure the onboarding documents indicate the asset allocation. Desired outcome: asset requests are indicated as 'Approved'; assets PH-LAPTOP-007 and PH-IPHONE-007 are allocated to cand_7; onboarding documents display phone_assigned=True and laptop_assigned=True; terminal logs record the assignment and authorization activities.",
        "actions": [
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAttachment",
                "arguments": {
                    "attachment_id": "attach_3"
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_4",
                        "file_name": "Training-Guide.pdf"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_card.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_202",
                    "label_id": "label_Training"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_202",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop assigned for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist item completed for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "training_status": "InProgress"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002B.status=Assigned | asset_request.req_202.status=Completed | checklist_item.check_202.status=Completed | attachment.Policies.pdf.removed=True | attachment.Training-Guide.pdf.added=True | onboarding_files.id_card.pdf.status=Verified | email.email_202.labels=label_Training | access_check.access_202.status=Pending | log.ASSET_ASSIGNED.message=Laptop assigned for cand_2 | log.CHECKLIST_COMPLETED.message=Checklist item completed for cand_2 | candidate.cand_2.training_status=InProgress"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_008",
        "instruction": "Authorize the laptop and phone requests for candidate cand_7, allocate the assets, revise onboarding documents for asset allocation, finalize checklist tasks, sanction access verifications, and categorize emails. Desired outcome: asset requests are marked 'Approved'; assets PH-LAPTOP-010, PH-IPHONE-005, and ACC-MOUSE-001 are assigned; checklist tasks marked 'Completed'; access verifications approved; onboarding documents reflect assigned assets; the email is categorized as 'Welcome'; terminal logs record all operations.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_301",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_302",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-003",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-003",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-004",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-KEYBOARD-003",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide_cand3.pdf",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan_cand3.pdf",
                    "updates": {
                        "verified": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/policy_ack_cand3.pdf",
                    "updates": {
                        "acknowledged": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_302",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_301",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_302",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_301",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_302",
                    "label_id": "label_Policy"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_301 and req_302 approved",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSETS_ASSIGNED",
                    "message": "Laptop, phone, mouse, and keyboard assigned",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELS_APPLIED",
                    "message": "Emails labeled 'Welcome' and 'Policy'",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "onboarding_status": "OnboardingCompleted"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_301.status=Approved | asset_request.req_302.status=Approved | asset.PH-LAPTOP-003.status=Assigned | asset.PH-IPHONE-003.status=Assigned | asset.ACC-MOUSE-004.status=Assigned | asset.ACC-KEYBOARD-003.status=Assigned | onboarding_files.welcome_guide_cand3.laptop_assigned=True | onboarding_files.welcome_guide_cand3.phone_assigned=True | onboarding_files.id_scan_cand3.verified=True | onboarding_files.policy_ack_cand3.acknowledged=True | checklist.check_301.status=Completed | checklist.check_302.status=Completed | access_check.access_301.status=Approved | access_check.access_302.status=Approved | email.email_301.labels=label_Welcome | email.email_302.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_301 and req_302 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, mouse, and keyboard assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome' and 'Policy' | candidate.cand_3.onboarding_status=OnboardingCompleted"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_010",
        "instruction": "Authorize candidate cand_7's request for a phone, allocate the asset, revise onboarding files to reflect the phone assignment, finalize checklist items, authorize access checks, assign email tags, and log the records. End state: phone request authorized; asset PH-IPHONE-005 allocated; onboarding files indicate phone_assigned=True; checklist items finalized; access checks authorized; email tagged 'Welcome'; terminal logs document all activities.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_103",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "MON-LG-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Peter_Jones/asset_request.json",
                    "updates": {
                        "laptop_assigned": true,
                        "monitor_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_102 and req_103 approved",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "LT-DELL-002 assigned",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "MONITOR_ASSIGNED",
                    "message": "MON-LG-001 assigned",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_102.status=Approved | asset_request.req_103.status=Approved | asset.LT-DELL-002.status=Assigned | asset.MON-LG-001.status=Assigned | onboarding_files.cand_3.laptop_assigned=True | onboarding_files.cand_3.monitor_assigned=True | log.ASSET_REQUEST_APPROVED.message=Asset requests req_102 and req_103 approved | log.LAPTOP_ASSIGNED.message=LT-DELL-002 assigned | log.MONITOR_ASSIGNED.message=MON-LG-001 assigned | candidate.cand_3.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_011",
        "instruction": "Handle the complete onboarding process for candidate cand_7: approve every asset request (laptop, phone, accessories), allocate assets, finalize all checklist items, give approval for all access checks, update several onboarding files, apply numerous email labels, and document terminal logs for each step. End state: all assets allocated; checklist items finalized; access checks approved; onboarding files updated; emails labeled; logs document all actions; candidate status indicates full onboarding.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-001A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-001B",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_101"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_102"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_105",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_3",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REASSIGNMENT",
                    "message": "Assets reassigned for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/Passport.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-001A.status=Available | asset.LT-001B.status=Assigned | asset_request.req_101.status=Completed | asset_request.req_102.status=Completed | access_check.access_101=Removed | access_check.access_102=Removed | access_check.access_105.status=Pending | attachment.Company-Policies.pdf.added=True | email.email_101.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_1 | log.ACCESS_UPDATED.message=Access checks updated for cand_1 | onboarding_files.Passport.pdf.status=Verified | candidate.cand_1.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_012",
        "instruction": "Coordinate full onboarding for candidate cand_1: approve all asset requests (laptop, phone, accessories), allocate assets, complete all checklist items, authorize all access checks, revise multiple onboarding files, apply email labels, and document terminal logs for each step. Final condition: all assets are allocated; checklist items are completed; access checks are authorized; onboarding files are updated; emails have labels; logs document all activities; candidate status shows full onboarding.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-004A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-004B",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_401",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_401"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_402"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_405",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_406",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_7",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_401",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/ID-Card.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-004A.status=Available | asset.LT-004B.status=Assigned | asset_request.req_401.status=Completed | access_check.access_401=Removed | access_check.access_402=Removed | access_check.access_405.status=Pending | access_check.access_406.status=Pending | attachment.Company-Policies.pdf.added=True | email.email_401.labels=label_AssetUpdate | log.ASSET_UPDATED.message=Assets updated for cand_4 | onboarding_files.ID-Card.pdf.status=Verified | candidate.cand_4.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_013",
        "instruction": "Coordinate the completion of onboarding for candidate cand_6: approve asset requests req_601, req_602, assign laptop LT-HP-006, phone PH-IP-006. Handle checklist items check_601, check_602, verify onboarding files offer_letter.pdf and id_scan.pdf. Approve access checks access_601, access_602. Label email email_601 as 'OnboardingReady' and log all updates accordingly.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_601",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_602",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-HP-006",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IP-006",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_601",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_602",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_601",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_602",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_601",
                    "label_id": "label_OnboardingReady"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Candidate cand_6 onboarding completed",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_601.status=Approved | asset_request.req_602.status=Approved | asset.LT-HP-006.status=Assigned | asset.PH-IP-006.status=Assigned | checklist_item.check_601.status=Completed | checklist_item.check_602.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_601.status=Approved | access_check.access_602.status=Approved | email.email_601.labels=label_OnboardingReady | log.ONBOARDING_COMPLETED.message=Candidate cand_6 onboarding completed | candidate.cand_6.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_014",
        "instruction": "For candidate cand_2, substitute temporary laptop LT-Temp02 with permanent laptop LT-002C, finish security induction checklist items check_221 and check_222, verify background_verification.pdf, update access check access_207 to 'Approved', add a new access check access_208, apply email label 'SecurityClearance' to email_221, record all updates, and revise candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-Temp02"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002C",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_221",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_222",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/background_verification.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_207",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_208",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_221",
                    "label_id": "label_SecurityClearance"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "SECURITY_CHECK",
                    "message": "Security induction completed for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATE",
                    "message": "Access updated for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "security_clearance": "Granted"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-Temp02.status=Available | asset.LT-002C.status=Assigned | checklist_item.check_221.status=Completed | checklist_item.check_222.status=Completed | onboarding_files.background_verification.pdf.status=Verified | access_check.access_207.status=Approved | access_check.access_208.status=Pending | email.email_221.labels=label_SecurityClearance | log.SECURITY_CHECK.message=Security induction completed for cand_2 | log.ACCESS_UPDATE.message=Access updated for cand_2 | candidate.cand_2.security_clearance=Granted"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_015",
        "instruction": "For candidate cand_4, distribute mobile device MB-004X, relinquish the old tablet TB-004Z, finalize orientation checklist items check_410 and check_411, confirm the signed_policy.pdf, attach the team_structure.pdf, tag email_410 with the 'Orientation' label, record the changes, and refresh the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "TB-004Z"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "MB-004X",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_410",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_411",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/signed_policy.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_9",
                        "file_name": "team_structure.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_410",
                    "label_id": "label_Orientation"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "DEVICE_UPDATE",
                    "message": "Mobile assigned to cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Orientation tasks done for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "FILE_VERIFIED",
                    "message": "Signed policy verified for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "orientation_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.TB-004Z.status=Available | asset.MB-004X.status=Assigned | checklist_item.check_410.status=Completed | checklist_item.check_411.status=Completed | onboarding_files.signed_policy.pdf.status=Verified | attachment.team_structure.pdf.added=True | email.email_410.labels=label_Orientation | log.DEVICE_UPDATE.message=Mobile assigned to cand_4 | log.CHECKLIST_COMPLETED.message=Orientation tasks done for cand_4 | log.FILE_VERIFIED.message=Signed policy verified for cand_4 | candidate.cand_4.orientation_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_016",
        "instruction": "Oversee the entire multi-step onboarding for candidate cand_1: authorize all asset requests, allocate all assets, finalize all checklist items, authorize all access checks, update all onboarding files, apply multiple email labels, and document detailed terminal logs for each step. End state: all assets allocated, onboarding files revised, checklist items finalized, access checks authorized, emails labeled, and candidate status indicates full completion.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-001X"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-001Y",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Closed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_103",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/confidentiality_agreement.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_105",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_106"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_103",
                    "label_id": "label_TrainingUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "New permanent laptop assigned to cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "training_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-001X.status=Available | asset.LT-001Y.status=Assigned | asset_request.req_102.status=Closed | checklist_item.check_103.status=Completed | onboarding_files.confidentiality_agreement.pdf.status=Verified | access_check.access_105.status=Pending | access_check.access_106=Removed | email.email_103.labels=label_TrainingUpdate | log.ASSET_ASSIGNED.message=New permanent laptop assigned to cand_1 | log.ACCESS_UPDATED.message=Access checks updated for cand_1 | candidate.cand_1.training_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_017",
        "instruction": "Handle the comprehensive multi-step onboarding for candidate cand_2: approve every pending asset request, assign all applicable assets, finalize each checklist item, authorize access checks, refresh onboarding files with asset and policy information, utilize suitable email labels, and meticulously log terminal activities throughout the process. Final goal: candidate cand_2 is fully assigned assets, checklist is finalized, access checks are authorized, onboarding files are updated, emails bear appropriate labels, and the candidate's status reads as fully completed.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-002A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_201"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_202"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_206",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_2",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_201",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REASSIGNMENT",
                    "message": "Assets reassigned for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/ID-Proof.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset_request.req_201.status=Completed | asset_request.req_202.status=Completed | access_check.access_201=Removed | access_check.access_202=Removed | access_check.access_206.status=Pending | attachment.Benefits-Guide.pdf.added=True | email.email_201.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_2 | log.ACCESS_UPDATED.message=Access checks updated for cand_2 | onboarding_files.ID-Proof.pdf.status=Verified | candidate.cand_2.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_019",
        "instruction": "Manage the release of the old monitor MON-202A and designate the new monitor MON-202B for candidate cand_2. Finalize checklist check_202, attach NDA-Form.pdf, revoke access check access_202, implement new access check access_204, and apply the 'HR' label to email email_202. Record updates and amend the candidate HR record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "MON-202A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "MON-202B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_12",
                        "file_name": "NDA-Form.pdf"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_202"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_204",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_202",
                    "label_id": "label_HR"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "MONITOR_UPDATED",
                    "message": "Monitor swapped for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "hr_status": "Updated"
                    }
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "email_id": "email_202",
                    "updates": {
                        "status": "Sent"
                    }
                }
            }
        ],
        "outputs": [
                "asset.MON-202A.status=Available | asset.MON-202B.status=Assigned | checklist_item.check_202.status=Completed | attachment.NDA-Form.pdf.added=True | access_check.access_202=Removed | access_check.access_204.status=Pending | email.email_202.labels=label_HR | log.MONITOR_UPDATED.message=Monitor swapped for cand_2 | log.ACCESS_UPDATED.message=Access updated for cand_2 | candidate.cand_2.hr_status=Updated | email.email_202.status=Sent"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_021",
        "instruction": "For candidate cand_4, handle decommissioning of the old phone PH-404A, assign the smartphone PH-404B, remove access check access_404, add access check access_405, attach Orientation-Schedule.pdf, update checklist check_404, apply label 'Orientation' to email email_404, log the activities, and mark candidate orientation complete.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "PH-404A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-404B",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_404"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_405",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_14",
                        "file_name": "Orientation-Schedule.pdf"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_404",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_404",
                    "label_id": "label_Orientation"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "PHONE_UPDATED",
                    "message": "Smartphone assigned to cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "orientation_status": "Completed"
                    }
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "email_id": "email_404",
                    "updates": {
                        "status": "Sent"
                    }
                }
            }
        ],
        "outputs": [
                "asset.PH-404A.status=Available | asset.PH-404B.status=Assigned | access_check.access_404=Removed | access_check.access_405.status=Pending | attachment.Orientation-Schedule.pdf.added=True | checklist_item.check_404.status=Completed | email.email_404.labels=label_Orientation | log.PHONE_UPDATED.message=Smartphone assigned to cand_4 | log.ACCESS_UPDATED.message=Access updated for cand_4 | candidate.cand_4.orientation_status=Completed | email.email_404.status=Sent"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_091",
        "instruction": "Manage the transition for candidate cand_3 by releasing headset HS-003A, allocating headset HS-003B, finalizing asset request req_301, withdrawing access check access_301, instituting new access check access_305, attaching Security-Guidelines.pdf, applying email label 'SecurityDocs' to email email_305, fulfilling checklist item check_305, recording updates for assets and access, and refreshing the candidate record.",
        "actions": [
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_102",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-001B"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-001D",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-001D",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_105",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_106",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_103"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_108",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_welcome_jane",
                        "file_name": "welcome_Jane_Smith.md"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_OnboardingComplete"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Onboarding completed for cand_1",
                    "candidate_id": "cand_1"
                }
            }
        ],
        "outputs": [
                "checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | asset.LT-001B.status=Available | asset.LT-001D.status=Assigned | asset.PH-001D.status=Assigned | asset_request.req_105.status=Completed | asset_request.req_106.status=Completed | access_check.access_103=Removed | access_check.access_108.status=Pending | attachment.welcome_Jane_Smith.md.added=True | email.email_101.labels=label_OnboardingComplete | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_1"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_092",
        "instruction": "Coordinate activities for candidate cand_5 by releasing tablet TB-005A, assigning tablet TB-005B, concluding asset request req_501, removing access check access_501, implementing access check access_506, attaching Training-Plan.pdf, applying email label 'Learning' to email email_506, completing checklist item check_506, documenting updates for assets and access, and revising the candidate record.",
        "actions": [
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_403"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_404"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_407",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_408",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-004D",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-004D",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_407",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_7",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "DEVICE_ASSIGNED",
                    "message": "Devices assigned for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "access_check.access_403=Removed | access_check.access_404=Removed | access_check.access_407.status=Pending | access_check.access_408.status=Pending | asset.LT-004D.status=Assigned | asset.PH-004D.status=Assigned | asset_request.req_407.status=Completed | attachment.Company-Policies.pdf.added=True | onboarding_files.offer_letter.pdf.status=Verified | log.DEVICE_ASSIGNED.message=Devices assigned for cand_4 | log.ACCESS_UPDATED.message=Access updated for cand_4 | candidate.cand_4.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_094",
        "instruction": "For candidate cand_7, designate the laptop LT-007C and phone PH-007C, manage the completion of asset requests req_701 and req_702. Discard old access checks access_701 and access_702, insert new access checks access_703 and access_704, include welcome_Robert_Singh.md, assign the 'OnboardingComplete' label to email email_701, document all modifications, and update the candidate record.",
        "actions": [
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-007C",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-007C",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_701"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_702"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_703",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_704",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_welcome_robert",
                        "file_name": "welcome_Robert_Singh.md"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_OnboardingComplete"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Onboarding completed for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-007C.status=Assigned | asset.PH-007C.status=Assigned | asset_request.req_701.status=Completed | asset_request.req_702.status=Completed | access_check.access_701=Removed | access_check.access_702=Removed | access_check.access_703.status=Pending | access_check.access_704.status=Pending | attachment.welcome_Robert_Singh.md.added=True | email.email_701.labels=label_OnboardingComplete | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_095",
        "instruction": "With respect to candidate cand_6, handle checklist items check_603 and check_604. Release the old laptop LT-006B, assign the new laptop LT-006C and phone PH-006C, and update asset requests req_603 and req_604. Remove the access check access_603, add the access check access_605, attach Benefits-Guide.pdf, log all changes, and update the candidate record.",
        "actions": [
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_603",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_604",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-006B"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-006C",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-006C",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_603",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_604",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_603"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_605",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_8",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "checklist_item.check_603.status=Completed | checklist_item.check_604.status=Completed | asset.LT-006B.status=Available | asset.LT-006C.status=Assigned | asset.PH-006C.status=Assigned | asset_request.req_603.status=Completed | asset_request.req_604.status=Completed | access_check.access_603=Removed | access_check.access_605.status=Pending | attachment.Benefits-Guide.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_096",
        "instruction": "Referring to candidate cand_2, coordinate the release of their old laptop LT-002A and the assignment of a new laptop LT-002B and phone PH-002B. Ensure asset requests req_203 and req_204 are completed. Remove previous access checks access_203 and access_204, and add new access checks access_205 and access_206. Attach the document Company-Policies.pdf, log all updates, and update the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-002A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_203",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_204",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_203"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_204"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_205",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_206",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_3",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REASSIGNED",
                    "message": "Assets reassigned for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset.PH-002B.status=Assigned | asset_request.req_203.status=Completed | asset_request.req_204.status=Completed | access_check.access_203=Removed | access_check.access_204=Removed | access_check.access_205.status=Pending | access_check.access_206.status=Pending | attachment.Company-Policies.pdf.added=True | log.ASSET_REASSIGNED.message=Assets reassigned for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_098",
        "instruction": "Ensure that candidate cand_3 is assigned the retired laptop LT-003B, along with the new laptop LT-003C and phone PH-003C, while asset requests req_303 and req_304 are updated. You need to remove access checks access_303 and access_304, incorporate access checks access_305 and access_306, append offer_letter.pdf, document all changes, and revise the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-003B"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-003C",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-003C",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_303",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_304",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_303"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_304"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_305",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_306",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_offer_letter",
                        "file_name": "offer_letter.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-003B.status=Available | asset.LT-003C.status=Assigned | asset.PH-003C.status=Assigned | asset_request.req_303.status=Completed | asset_request.req_304.status=Completed | access_check.access_303=Removed | access_check.access_304=Removed | access_check.access_305.status=Pending | access_check.access_306.status=Pending | attachment.offer_letter.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_3 | candidate.cand_3.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_099",
        "instruction": "The assignment for candidate cand_7 involves providing laptop LT-007D and phone PH-007D, finalizing asset requests req_705 and req_706, eliminating outdated access checks access_705 and access_706, setting up new access checks access_707 and access_708, appending welcome_Maria_Rodriguez.md, recording all updates, and revising the candidate record.",
        "actions": [
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-007D",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-007D",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_705",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_706",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_705"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_706"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_707",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_708",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_welcome_maria",
                        "file_name": "welcome_Maria_Rodriguez.md"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Onboarding completed for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-007D.status=Assigned | asset.PH-007D.status=Assigned | asset_request.req_705.status=Completed | asset_request.req_706.status=Completed | access_check.access_705=Removed | access_check.access_706=Removed | access_check.access_707.status=Pending | access_check.access_708.status=Pending | attachment.welcome_Maria_Rodriguez.md.added=True | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_100",
        "instruction": "Candidate cand_6 must return the old laptop LT-006C. You are to allocate the new laptop LT-006D and phone PH-006D, finalize asset requests req_607 and req_608, revoke access check access_605, grant access check access_606, include Benefits-Guide.pdf, document all changes, and revise the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-006C"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-006D",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-006D",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_607",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_608",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_605"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_606",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_8",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-006C.status=Available | asset.LT-006D.status=Assigned | asset.PH-006D.status=Assigned | asset_request.req_607.status=Completed | asset_request.req_608.status=Completed | access_check.access_605=Removed | access_check.access_606.status=Pending | attachment.Benefits-Guide.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_6 | log.ACCESS_UPDATED.message=Access updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_303",
        "instruction": "For candidate cand_3, retrieve the old laptop LT-003A, allocate the new laptop LT-003B, address checklist items check_303 and check_304, confirm the onboarding file offer_letter.pdf, assign email label 'AssetUpdate' to email email_303, record all modifications, update the candidate record, and append Company-Policies.pdf.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-003A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-003B",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_303",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_304",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_303",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_RELEASED",
                    "message": "Old assets released for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "New assets assigned for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_3",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-003A.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_303.status=Completed | checklist_item.check_304.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | email.email_303.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_3 | log.ASSET_ASSIGNED.message=New assets assigned for cand_3 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_3 | attachment.Company-Policies.pdf.added=True | candidate.cand_3.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_305",
        "instruction": "Regarding candidate cand_5, handle the release of the old laptop LT-005A, assign the new laptop LT-005B, fulfill asset requests req_501 and req_502, eliminate access checks access_501, introduce new access check access_507, attach Benefits-Guide.pdf, apply the label 'AssetChange' to email email_501, document the changes, update the candidate record, and confirm the onboarding file Driving-License.pdf.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-005A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_501"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_507",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_8",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_501",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/Driving-License.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-005A.status=Available | asset.LT-005B.status=Assigned | asset_request.req_501.status=Completed | asset_request.req_502.status=Completed | access_check.access_501=Removed | access_check.access_507.status=Pending | attachment.Benefits-Guide.pdf.added=True | email.email_501.labels=label_AssetChange | log.ASSET_UPDATED.message=Assets updated for cand_5 | onboarding_files.Driving-License.pdf.status=Verified | candidate.cand_5.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_306",
        "instruction": "Regarding candidate cand_6, manage the release of the old laptop LT-006A, assign the new laptop LT-006B, fulfill asset request req_601, remove access check access_601, introduce new access checks access_603 and access_604, attach Company-Policies.pdf, affix the label 'AssetUpdate' to email email_601, register the changes, update the candidate record, and confirm the onboarding file Passport.pdf.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-006A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-006B",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_601",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_601"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_603",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_604",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_7",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_601",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/Passport.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-006A.status=Available | asset.LT-006B.status=Assigned | asset_request.req_601.status=Completed | access_check.access_601=Removed | access_check.access_603.status=Pending | access_check.access_604.status=Pending | attachment.Company-Policies.pdf.added=True | email.email_601.labels=label_AssetUpdate | log.ASSET_UPDATED.message=Assets updated for cand_6 | onboarding_files.Passport.pdf.status=Verified | candidate.cand_6.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_307",
        "instruction": "Handle candidate cand_7 by releasing the old laptop LT-007A, assigning the new laptop LT-007B, completing checklist items check_701 and check_702, removing access check access_701, adding new access check access_705, attaching Benefits-Guide.pdf, applying the label 'AssetUpdate' to email email_701, logging the changes, updating the candidate record, and verifying the onboarding file ID-Proof.pdf.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-007A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-007B",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_701"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_705",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_8",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/ID-Proof.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-007A.status=Available | asset.LT-007B.status=Assigned | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | access_check.access_701=Removed | access_check.access_705.status=Pending | attachment.Benefits-Guide.pdf.added=True | email.email_701.labels=label_AssetUpdate | log.ASSET_UPDATED.message=Assets updated for cand_7 | onboarding_files.ID-Proof.pdf.status=Verified | candidate.cand_7.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_201",
        "instruction": "Coordinate tasks for candidate cand_1 by releasing the old asset LT-001A, assigning the new asset LT-001B, updating asset request req_101 to Completed, marking checklist items check_101 and check_102 as Completed, verifying the onboarding file offer_letter.pdf, applying the label 'OnboardingUpdate' to email email_101, removing access check access_101, adding access check access_105, attaching Handbook.pdf, logging the updates, and marking the candidate onboarding as Completed.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-001A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-001B",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_102",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_OnboardingUpdate"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_101"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_105",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_2",
                        "file_name": "Handbook.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "onboarding_progress": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-001A.status=Available | asset.LT-001B.status=Assigned | asset_request.req_101.status=Completed | checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | email.email_101.labels=label_OnboardingUpdate | access_check.access_101=Removed | access_check.access_105.status=Pending | attachment.Handbook.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_1 | candidate.cand_1.onboarding_progress=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_203",
        "instruction": "Regarding candidate cand_3, release asset LT-003A, assign LT-003B, update checklist items check_301 and check_302, verify tax_form.pdf, attach label 'Finance' to email email_303, revoke access check access_303, grant access check access_304, detach Benefits.pdf, attach Payroll-Form.pdf, document changes, and refresh payroll_status.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-003A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-003B",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_302",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/tax_form.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_303",
                    "label_id": "label_Finance"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_303"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_304",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "RemoveAttachment",
                "arguments": {
                    "attachment_id": "attach_5"
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_6",
                        "file_name": "Payroll-Form.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "FINANCE_UPDATE",
                    "message": "Payroll forms updated for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "payroll_status": "Active"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-003A.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | onboarding_files.tax_form.pdf.status=Verified | email.email_303.labels=label_Finance | access_check.access_303=Removed | access_check.access_304.status=Pending | attachment.Benefits.pdf.removed=True | attachment.Payroll-Form.pdf.added=True | log.FINANCE_UPDATE.message=Payroll forms updated for cand_3 | candidate.cand_3.payroll_status=Active"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_204",
        "instruction": "In reference to candidate cand_2, release laptop LT-002A, assign laptop LT-002B, update asset request req_201, finalize checklist items check_201 and check_202, remove onboarding file id_proof.pdf, include onboarding file nda.pdf, label email email_201 with 'OnboardingComplete', record all updates, and designate candidate record as fully onboarded.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-002A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveOnboardingFile",
                "arguments": {
                    "file_path": "files/id_proof.pdf"
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/nda.pdf",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_201",
                    "label_id": "label_OnboardingComplete"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "status": "Onboarded"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset_request.req_201.status=Completed | checklist_item.check_201.status=Completed | checklist_item.check_202.status=Completed | onboarding_files.id_proof.pdf=Removed | onboarding_files.nda.pdf.status=Pending | email.email_201.labels=label_OnboardingComplete | log.ASSET_UPDATED.message=Assets updated for cand_2 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_2 | candidate.cand_2.status=Onboarded"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_205",
        "instruction": "For candidate cand_5, handle the release of asset LT-005A, allocate asset LT-005B, modify asset request req_501, eliminate access verification access_501, incorporate new access verification access_502, finalize checklist check_502, refresh email email_501 content, apply the label 'AccessUpdate' to the same email, document the changes, and revise the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-005A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_501"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_502",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_502",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_501",
                    "updates": {
                        "subject": "Access Updated"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_501",
                    "label_id": "label_AccessUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist item completed for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "access_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-005A.status=Available | asset.LT-005B.status=Assigned | asset_request.req_501.status=Completed | access_check.access_501=Removed | access_check.access_502.status=Pending | checklist_item.check_502.status=Completed | email.email_501.subject=Access Updated | email.email_501.labels=label_AccessUpdate | log.ACCESS_UPDATED.message=Access updated for cand_5 | log.CHECKLIST_COMPLETED.message=Checklist item completed for cand_5 | candidate.cand_5.access_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_206",
        "instruction": "For candidate cand_7, manage the release of asset LT-007A, allocate asset LT-007B, finalize checklist items check_701 and check_702, update the onboarding file tax_form.pdf, attach Employee-Handbook.pdf, refresh email email_701, apply the label 'PolicyUpdate', document changes, and change the candidate onboarding phase to 'Finalized'.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-007A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-007B",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/tax_form.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_7",
                        "file_name": "Employee-Handbook.pdf"
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_701",
                    "updates": {
                        "subject": "Onboarding Policy Updated"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_PolicyUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_UPDATED",
                    "message": "Onboarding finalized for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "All checklist items completed for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "phase": "Finalized"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-007A.status=Available | asset.LT-007B.status=Assigned | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.tax_form.pdf.status=Verified | attachment.Employee-Handbook.pdf.added=True | email.email_701.subject=Onboarding Policy Updated | email.email_701.labels=label_PolicyUpdate | log.ONBOARDING_UPDATED.message=Onboarding finalized for cand_7 | log.CHECKLIST_COMPLETED.message=All checklist items completed for cand_7 | candidate.cand_7.phase=Finalized"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_207",
        "instruction": "Handle candidate cand_1 by releasing asset LT-001A, assigning LT-001C, finalizing checklist items check_101 and check_102, eliminating access check access_101, including access check access_103, revising onboarding file offer_letter.pdf, incorporating file signed_contract.pdf, amending email email_101 with subject 'Final Contract Signed', applying label 'ContractComplete', documenting the updates, and designating candidate as confirmed.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-001A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-001C",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_102",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_101"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_103",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/signed_contract.pdf",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_101",
                    "updates": {
                        "subject": "Final Contract Signed"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_ContractComplete"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CANDIDATE_CONFIRMED",
                    "message": "cand_1 fully confirmed",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "status": "Confirmed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-001A.status=Available | asset.LT-001C.status=Assigned | checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | access_check.access_101=Removed | access_check.access_103.status=Pending | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.signed_contract.pdf.status=Pending | email.email_101.subject=Final Contract Signed | email.email_101.labels=label_ContractComplete | log.CANDIDATE_CONFIRMED.message=cand_1 fully confirmed | candidate.cand_1.status=Confirmed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_208",
        "instruction": "Coordinate candidate cand_3 by releasing asset LT-003A, assigning LT-003B, updating asset request req_301, completing checklist check_301, modifying onboarding file id_proof.pdf, adding onboarding file medical_form.pdf, altering email email_301 with subject 'Onboarding Medical Cleared', applying label 'MedicalUpdate', removing attachment attach_3, adding attachment Training-Schedule.pdf, recording updates, and setting candidate stage to 'ReadyForTraining'.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-003A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-003B",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_proof.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/medical_form.pdf",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_301",
                    "updates": {
                        "subject": "Onboarding Medical Cleared"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_301",
                    "label_id": "label_MedicalUpdate"
                },
            },
            {
                "name": "RemoveAttachment",
                "arguments": {
                    "attachment_id": "attach_3"
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_3_new",
                        "file_name": "Training-Schedule.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_READY",
                    "message": "Medical cleared and training scheduled for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "stage": "ReadyForTraining"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-003A.status=Available | asset.LT-003B.status=Assigned | asset_request.req_301.status=Completed | checklist_item.check_301.status=Completed | onboarding_files.id_proof.pdf.status=Verified | onboarding_files.medical_form.pdf.status=Pending | email.email_301.subject=Onboarding Medical Cleared | email.email_301.labels=label_MedicalUpdate | attachment.attach_3=Removed | attachment.Training-Schedule.pdf.added=True | log.ONBOARDING_READY.message=Medical cleared and training scheduled for cand_3 | candidate.cand_3.stage=ReadyForTraining"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_209",
        "instruction": "Handle the tasks for candidate cand_4 by releasing LT-004A, assigning LT-004B, updating request req_401, fulfilling checklist items check_401 and check_402, adding access check access_404, removing the onboarding file old_resume.pdf, including the new file updated_resume.pdf, updating email email_401 with the subject 'Resume Verified', applying the label 'ResumeCheck', logging the actions, and setting the candidate profile to 'Verified'.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-004A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-004B",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_401",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_401",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_402",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_404",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "RemoveOnboardingFile",
                "arguments": {
                    "file_path": "files/old_resume.pdf"
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/updated_resume.pdf",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_401",
                    "updates": {
                        "subject": "Resume Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_401",
                    "label_id": "label_ResumeCheck"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "PROFILE_VERIFIED",
                    "message": "Resume verified for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "profile_status": "Verified"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-004A.status=Available | asset.LT-004B.status=Assigned | asset_request.req_401.status=Completed | checklist_item.check_401.status=Completed | checklist_item.check_402.status=Completed | access_check.access_404.status=Pending | onboarding_files.old_resume.pdf=Removed | onboarding_files.updated_resume.pdf.status=Pending | email.email_401.subject=Resume Verified | email.email_401.labels=label_ResumeCheck | log.PROFILE_VERIFIED.message=Resume verified for cand_4 | candidate.cand_4.profile_status=Verified"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_210",
        "instruction": "Coordinate the steps for candidate cand_6 by releasing LT-006A, assigning LT-006B, updating request req_601, completing checklist item check_601, adding access check access_606, updating the onboarding file training_doc.pdf, adding the file signed_training.pdf, updating email email_601 with the subject 'Training Completed', applying the label 'TrainingDone', logging the actions, and marking the candidate status as 'Trained'.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-006A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-006B",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_601",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_601",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_606",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/training_doc.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/signed_training.pdf",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_601",
                    "updates": {
                        "subject": "Training Completed"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_601",
                    "label_id": "label_TrainingDone"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "TRAINING_COMPLETED",
                    "message": "cand_6 training completed",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "status": "Trained"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-006A.status=Available | asset.LT-006B.status=Assigned | asset_request.req_601.status=Completed | checklist_item.check_601.status=Completed | access_check.access_606.status=Pending | onboarding_files.training_doc.pdf.status=Verified | onboarding_files.signed_training.pdf.status=Pending | email.email_601.subject=Training Completed | email.email_601.labels=label_TrainingDone | log.TRAINING_COMPLETED.message=cand_6 training completed | candidate.cand_6.status=Trained"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_211",
        "instruction": "Handle the release of LT-002B and assign LT-002C for candidate cand_2. Update asset request req_202, finalize checklist items check_203 and check_204, insert access verification access_205, revise onboarding document nda.pdf, append attachment Code-Of-Conduct.pdf, amend email email_202 including the subject 'Code of Conduct Signed', apply the label 'PolicySigned', record updates, and alter the candidate phase to 'ActiveEmployee'.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-002B"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002C",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_203",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_204",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_205",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/nda.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_2_new",
                        "file_name": "Code-Of-Conduct.pdf"
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_202",
                    "updates": {
                        "subject": "Code of Conduct Signed"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_202",
                    "label_id": "label_PolicySigned"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "POLICY_ACCEPTED",
                    "message": "Code of conduct signed for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "phase": "ActiveEmployee"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002B.status=Available | asset.LT-002C.status=Assigned | asset_request.req_202.status=Completed | checklist_item.check_203.status=Completed | checklist_item.check_204.status=Completed | access_check.access_205.status=Pending | onboarding_files.nda.pdf.status=Verified | attachment.Code-Of-Conduct.pdf.added=True | email.email_202.subject=Code of Conduct Signed | email.email_202.labels=label_PolicySigned | log.POLICY_ACCEPTED.message=Code of conduct signed for cand_2 | candidate.cand_2.phase=ActiveEmployee"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_086",
        "instruction": "Coordinate the release of old laptop LT-002A and the assignment of new laptop LT-002B for candidate cand_2. Fulfill asset request req_202, remove access verification access_202, incorporate new access check access_205, attach Code-of-Conduct.pdf, assign the email label 'PolicyUpdate' to email email_205, finalize checklist item check_205, document updates for both assets and access, and revise the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-002A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_202"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_205",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_11",
                        "file_name": "Code-of-Conduct.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_205",
                    "label_id": "label_PolicyUpdate"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_205",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Laptop updated for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access changes applied for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset_request.req_202.status=Completed | access_check.access_202=Removed | access_check.access_205.status=Pending | attachment.Code-of-Conduct.pdf.added=True | email.email_205.labels=label_PolicyUpdate | checklist_item.check_205.status=Completed | log.ASSET_UPDATED.message=Laptop updated for cand_2 | log.ACCESS_UPDATED.message=Access changes applied for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_087",
        "instruction": "For candidate cand_1, handle the release of the old laptop LT-001A, assign laptop LT-001B, finalize asset request req_101, remove access check access_101, add new access check access_103, attach Employee-Handbook.pdf, apply email label 'OnboardingDocs' to email email_103, fulfill checklist item check_103, log updates for assets and access, and update the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-001A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-001B",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_101"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_103",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_12",
                        "file_name": "Employee-Handbook.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_103",
                    "label_id": "label_OnboardingDocs"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_103",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Laptop updated for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-001A.status=Available | asset.LT-001B.status=Assigned | asset_request.req_101.status=Completed | access_check.access_101=Removed | access_check.access_103.status=Pending | attachment.Employee-Handbook.pdf.added=True | email.email_103.labels=label_OnboardingDocs | checklist_item.check_103.status=Completed | log.ASSET_UPDATED.message=Laptop updated for cand_1 | log.ACCESS_UPDATED.message=Access updated for cand_1 | candidate.cand_1.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_088",
        "instruction": "For candidate cand_4, manage the release of monitor MN-004A, assign monitor MN-004B, finalize asset request req_401, eliminate access check access_401, add access check access_402, attach Health-Safety.pdf, apply email label 'HealthPolicy' to email email_402, accomplish checklist item check_402, log changes for assets and access, and update the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "MN-004A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "MN-004B",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_401",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_401"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_402",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_13",
                        "file_name": "Health-Safety.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_402",
                    "label_id": "label_HealthPolicy"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_402",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Monitor updated for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.MN-004A.status=Available | asset.MN-004B.status=Assigned | asset_request.req_401.status=Completed | access_check.access_401=Removed | access_check.access_402.status=Pending | attachment.Health-Safety.pdf.added=True | email.email_402.labels=label_HealthPolicy | checklist_item.check_402.status=Completed | log.ASSET_UPDATED.message=Monitor updated for cand_4 | log.ACCESS_UPDATED.message=Access updated for cand_4 | candidate.cand_4.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_089",
        "instruction": "For candidate cand_6, handle the release of phone PH-006A, assign phone PH-006B, finalize asset request req_601, remove access check access_601, add access check access_603, attach Compliance-Report.pdf, apply the email label 'Compliance' to email email_603, complete checklist item check_603, record changes for assets and access, and update the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "PH-006A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-006B",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_601",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_601"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_603",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_14",
                        "file_name": "Compliance-Report.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_603",
                    "label_id": "label_Compliance"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_603",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Phone updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.PH-006A.status=Available | asset.PH-006B.status=Assigned | asset_request.req_601.status=Completed | access_check.access_601=Removed | access_check.access_603.status=Pending | attachment.Compliance-Report.pdf.added=True | email.email_603.labels=label_Compliance | checklist_item.check_603.status=Completed | log.ASSET_UPDATED.message=Phone updated for cand_6 | log.ACCESS_UPDATED.message=Access updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_090",
        "instruction": "For candidate cand_2, coordinate the release of desktop DT-002A, assign desktop DT-002B, finalize asset request req_201, remove access check access_201, add new access check access_204, attach Payroll-Guide.pdf, apply the email label 'FinanceDocs' to email email_204, complete checklist item check_204, document changes for assets and access, and update the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "DT-002A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "DT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_201"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_204",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_15",
                        "file_name": "Payroll-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_204",
                    "label_id": "label_FinanceDocs"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_204",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Desktop updated for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.DT-002A.status=Available | asset.DT-002B.status=Assigned | asset_request.req_201.status=Completed | access_check.access_201=Removed | access_check.access_204.status=Pending | attachment.Payroll-Guide.pdf.added=True | email.email_204.labels=label_FinanceDocs | checklist_item.check_204.status=Completed | log.ASSET_UPDATED.message=Desktop updated for cand_2 | log.ACCESS_UPDATED.message=Access updated for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_091",
        "instruction": "Manage the transition for candidate cand_3 by releasing headset HS-003A, allocating headset HS-003B, finalizing asset request req_301, withdrawing access check access_301, instituting new access check access_305, attaching Security-Guidelines.pdf, applying email label 'SecurityDocs' to email email_305, fulfilling checklist item check_305, recording updates for assets and access, and refreshing the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "HS-003A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "HS-003B",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_301"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_305",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_16",
                        "file_name": "Security-Guidelines.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_305",
                    "label_id": "label_SecurityDocs"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_305",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Headset updated for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.HS-003A.status=Available | asset.HS-003B.status=Assigned | asset_request.req_301.status=Completed | access_check.access_301=Removed | access_check.access_305.status=Pending | attachment.Security-Guidelines.pdf.added=True | email.email_305.labels=label_SecurityDocs | checklist_item.check_305.status=Completed | log.ASSET_UPDATED.message=Headset updated for cand_3 | log.ACCESS_UPDATED.message=Access updated for cand_3 | candidate.cand_3.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_092",
        "instruction": "Coordinate activities for candidate cand_5 by releasing tablet TB-005A, assigning tablet TB-005B, concluding asset request req_501, removing access check access_501, implementing access check access_506, attaching Training-Plan.pdf, applying email label 'Learning' to email email_506, completing checklist item check_506, documenting updates for assets and access, and revising the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "TB-005A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "TB-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_501"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_506",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_17",
                        "file_name": "Training-Plan.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_506",
                    "label_id": "label_Learning"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_506",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Tablet updated for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.TB-005A.status=Available | asset.TB-005B.status=Assigned | asset_request.req_501.status=Completed | access_check.access_501=Removed | access_check.access_506.status=Pending | attachment.Training-Plan.pdf.added=True | email.email_506.labels=label_Learning | checklist_item.check_506.status=Completed | log.ASSET_UPDATED.message=Tablet updated for cand_5 | log.ACCESS_UPDATED.message=Access updated for cand_5 | candidate.cand_5.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_093",
        "instruction": "For candidate cand_7, handle the release of docking station DS-007A, assign docking station DS-007B, carry out asset request req_701, eliminate access check access_701, incorporate new access check access_707, attach Onboarding-Schedule.pdf, apply the email label 'Onboarding' to email email_707, complete the checklist item check_707, document changes for assets and access, and refresh the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "DS-007A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "DS-007B",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_701"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_707",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_18",
                        "file_name": "Onboarding-Schedule.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_707",
                    "label_id": "label_Onboarding"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_707",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Docking station updated for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access updated for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.DS-007A.status=Available | asset.DS-007B.status=Assigned | asset_request.req_701.status=Completed | access_check.access_701=Removed | access_check.access_707.status=Pending | attachment.Onboarding-Schedule.pdf.added=True | email.email_707.labels=label_Onboarding | checklist_item.check_707.status=Completed | log.ASSET_UPDATED.message=Docking station updated for cand_7 | log.ACCESS_UPDATED.message=Access updated for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_081",
        "instruction": "For candidate cand_1, manage the release of old laptop LT-001A, allocate new laptop LT-001B, fulfill asset requests req_101 and req_102, delete access check access_101, introduce new access check access_103, attach Benefits-Guide.pdf, document changes, and revise the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-001A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-001B",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_101"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_103",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_2",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-001A.status=Available | asset.LT-001B.status=Assigned | asset_request.req_101.status=Completed | asset_request.req_102.status=Completed | access_check.access_101=Removed | access_check.access_103.status=Pending | attachment.Benefits-Guide.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_1 | log.ACCESS_UPDATED.message=Access checks updated for cand_1 | candidate.cand_1.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_082",
        "instruction": "For candidate cand_4, handle the release of the old laptop LT-004A, allocate the new laptop LT-004B and phone PH-004, finalize asset request req_401, eliminate access check access_401, incorporate new access check access_403, include Company-Policies.pdf, record all modifications, and refresh the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-004A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-004B",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_401",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_401"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_403",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_7",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-004A.status=Available | asset.LT-004B.status=Assigned | asset.PH-004.status=Assigned | asset_request.req_401.status=Completed | access_check.access_401=Removed | access_check.access_403.status=Pending | attachment.Company-Policies.pdf.added=True | log.ASSET_UPDATED.message=Assets updated for cand_4 | log.ACCESS_UPDATED.message=Access checks updated for cand_4 | candidate.cand_4.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_083",
        "instruction": "For candidate cand_6, handle the release of the old laptop LT-006A, allocate the new laptop LT-006B, finalize asset request req_601, eliminate access check access_601, incorporate new access check access_603, include Benefits-Guide.pdf, apply email label 'AssetUpdate' to email email_603, accomplish checklist item check_603, record changes, and refresh the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-006A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-006B",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_601",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_601"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_603",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_8",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_603",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_603",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-006A.status=Available | asset.LT-006B.status=Assigned | asset_request.req_601.status=Completed | access_check.access_601=Removed | access_check.access_603.status=Pending | attachment.Benefits-Guide.pdf.added=True | email.email_603.labels=label_AssetUpdate | checklist_item.check_603.status=Completed | log.ASSET_UPDATED.message=Assets updated for cand_6 | log.ACCESS_UPDATED.message=Access checks updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_071",
        "instruction": "Handle the reassignment of assets for candidate cand_6: release the old laptop LT-006, allocate the new laptop LT-006B and phone PH-006B, update asset requests req_601 and req_602 with the status 'Completed', remove access checks access_601 and access_602, implement new access checks access_603 and access_604, attach Company-Policies.pdf and Benefits-Guide.pdf, apply the label 'AssetChange' to email email_601, ensure all changes are logged, and mark the candidate record as updated.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-006"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-006B",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-006B",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_601",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_602",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_601"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_602"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_603",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_604",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_1",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_2",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_601",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REASSIGNMENT",
                    "message": "Assets reassigned for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-006.status=Available | asset.LT-006B.status=Assigned | asset.PH-006B.status=Assigned | asset_request.req_601.status=Completed | asset_request.req_602.status=Completed | access_check.access_601=Removed | access_check.access_602=Removed | access_check.access_603.status=Pending | access_check.access_604.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_601.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_6 | log.ACCESS_UPDATED.message=Access checks updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_072",
        "instruction": "Coordinate the assignment for candidate cand_7 with laptop LT-007 and phone PH-007, approve the asset requests req_701 and req_702, complete the checklist items check_701 and check_702, confirm the onboarding files welcome.pdf and id_scan.pdf are verified, apply the email label 'Ready' to email email_701, ensure all changes are logged, and mark the candidate record as updated.",
        "actions": [
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_701",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_702",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_Ready"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Onboarding completed for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-007.status=Assigned | asset.PH-007.status=Assigned | asset_request.req_701.status=Approved | asset_request.req_702.status=Approved | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.welcome.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | email.email_701.labels=label_Ready | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_7 | candidate.cand_7.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_073",
        "instruction": "For candidate cand_3, handle the release of the old laptop LT-003A, assign the new laptop LT-003B, finish checklist items check_303 and check_304, confirm the onboarding file offer_letter.pdf, attach Company-Policies.pdf, use the email label 'AssetUpdate' for email email_303, document all modifications, and amend the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-003A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-003B",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_303",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_304",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_1",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_303",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_RELEASED",
                    "message": "Old assets released for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "New assets assigned for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-003A.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_303.status=Completed | checklist_item.check_304.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | attachment.Company-Policies.pdf.added=True | email.email_303.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_3 | log.ASSET_ASSIGNED.message=New assets assigned for cand_3 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_3 | candidate.cand_3.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_041",
        "instruction": "Authorize laptop asset requests for candidates Emma Thompson (cand_2) and William Davis (cand_3), allocate the correct laptops, and revise onboarding files to indicate laptop assignment. Final status: asset requests are 'Approved'; laptops LT-DELL-003 and LT-DELL-002 are allocated; onboarding files reflect laptop_assigned=True; terminal logs record assignment and approval processes.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_Jane_Laptop",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_Peter_Laptop",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-003",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Jane_Smith/asset_request.json",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Peter_Jones/asset_request.json",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_REQUEST_APPROVED",
                    "message": "Laptop requests approved and assigned",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_REQUEST_APPROVED",
                    "message": "Laptop requests approved and assigned",
                    "candidate_id": "cand_3"
                }
            }
        ],
        "outputs": [
                "asset_request.req_Jane_Laptop.status=Approved | asset_request.req_Peter_Laptop.status=Approved | asset.LT-DELL-003.status=Assigned | asset.LT-DELL-002.status=Assigned | onboarding_files.Jane_Smith.laptop_assigned=True | onboarding_files.Peter_Jones.laptop_assigned=True | log.LAPTOP_REQUEST_APPROVED.message=Laptop requests approved and assigned"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_075",
        "instruction": "Handle the reassignment of candidate cand_2's assets: release laptop LT-002A, assign new laptop LT-002B and phone PH-002B, complete checklist items check_203 and check_204, verify onboarding file Company-Policies.pdf, apply email label 'AssetUpdate' to email email_203, document all steps, and refresh the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-002A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_203",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_204",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/Company-Policies.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_203",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_RELEASED",
                    "message": "Old assets released for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "New assets assigned for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset.PH-002B.status=Assigned | checklist_item.check_203.status=Completed | checklist_item.check_204.status=Completed | onboarding_files.Company-Policies.pdf.status=Verified | email.email_203.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_2 | log.ASSET_ASSIGNED.message=New assets assigned for cand_2 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_077",
        "instruction": "Coordinate the asset reassignment for candidate cand_4: release laptop LT-004A, assign new laptop LT-004B and phone PH-004B, complete checklist item check_404, verify onboarding file offer_letter.pdf, add attachment Company-Policies.pdf, apply email label 'AssetUpdate' to email email_404, record all actions, and refresh the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-004A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-004B",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-004B",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_404",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_1",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_404",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist item completed for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABEL_APPLIED",
                    "message": "Email labeled for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-004A.status=Available | asset.LT-004B.status=Assigned | asset.PH-004B.status=Assigned | checklist_item.check_404.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | attachment.Company-Policies.pdf.added=True | email.email_404.labels=label_AssetUpdate | log.ASSET_UPDATED.message=Assets updated for cand_4 | log.CHECKLIST_COMPLETED.message=Checklist item completed for cand_4 | log.EMAIL_LABEL_APPLIED.message=Email labeled for cand_4 | candidate.cand_4.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_078",
        "instruction": "Regarding candidate cand_5, allocate laptop LT-005B and phone PH-005B, finish checklist tasks check_505 and check_506, confirm onboarding documents resume.pdf and security_form.pdf, include attachment Company-Policies.pdf, place email label 'Welcome' on email email_505, record all modifications, and revise candidate record.",
        "actions": [
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_505",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_506",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/resume.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/security_form.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_1",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_505",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Onboarding completed for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-005B.status=Assigned | asset.PH-005B.status=Assigned | checklist_item.check_505.status=Completed | checklist_item.check_506.status=Completed | onboarding_files.resume.pdf.status=Verified | onboarding_files.security_form.pdf.status=Verified | attachment.Company-Policies.pdf.added=True | email.email_505.labels=label_Welcome | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_5 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_5 | candidate.cand_5.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_079",
        "instruction": "As for candidate cand_2, decommission old laptop LT-002A, allocate new laptop LT-002B and phone PH-002B, complete checklist items check_202 and check_203, confirm onboarding document offer_letter.pdf, attach Company-Policies.pdf, assign email label 'AssetChange' to email email_202, document all operations, and amend candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-002A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_203",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_1",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_202",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_UPDATED",
                    "message": "Assets updated for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset.PH-002B.status=Assigned | checklist_item.check_202.status=Completed | checklist_item.check_203.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | attachment.Company-Policies.pdf.added=True | email.email_202.labels=label_AssetChange | log.ASSET_UPDATED.message=Assets updated for cand_2 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_005",
        "instruction": "Handle asset reassignment for candidate cand_5: release old laptop LT-005, assign new laptop LT-005B, ensure completion of checklist item check_501, verify the onboarding file id_scan.pdf, apply email label 'AssetUpdate' to email email_501, log all updates, and update the candidate record.",
        "actions": [
            {
                "name": "UpdateEmailLabel",
                "arguments": {
                    "label_id": "label_2",
                    "updates": {
                        "priority": "Urgent"
                    }
                },
            },
            {
                "name": "UpdateEmailLabel",
                "arguments": {
                    "label_id": "label_3",
                    "updates": {
                        "priority": "High"
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_101",
                    "updates": {
                        "processed": true
                    }
                },
            },
            {
                "name": "UpdateEmail",
                "arguments": {
                    "email_id": "email_102",
                    "updates": {
                        "processed": true
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_2"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_102",
                    "label_id": "label_3"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "email_label_applied": true
                    }
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "candidate_id": "cand_6",
                    "file_name": "Email Confirmation",
                    "file_path": "/onboarding/email_confirmation.pdf"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MAC-001",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAsset",
                "arguments": {
                    "asset_tag": "LT-MAC-001",
                    "updates": {
                        "status": "Assigned"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABEL_UPDATED",
                    "message": "Email labels 'Urgent' and 'High' applied for cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_FILE_UPDATED",
                    "message": "Onboarding files updated for cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop assigned to cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "onboarding_status": "Ready"
                    }
                }
            }
        ],
        "outputs": [
                "email_label.label_2.priority=Urgent | email_label.label_3.priority=High | email.email_101.processed=True | email.email_102.processed=True | onboarding_files.email_label_applied=True | onboarding_files.Email Confirmation.file_path=/onboarding/email_confirmation.pdf | asset.LT-MAC-001.status=Assigned | log.EMAIL_LABEL_UPDATED.message=Email labels 'Urgent' and 'High' applied for cand_6 | log.ONBOARDING_FILE_UPDATED.message=Onboarding files updated for cand_6 | log.ASSET_ASSIGNED.message=Laptop assigned to cand_6 | candidate.cand_6.onboarding_status=Ready"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_006",
        "instruction": "Manage the onboarding of candidate cand_7 through approval of asset requests req_501, req_502, assign a laptop LT-DELL-010, a phone PH-SAMSUNG-005, and provide accessories ACC-MOUSE-001. Checklist tasks check_701, check_702 are fulfilled, onboarding documents welcome_guide.pdf and id_scan.pdf are confirmed, and access validations access_901, access_902 are sanctioned. An email email_701 has the label 'Welcome'. Final state: assets are assigned and approved; documents are verified; checklist and access validations completed; terminal logs are available; candidate's onboarding status is revised.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-010",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-SAMSUNG-005",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-001",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_901",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_902",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop, phone, and accessory assigned to cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_501 and req_502 approved"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed for cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved for cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABEL_APPLIED",
                    "message": "Email labeled 'Welcome' for cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.LT-DELL-010.status=Assigned | asset.PH-SAMSUNG-005.status=Assigned | asset.ACC-MOUSE-001.status=Assigned | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.welcome_guide.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_Welcome | log.ASSET_ASSIGNED.message=Laptop, phone, and accessory assigned to cand_7 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_501 and req_502 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_7 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_7 | log.EMAIL_LABEL_APPLIED.message=Email labeled 'Welcome' for cand_7 | candidate.cand_7.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_007",
        "instruction": "Authorize the laptop and phone requests for candidate cand_7, allocate the assets, and make sure the onboarding documents indicate the asset allocation. Desired outcome: asset requests are indicated as 'Approved'; assets PH-LAPTOP-007 and PH-IPHONE-007 are allocated to cand_7; onboarding documents display phone_assigned=True and laptop_assigned=True; terminal logs record the assignment and authorization activities.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_701",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_702",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/cand_7_onboarding.json",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_701 and req_702 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "PHONE_ASSIGNED",
                    "message": "PH-IPHONE-007 assigned",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "PH-LAPTOP-007 assigned",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_701.status=Approved | asset_request.req_702.status=Approved | asset.PH-LAPTOP-007.status=Assigned | asset.PH-IPHONE-007.status=Assigned | onboarding_files.cand_7.laptop_assigned=True | onboarding_files.cand_7.phone_assigned=True | log.ASSET_REQUEST_APPROVED.message=Asset requests req_701 and req_702 approved | log.PHONE_ASSIGNED.message=PH-IPHONE-007 assigned | log.LAPTOP_ASSIGNED.message=PH-LAPTOP-007 assigned | candidate.cand_7.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_008",
        "instruction": "Authorize the laptop and phone requests for candidate cand_7, allocate the assets, revise onboarding documents for asset allocation, finalize checklist tasks, sanction access verifications, and categorize emails. Desired outcome: asset requests are marked 'Approved'; assets PH-LAPTOP-010, PH-IPHONE-005, and ACC-MOUSE-001 are assigned; checklist tasks marked 'Completed'; access verifications approved; onboarding documents reflect assigned assets; the email is categorized as 'Welcome'; terminal logs record all operations.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-010",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-005",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-001",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true,
                        "accessory_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_901",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_902",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_501 and req_502 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSETS_ASSIGNED",
                    "message": "PH-LAPTOP-010, PH-IPHONE-005, and ACC-MOUSE-001 assigned",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items check_701 and check_702 completed",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks access_901 and access_902 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABEL_APPLIED",
                    "message": "Email email_701 labeled Welcome",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.PH-LAPTOP-010.status=Assigned | asset.PH-IPHONE-005.status=Assigned | asset.ACC-MOUSE-001.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | onboarding_files.welcome_guide.phone_assigned=True | onboarding_files.welcome_guide.accessory_assigned=True | onboarding_files.id_scan.status=Verified | checklist.check_701.status=Completed | checklist.check_702.status=Completed | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_Welcome | candidate.cand_7.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_009",
        "instruction": "Authorize candidate cand_7's request for a laptop, allocate the asset, revise onboarding files to reflect the laptop assignment, and log the records. End state: laptop request authorized; laptop PH-LAPTOP-010 allocated; onboarding files indicate laptop_assigned=True; terminal logs document assignment and authorization.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-010",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset request req_501 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "PH-LAPTOP-010 assigned",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "LaptopAssigned"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_501.status=Approved | asset.PH-LAPTOP-010.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | log.ASSET_REQUEST_APPROVED.message=Asset request req_501 approved | log.LAPTOP_ASSIGNED.message=PH-LAPTOP-010 assigned | candidate.cand_7.onboarding_status=LaptopAssigned"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_010",
        "instruction": "Authorize candidate cand_7's request for a phone, allocate the asset, revise onboarding files to reflect the phone assignment, finalize checklist items, authorize access checks, assign email tags, and log the records. End state: phone request authorized; asset PH-IPHONE-005 allocated; onboarding files indicate phone_assigned=True; checklist items finalized; access checks authorized; email tagged 'Welcome'; terminal logs document all activities.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-005",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_901",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_902",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset request req_502 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "PHONE_ASSIGNED",
                    "message": "PH-IPHONE-005 assigned",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items check_701 and check_702 completed",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks access_901 and access_902 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABEL_APPLIED",
                    "message": "Email email_701 labeled Welcome",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "AssetsAndChecksReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_502.status=Approved | asset.PH-IPHONE-005.status=Assigned | onboarding_files.welcome_guide.phone_assigned=True | checklist.check_701.status=Completed | checklist.check_702.status=Completed | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_Welcome | log.ASSET_REQUEST_APPROVED.message=Asset request req_502 approved | log.PHONE_ASSIGNED.message=PH-IPHONE-005 assigned | log.CHECKLIST_COMPLETED.message=Checklist items check_701 and check_702 completed | log.ACCESS_CHECK_APPROVED.message=Access checks access_901 and access_902 approved | log.EMAIL_LABEL_APPLIED.message=Email email_701 labeled Welcome | candidate.cand_7.onboarding_status=AssetsAndChecksReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_011",
        "instruction": "Handle the complete onboarding process for candidate cand_7: approve every asset request (laptop, phone, accessories), allocate assets, finalize all checklist items, give approval for all access checks, update several onboarding files, apply numerous email labels, and document terminal logs for each step. End state: all assets allocated; checklist items finalized; access checks approved; onboarding files updated; emails labeled; logs document all actions; candidate status indicates full onboarding.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-010",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-005",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-001",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-KEYBOARD-002",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "verified": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/policy_acknowledgment.pdf",
                    "updates": {
                        "acknowledged": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_703",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_901",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_902",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_903",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_702",
                    "label_id": "label_Policy"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_501 and req_502 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSETS_ASSIGNED",
                    "message": "Laptop, phone, mouse, and keyboard assigned",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items check_701, check_702, check_703 completed",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks access_901, access_902, access_903 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABEL_APPLIED",
                    "message": "Emails email_701 and email_702 labeled",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "OnboardingCompleted"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.PH-LAPTOP-010.status=Assigned | asset.PH-IPHONE-005.status=Assigned | asset.ACC-MOUSE-001.status=Assigned | asset.ACC-KEYBOARD-002.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | onboarding_files.welcome_guide.phone_assigned=True | onboarding_files.id_scan.verified=True | onboarding_files.policy_acknowledgment.acknowledged=True | checklist.check_701.status=Completed | checklist.check_702.status=Completed | checklist.check_703.status=Completed | access_check.access_901.status=Approved | access_check.access_902.status=Approved | access_check.access_903.status=Approved | email.email_701.labels=label_Welcome | email.email_702.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_501 and req_502 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, mouse, and keyboard assigned | log.CHECKLIST_COMPLETED.message=Checklist items check_701, check_702, check_703 completed | log.ACCESS_CHECK_APPROVED.message=Access checks access_901, access_902, access_903 approved | log.EMAIL_LABEL_APPLIED.message=Emails email_701 and email_702 labeled | candidate.cand_7.onboarding_status=OnboardingCompleted"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_055",
        "instruction": "Authorize candidate cand_5's laptop request req_105, allocate LT-MBP-003, confirm onboarding files verified, finalize checklist items check_207, check_208, authorize access checks access_306, access_307, and document all terminal logs. End state: candidate assets allocated and onboarding prepared.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_105",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-003",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_207",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_208",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_306",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_307",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop LT-MBP-003 assigned to cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset request req_105 approved"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed for cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved for cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_105.status=Approved | asset.LT-MBP-003.status=Assigned | onboarding_files.Alex_Thompson.laptop_assigned=True | checklist_item.check_207.status=Completed | checklist_item.check_208.status=Completed | access_check.access_306.status=Approved | access_check.access_307.status=Approved | log.ASSET_ASSIGNED.message=Laptop LT-MBP-003 assigned to cand_5 | log.ASSET_REQUEST_APPROVED.message=Asset request req_105 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_5 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_5 | candidate.cand_5.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_042",
        "instruction": "Authorize and allocate laptops to several candidates (Emma Thompson cand_2, William Davis cand_3, Sofia Martinez cand_4) according to asset requests. Choose suitable laptops that meet the specifications and check availability, update the onboarding files accordingly, and create terminal logs for each allocation. End state: asset requests marked 'Approved'; laptops LT-DELL-003, LT-DELL-002, LT-MBP-001 assigned; onboarding files show laptop_assigned=True; logs capture all approvals and assignments.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_Jane_Laptop",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_Peter_Laptop",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_Maria_Laptop",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-003",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-001",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Jane_Smith/asset_request.json",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Peter_Jones/asset_request.json",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "Laptops assigned to Jane, Peter, Maria",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "Laptops assigned to Jane, Peter, Maria",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "Laptops assigned to Jane, Peter, Maria",
                    "candidate_id": "cand_4"
                }
            }
        ],
        "outputs": [
                "asset_request.req_Jane_Laptop.status=Approved | asset_request.req_Peter_Laptop.status=Approved | asset_request.req_Maria_Laptop.status=Approved | asset.LT-DELL-003.status=Assigned | asset.LT-DELL-002.status=Assigned | asset.LT-MBP-001.status=Assigned | onboarding_files.Jane_Smith.laptop_assigned=True | onboarding_files.Peter_Jones.laptop_assigned=True | onboarding_files.Maria_Rodriguez.laptop_assigned=True | log.LAPTOP_ASSIGNED.message=Laptops assigned to Jane, Peter, Maria"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_043",
        "instruction": "Authorize and allocate both a laptop and phone to candidate Jordan Williams (cand_5). Update the onboarding file to reflect laptop_assigned=True and phone_assigned=True, make terminal log entries, and set the candidate's onboarding status to 'AssetsReady'. End state: asset requests marked 'Approved'; laptop LT-MBP-002 and phone PH-IPHONE-001 assigned; onboarding file updated; candidate status updated.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_Alex_Laptop",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_Alex_Phone",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-002",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-001",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Laptop and phone approved for Jordan Williams",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "LT-MBP-002 assigned",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "PHONE_ASSIGNED",
                    "message": "PH-IPHONE-001 assigned",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_Alex_Laptop.status=Approved | asset_request.req_Alex_Phone.status=Approved | asset.LT-MBP-002.status=Assigned | asset.PH-IPHONE-001.status=Assigned | onboarding_files.Alex_Thompson.laptop_assigned=True | onboarding_files.Alex_Thompson.phone_assigned=True | log.ASSET_REQUEST_APPROVED.message=Laptop and phone approved for Jordan Williams | log.LAPTOP_ASSIGNED.message=LT-MBP-002 assigned | log.PHONE_ASSIGNED.message=PH-IPHONE-001 assigned | candidate.cand_5.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_044",
        "instruction": "Authorize cand_2's laptop request, allocate the laptop, and modify the onboarding file to display the laptop assignment. Final condition: asset request authorized; LT-DELL-003 allocated to cand_2; onboarding file indicates laptop_assigned=True; terminal logs record approval and allocation events.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-003",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Jane_Smith/asset_request.json",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset request req_101 approved",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "LT-DELL-003 assigned",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_101.status=Approved | asset.LT-DELL-003.status=Assigned | onboarding_files.cand_2.laptop_assigned=True | log.ASSET_REQUEST_APPROVED.message=Asset request req_101 approved | log.LAPTOP_ASSIGNED.message=LT-DELL-003 assigned | candidate.cand_2.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_046",
        "instruction": "Authorize cand_4's requests for a laptop and phone, allocate the necessary assets, resolve any pending access problems, and amend the onboarding files. Final condition: asset requests authorized; LT-MBP-001 and PH-IPHONE-002 allocated; onboarding files reflect laptop_assigned=True, phone_assigned=True; access problems logged as resolved.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_104",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_105",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-001",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-002",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true,
                        "access_issues_resolved": true
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_104 and req_105 approved",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "LT-MBP-001 assigned",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "PHONE_ASSIGNED",
                    "message": "PH-IPHONE-002 assigned",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_104.status=Approved | asset_request.req_105.status=Approved | asset.LT-MBP-001.status=Assigned | asset.PH-IPHONE-002.status=Assigned | onboarding_files.cand_4.laptop_assigned=True | onboarding_files.cand_4.phone_assigned=True | onboarding_files.cand_4.access_issues_resolved=True | log.ASSET_REQUEST_APPROVED.message=Asset requests req_104 and req_105 approved | log.LAPTOP_ASSIGNED.message=LT-MBP-001 assigned | log.PHONE_ASSIGNED.message=PH-IPHONE-002 assigned | candidate.cand_4.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_033",
        "instruction": "Endorse candidate cand_7's laptop request, allocate the asset, update onboarding documentation reflecting the laptop allocation, finalize checklist tasks, authorize access checks, categorize emails, and document logs. Final state: laptop request endorsed; laptop PH-LAPTOP-010 allocated; onboarding documentation indicates laptop_assigned=True; checklist tasks completed; access checks authorized; email tagged 'Welcome'; terminal logs record all activities.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-010",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_901",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_902",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset request req_501 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "LAPTOP_ASSIGNED",
                    "message": "PH-LAPTOP-010 assigned",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items check_701 and check_702 completed",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks access_901 and access_902 approved",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABEL_APPLIED",
                    "message": "Email email_701 labeled Welcome",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "AssetsAndChecksReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_501.status=Approved | asset.PH-LAPTOP-010.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | checklist.check_701.status=Completed | checklist.check_702.status=Completed | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_Welcome | log.ASSET_REQUEST_APPROVED.message=Asset request req_501 approved | log.LAPTOP_ASSIGNED.message=PH-LAPTOP-010 assigned | log.CHECKLIST_COMPLETED.message=Checklist items check_701 and check_702 completed | log.ACCESS_CHECK_APPROVED.message=Access checks access_901 and access_902 approved | log.EMAIL_LABEL_APPLIED.message=Email email_701 labeled Welcome | candidate.cand_7.onboarding_status=AssetsAndChecksReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_001",
        "instruction": "Authorize asset requests req_101, req_102 for candidate cand_1, allocate laptop LT-001 and phone PH-001, finalize checklist tasks check_101 and check_102, confirm onboarding documents welcome.pdf and id_scan.pdf, label email email_101 with 'Welcome,' and register all modifications. Ensure the candidate record confirms completion.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_102",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Onboarding completed for cand_1",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_101.status=Approved | asset_request.req_102.status=Approved | asset.LT-001.status=Assigned | asset.PH-001.status=Assigned | checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | onboarding_files.welcome.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | email.email_101.labels=label_Welcome | log.ONBOARDING_COMPLETED.message=Onboarding completed for cand_1 | candidate.cand_1.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_002",
        "instruction": "Handle the approval of candidate cand_2's asset requests req_201 and req_202, allocate assets LT-002 and PH-002, finalize checklist check_201, check onboarding file offer_letter.pdf, tag email email_201 with 'Ready', and record all actions. Update the candidate record to indicate completion.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_201",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_202",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-002",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_201",
                    "label_id": "label_Ready"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Assets assigned to cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELED",
                    "message": "Email labeled 'Ready' for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_201.status=Approved | asset_request.req_202.status=Approved | asset.LT-002.status=Assigned | asset.PH-002.status=Assigned | checklist_item.check_201.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | email.email_201.labels=label_Ready | log.ASSET_ASSIGNED.message=Assets assigned to cand_2 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_2 | log.EMAIL_LABELED.message=Email labeled 'Ready' for cand_2 | candidate.cand_2.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_003",
        "instruction": "You handle the release of old assets LT-003 and PH-003 for candidate cand_3, allocate new laptop LT-003B, finish checklist items check_301 and check_302, incorporate onboarding file id_scan.pdf, attach email label 'AssetUpdate' to email email_301, document all changes, and revise the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-003"
                },
            },
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "PH-003"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-003B",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_302",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/id_scan.pdf",
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_301",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_RELEASED",
                    "message": "Old assets released for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELED",
                    "message": "Email labeled 'AssetUpdate' for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-003.status=Available | asset.PH-003.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | onboarding_files.id_scan.pdf.status=Verified | email.email_301.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_3 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_3 | log.EMAIL_LABELED.message=Email labeled 'AssetUpdate' for cand_3 | candidate.cand_3.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_003",
        "instruction": "You handle the release of old assets LT-003 and PH-003 for candidate cand_3, allocate new laptop LT-003B, finish checklist items check_301 and check_302, incorporate onboarding file id_scan.pdf, attach email label 'AssetUpdate' to email email_301, document all changes, and revise the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-003"
                },
            },
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "PH-003"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-003B",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_302",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/id_scan.pdf",
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_301",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_RELEASED",
                    "message": "Old assets released for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELED",
                    "message": "Email labeled 'AssetUpdate' for cand_3",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-003.status=Available | asset.PH-003.status=Available | asset.LT-003B.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | onboarding_files.id_scan.pdf.status=Verified | email.email_301.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_3 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_3 | log.EMAIL_LABELED.message=Email labeled 'AssetUpdate' for cand_3 | candidate.cand_3.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_004",
        "instruction": "You endorse asset requests req_401 for candidate cand_4, allocate laptop LT-004 and phone PH-004, fulfill checklist item check_401, incorporate onboarding file welcome_guide.pdf, attach email label 'Onboarded' to email email_401, document all actions, and designate candidate record as completed.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_401",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_401",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/welcome_guide.pdf",
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_401",
                    "label_id": "label_Onboarded"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Assets assigned for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELED",
                    "message": "Email labeled 'Onboarded' for cand_4",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_401.status=Approved | asset.LT-004.status=Assigned | asset.PH-004.status=Assigned | checklist_item.check_401.status=Completed | onboarding_files.welcome_guide.pdf.status=Verified | email.email_401.labels=label_Onboarded | log.ASSET_ASSIGNED.message=Assets assigned for cand_4 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_4 | log.EMAIL_LABELED.message=Email labeled 'Onboarded' for cand_4 | candidate.cand_4.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_005",
        "instruction": "Handle asset reassignment for candidate cand_5: release old laptop LT-005, assign new laptop LT-005B, ensure completion of checklist item check_501, verify the onboarding file id_scan.pdf, apply email label 'AssetUpdate' to email email_501, log all updates, and update the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-005"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_501",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_501",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_RELEASED",
                    "message": "Old assets released for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "New assets assigned for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist completed for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELED",
                    "message": "Email labeled 'AssetUpdate' for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-005.status=Available | asset.LT-005B.status=Assigned | checklist_item.check_501.status=Completed | onboarding_files.id_scan.pdf.status=Verified | email.email_501.labels=label_AssetUpdate | log.ASSET_RELEASED.message=Old assets released for cand_5 | log.ASSET_ASSIGNED.message=New assets assigned for cand_5 | log.CHECKLIST_COMPLETED.message=Checklist completed for cand_5 | log.EMAIL_LABELED.message=Email labeled 'AssetUpdate' for cand_5 | candidate.cand_5.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_068",
        "instruction": "Handle the onboarding of candidate cand_7: approve asset requests req_701 and req_702, assign laptop LT-HP-007, phone PH-IP-007, and accessory ACC-KEY-007. Complete checklist items check_801 and check_802. Verify onboarding files resume.pdf and id_scan.pdf. Approve access checks access_901 and access_902. Tag email email_701 with 'OnboardingComplete' and record all actions.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_401",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_402",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-SAMSUNG-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-004",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_401",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_402",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_401",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_402",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_401",
                    "label_id": "label_OnboardingReady"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Candidate cand_4 onboarding completed",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_401.status=Approved | asset_request.req_402.status=Approved | asset.LT-DELL-004.status=Assigned | asset.PH-SAMSUNG-004.status=Assigned | asset.ACC-MOUSE-004.status=Assigned | checklist_item.check_401.status=Completed | checklist_item.check_402.status=Completed | onboarding_files.welcome_guide.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_401.status=Approved | access_check.access_402.status=Approved | email.email_401.labels=label_OnboardingReady | log.ONBOARDING_COMPLETED.message=Candidate cand_4 onboarding completed | candidate.cand_4.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_065",
        "instruction": "Candidate cand_7 is tasked with cleaning up emails and reallocating assets. You eliminate email email_701, discard attachment attach_701, incorporate the new onboarding document policies_cand7.pdf, mark checklist item check_701 as Completed, and authorize access check access_701. Log terminal activities for each action performed.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-OLD-007"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-NEW-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-NEW-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-HEADSET-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_701"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_702"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_703",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_704",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_1",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REASSIGNMENT",
                    "message": "Assets reassigned for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-OLD-007.status=Available | asset.LT-NEW-007.status=Assigned | asset.PH-NEW-007.status=Assigned | asset.ACC-HEADSET-007.status=Assigned | asset_request.req_701.status=Completed | asset_request.req_702.status=Completed | access_check.access_701=Removed | access_check.access_702=Removed | access_check.access_703.status=Pending | access_check.access_704.status=Pending | attachment.Company-Policies.pdf.added=True | email.email_701.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_7 | log.ACCESS_UPDATED.message=Access checks updated for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_064",
        "instruction": "Candidate cand_6 has several assets and emails awaiting action. You approve asset request req_601, allocate laptop LT-LENOVO-006. Dispatch a welcome email ('Welcome!', 'Hello cand_6') email_601, attach the file welcome_attach.pdf, and apply the label 'Onboarding' to email_601. Release the outdated asset LT-OLD-001. Document all terminal logs for the executed tasks. The final state should be: new asset assigned, email dispatched with label, old asset released.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-HP-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IP-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_102",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_102",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_OnboardingReady"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Candidate cand_1 onboarding completed",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_101.status=Approved | asset_request.req_102.status=Approved | asset.LT-HP-001.status=Assigned | asset.PH-IP-001.status=Assigned | checklist_item.check_101.status=Completed | checklist_item.check_102.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_101.status=Approved | access_check.access_102.status=Approved | email.email_101.labels=label_OnboardingReady | log.ONBOARDING_COMPLETED.message=Candidate cand_1 onboarding completed | candidate.cand_1.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_062",
        "instruction": "Handle the onboarding of candidate cand_3 by endorsing laptop request req_203 and accessory requests req_204, allocate LT-DELL-003, monitor MON-LG-002, keyboard ACC-KEYBOARD-001, finalize checklist items check_303, check_304, sanction access checks access_403, access_404, update onboarding files, and register terminal logs. End state: all assets assigned and approved, files verified, checklist and access checks completed, candidate status updated.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_301",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_302",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-HP-003",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IP-003",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_302",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_301",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_302",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_301",
                    "label_id": "label_OnboardingReady"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Candidate cand_3 onboarding completed",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_301.status=Approved | asset_request.req_302.status=Approved | asset.LT-HP-003.status=Assigned | asset.PH-IP-003.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_301.status=Approved | access_check.access_302.status=Approved | email.email_301.labels=label_OnboardingReady | log.ONBOARDING_COMPLETED.message=Candidate cand_3 onboarding completed | candidate.cand_3.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_061",
        "instruction": "Coordinate candidate cand_2's onboarding by authorizing asset requests req_201, req_202, assigning laptop LT-MBP-004, phone PH-IPHONE-002, and accessory ACC-HEADSET-001. Fulfill checklist items check_301, check_302, endorse access verifications access_401, access_402, revise onboarding documents welcome_Jane_Smith.md and asset_request.json, and log terminal records. Completion state: assets allocated and approved, documents verified, checklist and access finalized, candidate onboarding status refreshed.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_201",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_202",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-004",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-002",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-HEADSET-001",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_301",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_302",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_401",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_402",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Jane_Smith/asset_request.json",
                    "updates": {
                        "assigned_assets": [
                            "LT-MBP-004",
                            "PH-IPHONE-002",
                            "ACC-HEADSET-001"
                        ]
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop, phone, and headset assigned to cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_201 and req_202 approved"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed for cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved for cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_201.status=Approved | asset_request.req_202.status=Approved | asset.LT-MBP-004.status=Assigned | asset.PH-IPHONE-002.status=Assigned | asset.ACC-HEADSET-001.status=Assigned | checklist_item.check_301.status=Completed | checklist_item.check_302.status=Completed | access_check.access_401.status=Approved | access_check.access_402.status=Approved | onboarding_files.Jane_Smith.laptop_assigned=True | onboarding_files.Jane_Smith.phone_assigned=True | onboarding_files.Jane_Smith.asset_request.assigned_assets=['LT-MBP-004','PH-IPHONE-002','ACC-HEADSET-001'] | log.ASSET_ASSIGNED.message=Laptop, phone, and headset assigned to cand_2 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_201 and req_202 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_2 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_2 | candidate.cand_2.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_062",
        "instruction": "Handle the onboarding of candidate cand_3 by endorsing laptop request req_203 and accessory requests req_204, allocate LT-DELL-003, monitor MON-LG-002, keyboard ACC-KEYBOARD-001, finalize checklist items check_303, check_304, sanction access checks access_403, access_404, update onboarding files, and register terminal logs. End state: all assets assigned and approved, files verified, checklist and access checks completed, candidate status updated.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_203",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_204",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-003",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "MON-LG-002",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-KEYBOARD-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_303",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_304",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_403",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_404",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md",
                    "updates": {
                        "laptop_assigned": true,
                        "monitor_assigned": true,
                        "keyboard_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Peter_Jones/asset_request.json",
                    "updates": {
                        "assigned_assets": [
                            "LT-DELL-003",
                            "MON-LG-002",
                            "ACC-KEYBOARD-001"
                        ]
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop, monitor, and keyboard assigned to cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_203 and req_204 approved"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed for cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved for cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_203.status=Approved | asset_request.req_204.status=Approved | asset.LT-DELL-003.status=Assigned | asset.MON-LG-002.status=Assigned | asset.ACC-KEYBOARD-001.status=Assigned | checklist_item.check_303.status=Completed | checklist_item.check_304.status=Completed | access_check.access_403.status=Approved | access_check.access_404.status=Approved | onboarding_files.Peter_Jones.laptop_assigned=True | onboarding_files.Peter_Jones.monitor_assigned=True | onboarding_files.Peter_Jones.keyboard_assigned=True | onboarding_files.Peter_Jones.asset_request.assigned_assets=['LT-DELL-003','MON-LG-002','ACC-KEYBOARD-001'] | log.ASSET_ASSIGNED.message=Laptop, monitor, and keyboard assigned to cand_3 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_203 and req_204 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_3 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_3 | candidate.cand_3.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_063",
        "instruction": "Coordinate the onboarding of candidate cand_4 by endorsing laptop request req_205, phone request req_206, accessory request req_207, allocate LT-MBP-005, PH-IPHONE-003, ACC-MOUSE-002, finalize checklist items check_305, check_306, authorize access checks access_405, access_406, update onboarding files welcome and asset_request.json, and document all actions. End state: all assets assigned, files verified, checklist and access completed, candidate status updated.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_205",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_206",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_207",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-005",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-003",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-002",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_305",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_306",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_405",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_406",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true,
                        "accessory_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                    "updates": {
                        "assigned_assets": [
                            "LT-MBP-005",
                            "PH-IPHONE-003",
                            "ACC-MOUSE-002"
                        ]
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop, phone, and accessory assigned to cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_205, req_206, req_207 approved"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed for cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved for cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_205.status=Approved | asset_request.req_206.status=Approved | asset_request.req_207.status=Approved | asset.LT-MBP-005.status=Assigned | asset.PH-IPHONE-003.status=Assigned | asset.ACC-MOUSE-002.status=Assigned | checklist_item.check_305.status=Completed | checklist_item.check_306.status=Completed | access_check.access_405.status=Approved | access_check.access_406.status=Approved | onboarding_files.Maria_Rodriguez.laptop_assigned=True | onboarding_files.Maria_Rodriguez.phone_assigned=True | onboarding_files.Maria_Rodriguez.accessory_assigned=True | onboarding_files.Maria_Rodriguez.asset_request.assigned_assets=['LT-MBP-005','PH-IPHONE-003','ACC-MOUSE-002'] | log.ASSET_ASSIGNED.message=Laptop, phone, and accessory assigned to cand_4 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_205, req_206, req_207 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_4 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_4 | candidate.cand_4.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_064",
        "instruction": "Candidate cand_6 has several assets and emails awaiting action. You approve asset request req_601, allocate laptop LT-LENOVO-006. Dispatch a welcome email ('Welcome!', 'Hello cand_6') email_601, attach the file welcome_attach.pdf, and apply the label 'Onboarding' to email_601. Release the outdated asset LT-OLD-001. Document all terminal logs for the executed tasks. The final state should be: new asset assigned, email dispatched with label, old asset released.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_601",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-LENOVO-006",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "email": {
                        "message_id": "email_601",
                        "subject": "Welcome!",
                        "body": "Hello cand_6"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_601",
                        "file_name": "welcome_attach.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_601",
                    "label_id": "label_Onboarding"
                },
            },
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-OLD-001"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "LT-LENOVO-006 assigned to cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_SENT",
                    "message": "Welcome email sent to cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_RELEASED",
                    "message": "LT-OLD-001 released from cand_6",
                    "candidate_id": "cand_6"
                }
            }
        ],
        "outputs": [
                "asset_request.req_601.status=Approved | asset.LT-LENOVO-006.status=Assigned | email.email_601.labels=label_Onboarding | attachment.attach_601.file_name=welcome_attach.pdf | asset.LT-OLD-001.status=Available | log.ASSET_ASSIGNED.message=LT-LENOVO-006 assigned to cand_6 | log.EMAIL_SENT.message=Welcome email sent to cand_6 | log.ASSET_RELEASED.message=LT-OLD-001 released from cand_6"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_065",
        "instruction": "Candidate cand_7 is tasked with cleaning up emails and reallocating assets. You eliminate email email_701, discard attachment attach_701, incorporate the new onboarding document policies_cand7.pdf, mark checklist item check_701 as Completed, and authorize access check access_701. Log terminal activities for each action performed.",
        "actions": [
            {
                "name": "DeleteEmail",
                "arguments": {
                    "message_id": "email_701"
                },
            },
            {
                "name": "RemoveAttachment",
                "arguments": {
                    "attachment_id": "attach_701"
                },
            },
            {
                "name": "AddOnboardingFile",
                "arguments": {
                    "file": {
                        "file_path": "files/policies_cand7.pdf",
                        "status": "Uploaded"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_701",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_DELETED",
                    "message": "email_701 deleted for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ATTACHMENT_REMOVED",
                    "message": "attach_701 removed for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_FILE_ADDED",
                    "message": "policies_cand7.pdf uploaded",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_UPDATED",
                    "message": "check_701 completed for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_APPROVED",
                    "message": "access_701 approved for cand_7",
                    "candidate_id": "cand_7"
                }
            }
        ],
        "outputs": [
                "email.email_701.status=Deleted | attachment.attach_701.status=Removed | onboarding_files.policies_cand7.pdf.status=Uploaded | checklist_item.check_701.status=Completed | access_check.access_701.status=Approved | log.EMAIL_DELETED.message=email_701 deleted for cand_7 | log.ATTACHMENT_REMOVED.message=attach_701 removed for cand_7 | log.ONBOARDING_FILE_ADDED.message=policies_cand7.pdf uploaded | log.CHECKLIST_UPDATED.message=check_701 completed for cand_7 | log.ACCESS_APPROVED.message=access_701 approved for cand_7"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_407",
        "instruction": "For candidate cand_7, handle the release of the old laptop LT-007A, allocate the new laptop LT-007B, complete asset requests req_701 and req_702, eliminate access checks access_701 and access_702, introduce new access checks access_703 and access_704, include Company-Policies.pdf and Benefits-Guide.pdf as attachments, apply the label 'AssetUpdate' to emails email_701 and email_702, update checklist items check_701 and check_702, ensure the verification of onboarding files ID-Card.pdf and Passport.pdf, record all modifications, and refresh the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-007A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-007B",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_701"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_702"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_703",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_704",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_13",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_14",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_702",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/ID-Card.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/Passport.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Full asset and checklist update for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-007A.status=Available | asset.LT-007B.status=Assigned | asset_request.req_701.status=Completed | asset_request.req_702.status=Completed | access_check.access_701=Removed | access_check.access_702=Removed | access_check.access_703.status=Pending | access_check.access_704.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_701.labels=label_AssetUpdate | email.email_702.labels=label_AssetUpdate | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.ID-Card.pdf.status=Verified | onboarding_files.Passport.pdf.status=Verified | log.ONBOARDING_COMPLETED.message=Full asset and checklist update for cand_7 | candidate.cand_7.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_067",
        "instruction": "Coordinate candidate cand_7's offboarding: manage the release of assets LT-OLD-007 and PH-OLD-007, erase checklist items check_701 and check_702, revoke access checks access_701 and access_702, remove onboarding files farewell.pdf and exit_form.pdf, and document the events.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-OLD-007"
                },
            },
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "PH-OLD-007"
                },
            },
            {
                "name": "RemoveChecklistItem",
                "arguments": {
                    "item_id": "check_701"
                },
            },
            {
                "name": "RemoveChecklistItem",
                "arguments": {
                    "item_id": "check_702"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_701"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_702"
                },
            },
            {
                "name": "RemoveOnboardingFile",
                "arguments": {
                    "file_path": "files/farewell.pdf"
                },
            },
            {
                "name": "RemoveOnboardingFile",
                "arguments": {
                    "file_path": "files/exit_form.pdf"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "OFFBOARDING_ASSETS_RELEASED",
                    "message": "Assets released for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "OFFBOARDING_COMPLETED",
                    "message": "Checklist, access, and files removed for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "offboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-OLD-007.status=Available | asset.PH-OLD-007.status=Available | checklist_item.check_701=Removed | checklist_item.check_702=Removed | access_check.access_701=Removed | access_check.access_702=Removed | onboarding_files.farewell.pdf=Removed | onboarding_files.exit_form.pdf=Removed | log.OFFBOARDING_ASSETS_RELEASED.message=Assets released for cand_7 | log.OFFBOARDING_COMPLETED.message=Checklist, access, and files removed for cand_7 | candidate.cand_7.offboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_068",
        "instruction": "Handle the onboarding of candidate cand_7: approve asset requests req_701 and req_702, assign laptop LT-HP-007, phone PH-IP-007, and accessory ACC-KEY-007. Complete checklist items check_801 and check_802. Verify onboarding files resume.pdf and id_scan.pdf. Approve access checks access_901 and access_902. Tag email email_701 with 'OnboardingComplete' and record all actions.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_701",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_702",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-HP-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IP-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-KEY-007",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_801",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_802",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/resume.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_901",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_902",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_701",
                    "label_id": "label_OnboardingComplete"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "All onboarding steps completed for cand_7",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "updates": {
                        "onboarding_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_701.status=Approved | asset_request.req_702.status=Approved | asset.LT-HP-007.status=Assigned | asset.PH-IP-007.status=Assigned | asset.ACC-KEY-007.status=Assigned | checklist_item.check_801.status=Completed | checklist_item.check_802.status=Completed | onboarding_files.resume.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_901.status=Approved | access_check.access_902.status=Approved | email.email_701.labels=label_OnboardingComplete | log.ONBOARDING_COMPLETED.message=All onboarding steps completed for cand_7 | candidate.cand_7.onboarding_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_069",
        "instruction": "Coordinate the reassignment of assets for candidate cand_6: release old phone PH-OLD-006, assign new laptop LT-NEW-006 and new phone PH-NEW-006. Update asset requests req_603 and req_604 to 'Completed'. Remove access checks access_603, add new access checks access_605 and access_606. Attach Company-Policies.pdf and Benefits-Guide.pdf, set label 'AssetChange' for email email_602, and document all changes.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "PH-OLD-006"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-NEW-006",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-NEW-006",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_603",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_604",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_603"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_605",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_606",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_1",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_2",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_602",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REASSIGNMENT",
                    "message": "Assets reassigned for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_UPDATED",
                    "message": "Access checks updated for cand_6",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_6",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.PH-OLD-006.status=Available | asset.LT-NEW-006.status=Assigned | asset.PH-NEW-006.status=Assigned | asset_request.req_603.status=Completed | asset_request.req_604.status=Completed | access_check.access_603=Removed | access_check.access_605.status=Pending | access_check.access_606.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_602.labels=label_AssetChange | log.ASSET_REASSIGNMENT.message=Assets reassigned for cand_6 | log.ACCESS_UPDATED.message=Access checks updated for cand_6 | candidate.cand_6.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_070",
        "instruction": "Handle the finalization of onboarding for candidate cand_5: approve asset requests req_501 and req_502, allocate laptop LT-DELL-005, phone PH-SAMSUNG-005, and mouse ACC-MOUSE-005. Mark checklist items check_701 and check_702 as completed. Confirm onboarding files offer_letter.pdf and id_scan.pdf. Approve access checks access_801 and access_802. Dispatch email email_501 with label 'OnboardingReady' and document terminal logs for all updates.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-005",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-SAMSUNG-005",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-005",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_701",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_702",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/offer_letter.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_801",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_802",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_501",
                    "label_id": "label_OnboardingReady"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_FINALIZED",
                    "message": "Candidate cand_5 onboarding finalized",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "onboarding_status": "Ready"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.LT-DELL-005.status=Assigned | asset.PH-SAMSUNG-005.status=Assigned | asset.ACC-MOUSE-005.status=Assigned | checklist_item.check_701.status=Completed | checklist_item.check_702.status=Completed | onboarding_files.offer_letter.pdf.status=Verified | onboarding_files.id_scan.pdf.status=Verified | access_check.access_801.status=Approved | access_check.access_802.status=Approved | email.email_501.labels=label_OnboardingReady | log.ONBOARDING_FINALIZED.message=Candidate cand_5 onboarding finalized | candidate.cand_5.onboarding_status=Ready"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_052",
        "instruction": "Coordinate the approval of candidate cand_2's laptop request req_101, assign laptop LT-MBP-001, update onboarding files to set laptop_assigned=True, fulfill checklist items check_201 and check_202, approve access checks access_301, and log all terminal records. Final condition: laptop assigned and approved, files, checklist, and access checks completed, onboarding status of candidate updated.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-001",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md",
                    "updates": {
                        "laptop_assigned": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_301",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop LT-MBP-001 assigned to cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset request req_101 approved"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed for cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved for cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_101.status=Approved | asset.LT-MBP-001.status=Assigned | onboarding_files.Jane_Smith.laptop_assigned=True | checklist_item.check_201.status=Completed | checklist_item.check_202.status=Completed | access_check.access_301.status=Approved | log.ASSET_ASSIGNED.message=Laptop LT-MBP-001 assigned to cand_2 | log.ASSET_REQUEST_APPROVED.message=Asset request req_101 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_2 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_2 | candidate.cand_2.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_405",
        "instruction": "Handle candidate cand_5 by relinquishing the old laptop LT-005A, assigning the new laptop LT-005B, fulfilling asset requests req_501 and req_502, discontinuing access checks access_501 and access_502, adding access checks access_503, access_504, attaching Company-Policies.pdf, attaching Benefits-Guide.pdf, applying label 'AssetChange' to the email email_501, updating checklist items check_501, check_502, ensuring verification of onboarding files ID-Card.pdf and Passport.pdf, logging all changes, and updating the candidate record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-005A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-005B",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_501"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_502"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_503",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_504",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_9",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_10",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_501",
                    "label_id": "label_AssetChange"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_501",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_502",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/ID-Card.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/Passport.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Full asset and checklist update for cand_5",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-005A.status=Available | asset.LT-005B.status=Assigned | asset_request.req_501.status=Completed | asset_request.req_502.status=Completed | access_check.access_501=Removed | access_check.access_502=Removed | access_check.access_503.status=Pending | access_check.access_504.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_501.labels=label_AssetChange | checklist_item.check_501.status=Completed | checklist_item.check_502.status=Completed | onboarding_files.ID-Card.pdf.status=Verified | onboarding_files.Passport.pdf.status=Verified | log.ONBOARDING_COMPLETED.message=Full asset and checklist update for cand_5 | candidate.cand_5.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_053",
        "instruction": "Coordinate the onboarding of candidate cand_3 by sanctioning laptop request req_102, assigning the laptop LT-DELL-002 and monitor MON-LG-001, marking files as verified in the onboarding, completing checklist items check_203, check_204, and endorsing access checks access_302, access_303. Document terminal logs and update the candidate onboarding status.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "MON-LG-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md",
                    "updates": {
                        "laptop_assigned": true,
                        "monitor_assigned": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_203",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_204",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_302",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_303",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop LT-DELL-002 and Monitor MON-LG-001 assigned to cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset request req_102 approved"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed for cand_3"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved for cand_3"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_3",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_102.status=Approved | asset.LT-DELL-002.status=Assigned | asset.MON-LG-001.status=Assigned | onboarding_files.Peter_Jones.laptop_assigned=True | onboarding_files.Peter_Jones.monitor_assigned=True | checklist_item.check_203.status=Completed | checklist_item.check_204.status=Completed | access_check.access_302.status=Approved | access_check.access_303.status=Approved | log.ASSET_ASSIGNED.message=Laptop LT-DELL-002 and Monitor MON-LG-001 assigned to cand_3 | log.ASSET_REQUEST_APPROVED.message=Asset request req_102 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_3 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_3 | candidate.cand_3.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_054",
        "instruction": "Handle onboarding for candidate cand_4 by approving the laptop request req_103 and phone request req_104, allocating LT-MBP-002 and PH-IPHONE-001, verifying onboarding files, fulfilling checklist items check_205, check_206, approving access checks access_304, access_305, and logging all activities.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_103",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_104",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-002",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-001",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_205",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_206",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_304",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_305",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_ASSIGNED",
                    "message": "Laptop LT-MBP-002 and Phone PH-IPHONE-001 assigned to cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_103 and req_104 approved"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed for cand_4"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved for cand_4"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_4",
                    "updates": {
                        "onboarding_status": "AssetsReady"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_103.status=Approved | asset_request.req_104.status=Approved | asset.LT-MBP-002.status=Assigned | asset.PH-IPHONE-001.status=Assigned | onboarding_files.Maria_Rodriguez.laptop_assigned=True | onboarding_files.Maria_Rodriguez.phone_assigned=True | checklist_item.check_205.status=Completed | checklist_item.check_206.status=Completed | access_check.access_304.status=Approved | access_check.access_305.status=Approved | log.ASSET_ASSIGNED.message=Laptop LT-MBP-002 and Phone PH-IPHONE-001 assigned to cand_4 | log.ASSET_REQUEST_APPROVED.message=Asset requests req_103 and req_104 approved | log.CHECKLIST_COMPLETED.message=Checklist items completed for cand_4 | log.ACCESS_CHECK_APPROVED.message=Access checks approved for cand_4 | candidate.cand_4.onboarding_status=AssetsReady"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_012",
        "instruction": "Coordinate full onboarding for candidate cand_1: approve all asset requests (laptop, phone, accessories), allocate assets, complete all checklist items, authorize all access checks, revise multiple onboarding files, apply email labels, and document terminal logs for each step. Final condition: all assets are allocated; checklist items are completed; access checks are authorized; onboarding files are updated; emails have labels; logs document all activities; candidate status shows full onboarding.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-002",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "verified": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_101 and req_102 approved",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSETS_ASSIGNED",
                    "message": "Laptop, phone, and mouse assigned",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "onboarding_status": "OnboardingCompleted"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_101.status=Approved | asset_request.req_102.status=Approved | asset.PH-LAPTOP-001.status=Assigned | asset.PH-IPHONE-001.status=Assigned | asset.ACC-MOUSE-002.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | onboarding_files.welcome_guide.phone_assigned=True | onboarding_files.id_scan.verified=True | checklist.check_101.status=Completed | access_check.access_101.status=Approved | email.email_101.labels=label_Welcome | log.ASSET_REQUEST_APPROVED.message=Asset requests req_101 and req_102 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, and mouse assigned | candidate.cand_1.onboarding_status=OnboardingCompleted"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_017",
        "instruction": "Handle the comprehensive multi-step onboarding for candidate cand_2: approve every pending asset request, assign all applicable assets, finalize each checklist item, authorize access checks, refresh onboarding files with asset and policy information, utilize suitable email labels, and meticulously log terminal activities throughout the process. Final goal: candidate cand_2 is fully assigned assets, checklist is finalized, access checks are authorized, onboarding files are updated, emails bear appropriate labels, and the candidate's status reads as fully completed.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_201",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_202",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-002",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-002",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-003",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide_cand2.pdf",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan_cand2.pdf",
                    "updates": {
                        "verified": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/policy_ack_cand2.pdf",
                    "updates": {
                        "acknowledged": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_203",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_201",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_202",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_201",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_202",
                    "label_id": "label_Policy"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_203",
                    "label_id": "label_Onboarding"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_201 and req_202 approved",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSETS_ASSIGNED",
                    "message": "Laptop, phone, and mouse assigned",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELS_APPLIED",
                    "message": "Emails labeled 'Welcome', 'Policy', 'Onboarding'",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "onboarding_status": "OnboardingCompleted"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_201.status=Approved | asset_request.req_202.status=Approved | asset.PH-LAPTOP-002.status=Assigned | asset.PH-IPHONE-002.status=Assigned | asset.ACC-MOUSE-003.status=Assigned | onboarding_files.welcome_guide_cand2.laptop_assigned=True | onboarding_files.welcome_guide_cand2.phone_assigned=True | onboarding_files.id_scan_cand2.verified=True | onboarding_files.policy_ack_cand2.acknowledged=True | checklist.check_201.status=Completed | checklist.check_202.status=Completed | checklist.check_203.status=Completed | access_check.access_201.status=Approved | access_check.access_202.status=Approved | email.email_201.labels=label_Welcome | email.email_202.labels=label_Policy | email.email_203.labels=label_Onboarding | log.ASSET_REQUEST_APPROVED.message=Asset requests req_201 and req_202 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, and mouse assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome', 'Policy', 'Onboarding' | candidate.cand_2.onboarding_status=OnboardingCompleted"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_402",
        "instruction": "For candidate cand_2, coordinate the release of old laptop LT-002A, allocate new laptop LT-002B, fulfill asset requests req_201 and req_202, eliminate access checks access_201, access_202, introduce new access checks access_203, access_204, attach Company-Policies.pdf, append Benefits-Guide.pdf, apply the label 'AssetUpdate' to email email_201, update checklist items check_201, check_202, confirm onboarding files ID-Card.pdf and Driving-License.pdf, document all modifications, and refresh the candidate's record.",
        "actions": [
            {
                "name": "ReleaseAsset",
                "arguments": {
                    "asset_tag": "LT-002A"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "LT-002B",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_201"
                },
            },
            {
                "name": "RemoveAccessCheck",
                "arguments": {
                    "check_id": "access_202"
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_203",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAccessCheck",
                "arguments": {
                    "check": {
                        "check_id": "access_204",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_3",
                        "file_name": "Company-Policies.pdf"
                    }
                },
            },
            {
                "name": "AddAttachment",
                "arguments": {
                    "attachment": {
                        "attachment_id": "attach_4",
                        "file_name": "Benefits-Guide.pdf"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_201",
                    "label_id": "label_AssetUpdate"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_201",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_202",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/ID-Card.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/Driving-License.pdf",
                    "updates": {
                        "status": "Verified"
                    }
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ONBOARDING_COMPLETED",
                    "message": "Full asset and checklist update for cand_2",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_2",
                    "updates": {
                        "asset_update_status": "Completed"
                    }
                }
            }
        ],
        "outputs": [
                "asset.LT-002A.status=Available | asset.LT-002B.status=Assigned | asset_request.req_201.status=Completed | asset_request.req_202.status=Completed | access_check.access_201=Removed | access_check.access_202=Removed | access_check.access_203.status=Pending | access_check.access_204.status=Pending | attachment.Company-Policies.pdf.added=True | attachment.Benefits-Guide.pdf.added=True | email.email_201.labels=label_AssetUpdate | checklist_item.check_201.status=Completed | checklist_item.check_202.status=Completed | onboarding_files.ID-Card.pdf.status=Verified | onboarding_files.Driving-License.pdf.status=Verified | log.ONBOARDING_COMPLETED.message=Full asset and checklist update for cand_2 | candidate.cand_2.asset_update_status=Completed"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_020",
        "instruction": "Handle onboarding for candidate cand_5: authorize asset requests, allocate assets such as laptop, phone, and accessories, finalize checklist items, authorize access checks, revise onboarding files, label emails, and document terminal logs.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_502",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-005",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-005",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-006",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-KEYBOARD-004",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide_cand5.pdf",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan_cand5.pdf",
                    "updates": {
                        "verified": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_501",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_502",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_501",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_501",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_502",
                    "label_id": "label_Policy"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_501 and req_502 approved",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSETS_ASSIGNED",
                    "message": "Laptop, phone, mouse, and keyboard assigned",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELS_APPLIED",
                    "message": "Emails labeled 'Welcome' and 'Policy'",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_5",
                    "updates": {
                        "onboarding_status": "OnboardingCompleted"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_501.status=Approved | asset_request.req_502.status=Approved | asset.PH-LAPTOP-005.status=Assigned | asset.PH-IPHONE-005.status=Assigned | asset.ACC-MOUSE-006.status=Assigned | asset.ACC-KEYBOARD-004.status=Assigned | onboarding_files.welcome_guide_cand5.laptop_assigned=True | onboarding_files.welcome_guide_cand5.phone_assigned=True | onboarding_files.id_scan_cand5.verified=True | checklist.check_501.status=Completed | checklist.check_502.status=Completed | access_check.access_501.status=Approved | email.email_501.labels=label_Welcome | email.email_502.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_501 and req_502 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, mouse, and keyboard assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome' and 'Policy' | candidate.cand_5.onboarding_status=OnboardingCompleted"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "onboarding_ds_016",
        "instruction": "Oversee the entire multi-step onboarding for candidate cand_1: authorize all asset requests, allocate all assets, finalize all checklist items, authorize all access checks, update all onboarding files, apply multiple email labels, and document detailed terminal logs for each step. End state: all assets allocated, onboarding files revised, checklist items finalized, access checks authorized, emails labeled, and candidate status indicates full completion.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "req_102",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-LAPTOP-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-MOUSE-002",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_tag": "ACC-KEYBOARD-002",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/welcome_guide.pdf",
                    "updates": {
                        "laptop_assigned": true,
                        "phone_assigned": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/id_scan.pdf",
                    "updates": {
                        "verified": true
                    }
                },
            },
            {
                "name": "UpdateOnboardingFile",
                "arguments": {
                    "file_path": "files/policy_acknowledgment.pdf",
                    "updates": {
                        "acknowledged": true
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_101",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "check_102",
                    "updates": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_101",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateAccessCheck",
                "arguments": {
                    "check_id": "access_102",
                    "updates": {
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_101",
                    "label_id": "label_Welcome"
                },
            },
            {
                "name": "ApplyLabelToEmail",
                "arguments": {
                    "email_id": "email_102",
                    "label_id": "label_Policy"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSET_REQUEST_APPROVED",
                    "message": "Asset requests req_101 and req_102 approved",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ASSETS_ASSIGNED",
                    "message": "Laptop, phone, mouse, and keyboard assigned",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "CHECKLIST_COMPLETED",
                    "message": "Checklist items completed",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "ACCESS_CHECK_APPROVED",
                    "message": "Access checks approved",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "EMAIL_LABELS_APPLIED",
                    "message": "Emails labeled 'Welcome' and 'Policy'",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpdateCandidate",
                "arguments": {
                    "candidate_id": "cand_1",
                    "updates": {
                        "onboarding_status": "OnboardingCompleted"
                    }
                }
            }
        ],
        "outputs": [
                "asset_request.req_101.status=Approved | asset_request.req_102.status=Approved | asset.PH-LAPTOP-001.status=Assigned | asset.PH-IPHONE-001.status=Assigned | asset.ACC-MOUSE-002.status=Assigned | asset.ACC-KEYBOARD-002.status=Assigned | onboarding_files.welcome_guide.laptop_assigned=True | onboarding_files.welcome_guide.phone_assigned=True | onboarding_files.id_scan.verified=True | onboarding_files.policy_acknowledgment.acknowledged=True | checklist.check_101.status=Completed | checklist.check_102.status=Completed | access_check.access_101.status=Approved | access_check.access_102.status=Approved | email.email_101.labels=label_Welcome | email.email_102.labels=label_Policy | log.ASSET_REQUEST_APPROVED.message=Asset requests req_101 and req_102 approved | log.ASSETS_ASSIGNED.message=Laptop, phone, mouse, and keyboard assigned | log.CHECKLIST_COMPLETED.message=Checklist items completed | log.ACCESS_CHECK_APPROVED.message=Access checks approved | log.EMAIL_LABELS_APPLIED.message=Emails labeled 'Welcome' and 'Policy' | candidate.cand_1.onboarding_status=OnboardingCompleted"
        ]
    }
]
