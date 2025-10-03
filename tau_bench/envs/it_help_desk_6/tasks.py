
tasks = [
    {
        "annotator": it6,
        "user_id": "it_v6_task_01",
        "instruction": "Handle the onboarding process for Marketing\u2019s new Content Strategist, Devin Martinez (employee_id=emp_0024). Align the RBAC to the role baseline and verify the inclusion of the default license bundle from the RBAC map (lic_m365_e3, lic_salesforce, lic_slack_ent). Coordinate the provisioning of a managed laptop selected from in_stock inventory, using the policy tie-breakers, and monitor a deterministic pickup workflow. If capacity permits, optionally include CreativeWorks Creative Cloud as an added license. Provision TeamChat and WikiSpace app accounts. Anchor all writes to the 2025-07-16 onboarding window: lifecycle at 09:00Z, groups at 09:05Z, licenses at 09:06\u201309:09Z, device workflow at 09:10Z/10:00Z, apps at 09:12Z, and completion at 10:05Z.You must align RBAC to the role baseline and ensure the default license bundle from the RBAC map is present (lic_m365_e3, lic_salesforce, lic_slack_ent). You must provision a managed laptop selected from in_stock inventory using the policy tie\u2011breakers and track a deterministic pickup workflow. If capacity allows, you must add CreativeWorks Creative Cloud as an optional license. You must provision TeamChat and WikiSpace app accounts. Anchor all writes to the 2025-07-16 onboarding window: lifecycle at 09:00Z, groups at 09:05Z, licenses at 09:06\u201309:09Z, device workflow at 09:10Z/10:00Z, apps at 09:12Z, completion at 10:05Z.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00024",
                    "memo_id": "memo_onb_0024",
                    "employee_ref": "emp_0024",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-16T09:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_9071d5",
                    "group_ids": [],
                    "actor": "service_desk",
                    "timestamp": "2025-07-16T09:05:00+00:00"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_9071d5",
                    "group_ids": [
                        "grp_marketing_719b",
                        "grp_marketing_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-16T09:05:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0024",
                    "priority": "P2",
                    "created_at": "2025-07-16T09:06:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0024_lic_m365_e3",
                    "account_id": "acc_9071d5",
                    "employee_id": "emp_0024",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-16T09:06:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_salesforce-emp_0024",
                    "priority": "P2",
                    "created_at": "2025-07-16T09:07:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0024_lic_salesforce",
                    "account_id": "acc_9071d5",
                    "employee_id": "emp_0024",
                    "license_id": "lic_salesforce",
                    "assigned_at": "2025-07-16T09:07:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0024",
                    "priority": "P2",
                    "created_at": "2025-07-16T09:08:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0024_lic_slack_ent",
                    "account_id": "acc_9071d5",
                    "employee_id": "emp_0024",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-16T09:08:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_adobe_cc-emp_0024",
                    "priority": "P2",
                    "created_at": "2025-07-16T09:09:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0024_lic_adobe_cc",
                    "account_id": "acc_9071d5",
                    "employee_id": "emp_0024",
                    "license_id": "lic_adobe_cc",
                    "assigned_at": "2025-07-16T09:09:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0024_1",
                    "employee_id": "emp_0024",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0024_1",
                    "created_at": "2025-07-16T09:10:00+00:00",
                    "completed_at": "2025-07-16T10:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0024_slack",
                    "employee_id": "emp_0024",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2025-07-16T09:12:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0024_conf",
                    "employee_id": "emp_0024",
                    "app_id": "app_confluence",
                    "status": "active",
                    "created_at": "2025-07-16T09:12:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00024",
                    "status": "completed",
                    "timestamp": "2025-07-16T10:05:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "lic_adobe_cc",
                "acc_9071d5"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_02",
        "instruction": "Complete the onboarding for Riley Wang (employee_id=emp_0011, Support Manager). Apply the baseline RBAC, ensure core licenses are in place, provision a laptop from in_stock with MDM pickup, and grant access to the TaskTrack app. Use the timestamp 2025-07-16T11:02:00+00:00 for all time-related tasks deterministically.You must apply baseline RBAC, ensure core licenses, provision an in_stock laptop with MDM pickup, and add TaskTrack app access and use timestamps 2025-07-16T11:02:00+00:00 for all tiem realted things deterministically.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00011",
                    "memo_id": "memo_onb_emp_0011",
                    "employee_ref": "emp_0011",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-16T11:02:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Support",
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_51e138",
                    "group_ids": [
                        "grp_support_ada3",
                        "grp_support_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-16T11:02:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0011",
                    "priority": "P2",
                    "created_at": "2025-07-16T11:02:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0011_lic_m365_e3",
                    "account_id": "acc_51e138",
                    "employee_id": "emp_0011",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-16T11:02:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0011",
                    "priority": "P2",
                    "created_at": "2025-07-16T11:02:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0011_lic_slack_ent",
                    "account_id": "acc_51e138",
                    "employee_id": "emp_0011",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-16T11:02:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0011_1",
                    "employee_id": "emp_0011",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0011_1",
                    "created_at": "2025-07-16T11:02:00+00:00",
                    "completed_at": "2025-07-16T11:02:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0011_jira",
                    "employee_id": "emp_0011",
                    "app_id": "app_jira",
                    "status": "active",
                    "created_at": "2025-07-16T11:02:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00011",
                    "status": "completed",
                    "timestamp": "2025-07-16T11:02:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "acc_51e138"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_03",
        "instruction": "Handle the onboarding hardware tasks for Casey Liu (employee_id=emp_0002, Marketing Content Strategist). Align RBAC, allocate the baseline license bundle, provide an in_stock laptop using the pickup workflow, and verify TeamChat & WikiSpace app accounts.You will align RBAC, assign the baseline license bundle, provide an in_stock laptop with pickup workflow, and confirm TeamChat & WikiSpace app accounts.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00002",
                    "memo_id": "memo_onb_emp_0002",
                    "employee_ref": "emp_0002",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-16T13:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_287fb8",
                    "group_ids": [
                        "grp_marketing_719b",
                        "grp_marketing_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-16T13:02:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0002",
                    "priority": "P2",
                    "created_at": "2025-07-16T13:02:30+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0002_lic_m365_e3",
                    "account_id": "acc_287fb8",
                    "employee_id": "emp_0002",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-16T13:02:35+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_salesforce-emp_0002",
                    "priority": "P2",
                    "created_at": "2025-07-16T13:02:40+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0002_lic_salesforce",
                    "account_id": "acc_287fb8",
                    "employee_id": "emp_0002",
                    "license_id": "lic_salesforce",
                    "assigned_at": "2025-07-16T13:02:45+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0002",
                    "priority": "P2",
                    "created_at": "2025-07-16T13:02:50+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0002_lic_slack_ent",
                    "account_id": "acc_287fb8",
                    "employee_id": "emp_0002",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-16T13:02:55+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0002_1",
                    "employee_id": "emp_0002",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0002_1",
                    "created_at": "2025-07-16T13:05:00+00:00",
                    "completed_at": "2025-07-16T14:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0002_slack",
                    "employee_id": "emp_0002",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2025-07-16T13:06:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0002_conf",
                    "employee_id": "emp_0002",
                    "app_id": "app_confluence",
                    "status": "active",
                    "created_at": "2025-07-16T13:06:30+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00002",
                    "status": "completed",
                    "timestamp": "2025-07-16T14:05:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "acc_287fb8"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_04",
        "instruction": "Coordinate the provisioning for HR Recruiter Remy Clark (employee_id=emp_0020) by setting up baseline groups, assigning baseline licenses, delivering a laptop, and establishing the TeamChat app account. Follow the in_stock selection policy, and monitor provisioning using a deterministic pickup code.Follow in_stock selection policy; track provisioning with a deterministic pickup code.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00020",
                    "memo_id": "memo_onb_emp_0020",
                    "employee_ref": "emp_0020",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-16T15:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "HR",
                    "job_title": "Recruiter"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_401a71",
                    "group_ids": [
                        "grp_hr_92d4",
                        "grp_hr_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-16T15:02:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0020",
                    "priority": "P2",
                    "created_at": "2025-07-16T15:02:30+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0020_lic_m365_e3",
                    "account_id": "acc_401a71",
                    "employee_id": "emp_0020",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-16T15:02:35+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0020",
                    "priority": "P2",
                    "created_at": "2025-07-16T15:02:40+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0020_lic_slack_ent",
                    "account_id": "acc_401a71",
                    "employee_id": "emp_0020",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-16T15:02:45+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0020_1",
                    "employee_id": "emp_0020",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0020_1",
                    "created_at": "2025-07-16T15:05:00+00:00",
                    "completed_at": "2025-07-16T16:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0020_slack",
                    "employee_id": "emp_0020",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2025-07-16T15:06:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00020",
                    "status": "completed",
                    "timestamp": "2025-07-16T16:05:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "acc_401a71"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_05",
        "instruction": "Ensure the completion of onboarding for Operations Manager Wyatt Adams (employee_id=emp_0035): baseline RBAC, baseline licenses, laptop provisioning, TeamChat & TaskTrack app access.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00035",
                    "memo_id": "memo_onb_emp_0035",
                    "employee_ref": "emp_0035",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-16T17:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Operations",
                    "job_title": "Operations Manager"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_d89d5c",
                    "group_ids": [
                        "grp_operations_9079",
                        "grp_operations_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-16T17:02:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0035",
                    "priority": "P2",
                    "created_at": "2025-07-16T17:02:30+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0035_lic_m365_e3",
                    "account_id": "acc_d89d5c",
                    "employee_id": "emp_0035",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-16T17:02:35+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0035",
                    "priority": "P2",
                    "created_at": "2025-07-16T17:02:40+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0035_lic_slack_ent",
                    "account_id": "acc_d89d5c",
                    "employee_id": "emp_0035",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-16T17:02:45+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0035_1",
                    "employee_id": "emp_0035",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0035_1",
                    "created_at": "2025-07-16T17:05:00+00:00",
                    "completed_at": "2025-07-16T18:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0035_slack",
                    "employee_id": "emp_0035",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2025-07-16T17:06:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0035_jira",
                    "employee_id": "emp_0035",
                    "app_id": "app_jira",
                    "status": "active",
                    "created_at": "2025-07-16T17:06:30+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00035",
                    "status": "completed",
                    "timestamp": "2025-07-16T18:05:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "acc_d89d5c"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_06",
        "instruction": "Facilitate the onboarding of Engineering Software Engineer Nico Turner (employee_id=emp_0037) with baseline groups, baseline licenses, a laptop, and CodeHub/TaskTrack app access.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00037",
                    "memo_id": "memo_onb_emp_0037",
                    "employee_ref": "emp_0037",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-17T09:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0037"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0037"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Engineering",
                    "job_title": "Software Engineer"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_451983",
                    "group_ids": [
                        "grp_engineering_cbaf",
                        "grp_engineering_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-17T09:02:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0037",
                    "priority": "P2",
                    "created_at": "2025-07-17T09:02:30+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0037_lic_m365_e3",
                    "account_id": "acc_451983",
                    "employee_id": "emp_0037",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-17T09:02:35+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_github_ent-emp_0037",
                    "priority": "P2",
                    "created_at": "2025-07-17T09:02:40+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0037_lic_github_ent",
                    "account_id": "acc_451983",
                    "employee_id": "emp_0037",
                    "license_id": "lic_github_ent",
                    "assigned_at": "2025-07-17T09:02:45+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0037",
                    "priority": "P2",
                    "created_at": "2025-07-17T09:02:50+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0037_lic_slack_ent",
                    "account_id": "acc_451983",
                    "employee_id": "emp_0037",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-17T09:02:55+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0037"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0037_1",
                    "employee_id": "emp_0037",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0037_1",
                    "created_at": "2025-07-17T09:05:00+00:00",
                    "completed_at": "2025-07-17T10:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0037_gh",
                    "employee_id": "emp_0037",
                    "app_id": "app_github",
                    "status": "active",
                    "created_at": "2025-07-17T09:06:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0037_jira",
                    "employee_id": "emp_0037",
                    "app_id": "app_jira",
                    "status": "active",
                    "created_at": "2025-07-17T09:06:30+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00037",
                    "status": "completed",
                    "timestamp": "2025-07-17T10:05:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "acc_451983"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_07",
        "instruction": "Handle the onboarding of Sales Manager Alex Park (employee_id=emp_0006) by providing a managed phone from in_stock, developing a deterministic pickup workflow, and activating TeamChat & CloudCRM apps, which include baseline licenses.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00006",
                    "memo_id": "memo_onb_emp_0006",
                    "employee_ref": "emp_0006",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-17T11:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0006"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0006"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Sales",
                    "job_title": "Sales Manager"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0006",
                    "priority": "P2",
                    "created_at": "2025-07-17T11:02:30+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0006_lic_m365_e3",
                    "account_id": "acc_e7e9ee",
                    "employee_id": "emp_0006",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-17T11:02:35+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_salesforce-emp_0006",
                    "priority": "P2",
                    "created_at": "2025-07-17T11:02:40+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0006_lic_salesforce",
                    "account_id": "acc_e7e9ee",
                    "employee_id": "emp_0006",
                    "license_id": "lic_salesforce",
                    "assigned_at": "2025-07-17T11:02:45+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0006",
                    "priority": "P2",
                    "created_at": "2025-07-17T11:02:50+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0006_lic_slack_ent",
                    "account_id": "acc_e7e9ee",
                    "employee_id": "emp_0006",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-17T11:02:55+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "phone",
                    "status": "in_stock",
                    "mdm_enrolled": true
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0016",
                    "employee_id": "emp_0006"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0006_1",
                    "employee_id": "emp_0006",
                    "asset_id": "ast_0016",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0006_1",
                    "created_at": "2025-07-17T11:05:00+00:00",
                    "completed_at": "2025-07-17T12:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0006_slack",
                    "employee_id": "emp_0006",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2025-07-17T11:06:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0006_sf",
                    "employee_id": "emp_0006",
                    "app_id": "app_salesforce",
                    "status": "active",
                    "created_at": "2025-07-17T11:06:30+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00006",
                    "status": "completed",
                    "timestamp": "2025-07-17T12:05:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0016",
                "acc_e7e9ee"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_08",
        "instruction": "Coordinate the completion of onboarding for Finance Controller Dakota Wilson (employee_id=emp_0017) by supplying a laptop according to policy, assigning baseline licenses, setting up a mailbox with finance retention, and setting up accounts for the WikiSpace and TaskTrack apps.assigning baseline licenses, creating a mailbox with finance retention, and provisioning WikiSpace and TaskTrack app accounts.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00017",
                    "memo_id": "memo_onb_emp_0017",
                    "employee_ref": "emp_0017",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-17T13:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Finance",
                    "job_title": "Controller"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0017",
                    "priority": "P2",
                    "created_at": "2025-07-17T13:02:30+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0017_lic_m365_e3",
                    "account_id": "acc_82aecf",
                    "employee_id": "emp_0017",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-17T13:02:35+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0017",
                    "priority": "P2",
                    "created_at": "2025-07-17T13:02:40+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0017_lic_slack_ent",
                    "account_id": "acc_82aecf",
                    "employee_id": "emp_0017",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-17T13:02:45+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0017_1",
                    "employee_id": "emp_0017",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0017_1",
                    "created_at": "2025-07-17T13:05:00+00:00",
                    "completed_at": "2025-07-17T14:00:00+00:00"
                },
            },
            {
                "name": "CreateMailbox",
                "arguments": {
                    "mailbox_id": "mbx_onb_0017",
                    "employee_id": "emp_0017",
                    "address": "dakota.wilson@example.com",
                    "retention_policy": "finance_7y",
                    "created_at": "2025-07-17T13:05:30+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0017_conf",
                    "employee_id": "emp_0017",
                    "app_id": "app_confluence",
                    "status": "active",
                    "created_at": "2025-07-17T13:06:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0017_jira",
                    "employee_id": "emp_0017",
                    "app_id": "app_jira",
                    "status": "active",
                    "created_at": "2025-07-17T13:06:30+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00017",
                    "status": "completed",
                    "timestamp": "2025-07-17T14:05:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "acc_82aecf"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_09",
        "instruction": "Ensure Noel Rodriguez (employee_id=emp_0031, Marketing Content Strategist) is brought to baseline. RBAC memberships must be derived from the RBAC baseline for Marketing/Content Strategist, and verify the assignment of the role\u2019s default license bundle. Select a managed laptop from in_stock inventory using policy tie-breakers with a deterministic pickup workflow, then provision app accounts for the baseline collaboration and sales apps (TeamChat and CloudCRM). All write timestamps must be deterministically derived from emp_0031\u2019s directory account created_at (2023-07-18T09:00:00+00:00); don't introduce other times.You must derive RBAC memberships from the RBAC baseline for Marketing/Content Strategist and ensure the role\u2019s default license bundle is assigned. You must provision a managed laptop selected from in_stock inventory using the policy tie\u2011breakers with a deterministic pickup workflow, and you must provision app accounts for the baseline collaboration and sales apps (TeamChat and CloudCRM). You must derive all write timestamps deterministically from emp_0031\u2019s directory account created_at (2023-07-18T09:00:00+00:00); do not introduce other times.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00031",
                    "memo_id": "memo_onb_emp_0031",
                    "employee_ref": "emp_0031",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "group_ids": [
                        "grp_marketing_719b",
                        "grp_marketing_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0031",
                    "priority": "P2",
                    "created_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0031_lic_m365_e3",
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_salesforce-emp_0031",
                    "priority": "P2",
                    "created_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0031_lic_salesforce",
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_salesforce",
                    "assigned_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0031",
                    "priority": "P2",
                    "created_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0031_lic_slack_ent",
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0031_1",
                    "employee_id": "emp_0031",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0031_1",
                    "created_at": "2023-07-18T09:00:00+00:00",
                    "completed_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0031_slack",
                    "employee_id": "emp_0031",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0031_sf",
                    "employee_id": "emp_0031",
                    "app_id": "app_salesforce",
                    "status": "active",
                    "created_at": "2023-07-18T09:00:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00031",
                    "status": "completed",
                    "timestamp": "2023-07-18T09:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "acc_351bb4"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_10",
        "instruction": "Finalize onboarding for Jesse Moore (employee_id=emp_0027, Marketing Growth Marketer) by completing baseline groups, baseline licenses, CreativeWorks optional license if capacity allows, a laptop per policy, and app accounts for all licensed apps (Slack, CloudCRM, CreativeWorks).CreativeWorks optional license if capacity, laptop per policy, and app accounts for all licensed apps (Slack, CloudCRM, CreativeWorks).",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00027",
                    "memo_id": "memo_onb_emp_0027",
                    "employee_ref": "emp_0027",
                    "event": "onboarding",
                    "status": "queued",
                    "created_at": "2025-07-17T17:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0027"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0027"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_5494f2",
                    "group_ids": [
                        "grp_marketing_231e",
                        "grp_marketing_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-17T17:02:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0027",
                    "priority": "P2",
                    "created_at": "2025-07-17T17:02:30+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0027_lic_m365_e3",
                    "account_id": "acc_5494f2",
                    "employee_id": "emp_0027",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-07-17T17:02:35+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_salesforce-emp_0027",
                    "priority": "P2",
                    "created_at": "2025-07-17T17:02:40+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0027_lic_salesforce",
                    "account_id": "acc_5494f2",
                    "employee_id": "emp_0027",
                    "license_id": "lic_salesforce",
                    "assigned_at": "2025-07-17T17:02:45+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0027",
                    "priority": "P2",
                    "created_at": "2025-07-17T17:02:50+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0027_lic_slack_ent",
                    "account_id": "acc_5494f2",
                    "employee_id": "emp_0027",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-07-17T17:02:55+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_adobe_cc-emp_0027",
                    "priority": "P2",
                    "created_at": "2025-07-17T17:03:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0027_lic_adobe_cc",
                    "account_id": "acc_5494f2",
                    "employee_id": "emp_0027",
                    "license_id": "lic_adobe_cc",
                    "assigned_at": "2025-07-17T17:04:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0027"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_onb_0027_1",
                    "employee_id": "emp_0027",
                    "asset_id": "ast_0013",
                    "process": "provisioning",
                    "status": "completed",
                    "pickup_code": "pc_dwf_onb_0027_1",
                    "created_at": "2025-07-17T17:05:00+00:00",
                    "completed_at": "2025-07-17T18:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0027_slack",
                    "employee_id": "emp_0027",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2025-07-17T17:06:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0027_sf",
                    "employee_id": "emp_0027",
                    "app_id": "app_salesforce",
                    "status": "active",
                    "created_at": "2025-07-17T17:06:30+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0027_adobe",
                    "employee_id": "emp_0027",
                    "app_id": "app_adobe_cc",
                    "status": "active",
                    "created_at": "2025-07-17T17:07:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_onb_00027",
                    "status": "completed",
                    "timestamp": "2025-07-17T18:05:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013",
                "lic_adobe_cc",
                "acc_5494f2"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_11",
        "instruction": "Handle the offboarding of Operations Manager Sawyer Harris (employee_id=emp_0019) according to standard policy. Anchor all writes deterministically to the directory account created_at (2023-10-24T09:00:00+00:00); derive identifiers exclusively from stable IDs. Implement identity disablement, align RBAC to empty with audited removals, revoke active baseline licenses, honor mailbox retention (std_2y), and adjust TeamChat app access based on current state. Record manager notification and complete the lifecycle; avoid detailing steps beyond these policy outcomes.Anchor all writes deterministically to the directory account created_at (2023-10-24T09:00:00+00:00); derive identifiers from stable IDs only. Apply identity disable, align RBAC to empty with audited removals, revoke active baseline licenses, honor mailbox retention (std_2y), and reflect TeamChat app access based on current state. Record manager notification and complete the lifecycle; do not enumerate steps beyond these policy outcomes.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00019",
                    "memo_id": "memo_offb_emp_0019",
                    "employee_ref": "emp_0019",
                    "event": "offboarding",
                    "status": "queued",
                    "created_at": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "UpdateDirectoryAccountStatus",
                "arguments": {
                    "account_id": "acc_1d0980",
                    "status": "disabled",
                    "disabled_at": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_1d0980",
                    "group_ids": [
                        "grp_operations_9079"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_1d0980",
                    "group_ids": [
                        "grp_operations_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_1d0980",
                    "group_ids": [],
                    "actor": "service_desk",
                    "timestamp": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_1d0980",
                    "employee_id": "emp_0019",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_1d0980",
                    "employee_id": "emp_0019",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_offb_emp_0019",
                    "mailbox_id": "mbx_1d0980",
                    "employee_id": "emp_0019",
                    "archive_path": "s3://corp-archives/mail/emp_0019/2023-10-24",
                    "retention_policy": "std_2y",
                    "created_at": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0019",
                    "app_id": "app_slack"
                },
            },
            {
                "name": "DisableAppAccount",
                "arguments": {
                    "app_account_id": "appacc_fef353",
                    "disabled_at": "2023-10-24T09:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00019",
                    "event": "manager_notified",
                    "timestamp": "2023-10-24T09:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00019",
                    "status": "completed",
                    "timestamp": "2023-10-24T09:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "acc_1d0980",
                "mbx_1d0980"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_12",
        "instruction": "Coordinate the offboarding of Marketing Growth Marketer River Thompson (employee_id=emp_0032) in accordance with standard policy, anchored deterministically to the directory account created_at (2023-12-24T09:00:00+00:00). Derive identifiers from the employee id; ensure RBAC changes are auditable, license posture is corrected, device handling is recorded deterministically, retention is honored, and app access changes mirror the current state for collaboration and productivity applications.Derive identifiers from the employee id; ensure RBAC changes are auditable, license posture is corrected, device handling is recorded deterministically, retention is honored, and app access changes reflect current state for collaboration and productivity apps.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00032",
                    "memo_id": "memo_offb_emp_0032",
                    "employee_ref": "emp_0032",
                    "event": "offboarding",
                    "status": "queued",
                    "created_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "UpdateDirectoryAccountStatus",
                "arguments": {
                    "account_id": "acc_f06213",
                    "status": "disabled",
                    "disabled_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_f06213",
                    "group_ids": [
                        "grp_marketing_231e"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_f06213",
                    "group_ids": [
                        "grp_marketing_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_f06213",
                    "employee_id": "emp_0032",
                    "license_id": "lic_salesforce",
                    "revoked_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_f06213",
                    "employee_id": "emp_0032",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_f06213",
                    "employee_id": "emp_0032",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0032"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00032",
                    "event": "device_none_assigned",
                    "timestamp": "2023-12-24T09:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_slack"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00032",
                    "event": "app_slack_none",
                    "timestamp": "2023-12-24T09:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00032",
                    "event": "no_m365_app_account",
                    "timestamp": "2023-12-24T09:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_offb_emp_0032",
                    "mailbox_id": "mbx_f06213",
                    "employee_id": "emp_0032",
                    "archive_path": "s3://corp-archives/mail/emp_0032/2023-12-24",
                    "retention_policy": "std_2y",
                    "created_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_salesforce"
                },
            },
            {
                "name": "DisableAppAccount",
                "arguments": {
                    "app_account_id": "appacc_dfb864",
                    "disabled_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_github"
                },
            },
            {
                "name": "DisableAppAccount",
                "arguments": {
                    "app_account_id": "appacc_f69e6a",
                    "disabled_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_confluence"
                },
            },
            {
                "name": "DisableAppAccount",
                "arguments": {
                    "app_account_id": "appacc_6fc5eb",
                    "disabled_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_jira"
                },
            },
            {
                "name": "DisableAppAccount",
                "arguments": {
                    "app_account_id": "appacc_7b53ec",
                    "disabled_at": "2023-12-24T09:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00032",
                    "event": "manager_notified",
                    "timestamp": "2023-12-24T09:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00032",
                    "status": "completed",
                    "timestamp": "2023-12-24T09:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "acc_f06213",
                "mbx_f06213"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_13",
        "instruction": "Handle the offboarding of Marketing Content Strategist Devin Martinez (employee_id=emp_0024) following identity, RBAC, licensing, device, and retention policies. Base all writes on the determined date, 2025-07-20, and utilize both employee_id and anchors for generating identifiers and pickup codes. During the specified time frame, ensure to use the anchor timestamp (11:00:00Z) for all write operations; however, the device return entry should exclusively use its scheduled due time (2025-07-27T17:00:00+00:00) set as created_at in accordance with the policy. Avoid hard-coding database internals beyond necessary policy-anchored timestamps and due times.Anchor all writes deterministically to 2025-07-20 and derive identifiers and pickup codes from employee_id and anchors. Within the anchored window, you must use the anchor timestamp (11:00:00Z) for all writes; only the scheduled device return entry uses its due time (2025-07-27T17:00:00+00:00) as created_at by policy. Do not hard\u2011code database internals beyond policy\u2011required anchors and due times.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00024",
                    "memo_id": "memo_offb_emp_0024",
                    "employee_ref": "emp_0024",
                    "event": "offboarding",
                    "status": "queued",
                    "created_at": "2025-07-20T11:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "UpdateDirectoryAccountStatus",
                "arguments": {
                    "account_id": "acc_9071d5",
                    "status": "disabled",
                    "disabled_at": "2025-07-20T11:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_9071d5",
                    "group_ids": [
                        "grp_marketing_719b"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-20T11:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_9071d5",
                    "group_ids": [
                        "grp_marketing_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-20T11:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_9071d5",
                    "employee_id": "emp_0024",
                    "license_id": "lic_salesforce",
                    "revoked_at": "2025-07-20T11:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_9071d5",
                    "employee_id": "emp_0024",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-20T11:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_9071d5",
                    "employee_id": "emp_0024",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-20T11:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0024"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_ret_emp_0024_ast_0056_req",
                    "employee_id": "emp_0024",
                    "asset_id": "ast_0056",
                    "process": "return",
                    "status": "requested",
                    "pickup_code": "pc_ret_emp_0024_ast_0056",
                    "created_at": "2025-07-20T11:00:00+00:00",
                    "completed_at": null
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_ret_emp_0024_ast_0056_due",
                    "employee_id": "emp_0024",
                    "asset_id": "ast_0056",
                    "process": "return_due",
                    "status": "scheduled",
                    "pickup_code": "pc_ret_emp_0024_ast_0056",
                    "created_at": "2025-07-27T17:00:00+00:00",
                    "completed_at": null
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_offb_emp_0024",
                    "mailbox_id": "mbx_9071d5",
                    "employee_id": "emp_0024",
                    "archive_path": "s3://corp-archives/mail/emp_0024/2025-07-20",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-20T11:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00024",
                    "event": "manager_notified",
                    "timestamp": "2025-07-20T11:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00024",
                    "status": "completed",
                    "timestamp": "2025-07-20T11:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0056",
                "mbx_9071d5"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_14",
        "instruction": "Execute license posture maintenance for Marketing\u2019s Content Strategist Tatum Green (employee_id=emp_0034). Base all record updates on the license audit timestamp, 2025-07-15T08:00:00+00:00. You are required to deterministically revoke active baseline licenses from the directory account and reflect these inventory updates. Ensure no modifications are made to RBAC, devices, or mailboxes. Record a deterministic TaskTrack maintenance entry (priority=P2, status=Closed), which should be generated using the anchor and employee id.Anchor all writes to the license audit time 2025-07-15T08:00:00+00:00. You must deterministically revoke any active baseline licenses from the directory account and reflect inventory updates. Do not modify RBAC, devices, or mailboxes. You must register a deterministic TaskTrack maintenance record (priority=P2, status=Closed) derived from the anchor and employee id.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_baacc3",
                    "employee_id": "emp_0034",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_baacc3",
                    "employee_id": "emp_0034",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_baacc3",
                    "employee_id": "emp_0034",
                    "license_id": "lic_salesforce",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "JIRA-lic_maint-emp_0034-2025_07_15_0800",
                    "issue_type": "Maintenance",
                    "summary": "license_maintenance_emp_0034_2025_07_15_0800",
                    "priority": "P2",
                    "status": "Closed",
                    "created_at": "2025-07-15T08:00:00+00:00",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "acc_baacc3"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_15",
        "instruction": "Handle the offboarding of Engineering DevOps Engineer Zion Mitchell (employee_id=emp_0036) concerning identity, RBAC, licensing, device, and retention policy. Anchor all writes deterministically to the directory account created_at (2024-06-21T09:00:00+00:00). Utilize a single scheduled device return entry at due 2025-07-29T17:00:00+00:00 (policy: the scheduled return uses the due time as created_at), enforce std_2y mailbox retention with a path derived from the anchor date, and make sure RBAC/license posture and lifecycle handling are compliant. Derive the workflow identifier and pickup code deterministically from employee_id and asset_id; avoid reliance on random values or hard-coded database internals.Anchor all writes deterministically to the directory account created_at (2024-06-21T09:00:00+00:00). Use a single scheduled device return entry at due 2025-07-29T17:00:00+00:00 (policy: the scheduled return uses the due time as created_at), apply std_2y mailbox retention with a path derived from the anchor date, and ensure RBAC/license posture and lifecycle handling are compliant. Derive the workflow identifier and pickup code deterministically from employee_id and asset_id; do not rely on random values or hard\u2011coded database internals.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00036",
                    "memo_id": "memo_offb_emp_0036",
                    "employee_ref": "emp_0036",
                    "event": "offboarding",
                    "status": "queued",
                    "created_at": "2024-06-21T09:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "UpdateDirectoryAccountStatus",
                "arguments": {
                    "account_id": "acc_f9a6bc",
                    "status": "disabled",
                    "disabled_at": "2024-06-21T09:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_f9a6bc",
                    "group_ids": [
                        "grp_engineering_4162"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2024-06-21T09:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_f9a6bc",
                    "group_ids": [
                        "grp_engineering_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2024-06-21T09:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_f9a6bc",
                    "employee_id": "emp_0036",
                    "license_id": "lic_github_ent",
                    "revoked_at": "2024-06-21T09:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_f9a6bc",
                    "employee_id": "emp_0036",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2024-06-21T09:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_f9a6bc",
                    "employee_id": "emp_0036",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2024-06-21T09:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0036"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_ret_emp_0036_ast_0055_due",
                    "employee_id": "emp_0036",
                    "asset_id": "ast_0055",
                    "process": "return_due",
                    "status": "scheduled",
                    "pickup_code": "pc_ret_emp_0036_ast_0055",
                    "created_at": "2025-07-29T17:00:00+00:00",
                    "completed_at": null
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_offb_emp_0036",
                    "mailbox_id": "mbx_f9a6bc",
                    "employee_id": "emp_0036",
                    "archive_path": "s3://corp-archives/mail/emp_0036/2024-06-21",
                    "retention_policy": "std_2y",
                    "created_at": "2024-06-21T09:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00036",
                    "event": "manager_notified",
                    "timestamp": "2024-06-21T09:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00036",
                    "status": "completed",
                    "timestamp": "2024-06-21T09:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0055",
                "mbx_f9a6bc"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_16",
        "instruction": "Coordinate the offboarding of Support Manager Briar Campbell (employee_id=emp_0039) in line with identity, RBAC, licensing, device, and retention policy. Anchor all writes to 2025-07-20T14:00:00+00:00 and schedule the assigned device return due on 2025-07-30T17:00:00+00:00 (the scheduled entry uses the due time as its created_at). Apply std_2y mailbox retention with an archive path derived from the anchor date, and ensure that all directory access changes are auditable. You must anchor all writes to 2025-07-20T14:00:00+00:00 and you must schedule the assigned device return due on 2025-07-30T17:00:00+00:00 (the scheduled entry uses the due time as its created_at). You must apply std_2y mailbox retention with an archive path derived from the anchor date, and you must ensure all directory access changes are auditable.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00039",
                    "memo_id": "memo_offb_emp_0039",
                    "employee_ref": "emp_0039",
                    "event": "offboarding",
                    "status": "queued",
                    "created_at": "2025-07-20T14:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "UpdateDirectoryAccountStatus",
                "arguments": {
                    "account_id": "acc_c42c15",
                    "status": "disabled",
                    "disabled_at": "2025-07-20T14:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_c42c15",
                    "group_ids": [
                        "grp_support_ada3"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-20T14:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_c42c15",
                    "group_ids": [
                        "grp_support_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-20T14:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_c42c15",
                    "employee_id": "emp_0039",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-20T14:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_c42c15",
                    "employee_id": "emp_0039",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-20T14:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0039"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_ret_0039_1",
                    "employee_id": "emp_0039",
                    "asset_id": "ast_0010",
                    "process": "return_due",
                    "status": "scheduled",
                    "pickup_code": null,
                    "created_at": "2025-07-30T17:00:00+00:00",
                    "completed_at": null
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_offb_emp_0039",
                    "mailbox_id": "mbx_c42c15",
                    "employee_id": "emp_0039",
                    "archive_path": "s3://corp-archives/mail/emp_0039/2025-07-20",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-20T14:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00039",
                    "event": "manager_notified",
                    "timestamp": "2025-07-20T14:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00039",
                    "status": "completed",
                    "timestamp": "2025-07-20T14:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0010",
                "mbx_c42c15"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_17",
        "instruction": "Manage the offboarding of Sales Manager Kai Jackson (employee_id=emp_0028). Disable sign-in, remove from groups, revoke CloudCRM/Slack/M365 access, and initiate dock return (to be completed by 2025-07-30 17:00 UTC). Archive the mailbox (std_2y) and disable the TeamChat app account. Utilize deterministic anchors: lifecycle_id=lcq_offb_00028; memo_id=memo_offb_emp_0028; archive_id=arch_offb_emp_0028; archive_path=s3://corp-archives/mail/emp_0028/2025-07-20. Ensure all updates are anchored to 2025-07-20: created_at=15:00:00Z, disabled_at=15:01:00Z, groups timestamp=15:02:00Z, revoke CloudCRM=15:03:00Z, revoke TeamChat=15:03:30Z, revoke M365=15:04:00Z. Create the return request with created_at=15:04:30Z, workflow_id=dwf_ret_0028_1, and pickup_code=pc_ret_0028_1. Schedule the return with due_ts=2025-07-30T17:00:00+00:00 as a second entry, workflow_id=dwf_ret_0028_2, using the same pickup_code. Set the archive created_at=15:05:00Z, disable TeamChat app at 15:05:30Z, notify manager at 15:06:00Z, and complete at 15:07:00Z.Disable sign\u2011in, clear groups, revoke CloudCRM/Slack/M365, request dock return (due by 2025-07-30 17:00 UTC), archive mailbox (std_2y), and disable TeamChat app account.Use deterministic anchors: lifecycle_id=lcq_offb_00028; memo_id=memo_offb_emp_0028; archive_id=arch_offb_emp_0028; archive_path=s3://corp-archives/mail/emp_0028/2025-07-20; all writes anchored to 2025-07-20: created_at=15:00:00Z, disabled_at=15:01:00Z, groups timestamp=15:02:00Z, revoke CloudCRM=15:03:00Z, revoke TeamChat=15:03:30Z, revoke M365=15:04:00Z; return request created_at=15:04:30Z with workflow_id=dwf_ret_0028_1 and pickup_code=pc_ret_0028_1; schedule the return at due_ts=2025-07-30T17:00:00+00:00 as a second entry workflow_id=dwf_ret_0028_2 with the same pickup_code; archive created_at=15:05:00Z, TeamChat app disable at 15:05:30Z, manager_notified=15:06:00Z, completed=15:07:00Z.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00028",
                    "memo_id": "memo_offb_emp_0028",
                    "employee_ref": "emp_0028",
                    "event": "offboarding",
                    "status": "queued",
                    "created_at": "2025-07-20T15:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "UpdateDirectoryAccountStatus",
                "arguments": {
                    "account_id": "acc_81d8d5",
                    "status": "disabled",
                    "disabled_at": "2025-07-20T15:01:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_81d8d5",
                    "group_ids": [
                        "grp_sales_4bcb",
                        "grp_sales_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-20T15:02:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_81d8d5",
                    "employee_id": "emp_0028",
                    "license_id": "lic_salesforce",
                    "revoked_at": "2025-07-20T15:03:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_81d8d5",
                    "employee_id": "emp_0028",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-20T15:03:30+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_81d8d5",
                    "employee_id": "emp_0028",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-20T15:04:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0028"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_ret_0028_1",
                    "employee_id": "emp_0028",
                    "asset_id": "ast_0028",
                    "process": "return",
                    "status": "requested",
                    "pickup_code": "pc_ret_0028_1",
                    "created_at": "2025-07-20T15:04:30+00:00",
                    "completed_at": null
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_ret_0028_2",
                    "employee_id": "emp_0028",
                    "asset_id": "ast_0028",
                    "process": "return_due",
                    "status": "scheduled",
                    "pickup_code": "pc_ret_0028_1",
                    "created_at": "2025-07-30T17:00:00+00:00",
                    "completed_at": null
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_offb_emp_0028",
                    "mailbox_id": "mbx_81d8d5",
                    "employee_id": "emp_0028",
                    "archive_path": "s3://corp-archives/mail/emp_0028/2025-07-20",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-20T15:05:00+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0028",
                    "app_id": "app_slack"
                },
            },
            {
                "name": "DisableAppAccount",
                "arguments": {
                    "app_account_id": "appacc_a3d740",
                    "disabled_at": "2025-07-20T15:05:30+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00028",
                    "event": "manager_notified",
                    "timestamp": "2025-07-20T15:06:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00028",
                    "status": "completed",
                    "timestamp": "2025-07-20T15:07:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0028",
                "mbx_81d8d5"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_18",
        "instruction": "Coordinate the license posture maintenance for Engineering's DevOps Engineer Micah White (employee_id=emp_0030) under the license-governance policy. Anchor all updates to the license audit time 2025-07-15T08:00:00+00:00. Confirm current assignments, strictly adhere to capacity limits, and record changes deterministically. Remove collaboration licenses that are not essential for the position (TeamChat Enterprise and TechSoft 365 E3). Avoid any modifications to RBAC, mailbox, devices, or app accounts. Log a maintenance record in TaskTrack with issue_type=Maintenance and priority=P2, progressing from New\u2192In Progress\u2192Resolved at the anchor.Anchor all writes to the license audit time 2025-07-15T08:00:00+00:00. Validate current assignments, operate strictly within capacity, and record the change deterministically. You must revoke collaboration licenses that are not required for the role (TeamChat Enterprise and TechSoft 365 E3). Do not modify RBAC, mailbox, devices, or app accounts. Register a maintenance record in TaskTrack with issue_type=Maintenance and priority=P2, following New\u2192In Progress\u2192Resolved at the anchor.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_db017d",
                    "employee_id": "emp_0030",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_db017d",
                    "employee_id": "emp_0030",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "JIRA-lic_cleanup-emp_0030-2025_07_15_0800",
                    "issue_type": "Maintenance",
                    "summary": "license_revoke;licenses=lic_slack_ent,lic_m365_e3;employee=emp_0030;audit=2025-07-15T08:00:00+00:00",
                    "priority": "P2",
                    "status": "New",
                    "created_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "JIRA-lic_cleanup-emp_0030-2025_07_15_0800",
                    "status": "In Progress",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "JIRA-lic_cleanup-emp_0030-2025_07_15_0800",
                    "status": "Resolved",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "lic_slack_ent",
                "lic_m365_e3"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_19",
        "instruction": "Handle the offboarding of Marketing Content Strategist Noel Rodriguez (employee_id=emp_0031) following identity, RBAC, licensing, device, and retention policies. Anchor all operations deterministically to 2025-07-20 and generate identifiers based on inputs. During the anchored timeframe, utilize the anchor timestamp (17:00:00Z) for all processes; archive the mailbox under std_2y with a path derived from the anchor date (s3://corp-archives/mail/emp_0031/2025-07-20). Manage devices deterministically; if there are no devices assigned, record this deterministically at the anchor time.Anchor all writes deterministically to 2025-07-20 and derive identifiers from inputs. Within the anchored window, you must use the anchor timestamp (17:00:00Z) for all writes; archive the mailbox under std_2y with a path derived from the anchor date (s3://corp-archives/mail/emp_0031/2025-07-20). Execute device handling deterministically; if no devices are assigned you must record that deterministically at the anchor time.",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00031",
                    "memo_id": "memo_offb_emp_0031",
                    "employee_ref": "emp_0031",
                    "event": "offboarding",
                    "status": "queued",
                    "created_at": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "UpdateDirectoryAccountStatus",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "status": "disabled",
                    "disabled_at": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "group_ids": [
                        "grp_marketing_719b"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "RemoveAccountGroups",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "group_ids": [
                        "grp_marketing_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "group_ids": [],
                    "actor": "service_desk",
                    "timestamp": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0031"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00031",
                    "event": "device_none_assigned",
                    "timestamp": "2025-07-20T17:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_salesforce",
                    "revoked_at": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_adobe_cc",
                    "revoked_at": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_offb_emp_0031",
                    "mailbox_id": "mbx_351bb4",
                    "employee_id": "emp_0031",
                    "archive_path": "s3://corp-archives/mail/emp_0031/2025-07-20",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_slack"
                },
            },
            {
                "name": "DisableAppAccount",
                "arguments": {
                    "app_account_id": "appacc_14cdf3",
                    "disabled_at": "2025-07-20T17:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00031",
                    "event": "manager_notified",
                    "timestamp": "2025-07-20T17:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_offb_00031",
                    "status": "completed",
                    "timestamp": "2025-07-20T17:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "mbx_351bb4",
                "acc_351bb4"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_20",
        "instruction": "Coordinate the correction of the Finance license posture for Accounting Manager Lane Taylor (employee_id=emp_0029) in accordance with the license-governance policy. Anchor all documentation to the license audit time 2025-07-15T08:00:00+00:00. Validate current license assignments, ensure operations are strictly within capacity, and document the changes as deterministic maintenance. Revoke only the collaboration licenses not required for the role (TeamChat Enterprise and TechSoft 365 E3) and document it in TaskTrack; do not alter RBAC, mailbox, devices, or app accounts. In TaskTrack, generate a maintenance record with issue_type=Maintenance and priority=P2, and follow the status transitions from New to In Progress to Resolved at the anchor time.Anchor all writes to the license audit time 2025-07-15T08:00:00+00:00. You must validate current assignments, operate strictly within capacity, and record the change as deterministic maintenance. You must revoke only the collaboration licenses that are not required for the role (TeamChat Enterprise and TechSoft 365 E3) and document the change in TaskTrack; you must not modify RBAC, mailbox, devices, or app accounts. In TaskTrack, you must create a maintenance record with issue_type=Maintenance and priority=P2 and follow the status transitions New\u2192In Progress\u2192Resolved at the anchor time.",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_48efe8",
                    "employee_id": "emp_0029",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_48efe8",
                    "employee_id": "emp_0029",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "JIRA-lic_cleanup-emp_0029-2025_07_15_0800",
                    "issue_type": "Maintenance",
                    "summary": "license_revoke;licenses=lic_slack_ent,lic_m365_e3;employee=emp_0029;audit=2025-07-15T08:00:00+00:00",
                    "priority": "P2",
                    "status": "New",
                    "created_at": "2025-07-15T08:00:00+00:00",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "JIRA-lic_cleanup-emp_0029-2025_07_15_0800",
                    "status": "In Progress",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "JIRA-lic_cleanup-emp_0029-2025_07_15_0800",
                    "status": "Resolved",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "lic_slack_ent",
                "lic_m365_e3"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_21",
        "instruction": "Rebalance CreativeWorks Creative Cloud seats by retrieving one from Noel Rodriguez (employee_id=emp_0031) and reallocating it to Devin Martinez (employee_id=emp_0024) in compliance with license governance. Anchor all writes to the CreativeWorks CC audit time 2025-07-15T08:00:00+00:00. Confirm inventory and assignments, adhere to capacity (initiate a shortage ticket if necessary), and log the activity as deterministic license maintenance (lifecycle + TaskTrack).Anchor all writes to the CreativeWorks CC audit time 2025-07-15T08:00:00+00:00. Ensure inventory and assignments are validated, capacity is honored (open a shortage ticket if required), and record the operation as deterministic license maintenance (lifecycle + TaskTrack).",
        "actions": [
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_rebalance_2025_07_15",
                    "memo_id": "memo_lic_adobe_cc_rebalance_2025_07_15",
                    "employee_ref": "lic_adobe_cc",
                    "event": "license_maintenance",
                    "status": "queued",
                    "created_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_rebalance_2025_07_15",
                    "event": "started",
                    "timestamp": "2025-07-15T08:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_adobe_cc",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_adobe_cc-rebalance-emp_0031-to-emp_0024-2025_07_15_0800",
                    "priority": "P3",
                    "created_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0024_lic_adobe_cc_2025_07_15",
                    "account_id": "acc_9071d5",
                    "employee_id": "emp_0024",
                    "license_id": "lic_adobe_cc",
                    "assigned_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "JIRA-lic_adobe_cc-rebalance-emp_0031-to-emp_0024-2025_07_15_0800",
                    "issue_type": "Incident",
                    "summary": "license_id=lic_adobe_cc;action=rebalance;from=emp_0031;to=emp_0024;audit=2025-07-15T08:00:00+00:00",
                    "priority": "P3",
                    "status": "New",
                    "created_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "JIRA-lic_adobe_cc-rebalance-emp_0031-to-emp_0024-2025_07_15_0800",
                    "status": "In Progress",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "JIRA-lic_adobe_cc-rebalance-emp_0031-to-emp_0024-2025_07_15_0800",
                    "status": "Resolved",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_rebalance_2025_07_15",
                    "status": "completed",
                    "timestamp": "2025-07-15T08:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "lic_adobe_cc",
                "acc_9071d5"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_22",
        "instruction": "Minimize active TeamChat and M365 usage by rescinding seats from employees on leave (emp_0004 and emp_0032). Confirm assignments, and utilize each license's audit timestamp as the deterministic change moment.Validate assignments, and use each license's audit timestamp as the deterministic change time.",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_38d007",
                    "employee_id": "emp_0004",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_f06213",
                    "employee_id": "emp_0032",
                    "license_id": "lic_slack_ent",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_38d007",
                    "employee_id": "emp_0004",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_f06213",
                    "employee_id": "emp_0032",
                    "license_id": "lic_m365_e3",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                }
            }
        ],
        "outputs": [
                "lic_slack_ent",
                "lic_m365_e3"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_23",
        "instruction": "Handle CreativeWorks CC reservation posture for July onboarding: increment reserved capacity by one seat only if inventory indicates reserved_seats are below the target buffer of 4. Utilize deterministic anchors from the CreativeWorks CC audit (2025-07-15T08:00:00+00:00), document the lifecycle with the license id as the focus, and deterministically assign the reservation reason to reason=buffer_2025_07_15. Oversee the maintenance under ITSD-1013 (License Maintenance, P3, Resolved).Use deterministic anchors from the CreativeWorks CC audit (2025-07-15T08:00:00+00:00), record lifecycle using the license id as the subject, and set the reservation reason deterministically to reason=buffer_2025_07_15. Track the maintenance under ITSD-1013 (License Maintenance, P3, Resolved).",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_2025_07_15",
                    "memo_id": "memo_lic_adobe_cc_2025_07_15",
                    "employee_ref": "lic_adobe_cc",
                    "event": "license_maintenance",
                    "status": "queued",
                    "created_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_2025_07_15",
                    "event": "started",
                    "timestamp": "2025-07-15T08:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "ReserveLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "count": 1,
                    "reason": "buffer_2025_07_15"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_2025_07_15",
                    "event": "reserved_to_4",
                    "timestamp": "2025-07-15T08:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1013",
                    "issue_type": "License Maintenance",
                    "summary": "license_id=lic_adobe_cc;action=reservation_set;from=3;to=4;reserve=1;reason=buffer_2025_07_15",
                    "priority": "P3",
                    "status": "Resolved",
                    "created_at": "2025-07-15T08:00:00+00:00",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_2025_07_15",
                    "status": "completed",
                    "timestamp": "2025-07-15T08:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                }
            }
        ],
        "outputs": [
                "lic_adobe_cc"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_24",
        "instruction": "Coordinate the provisioning of TechSoft 365 E5 for DevOps Engineer Zion Mitchell (emp_0036) and Software Engineer Nico Turner (emp_0037) following license governance. Confirm available capacity and assign anchor timestamps to the license audit (2025-07-15T08:00:00+00:00). Monitor under ITSD-1018 (License Maintenance, P3, Done).Validate available capacity and anchor assignment timestamps to the license audit (2025-07-15T08:00:00+00:00). Track under ITSD-1018 (License Maintenance, P3, Done).",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                {}
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_00106",
                    "account_id": "acc_f9a6bc",
                    "employee_id": "emp_0036",
                    "license_id": "lic_m365_e5",
                    "assigned_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0037"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0037"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                {}
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_00107",
                    "account_id": "acc_451983",
                    "employee_id": "emp_0037",
                    "license_id": "lic_m365_e5",
                    "assigned_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1018",
                    "issue_type": "License Maintenance",
                    "summary": "tracking=ITSD-1018;license=lic_m365_e5;op=assign;to=emp_0036,emp_0037;audit=2025-07-15T08:00:00+00:00",
                    "priority": "P3",
                    "status": "Done",
                    "created_at": "2025-07-15T08:00:00+00:00",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "lic_m365_e5"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_25",
        "instruction": "Handle the release of two CodeHub Enterprise seats by revoking licenses assigned to Micah White (employee_id=emp_0030) and Drew Evans (employee_id=emp_0040). Check their assignments initially and utilize the CodeHub license audit time for precise timestamps. Record the license reclaim in TaskTrack as ITSD-1017 (issue_type='License Maintenance', priority='P3', status='Done').Validate their assignments first and use the CodeHub license audit time for deterministic timestamps.Log the reclaim in TaskTrack as ITSD-1017 (issue_type='License Maintenance', priority='P3', status='Done').",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_db017d",
                    "employee_id": "emp_0030",
                    "license_id": "lic_github_ent",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_54337a",
                    "employee_id": "emp_0040",
                    "license_id": "lic_github_ent",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1017",
                    "issue_type": "License Maintenance",
                    "summary": "license_id=lic_github_ent;action=revoke;revoke_from=emp_0030,emp_0040;count=2",
                    "priority": "P3",
                    "status": "Done",
                    "created_at": "2025-07-15T08:00:00+00:00",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_github_ent"
                }
            }
        ],
        "outputs": [
                "lic_github_ent"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_26",
        "instruction": "Coordinate compliant CloudCRM access for Ops Manager Harper Hernandez (employee_id=emp_0042) according to license governance: remain within capacity, prevent duplicate grants, and align all write timestamps to the CloudCRM audit time (2025-07-15T08:00:00+00:00). Document this under ITSD-1014 (License Maintenance, P3, Done). If there is available capacity, assign directly without needing to trim reservations to maintain clarity in the final state.Track this under ITSD-1014 (License Maintenance, P3, Done). If capacity allows, assign directly without trimming reservations to avoid ambiguity in final state.",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0042"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0042"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0042"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_00106",
                    "account_id": "acc_f76658",
                    "employee_id": "emp_0042",
                    "license_id": "lic_salesforce",
                    "assigned_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1014",
                    "issue_type": "License Maintenance",
                    "summary": "tracking=ITSD-1014;license=lic_salesforce;op=assign;to=emp_0042;audit=2025-07-15T08:00:00+00:00",
                    "priority": "P3",
                    "status": "Resolved",
                    "created_at": "2025-07-15T08:00:00+00:00",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_salesforce"
                }
            }
        ],
        "outputs": [
                "lic_salesforce",
                "acc_f76658"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_27",
        "instruction": "Coordinate the alignment of TechSoft 365 E5 reservation posture with the pilot threshold of 2 by reducing reservations only if current reserved_seats exceed 2. Utilize the E5 audit anchor (2025-07-15T08:00:00+00:00) for precise timing and document a before/after inventory read for audit purposes. Monitor this under ITSD-1015 (License Maintenance, P3, Resolved).Use the E5 audit anchor (2025-07-15T08:00:00+00:00) for deterministic timing and capture a before/after inventory read for auditability. Track under ITSD-1015 (License Maintenance, P3, Resolved).",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "ReleaseLicenseReservation",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "count": 2
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1015",
                    "issue_type": "License Maintenance",
                    "summary": "tracking=ITSD-1015;license=lic_m365_e5;op=reservation_trim;to=2;audit=2025-07-15T08:00:00+00:00",
                    "priority": "P3",
                    "status": "Resolved",
                    "created_at": "2025-07-15T08:00:00+00:00",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "lic_m365_e5"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_28",
        "instruction": "Handle the reallocation of CreativeWorks CC within Marketing by reclaiming one from Elliot Johnson (employee_id=emp_0025) and assigning it to Hayden Brown (employee_id=emp_0016). Confirm the assignments and employ the audit timestamp for exact times.Validate assignments and use the audit timestamp for deterministic times.",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "department": "Marketing",
                    "status": "active"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0025"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0025"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0025"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_1e8432",
                    "employee_id": "emp_0025",
                    "license_id": "lic_adobe_cc",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0016"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0016"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0016"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_00063",
                    "account_id": "acc_0099f1",
                    "employee_id": "emp_0016",
                    "license_id": "lic_adobe_cc",
                    "assigned_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                }
            }
        ],
        "outputs": [
                "lic_adobe_cc",
                "acc_0099f1"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_29",
        "instruction": "Handle the expansion of CreativeWorks CC availability for content work by assigning CreativeWorks CC to Logan Nguyen (employee_id=emp_0021) and Jesse Moore (employee_id=emp_0027) in accordance with the license\u2011governance policy. Ensure all writes are anchored to the CreativeWorks CC audit (2025-07-15T08:00:00+00:00). Confirm capacity in a deterministic manner through inventory reads and generate new assignment identifiers as sequential values following the current maximum in the assignments table at the audit anchor. Conduct a lightweight license\u2011maintenance run at the same anchor for audit purposes; do not escalate issues when capacity is adequate.Anchor all writes to the CreativeWorks CC audit (2025-07-15T08:00:00+00:00). Verify capacity deterministically via inventory reads and derive new assignment identifiers as the next sequential values after the current maximum in the assignments table at the audit anchor.Record a lightweight license\u2011maintenance run at the same anchor for auditability; do not raise escalations when capacity suffices.",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_expand_2025_07_15",
                    "memo_id": "memo_lic_adobe_cc_expand_2025_07_15",
                    "employee_ref": "lic_adobe_cc",
                    "event": "license_maintenance",
                    "status": "queued",
                    "created_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_expand_2025_07_15",
                    "event": "started",
                    "timestamp": "2025-07-15T08:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_00106",
                    "account_id": "acc_43980f",
                    "employee_id": "emp_0021",
                    "license_id": "lic_adobe_cc",
                    "assigned_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0027"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0027"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0027"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_00107",
                    "account_id": "acc_5494f2",
                    "employee_id": "emp_0027",
                    "license_id": "lic_adobe_cc",
                    "assigned_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_lic_adobe_cc_expand_2025_07_15",
                    "event": "completed",
                    "timestamp": "2025-07-15T08:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "lic_adobe_cc"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_30",
        "instruction": "Coordinate the CreativeWorks cleanup alongside future planning by revoking CreativeWorks CC from Noel Rodriguez (employee_id=emp_0031) and Elliot Johnson (employee_id=emp_0025), then securing 2 seats for upcoming content projects using reason 'content_projects_q3'. Validate assignments first while ensuring the times remain deterministic via the audit timestamp. Document this under tracking_id ITSD-1016 (License Maintenance, P3, Done).Validate assignments first and keep times deterministic via the audit timestamp. Record this under tracking_id ITSD-1016 (License Maintenance, P3, Done).",
        "actions": [
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "employee_id": "emp_0031",
                    "license_id": "lic_adobe_cc",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0025"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0025"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0025"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_1e8432",
                    "employee_id": "emp_0025",
                    "license_id": "lic_adobe_cc",
                    "revoked_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "ReserveLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "count": 2,
                    "reason": "content_projects_q3"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1016",
                    "issue_type": "License Maintenance",
                    "summary": "license_id=lic_adobe_cc;action=revoke+reserve;revoke_from=emp_0031,emp_0025;reserve=2;reason=content_projects_q3",
                    "priority": "P3",
                    "status": "Done",
                    "created_at": "2025-07-15T08:00:00+00:00",
                    "updated_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                }
            }
        ],
        "outputs": [
                "lic_adobe_cc"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_31",
        "instruction": "Ensure a compliant in-stock laptop is provided to Logan Nguyen (employee_id=emp_0021) in accordance with the tie-breaker policy. Complete MDM enrollment in a deterministic manner, verify the asset assignment and management, and utilize the timestamp 2023-06-10T09:00:00+00:00 for anything time-related.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0021",
                    "memo_id": "memo_hw_emp_0021",
                    "employee_ref": "emp_0021",
                    "event": "hardware_provision",
                    "status": "queued",
                    "created_at": "2023-06-10T09:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "wf_mdm_emp_0021_ast_0013",
                    "employee_id": "emp_0021",
                    "asset_id": "ast_0013",
                    "process": "mdm",
                    "status": "completed",
                    "pickup_code": "pc_mdm_emp_0021_ast_0013",
                    "created_at": "2023-06-10T09:00:00+00:00",
                    "completed_at": "2023-06-10T09:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0021"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "assigned_to": "emp_0021",
                    "mdm_enrolled": true
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0021",
                    "status": "completed",
                    "timestamp": "2023-06-10T09:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_32",
        "instruction": "You need to allocate a managed phone to Sales Manager Cameron Patel (employee_id=emp_0013). Select an in-stock phone following the policy, enroll it through MDM, and confirm its assignment. Document using workflow_id=dwf_asset_emp_0013_1 and pickup_code=pc_dwf_asset_emp_0013_1; created_at=2025-07-18T10:05:00+00:00; mdm_enroll at 2025-07-18T10:10:00+00:00.Choose an in_stock phone per policy, enroll it via MDM, and verify the assignment.Track with workflow_id=dwf_asset_emp_0013_1 and pickup_code=pc_dwf_asset_emp_0013_1; created_at=2025-07-18T10:05:00+00:00; mdm_enroll at 2025-07-18T10:10:00+00:00.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "phone",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0016",
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_asset_emp_0013_1",
                    "employee_id": "emp_0013",
                    "asset_id": "ast_0016",
                    "process": "mdm",
                    "status": "completed",
                    "pickup_code": "pc_dwf_asset_emp_0013_1",
                    "created_at": "2025-07-18T10:05:00+00:00",
                    "completed_at": "2025-07-18T10:10:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "phone",
                    "assigned_to": "emp_0013"
                }
            }
        ],
        "outputs": [
                "ast_0016"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_33",
        "instruction": "Ensure device compliance for Hayden Brown (employee_id=emp_0016) according to asset and RBAC policy: the assigned phone needs to be MDM\u2011managed, RBAC groups must match the baseline for Marketing/Content Strategist, licenses should reflect the baseline bundle, and mailbox must be active. Anchor all operations to 2025-07-18T11:10:00+00:00 for consistency; utilize lifecycle_id=lcq_devcomp_emp_0016_2025_07_18 and memo_id=memo_devcomp_emp_0016_2025_07_18 for audit purposes.Anchor all writes to 2025-07-18T11:10:00+00:00 for determinism; use lifecycle_id=lcq_devcomp_emp_0016_2025_07_18 and memo_id=memo_devcomp_emp_0016_2025_07_18 for auditable tracking.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0016"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0016"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_0099f1",
                    "group_ids": [
                        "grp_marketing_719b",
                        "grp_marketing_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-18T11:10:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0016"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0016"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0016"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "wf_mdm_emp_0016_ast_0022",
                    "employee_id": "emp_0016",
                    "asset_id": "ast_0022",
                    "process": "mdm",
                    "status": "completed",
                    "pickup_code": "pc_mdm_emp_0016_ast_0022",
                    "created_at": "2025-07-18T11:10:00+00:00",
                    "completed_at": "2025-07-18T11:10:00+00:00"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18",
                    "memo_id": "memo_devcomp_emp_0016_2025_07_18",
                    "employee_ref": "emp_0016",
                    "event": "device_compliance",
                    "status": "queued",
                    "created_at": "2025-07-18T11:10:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18",
                    "event": "rbac_verified",
                    "timestamp": "2025-07-18T11:10:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18",
                    "event": "licenses_verified",
                    "timestamp": "2025-07-18T11:10:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18",
                    "event": "mailbox_verified",
                    "timestamp": "2025-07-18T11:10:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18",
                    "event": "mdm_verified",
                    "timestamp": "2025-07-18T11:10:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18",
                    "status": "completed",
                    "timestamp": "2025-07-18T11:10:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0022"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_34",
        "instruction": "Allocate an in-stock laptop to Skyler Lopez (employee_id=emp_0022) consistent with policy, ensure MDM enrollment is completed deterministically, and confirm it is assigned and managed.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0022"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0022"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0022"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Operations",
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_51ba73",
                    "group_ids": [
                        "grp_operations_772e",
                        "grp_operations_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-01-21T09:00:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_m365_e3-emp_0022",
                    "priority": "P2",
                    "created_at": "2025-01-21T09:00:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0022_lic_m365_e3",
                    "account_id": "acc_51ba73",
                    "employee_id": "emp_0022",
                    "license_id": "lic_m365_e3",
                    "assigned_at": "2025-01-21T09:00:00+00:00"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_slack_ent-emp_0022",
                    "priority": "P2",
                    "created_at": "2025-01-21T09:00:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0022_lic_slack_ent",
                    "account_id": "acc_51ba73",
                    "employee_id": "emp_0022",
                    "license_id": "lic_slack_ent",
                    "assigned_at": "2025-01-21T09:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_onb_0022_slack",
                    "employee_id": "emp_0022",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2025-01-21T09:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0022"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "wf_mdm_emp_0022_ast_0013",
                    "employee_id": "emp_0022",
                    "asset_id": "ast_0013",
                    "process": "mdm",
                    "status": "completed",
                    "pickup_code": "pc_mdm_emp_0022_ast_0013",
                    "created_at": "2025-01-21T09:00:00+00:00",
                    "completed_at": "2025-01-21T09:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0022"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "assigned_to": "emp_0022",
                    "mdm_enrolled": true
                }
            }
        ],
        "outputs": [
                "ast_0013"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_35",
        "instruction": "Arrange a device return and coordinate an MDM wipe for Micah White's assigned phone (employee_id=emp_0030) at the specified due time at=2025-07-25T17:00:00+00:00; refrain from changing ownership until the collection is finalized.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "phone",
                    "assigned_to": "emp_0030",
                    "mdm_enrolled": true
                },
            },
            {
                "name": "RequestAssetReturn",
                "arguments": {
                    "asset_id": "ast_0014",
                    "employee_id": "emp_0030",
                    "due_ts": "2025-07-25T17:00:00+00:00",
                    "workflow_id": "wf_ret_ast_0014"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "wf_ret_ast_0014",
                    "employee_id": "emp_0030",
                    "asset_id": "ast_0014",
                    "process": "return",
                    "status": "requested",
                    "pickup_code": "pc_ret_ast_0014",
                    "created_at": "2025-07-25T17:00:00+00:00"
                },
            },
            {
                "name": "ScheduleMdmAction",
                "arguments": {
                    "asset_id": "ast_0014",
                    "when": "2025-07-25T17:00:00+00:00",
                    "action": "wipe",
                    "workflow_id": "wf_ret_ast_0014"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_ret_emp_0030_ast_0014",
                    "memo_id": "memo_ret_emp_0030_ast_0014",
                    "employee_ref": "emp_0030",
                    "event": "return",
                    "status": "queued",
                    "created_at": "2025-07-25T17:00:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_ret_emp_0030_ast_0014",
                    "event": "return_scheduled",
                    "timestamp": "2025-07-25T17:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_ret_emp_0030_ast_0014",
                    "event": "wipe_scheduled",
                    "timestamp": "2025-07-25T17:00:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0014"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_36",
        "instruction": "Organize managed phone returns for Accounting Manager Lane Taylor (employee_id=emp_0029) for both assigned phones with specific due times. Develop return workflows for each device and set up MDM wipes at the respective due times; avoid altering ownership until collection is complete. Utilize due_ts=2025-07-26T17:00:00+00:00 for ast_0039 and due_ts=2025-07-26T17:30:00+00:00 for ast_0049.Create return workflows for each device and schedule MDM wipes at the respective due times; do not change ownership until collection is completed.Use due_ts=2025-07-26T17:00:00+00:00 for ast_0039 and due_ts=2025-07-26T17:30:00+00:00 for ast_0049.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0029"
                },
            },
            {
                "name": "RequestAssetReturn",
                "arguments": {
                    "asset_id": "ast_0039",
                    "employee_id": "emp_0029",
                    "due_ts": "2025-07-26T17:00:00+00:00",
                    "workflow_id": "wf_ret_emp_0029_ast_0039"
                },
            },
            {
                "name": "ScheduleMdmAction",
                "arguments": {
                    "asset_id": "ast_0039",
                    "when": "2025-07-26T17:00:00+00:00",
                    "action": "wipe",
                    "workflow_id": "wf_ret_emp_0029_ast_0039"
                },
            },
            {
                "name": "RequestAssetReturn",
                "arguments": {
                    "asset_id": "ast_0049",
                    "employee_id": "emp_0029",
                    "due_ts": "2025-07-26T17:30:00+00:00",
                    "workflow_id": "wf_ret_emp_0029_ast_0049"
                },
            },
            {
                "name": "ScheduleMdmAction",
                "arguments": {
                    "asset_id": "ast_0049",
                    "when": "2025-07-26T17:30:00+00:00",
                    "action": "wipe",
                    "workflow_id": "wf_ret_emp_0029_ast_0049"
                }
            }
        ],
        "outputs": [
                "ast_0039",
                "ast_0049"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_37",
        "instruction": "Handle the provisioning of a compliant managed laptop for Support Manager Sasha Phillips (employee_id=emp_0038) adhering to onboarding hardware policy. Ensure the RBAC aligns with the Support/Support Manager baseline, inclusive of audited changes, verify baseline licenses, activate the mailbox, and confirm the laptop is assigned and MDM-managed. Anchor workflow writes to 2025-07-18T13:05:00+00:00 (MDM completion at 13:10) and systematically track the activity.Ensure RBAC matches the Support/Support Manager baseline with audited changes, baseline licenses are present, the mailbox is active, and the laptop is assigned and MDM\u2011managed. Anchor workflow writes to 2025-07-18T13:05:00+00:00 (MDM completion at 13:10) and track the activity deterministically.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Support",
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0038",
                    "memo_id": "memo_hw_emp_0038",
                    "employee_ref": "emp_0038",
                    "event": "hardware_provision",
                    "status": "queued",
                    "created_at": "2025-07-18T13:05:00+00:00"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_839501",
                    "group_ids": [
                        "grp_support_ada3",
                        "grp_support_all"
                    ],
                    "actor": "service_desk",
                    "timestamp": "2025-07-18T13:05:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_asset_emp_0038_ast_0013",
                    "employee_id": "emp_0038",
                    "asset_id": "ast_0013",
                    "process": "mdm",
                    "status": "completed",
                    "pickup_code": "pc_dwf_asset_emp_0038_ast_0013",
                    "created_at": "2025-07-18T13:05:00+00:00",
                    "completed_at": "2025-07-18T13:10:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "assigned_to": "emp_0038",
                    "mdm_enrolled": true
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0038",
                    "event": "rbac_verified",
                    "timestamp": "2025-07-18T13:05:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0038",
                    "event": "licenses_verified",
                    "timestamp": "2025-07-18T13:05:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0038",
                    "event": "mdm_completed",
                    "timestamp": "2025-07-18T13:10:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0038",
                    "status": "completed",
                    "timestamp": "2025-07-18T13:10:00+00:00",
                    "actor": "service_desk"
                }
            }
        ],
        "outputs": [
                "ast_0013"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_38",
        "instruction": "Coordinate the supply of an in-stock laptop to Emerson Davis (employee_id=emp_0014) following policy, complete MDM enrollment consistently, and ensure it is assigned and under management.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0014"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0014"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0014"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0014"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_asset_emp_0014_ast_0013",
                    "employee_id": "emp_0014",
                    "asset_id": "ast_0013",
                    "process": "mdm",
                    "status": "completed",
                    "pickup_code": "pc_dwf_asset_emp_0014_ast_0013",
                    "created_at": "2024-10-13T09:00:00+00:00",
                    "completed_at": "2024-10-13T09:00:00+00:00"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0014",
                    "memo_id": "memo_hw_emp_0014",
                    "employee_ref": "emp_0014",
                    "event": "hardware_provision",
                    "status": "queued",
                    "created_at": "2024-10-13T09:00:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_hw_emp_0014",
                    "status": "completed",
                    "timestamp": "2024-10-13T09:00:00+00:00",
                    "actor": "service_desk"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0014"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "assigned_to": "emp_0014",
                    "mdm_enrolled": true
                }
            }
        ],
        "outputs": [
                "ast_0013"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_39",
        "instruction": "Handle issuing an in-stock phone to Avery Zhang (employee_id=emp_0010) in accordance with the tie-breaker policy, finalize MDM enrollment methodically, and confirm the assignment is managed. Utilize the directory account creation date (2023-11-10T09:00:00+00:00) for any workflow timestamps; do not create other times.Derive any workflow timestamps from the employee's directory account created_at (2023-11-10T09:00:00+00:00); do not invent other times.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "phone",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0016",
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "dwf_asset_emp_0010_ast_0016",
                    "employee_id": "emp_0010",
                    "asset_id": "ast_0016",
                    "process": "mdm",
                    "status": "completed",
                    "pickup_code": "pc_dwf_asset_emp_0010_ast_0016",
                    "created_at": "2023-11-10T09:00:00+00:00",
                    "completed_at": "2023-11-10T09:00:00+00:00"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0010"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "phone",
                    "assigned_to": "emp_0010"
                }
            }
        ],
        "outputs": [
                "ast_0016"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_40",
        "instruction": "Coordinate the issuance of an in-stock laptop to Finley Thomas (employee_id=emp_0026) as per policy, ensure MDM enrollment is completed systematically, and check the managed state is assigned. Utilize the directory account creation date (2025-05-15T09:00:00+00:00) for any workflow timestamps; do not construct other times.Derive any workflow timestamps from the employee's directory account created_at (2025-05-15T09:00:00+00:00); do not invent other times.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0026"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0026"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "asset_type": "laptop",
                    "status": "in_stock"
                },
            },
            {
                "name": "AssignAsset",
                "arguments": {
                    "asset_id": "ast_0013",
                    "employee_id": "emp_0026"
                },
            },
            {
                "name": "CreateDeviceWorkflow",
                "arguments": {
                    "workflow_id": "wf_mdm_emp_0026_ast_0013",
                    "employee_id": "emp_0026",
                    "asset_id": "ast_0013",
                    "process": "mdm",
                    "status": "completed",
                    "pickup_code": "pc_mdm_emp_0026_ast_0013",
                    "created_at": "2025-05-15T09:00:00+00:00",
                    "completed_at": "2025-05-15T09:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "ast_0013"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_41",
        "instruction": "Handle the initial response on 2025\u201107\u201116 at 09:00 UTC. You need to verify that every Urgent ticket currently labeled as New is being actively managed per policy by shifting New \u2192 In Progress. Operate with auditability using deterministic anchors established from the 09:00 cutoff: document the post-triage backlog state (snapshot_id=snap_2025_07_16_0900 at 2025-07-16T09:00:00+00:00 for {New, Open, In Progress, On Hold}) and log the health report (run_id=rpt_2025_07_16_0902, started_at=2025-07-16T09:01:00+00:00, completed_at=2025-07-16T09:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf).Operate with auditability using deterministic anchors derived from the 09:00 cutoff: record the post\u2011triage backlog state (snapshot_id=snap_2025_07_16_0900 at 2025-07-16T09:00:00+00:00 for {New, Open, In Progress, On Hold}) and register the health report (run_id=rpt_2025_07_16_0902, started_at=2025-07-16T09:01:00+00:00, completed_at=2025-07-16T09:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf).",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "New",
                    "priority": "Urgent"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5002",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5009",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5011",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5048",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5049",
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_0900",
                    "taken_at": "2025-07-16T09:00:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_0902",
                    "started_at": "2025-07-16T09:01:00+00:00",
                    "completed_at": "2025-07-16T09:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf"
                }
            }
        ],
        "outputs": [
                "snap_2025_07_16_0900"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_42",
        "instruction": "Finalize all tickets currently in Resolved status by closing them, utilizing their existing closed_at timestamps. Explicitly close T5022, T5033, T5040, T5041, T5045, T5047, and T5064. Subsequently, capture a backlog snapshot with snapshot_id=snap_2025_07_16_1200 and taken_at=2025-07-16T12:00:00+00:00 for statuses {New, Open, In Progress, On Hold}; register the service-desk health report under run_id=rpt_2025_07_16_1202 (started_at=2025-07-16T12:01:00+00:00, completed_at=2025-07-16T12:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_noon_close.pdf); and append daily metrics for 2025-07-16.Explicitly close T5022, T5033, T5040, T5041, T5045, T5047, and T5064.Then capture a backlog snapshot using snapshot_id=snap_2025_07_16_1200 and taken_at=2025-07-16T12:00:00+00:00 for statuses {New, Open, In Progress, On Hold}; register the service\u2011desk health report with run_id=rpt_2025_07_16_1202 (started_at=2025-07-16T12:01:00+00:00, completed_at=2025-07-16T12:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_noon_close.pdf); and append daily metrics for 2025-07-16.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "Resolved"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5022",
                    "status": "Closed",
                    "closed_at": "2025-07-11T11:24:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5033",
                    "status": "Closed",
                    "closed_at": "2025-07-11T15:22:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5040",
                    "status": "Closed",
                    "closed_at": "2025-07-09T16:11:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5041",
                    "status": "Closed",
                    "closed_at": "2025-07-10T13:44:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5045",
                    "status": "Closed",
                    "closed_at": "2025-07-07T11:40:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5047",
                    "status": "Closed",
                    "closed_at": "2025-07-11T14:17:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5064",
                    "status": "Closed",
                    "closed_at": "2025-07-10T15:30:00+00:00"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1200",
                    "taken_at": "2025-07-16T12:00:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1202",
                    "started_at": "2025-07-16T12:01:00+00:00",
                    "completed_at": "2025-07-16T12:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_noon_close.pdf"
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "snap_2025_07_16_1200"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_43",
        "instruction": "Following the escalation policy, you are required to verify that all Urgent tickets set to On Hold as of the 2025-07-16 13:00 UTC deadline are escalated and work begins within five minutes. Operate based on policy rather than specific steps: an escalation is demonstrated by generating an escalation record linked to the ticket reference and changing its status to In Progress; capture the backlog state results for {New, Open, In Progress, On Hold} at 13:05Z and log the standard daily health report during the same time frame. Utilize the standard reporting policy parameters in a fixed manner: a 30\u2011day source window and the official output path name 'ServiceDesk_Health_Report_YYYY\u2011MM\u2011DD_escalation.pdf' under s3://reports/, fixed to 13:06Z for the run. Fix identifiers to the 13:05Z/13:06Z timeframe; prevent redundant searches and omit daily aggregate computations in this process.Operate under policy rather than steps: escalation is evidenced by creating an escalation record tied to the ticket reference and transitioning its handling state to In Progress; document the resulting backlog state for {New, Open, In Progress, On Hold} at 13:05Z and register the standard daily health report in the same window.Use the standard reporting policy parameters deterministically: a 30\u2011day source window and the canonical output path name 'ServiceDesk_Health_Report_YYYY\u2011MM\u2011DD_escalation.pdf' under s3://reports/, anchored to 13:06Z for the run. Anchor identifiers to the 13:05Z/13:06Z window; avoid redundant lookups and do not compute daily aggregates in this run.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "On Hold",
                    "priority": "Urgent"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "SLA-T5017",
                    "issue_type": "SLA Escalation",
                    "summary": "Escalate ticket T5017 (Urgent On Hold)",
                    "priority": "P1",
                    "status": "New",
                    "created_at": "2025-07-16T13:00:00+00:00",
                    "updated_at": "2025-07-16T13:00:00+00:00"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "SLA-T5029",
                    "issue_type": "SLA Escalation",
                    "summary": "Escalate ticket T5029 (Urgent On Hold)",
                    "priority": "P1",
                    "status": "New",
                    "created_at": "2025-07-16T13:00:00+00:00",
                    "updated_at": "2025-07-16T13:00:00+00:00"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "SLA-T5036",
                    "issue_type": "SLA Escalation",
                    "summary": "Escalate ticket T5036 (Urgent On Hold)",
                    "priority": "P1",
                    "status": "New",
                    "created_at": "2025-07-16T13:00:00+00:00",
                    "updated_at": "2025-07-16T13:00:00+00:00"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "SLA-T5058",
                    "issue_type": "SLA Escalation",
                    "summary": "Escalate ticket T5058 (Urgent On Hold)",
                    "priority": "P1",
                    "status": "New",
                    "created_at": "2025-07-16T13:00:00+00:00",
                    "updated_at": "2025-07-16T13:00:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "SLA-T5017",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T13:05:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "SLA-T5029",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T13:05:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "SLA-T5036",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T13:05:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "SLA-T5058",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T13:05:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5017",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5029",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5036",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5058",
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1305",
                    "taken_at": "2025-07-16T13:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1306",
                    "started_at": "2025-07-16T13:05:30+00:00",
                    "completed_at": "2025-07-16T13:06:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_escalation.pdf"
                }
            }
        ],
        "outputs": [
                "SLA-T5017",
                "SLA-T5029",
                "SLA-T5036",
                "SLA-T5058"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_44",
        "instruction": "According to the triage policy, you must confirm that by the 2025-07-16 14:00 UTC deadline, all High\u2011priority tickets still in New or Open are actively being processed (In Progress). Maintain auditability: document the backlog state post-triage, create a health report for governance, and update daily metrics for 2025\u201107\u201116 using fixed identifiers based on the cutoff time: snapshot_id=snap_2025_07_16_1400 at 2025-07-16T14:00:00+00:00 and report run_id=rpt_2025_07_16_1406 (initiated_at=2025-07-16T14:05:30+00:00, finished_at=2025-07-16T14:06:30+00:00, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_triage.pdf).Operate with auditability: record the post\u2011triage backlog state, produce a health report for governance, and refresh daily metrics for 2025\u201107\u201116 using deterministic identifiers derived from the cutoff time: snapshot_id=snap_2025_07_16_1400 at 2025-07-16T14:00:00+00:00 and report run_id=rpt_2025_07_16_1406 (started_at=2025-07-16T14:05:30+00:00, completed_at=2025-07-16T14:06:30+00:00, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_triage.pdf).",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "New",
                    "priority": "High"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5014",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5020",
                    "status": "In Progress"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "Open",
                    "priority": "High"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5035",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5060",
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1400",
                    "taken_at": "2025-07-16T14:00:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1406",
                    "started_at": "2025-07-16T14:05:30+00:00",
                    "completed_at": "2025-07-16T14:06:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_triage.pdf"
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "snap_2025_07_16_1400"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_45",
        "instruction": "According to the first-response policy dated 2025-07-16, it is required that all Urgent tickets currently marked as New and any New Software tickets are actively in progress by 15:00 UTC. Document the post-triage backlog using snapshot_id=snap_2025_07_16_1500 precisely at 2025-07-16T15:00:00+00:00 over the statuses {New, Open, In Progress, On Hold}; log the health report with run_id=rpt_2025_07_16_1502 (started_at=2025-07-16T15:01:00+00:00, completed_at=2025-07-16T15:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf); and recalculate the daily metrics for 2025-07-16.Capture the post\u2011triage backlog snapshot using snapshot_id=snap_2025_07_16_1500 at 2025-07-16T15:00:00+00:00 over statuses {New, Open, In Progress, On Hold}; register the health report using run_id=rpt_2025_07_16_1502 (started_at=2025-07-16T15:01:00+00:00, completed_at=2025-07-16T15:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf); and recompute daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "New",
                    "priority": "Urgent"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5002",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5009",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5011",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5048",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5049",
                    "status": "In Progress"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "New",
                    "category": "Software"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5046",
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1500",
                    "taken_at": "2025-07-16T15:00:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1502",
                    "started_at": "2025-07-16T15:01:00+00:00",
                    "completed_at": "2025-07-16T15:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf"
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "snap_2025_07_16_1500"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_46",
        "instruction": "On 2025-07-16, it is necessary to finalize incident hygiene for 'Password reset needed' cases by closing relevant tickets that are currently in progress with a definitive closed_at (2025-07-16T16:45:00+00:00). Act with governance: log the daily health report using run_id=rpt_2025_07_16_1647 (started_at=2025-07-16T16:46:00+00:00, completed_at=2025-07-16T16:47:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_password_resets.pdf); maintain consistency in identifiers and timestamps linked to the same date.Operate with governance: register the daily health report with run_id=rpt_2025_07_16_1647 (started_at=2025-07-16T16:46:00+00:00, completed_at=2025-07-16T16:47:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_password_resets.pdf); keep identifiers and timestamps anchored to the same date.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5005",
                    "status": "Resolved"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5006",
                    "status": "Resolved"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5030",
                    "status": "Resolved"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5005",
                    "status": "Closed",
                    "closed_at": "2025-07-16T16:45:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5006",
                    "status": "Closed",
                    "closed_at": "2025-07-16T16:45:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5030",
                    "status": "Closed",
                    "closed_at": "2025-07-16T16:45:00+00:00"
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1647",
                    "started_at": "2025-07-16T16:46:00+00:00",
                    "completed_at": "2025-07-16T16:47:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_password_resets.pdf"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1647"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_47",
        "instruction": "According to the MDM backlog policy on 2025-07-16, you need to ensure all MDM tickets that are On Hold or Open are being actively progressed (In Progress) by the 17:00 UTC deadline, and maintain an audit trail with clear anchors (snapshot and report identifiers/times). Refrain from introducing any parameters not explicitly listed below; avoid unspecified report windows. Utilize snapshot_id=snap_2025_07_16_1700 at 2025-07-16T17:00:00+00:00 and log the health report with run_id=rpt_2025_07_16_1701 (started_at=2025-07-16T17:00:00+00:00, completed_at=2025-07-16T17:01:00+00:00, source_ticket_window_days=14, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_mdm_1701.pdf).Do not introduce parameters beyond those explicitly anchored below; avoid unspecified report windows.Use snapshot_id=snap_2025_07_16_1700 at 2025-07-16T17:00:00+00:00 and register the health report with run_id=rpt_2025_07_16_1701 (started_at=2025-07-16T17:00:00+00:00, completed_at=2025-07-16T17:01:00+00:00, source_ticket_window_days=14, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_mdm_1701.pdf).",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "On Hold",
                    "category": "MDM"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5053",
                    "status": "In Progress"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "Open",
                    "category": "MDM"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5013",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5035",
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1700",
                    "taken_at": "2025-07-16T17:00:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1701",
                    "started_at": "2025-07-16T17:00:00+00:00",
                    "completed_at": "2025-07-16T17:01:00+00:00",
                    "source_ticket_window_days": 14,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_mdm_1701.pdf"
                }
            }
        ],
        "outputs": [
                "snap_2025_07_16_1700"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_48",
        "instruction": "You are tasked with handling the daily service\u2011desk health reporting for 2025-07-16. You must generate the report using run_id=rpt_2025_07_16_1700 (started_at=2025-07-16T17:00:00+00:00, completed_at=2025-07-16T17:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16.pdf). You must take a pre\u2011run backlog snapshot using snapshot_id=snap_2025_07_16_1655 at 2025-07-16T16:55:00+00:00 and a post\u2011run snapshot using snapshot_id=snap_2025_07_16_1705 at 2025-07-16T17:05:00+00:00 for statuses {New, Open, In Progress, On Hold}, and recompute daily metrics for 2025-07-16.You must capture a pre\u2011run backlog snapshot using snapshot_id=snap_2025_07_16_1655 at 2025-07-16T16:55:00+00:00 and a post\u2011run snapshot using snapshot_id=snap_2025_07_16_1705 at 2025-07-16T17:05:00+00:00 for statuses {New, Open, In Progress, On Hold}, and recompute daily metrics for 2025-07-16.",
        "actions": [
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1655",
                    "taken_at": "2025-07-16T16:55:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1700",
                    "started_at": "2025-07-16T17:00:00+00:00",
                    "completed_at": "2025-07-16T17:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1705",
                    "taken_at": "2025-07-16T17:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1700"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_49",
        "instruction": "On 2025\u201107\u201116, you are required to oversee MDM incident handling for Lane Taylor (employee_id=emp_0029) following established incident and reporting guidelines. For this specific day, the policy directives are: incidents begin at 17:10Z and conclude at 18:00Z (priority High, category MDM); capture the backlog snapshot at 17:12Z while incidents remain active (statuses {New, In Progress}); and the timeline for the daily health report is 18:06\u201318:07Z with a 30\u2011day ticket duration and the designated report path. You need to deduce identifiers and subjects consistently using stable IDs and update daily metrics for the given date.For this date, the policy anchors are: incidents open at 17:10Z and close at 18:00Z (priority High, category MDM); take the backlog snapshot at 17:12Z while incidents are still open (statuses {New, In Progress}); and the daily health report horizon is 18:06\u201318:07Z with a 30\u2011day ticket window and the canonical report path. You must derive identifiers and subjects deterministically from stable IDs and refresh daily metrics for the date.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_incident_mdm_emp_0029_2025_07_16",
                    "event": "mdm_window_applied_open_17_10_close_18_00",
                    "timestamp": "2025-07-16T17:10:00+00:00",
                    "actor": "incident_policy"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0029"
                },
            },
            {
                "name": "CreateTicket",
                "arguments": {
                    "ticket_id": "T_mdm_emp_0029_ast_0039",
                    "employee_id": "emp_0029",
                    "category": "MDM",
                    "priority": "High",
                    "status": "New",
                    "subject": "mdm_wipe_ast_0039",
                    "opened_at": "2025-07-16T17:10:00+00:00",
                    "related_asset_id": "ast_0039"
                },
            },
            {
                "name": "CreateTicket",
                "arguments": {
                    "ticket_id": "T_mdm_emp_0029_ast_0049",
                    "employee_id": "emp_0029",
                    "category": "MDM",
                    "priority": "High",
                    "status": "New",
                    "subject": "mdm_wipe_ast_0049",
                    "opened_at": "2025-07-16T17:10:00+00:00",
                    "related_asset_id": "ast_0049"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1712",
                    "taken_at": "2025-07-16T17:12:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "In Progress"
                    ]
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T_mdm_emp_0029_ast_0039",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T_mdm_emp_0029_ast_0039",
                    "status": "Resolved"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T_mdm_emp_0029_ast_0039",
                    "status": "Closed",
                    "closed_at": "2025-07-16T18:00:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T_mdm_emp_0029_ast_0049",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T_mdm_emp_0029_ast_0049",
                    "status": "Resolved"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T_mdm_emp_0029_ast_0049",
                    "status": "Closed",
                    "closed_at": "2025-07-16T18:00:00+00:00"
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1807",
                    "started_at": "2025-07-16T18:06:00+00:00",
                    "completed_at": "2025-07-16T18:07:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_mdm_wipes.pdf"
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1807"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_50",
        "instruction": "According to backlog policy, confirm that by 2025-07-16 18:30 UTC, Access Request tickets in a state of New or On Hold are being actively transitioned to In Progress. Operate with a verifiable approach using deterministic criteria based on the deadline: capture a snapshot at 18:30 (snapshot_id=snap_2025_07_16_1830 for {New, Open, In Progress, On Hold}), log the health report (run_id=rpt_2025_07_16_1832, started_at=2025-07-16T18:31:00+00:00, completed_at=2025-07-16T18:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_access.pdf), and update daily metrics for 2025\u201107\u201116.Operate with auditability using deterministic anchors derived from the cutoff: take a snapshot at 18:30 (snapshot_id=snap_2025_07_16_1830 for {New, Open, In Progress, On Hold}), register the health report (run_id=rpt_2025_07_16_1832, started_at=2025-07-16T18:31:00+00:00, completed_at=2025-07-16T18:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_access.pdf), and refresh daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "Access Request",
                    "status": "New"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5002",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5059",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5063",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5014",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5020",
                    "status": "In Progress"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "Access Request",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5021",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5031",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5036",
                    "status": "In Progress"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5058",
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1830",
                    "taken_at": "2025-07-16T18:30:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1832",
                    "started_at": "2025-07-16T18:31:00+00:00",
                    "completed_at": "2025-07-16T18:32:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_access.pdf"
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1832"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_51",
        "instruction": "Ensure you handle the early-morning health check scheduled on 2025-07-16 in compliance with the standard reporting policy. Anchor all writes to the 07:30Z window, utilizing deterministic identifiers derived from the anchor. Pre-run snapshot: snapshot_id=snap_2025_07_16_0725 at 2025-07-16T07:25:00+00:00 for {New, Open, In Progress, On Hold}. Report execution: run_id=rpt_2025_07_16_0732 initiated at 2025-07-16T07:30:00+00:00, concluded at 2025-07-16T07:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_0732.pdf. Post-run snapshot: snapshot_id=snap_2025_07_16_0735 at 2025-07-16T07:35:00+00:00 for the same statuses. Record a validation entry that references the run and both snapshots.Pre\u2011run snapshot: snapshot_id=snap_2025_07_16_0725 at 2025-07-16T07:25:00+00:00 for {New, Open, In Progress, On Hold}. Report run: run_id=rpt_2025_07_16_0732 with started_at=2025-07-16T07:30:00+00:00, completed_at=2025-07-16T07:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_0732.pdf. Post\u2011run snapshot: snapshot_id=snap_2025_07_16_0735 at 2025-07-16T07:35:00+00:00 for the same statuses. Record one validation entry referencing the run and both snapshots.",
        "actions": [
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_0725",
                    "taken_at": "2025-07-16T07:25:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_0732",
                    "started_at": "2025-07-16T07:30:00+00:00",
                    "completed_at": "2025-07-16T07:32:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_0732.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_0735",
                    "taken_at": "2025-07-16T07:35:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_2025_07_16_0732_morning_check",
                    "entity": "report",
                    "entity_id": "rpt_2025_07_16_0732",
                    "field": "morning_health_check",
                    "rule": "reporting_policy",
                    "details": "pre=snap_2025_07_16_0725; post=snap_2025_07_16_0735",
                    "created_at": "2025-07-16T07:32:00+00:00"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_0732"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_52",
        "instruction": "Coordinate a mid-morning service-desk review on 2025-07-16. Examine High priority tickets and items that are In Progress, capture snapshots, and generate the health report using run_id=rpt_2025_07_16_1102 (started_at=2025-07-16T11:00:00+00:00, completed_at=2025-07-16T11:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1102.pdf). Log the pre-run snapshot_id=snap_2025_07_16_1055 at 2025-07-16T10:55:00+00:00 and the post-run snapshot_id=snap_2025_07_16_1105 at 2025-07-16T11:05:00+00:00 for {New, Open, In Progress, On Hold}, and recalculate the daily metrics for 2025-07-16.You must record pre\u2011run snapshot_id=snap_2025_07_16_1055 at 2025-07-16T10:55:00+00:00 and post\u2011run snapshot_id=snap_2025_07_16_1105 at 2025-07-16T11:05:00+00:00 for {New, Open, In Progress, On Hold}, and recompute daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "priority": "High"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1055",
                    "taken_at": "2025-07-16T10:55:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1102",
                    "started_at": "2025-07-16T11:00:00+00:00",
                    "completed_at": "2025-07-16T11:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1102.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1105",
                    "taken_at": "2025-07-16T11:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1102"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_53",
        "instruction": "Handle a category-focused midday report on 2025-07-16. Inspect Access Request and MDM tickets across statuses New and On Hold, capture necessary snapshots, and generate the health report using run_id=rpt_2025_07_16_1232 (started_at=2025-07-16T12:30:00+00:00, completed_at=2025-07-16T12:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1232.pdf). Record a pre-run snapshot_id=snap_2025_07_16_1225 at 2025-07-16T12:25:00+00:00 and a post-run snapshot_id=snap_2025_07_16_1235 at 2025-07-16T12:35:00+00:00 for statuses {New, Open, In Progress, On Hold}, and recalculate daily metrics for 2025-07-16.You must record pre\u2011run snapshot_id=snap_2025_07_16_1225 at 2025-07-16T12:25:00+00:00 and post\u2011run snapshot_id=snap_2025_07_16_1235 at 2025-07-16T12:35:00+00:00 for statuses {New, Open, In Progress, On Hold}, and recompute daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "Access Request",
                    "status": "New"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "Access Request",
                    "status": "On Hold"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "MDM",
                    "status": "New"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "MDM",
                    "status": "On Hold"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1225",
                    "taken_at": "2025-07-16T12:25:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1232",
                    "started_at": "2025-07-16T12:30:00+00:00",
                    "completed_at": "2025-07-16T12:32:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1232.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1235",
                    "taken_at": "2025-07-16T12:35:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1232"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_54",
        "instruction": "Coordinate an afternoon SLA oversight on 2025-07-16: examine active SLA escalation records (issue_type=SLA Escalation, status=In Progress) and Urgent tickets in On Hold, then create the health report using run_id=rpt_2025_07_16_1502 (started_at=2025-07-16T15:00:00+00:00, completed_at=2025-07-16T15:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1502.pdf). Document the backlog state immediately before and after the run with snapshot_id=snap_2025_07_16_1455 (taken_at=2025-07-16T14:55:00+00:00) and snapshot_id=snap_2025_07_16_1505 (taken_at=2025-07-16T15:05:00+00:00) for statuses {New, Open, In Progress, On Hold}. Register a validation entry issue_id=vld_2025_07_16_1502_sla_oversight referencing the run and snapshots, and update daily metrics for 2025-07-16.Record the backlog state immediately before and after the run with snapshot_id=snap_2025_07_16_1455 (taken_at=2025-07-16T14:55:00+00:00) and snapshot_id=snap_2025_07_16_1505 (taken_at=2025-07-16T15:05:00+00:00) for statuses {New, Open, In Progress, On Hold}. Register a validation entry issue_id=vld_2025_07_16_1502_sla_oversight referencing the run and snapshots, and recompute daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindJiraTickets",
                "arguments": {
                    "issue_type": "SLA Escalation",
                    "status": "In Progress"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "On Hold",
                    "priority": "Urgent"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1455",
                    "taken_at": "2025-07-16T14:55:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1502",
                    "started_at": "2025-07-16T15:00:00+00:00",
                    "completed_at": "2025-07-16T15:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1502.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1505",
                    "taken_at": "2025-07-16T15:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_2025_07_16_1502_sla_oversight",
                    "entity": "report",
                    "entity_id": "rpt_2025_07_16_1502",
                    "field": "sla_oversight",
                    "rule": "reporting_policy",
                    "details": "pre=snap_2025_07_16_1455; post=snap_2025_07_16_1505",
                    "created_at": "2025-07-16T15:02:00+00:00"
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1502"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_55",
        "instruction": "Handle a priority-focused afternoon review on 2025-07-16. Examine High and Urgent tickets, collect snapshots, and create the health report using run_id=rpt_2025_07_16_1602 (started_at=2025-07-16T16:00:00+00:00, completed_at=2025-07-16T16:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1602.pdf). You should log pre/post snapshots (snap_2025_07_16_1555 at 2025-07-16T15:55:00+00:00 and snap_2025_07_16_1605 at 2025-07-16T16:05:00+00:00 for statuses {New, Open, In Progress, On Hold}). To guarantee date-bounded metrics, you must document two deterministic review markers at 16:00Z linked to the review owner (employee_id=emp_0023, the Service Desk Analyst), both in category 'Service Desk'. Identify ticket_ids as T2025_07_16_1600_high and T2025_07_16_1600_urgent, and determine subjects from the run_id as rpt_2025_07_16_1602_high and rpt_2025_07_16_1602_urgent; ensure only the High marker is closed at 16:02Z. After this, recalculate daily metrics for 2025-07-16.You must record pre/post snapshots (snap_2025_07_16_1555 at 2025-07-16T15:55:00+00:00 and snap_2025_07_16_1605 at 2025-07-16T16:05:00+00:00 for statuses {New, Open, In Progress, On Hold}).To ensure date\u2011bounded metrics, you must log two deterministic review markers at 16:00Z attributed to the review owner (employee_id=emp_0023, the Service Desk Analyst), both in category 'Service Desk'. Derive ticket_ids as T2025_07_16_1600_high and T2025_07_16_1600_urgent, and derive subjects from the run_id as rpt_2025_07_16_1602_high and rpt_2025_07_16_1602_urgent; close only the High marker at 16:02Z. Then recompute daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "priority": "Urgent"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "priority": "High"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1555",
                    "taken_at": "2025-07-16T15:55:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "CreateTicket",
                "arguments": {
                    "ticket_id": "T2025_07_16_1600_high",
                    "employee_id": "emp_0023",
                    "category": "Service Desk",
                    "priority": "High",
                    "status": "New",
                    "subject": "rpt_2025_07_16_1602_high",
                    "opened_at": "2025-07-16T16:00:00+00:00"
                },
            },
            {
                "name": "CreateTicket",
                "arguments": {
                    "ticket_id": "T2025_07_16_1600_urgent",
                    "employee_id": "emp_0023",
                    "category": "Service Desk",
                    "priority": "Urgent",
                    "status": "New",
                    "subject": "rpt_2025_07_16_1602_urgent",
                    "opened_at": "2025-07-16T16:00:00+00:00"
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1602",
                    "started_at": "2025-07-16T16:00:00+00:00",
                    "completed_at": "2025-07-16T16:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1602.pdf"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T2025_07_16_1600_high",
                    "status": "Closed",
                    "closed_at": "2025-07-16T16:02:00+00:00"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1605",
                    "taken_at": "2025-07-16T16:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1602"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_56",
        "instruction": "In accordance with reporting policy, conduct a category audit slice on 2025-07-16 evaluating Software and Account tickets in New and In Progress states. Implement run_id=rpt_2025_07_16_1632 (started_at=2025-07-16T16:30:00+00:00, completed_at=2025-07-16T16:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1632.pdf), and record the backlog state just before and after the run with snapshot_id=snap_2025_07_16_1625 (16:25 UTC) and snapshot_id=snap_2025_07_16_1635 (16:35 UTC) for statuses {New, Open, In Progress, On Hold}.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "Software",
                    "status": "New"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "Software",
                    "status": "In Progress"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "Account",
                    "status": "In Progress"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "category": "Account",
                    "status": "New"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1625",
                    "taken_at": "2025-07-16T16:25:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1632",
                    "started_at": "2025-07-16T16:30:00+00:00",
                    "completed_at": "2025-07-16T16:32:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1632.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1635",
                    "taken_at": "2025-07-16T16:35:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1632"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_57",
        "instruction": "Handle an On Hold queue focus specifically on 2025\u201107\u201116 under the reporting policy: review On Hold tickets across various categories, maintain a before-and-after view, and generate the daily health report using deterministic anchors. Utilize run_id=rpt_2025_07_16_1702 (started_at=2025-07-16T17:00:00+00:00, completed_at=2025-07-16T17:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1702.pdf) along with snapshots snap_2025_07_16_1655 (16:55) and snap_2025_07_16_1705 (17:05) over {New, Open, In Progress, On Hold}. Log one validation entry that mentions the report and both snapshots once the post snapshot is captured, with created_at set to the post snapshot taken_at (2025-07-16T17:05:00+00:00); recalculate daily metrics for 2025\u201107\u201116.Use run_id=rpt_2025_07_16_1702 (started_at=2025-07-16T17:00:00+00:00, completed_at=2025-07-16T17:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1702.pdf) and snapshots snap_2025_07_16_1655 (16:55) and snap_2025_07_16_1705 (17:05) over {New, Open, In Progress, On Hold}.Register one validation entry that references the report and both snapshots after the post snapshot is captured, with created_at equal to the post snapshot taken_at (2025-07-16T17:05:00+00:00); recompute daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "On Hold"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1655",
                    "taken_at": "2025-07-16T16:55:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1702",
                    "started_at": "2025-07-16T17:00:00+00:00",
                    "completed_at": "2025-07-16T17:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1702.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1705",
                    "taken_at": "2025-07-16T17:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_2025_07_16_1702_on_hold_focus",
                    "entity": "report",
                    "entity_id": "rpt_2025_07_16_1702",
                    "field": "on_hold_focus",
                    "rule": "reporting_policy",
                    "details": "pre=snap_2025_07_16_1655; post=snap_2025_07_16_1705",
                    "created_at": "2025-07-16T17:05:00+00:00"
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1702"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_58",
        "instruction": "Coordinate an evening New\u2011ticket focus on 2025\u201107\u201116. Conduct an inspection of New tickets by category (Software, Account), save snapshots, and generate the health report using run_id=rpt_2025_07_16_1802 (started_at=2025-07-16T18:00:00+00:00, completed_at=2025-07-16T18:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1802.pdf). Ensure to save pre/post snapshots (snap_2025_07_16_1755 at 2025-07-16T17:55:00+00:00 and snap_2025_07_16_1805 at 2025-07-16T18:05:00+00:00 for statuses {New, Open, In Progress, On Hold}) and update daily metrics for 2025\u201107\u201116.You must save pre/post snapshots (snap_2025_07_16_1755 at 2025-07-16T17:55:00+00:00 and snap_2025_07_16_1805 at 2025-07-16T18:05:00+00:00 for statuses {New, Open, In Progress, On Hold}) and recompute daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "New",
                    "category": "Software"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "New",
                    "category": "Account"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1755",
                    "taken_at": "2025-07-16T17:55:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1802",
                    "started_at": "2025-07-16T18:00:00+00:00",
                    "completed_at": "2025-07-16T18:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1802.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1805",
                    "taken_at": "2025-07-16T18:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1802"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_59",
        "instruction": "Handle a late-evening hold/priority review on 2025\u201107\u201116. Inspect On Hold and Urgent tickets, capture snapshots, and generate the health report using run_id=rpt_2025_07_16_1902 (started_at=2025-07-16T19:00:00+00:00, completed_at=2025-07-16T19:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1902.pdf). Record snapshots (snap_2025_07_16_1855 at 2025-07-16T18:55:00+00:00 and snap_2025_07_16_1905 at 2025-07-16T19:05:00+00:00 for statuses {New, Open, In Progress, On Hold}) and recalculate daily metrics for 2025\u201107\u201116.You must record snapshots (snap_2025_07_16_1855 at 2025-07-16T18:55:00+00:00 and snap_2025_07_16_1905 at 2025-07-16T19:05:00+00:00 for statuses {New, Open, In Progress, On Hold}) and recompute daily metrics for 2025\u201107\u201116.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "On Hold"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "priority": "Urgent"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1855",
                    "taken_at": "2025-07-16T18:55:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1902",
                    "started_at": "2025-07-16T19:00:00+00:00",
                    "completed_at": "2025-07-16T19:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1902.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1905",
                    "taken_at": "2025-07-16T19:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "RecomputeDailyMetrics",
                "arguments": {
                    "date": "2025-07-16"
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_1902"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_60",
        "instruction": "In accordance with the end-of-day reporting policy for 2025\u201107\u201116, evaluate the Open and In Progress queues, record the backlog state both immediately before and after the execution, and create the final service-desk health report. Use run_id=rpt_2025_07_16_2002 (started_at=2025-07-16T20:00:00+00:00, completed_at=2025-07-16T20:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_2002.pdf), and capture snapshots with snapshot_id=snap_2025_07_16_1955 (19:55 UTC) and snapshot_id=snap_2025_07_16_2005 (20:05 UTC) for statuses {New, Open, In Progress, On Hold}.Use run_id=rpt_2025_07_16_2002 (started_at=2025-07-16T20:00:00+00:00, completed_at=2025-07-16T20:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_2002.pdf), and capture snapshots with snapshot_id=snap_2025_07_16_1955 (19:55 UTC) and snapshot_id=snap_2025_07_16_2005 (20:05 UTC) for statuses {New, Open, In Progress, On Hold}.",
        "actions": [
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "Open"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1955",
                    "taken_at": "2025-07-16T19:55:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_2002",
                    "started_at": "2025-07-16T20:00:00+00:00",
                    "completed_at": "2025-07-16T20:02:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_2002.pdf"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_2005",
                    "taken_at": "2025-07-16T20:05:00+00:00",
                    "statuses_in_scope": [
                        "New",
                        "Open",
                        "In Progress",
                        "On Hold"
                    ]
                }
            }
        ],
        "outputs": [
                "rpt_2025_07_16_2002"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_61",
        "instruction": "In line with the RBAC review policy from 2025-07-16, ensure that Marketing accounts mirror the baseline group membership for their designated roles. Examine Noel Rodriguez (employee_id=emp_0031, job_title=Content Strategist) and Logan Nguyen (employee_id=emp_0021, job_title=Design Lead), align their directory accounts with the Marketing baselines from the role map, and confirm this alignment is auditable. Utilize actor rbac_audit and fixed anchors 2025-07-16T10:00:00+00:00 (emp_0031) and 2025-07-16T10:01:00+00:00 (emp_0021). Do not alter licenses, devices, or mailboxes.You must review Noel Rodriguez (employee_id=emp_0031, job_title=Content Strategist) and Logan Nguyen (employee_id=emp_0021, job_title=Design Lead), align their directory accounts to the Marketing baselines derived from the role map, and ensure the alignment is auditable. Use actor rbac_audit and fixed anchors 2025-07-16T10:00:00+00:00 (emp_0031) and 2025-07-16T10:01:00+00:00 (emp_0021). Do not modify licenses, devices, or mailboxes.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0031"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_351bb4",
                    "group_ids": [
                        "grp_marketing_719b",
                        "grp_marketing_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_43980f",
                    "group_ids": [
                        "grp_marketing_c05f",
                        "grp_marketing_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:01:00+00:00"
                }
            }
        ],
        "outputs": [
                "acc_351bb4",
                "acc_43980f"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_62",
        "instruction": "In accordance with the RBAC review policy dated 2025-07-16, verify that HR accounts exhibit the baseline group membership for their roles. Assess Jamie Chen (employee_id=emp_0001, job_title=HRBP) and Emerson Davis (employee_id=emp_0014, job_title=HR Generalist), align their directory accounts to HR baselines, and document the remediation. Employ deterministic audit anchors on 2025-07-16: perform group alignment for emp_0001 at 10:05:00Z and for emp_0014 at 10:06:00Z by actor rbac_audit; then record validation entries with IDs vld_acc_dc71c8_2025_07_16_1007 at 10:07:00Z and vld_acc_88c4f4_2025_07_16_1007 at 10:07:30Z capturing the precise groups after alignment.You must review Jamie Chen (employee_id=emp_0001, job_title=HRBP) and Emerson Davis (employee_id=emp_0014, job_title=HR Generalist), align their directory accounts to HR baselines, and register the remediation.Use deterministic audit anchors on 2025-07-16: apply group alignment for emp_0001 at 10:05:00Z and for emp_0014 at 10:06:00Z by actor rbac_audit; then record validation entries with IDs vld_acc_dc71c8_2025_07_16_1007 at 10:07:00Z and vld_acc_88c4f4_2025_07_16_1007 at 10:07:30Z capturing the exact groups after alignment.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "HR",
                    "job_title": "HRBP"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_dc71c8",
                    "group_ids": [
                        "grp_hr_82f8",
                        "grp_hr_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:05:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0014"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0014"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "HR",
                    "job_title": "HR Generalist"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_88c4f4",
                    "group_ids": [
                        "grp_hr_a74e",
                        "grp_hr_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:06:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_dc71c8_2025_07_16_1007",
                    "entity": "directory_accounts",
                    "entity_id": "acc_dc71c8",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_hr_82f8','grp_hr_all']",
                    "created_at": "2025-07-16T10:07:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_88c4f4_2025_07_16_1007",
                    "entity": "directory_accounts",
                    "entity_id": "acc_88c4f4",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_hr_a74e','grp_hr_all']",
                    "created_at": "2025-07-16T10:07:30+00:00"
                }
            }
        ],
        "outputs": [
                "vld_acc_dc71c8_2025_07_16_1007",
                "vld_acc_88c4f4_2025_07_16_1007"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_63",
        "instruction": "According to the RBAC review policy dated 2025-07-16, you are responsible for ensuring Support accounts exhibit baseline access and posture, rather than just group memberships. Assess Finley Thomas (employee_id=emp_0026) and Sasha Phillips (employee_id=emp_0038), align their groups to the Support/Support Manager baseline fixed at anchors (10:10Z and 10:11Z, actor rbac_audit), and confirm the baseline posture across license bundle and mailbox retention. Document the verified posture deterministically by using validation records derived from account_id and anchor time; do not initiate escalation tickets unless deviations are found.Review Finley Thomas (employee_id=emp_0026) and Sasha Phillips (employee_id=emp_0038), align groups to the Support/Support Manager baseline at fixed anchors (10:10Z and 10:11Z, actor rbac_audit), and verify baseline posture across license bundle and mailbox retention.Document the verified posture deterministically using validation records derived from account_id and the anchor time; do not open escalation tickets unless drift is detected.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0026"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0026"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Support",
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_bac647",
                    "group_ids": [
                        "grp_support_ada3",
                        "grp_support_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:10:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_bac647"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0026"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_bac647_2025_07_16_1010_posture",
                    "entity": "directory_accounts",
                    "entity_id": "acc_bac647",
                    "field": "posture",
                    "rule": "support_baseline_verified",
                    "details": "licenses=['lic_slack_ent','lic_m365_e3']; mailbox_retention=std_2y",
                    "created_at": "2025-07-16T10:10:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Support",
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_839501",
                    "group_ids": [
                        "grp_support_ada3",
                        "grp_support_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:11:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_839501"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_839501_2025_07_16_1011_posture",
                    "entity": "directory_accounts",
                    "entity_id": "acc_839501",
                    "field": "posture",
                    "rule": "support_baseline_verified",
                    "details": "licenses=['lic_slack_ent','lic_m365_e3']; mailbox_retention=std_2y",
                    "created_at": "2025-07-16T10:11:00+00:00"
                }
            }
        ],
        "outputs": [
                "acc_bac647",
                "acc_839501",
                "vld_acc_bac647_2025_07_16_1010_posture",
                "vld_acc_839501_2025_07_16_1011_posture"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_64",
        "instruction": "Following the RBAC review policy dated 2025-07-16, ensure that Engineering accounts mirror baseline group memberships for their respective roles. You need to examine Micah White (employee_id=emp_0030, DevOps Engineer) and Drew Evans (employee_id=emp_0040, Software Engineer), align their directory accounts with Engineering baselines, and make certain the alignment is auditable. Utilize actor rbac_audit with fixed audit timestamps 2025-07-16T10:15:00+00:00 (for emp_0030) and 2025-07-16T10:16:00+00:00 (for emp_0040). Moreover, verify that each account possesses the default license bundle for Engineering (lic_m365_e3, lic_github_ent, lic_slack_ent) and that their mailboxes adhere to standard retention (std_2y). For auditing purposes, record validation entries vld_acc_db017d_2025_07_16_1015 and vld_acc_54337a_2025_07_16_1016 at 10:15:30 and 10:16:30 respectively, reflecting the aligned group_ids.You must review Micah White (employee_id=emp_0030, DevOps Engineer) and Drew Evans (employee_id=emp_0040, Software Engineer), align their directory accounts to Engineering baselines, and ensure the alignment is auditable. Use actor rbac_audit with fixed audit timestamps 2025-07-16T10:15:00+00:00 (for emp_0030) and 2025-07-16T10:16:00+00:00 (for emp_0040). Also verify that each account holds the default license bundle for Engineering (lic_m365_e3, lic_github_ent, lic_slack_ent) and that their mailboxes have standard retention (std_2y). For auditability, record validation entries vld_acc_db017d_2025_07_16_1015 and vld_acc_54337a_2025_07_16_1016 at 10:15:30 and 10:16:30 respectively, reflecting the aligned group_ids.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Engineering",
                    "job_title": "DevOps Engineer"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_db017d"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_db017d",
                    "group_ids": [
                        "grp_engineering_4162",
                        "grp_engineering_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:15:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_db017d_2025_07_16_1015",
                    "entity": "directory_accounts",
                    "entity_id": "acc_db017d",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_engineering_4162','grp_engineering_all']",
                    "created_at": "2025-07-16T10:15:30+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Engineering",
                    "job_title": "Software Engineer"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_54337a"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_54337a",
                    "group_ids": [
                        "grp_engineering_cbaf",
                        "grp_engineering_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:16:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_54337a_2025_07_16_1016",
                    "entity": "directory_accounts",
                    "entity_id": "acc_54337a",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_engineering_cbaf','grp_engineering_all']",
                    "created_at": "2025-07-16T10:16:30+00:00"
                }
            }
        ],
        "outputs": [
                "acc_db017d",
                "acc_54337a",
                "vld_acc_db017d_2025_07_16_1015",
                "vld_acc_54337a_2025_07_16_1016"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_65",
        "instruction": "According to the RBAC review policy dated 2025-07-16, handle the task of ensuring Finance accounts accurately show baseline group membership as per their roles. Examine Dakota Wilson (employee_id=emp_0017, Controller) and Lane Taylor (employee_id=emp_0029, Accounting Manager); adjust their directory accounts to match Finance baselines and log the remediation using the actor rbac_audit. Anchor audit timestamps at 2025-07-16T10:20:00+00:00 (emp_0017) and 2025-07-16T10:21:00+00:00 (emp_0029). Confirm the Finance license posture and mailbox retention for both accounts. For auditability purposes, draft validation records that demonstrate the aligned group_ids, deriving deterministic identifiers from the account_id and the respective anchor time (while avoiding creation of any uncontrolled values).Review Dakota Wilson (employee_id=emp_0017, Controller) and Lane Taylor (employee_id=emp_0029, Accounting Manager); align their directory accounts to Finance baselines and register the remediation using actor rbac_audit.Anchor audit timestamps at 2025-07-16T10:20:00+00:00 (emp_0017) and 2025-07-16T10:21:00+00:00 (emp_0029). Verify Finance license posture and mailbox retention for both accounts.For auditability, write validation records that reflect the aligned group_ids, deriving deterministic identifiers from the account_id and the corresponding anchor time (without inventing any uncontrolled values).",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Finance",
                    "job_title": "Controller"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_82aecf"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_82aecf",
                    "group_ids": [
                        "grp_finance_c147",
                        "grp_finance_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:20:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_82aecf_2025_07_16_1020",
                    "entity": "directory_accounts",
                    "entity_id": "acc_82aecf",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_finance_c147','grp_finance_all']",
                    "created_at": "2025-07-16T10:20:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Finance",
                    "job_title": "Accounting Manager"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_48efe8"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_48efe8",
                    "group_ids": [
                        "grp_finance_5d50",
                        "grp_finance_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:21:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_48efe8_2025_07_16_1021",
                    "entity": "directory_accounts",
                    "entity_id": "acc_48efe8",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_finance_5d50','grp_finance_all']",
                    "created_at": "2025-07-16T10:21:00+00:00"
                }
            }
        ],
        "outputs": [
                "acc_82aecf",
                "acc_48efe8",
                "vld_acc_82aecf_2025_07_16_1020",
                "vld_acc_48efe8_2025_07_16_1021"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_66",
        "instruction": "In accordance with the RBAC review policy dated 2025-07-16, you are tasked with ensuring Operations accounts show correct baseline group membership for their respective roles. Review Avery Zhang (employee_id=emp_0010, Ops Coordinator) and Peyton Shah (employee_id=emp_0015, Supply Chain Analyst), align their directory accounts to match Operations baselines, and verify that the alignment is auditable. Use the actor rbac_audit and apply the fixed audit timestamps 2025-07-16T10:25:00+00:00 (for emp_0010) and 2025-07-16T10:26:00+00:00 (for emp_0015). Additionally, check the license posture through license-assignments and mailbox retention for both accounts. For audit purposes, record validation entries vld_acc_4d16c0_2025_07_16_1025 and vld_acc_3818d8_2025_07_16_1026 at 10:25:30 and 10:26:30 respectively, reflecting the aligned group_ids.You must review Avery Zhang (employee_id=emp_0010, Ops Coordinator) and Peyton Shah (employee_id=emp_0015, Supply Chain Analyst), align their directory accounts to Operations baselines, and ensure the alignment is auditable. Use actor rbac_audit and the fixed audit timestamps 2025-07-16T10:25:00+00:00 (for emp_0010) and 2025-07-16T10:26:00+00:00 (for emp_0015).Also verify license posture via license-assignments and mailbox retention for both accounts. For auditability, record validation entries vld_acc_4d16c0_2025_07_16_1025 and vld_acc_3818d8_2025_07_16_1026 at 10:25:30 and 10:26:30 respectively, reflecting the aligned group_ids.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Operations",
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_4d16c0"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_4d16c0",
                    "group_ids": [
                        "grp_operations_772e",
                        "grp_operations_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:25:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_4d16c0_2025_07_16_1025",
                    "entity": "directory_accounts",
                    "entity_id": "acc_4d16c0",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_operations_772e','grp_operations_all']",
                    "created_at": "2025-07-16T10:25:30+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0015"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0015"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Operations",
                    "job_title": "Supply Chain Analyst"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_3818d8"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0015"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_3818d8",
                    "group_ids": [
                        "grp_operations_dcb3",
                        "grp_operations_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:26:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_3818d8_2025_07_16_1026",
                    "entity": "directory_accounts",
                    "entity_id": "acc_3818d8",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_operations_dcb3','grp_operations_all']",
                    "created_at": "2025-07-16T10:26:30+00:00"
                }
            }
        ],
        "outputs": [
                "acc_4d16c0",
                "acc_3818d8",
                "vld_acc_4d16c0_2025_07_16_1025",
                "vld_acc_3818d8_2025_07_16_1026"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_67",
        "instruction": "According to the RBAC review policy dated 2025-07-16, handle making sure IT accounts mirror the baseline access posture for their roles. You need to review Sam Tran (employee_id=emp_0004, Systems Engineer) and Kendall Garcia (employee_id=emp_0023, Service Desk Analyst). Align directory groups to the IT baselines using actor rbac_audit at fixed anchors within the 10:30Z window to eliminate ambiguity: allocate the earlier audit to the lower employee_id at 2025-07-16T10:30:00+00:00 and the subsequent audit at 2025-07-16T10:31:00+00:00. Ensure each account possesses its baseline license bundle and standard mailbox retention; when the posture is already fulfilled, release an auditable no-change group write. Document validation entries with created_at=audit+30s and the issue_id format vld_acc_<account_id>_YYYY_MM_DD_HHMM to ensure outputs are unique and reproducible.You must review Sam Tran (employee_id=emp_0004, Systems Engineer) and Kendall Garcia (employee_id=emp_0023, Service Desk Analyst). You must align directory groups to the IT baselines using actor rbac_audit at fixed anchors within the 10:30Z window to remove ambiguity: assign the earlier audit to the lower employee_id at 2025-07-16T10:30:00+00:00 and the later audit at 2025-07-16T10:31:00+00:00.You must verify each account holds its baseline license bundle and standard mailbox retention; when posture is already satisfied, you must emit an auditable no\u2011change group write. You must record validation entries with created_at=audit+30s and issue_id format vld_acc_<account_id>_YYYY_MM_DD_HHMM to make outputs unique and reproducible.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "IT",
                    "job_title": "Systems Engineer"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_38d007"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_38d007",
                    "group_ids": [
                        "grp_it_6b89",
                        "grp_it_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:30:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_38d007_2025_07_16_1030",
                    "entity": "directory_accounts",
                    "entity_id": "acc_38d007",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_it_6b89','grp_it_all']; licenses=['lic_m365_e3','lic_github_ent','lic_slack_ent']; mailbox_retention=std_2y",
                    "created_at": "2025-07-16T10:30:30+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0023"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0023"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "IT",
                    "job_title": "Service Desk Analyst"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_696506"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0023"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_696506",
                    "group_ids": [
                        "grp_it_2990",
                        "grp_it_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:31:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_696506_2025_07_16_1031",
                    "entity": "directory_accounts",
                    "entity_id": "acc_696506",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_it_2990','grp_it_all']; licenses=['lic_m365_e3','lic_github_ent','lic_slack_ent']; mailbox_retention=std_2y",
                    "created_at": "2025-07-16T10:31:30+00:00"
                }
            }
        ],
        "outputs": [
                "acc_38d007",
                "acc_696506",
                "vld_acc_38d007_2025_07_16_1030",
                "vld_acc_696506_2025_07_16_1031"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_68",
        "instruction": "Based on the RBAC review policy dated 2025-07-16, coordinate ensuring Sales accounts reflect baseline group membership for their roles. You have to review Cameron Patel (employee_id=emp_0013, Sales Manager) and Kai Jackson (employee_id=emp_0028, Sales Manager), align their directory accounts to Sales baselines, and guarantee the alignment is auditable. Utilize actor rbac_audit with fixed audit timestamps 2025-07-16T10:35:00+00:00 (for emp_0013) and 2025-07-16T10:36:00+00:00 (for emp_0028). Also, check that each account holds the default Sales license bundle (lic_m365_e3, lic_salesforce, lic_slack_ent), that their mailboxes adhere to standard retention (std_2y), and that their assigned assets are documented.You must review Cameron Patel (employee_id=emp_0013, Sales Manager) and Kai Jackson (employee_id=emp_0028, Sales Manager), align their directory accounts to Sales baselines, and ensure the alignment is auditable. Use actor rbac_audit with fixed audit timestamps 2025-07-16T10:35:00+00:00 (for emp_0013) and 2025-07-16T10:36:00+00:00 (for emp_0028). Also verify that each account holds the default Sales license bundle (lic_m365_e3, lic_salesforce, lic_slack_ent), that their mailboxes use standard retention (std_2y), and that their assigned assets are recorded.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Sales",
                    "job_title": "Sales Manager"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_78fb5c"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0013"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_78fb5c",
                    "group_ids": [
                        "grp_sales_4bcb",
                        "grp_sales_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:35:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Sales",
                    "job_title": "Sales Manager"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_81d8d5"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "FindAssets",
                "arguments": {
                    "assigned_to": "emp_0028"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_81d8d5",
                    "group_ids": [
                        "grp_sales_4bcb",
                        "grp_sales_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:36:00+00:00"
                }
            }
        ],
        "outputs": [
                "acc_78fb5c",
                "acc_81d8d5"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_69",
        "instruction": "In accordance with RBAC remediation scheduled for 2025-07-16, handle the reassertion of Marketing baselines to avoid any drift. Evaluate Casey Liu (employee_id=emp_0002, Content Strategist) and Tatum Green (employee_id=emp_0034, Content Strategist), reapply baselines, and make sure the alignment is auditable. Utilize the actor rbac_audit and apply fixed audit timestamps of 2025-07-16T10:40:00+00:00 (for emp_0002) and 2025-07-16T10:41:00+00:00 (for emp_0034). Should you find any non-baseline license entitlements for emp_0002, proceed to revoke them with revoked_at=2025-07-16T10:41:30+00:00.You must review Casey Liu (employee_id=emp_0002, Content Strategist) and Tatum Green (employee_id=emp_0034, Content Strategist), reapply baselines, and ensure alignment is auditable. Use actor rbac_audit and fixed audit timestamps 2025-07-16T10:40:00+00:00 (for emp_0002) and 2025-07-16T10:41:00+00:00 (for emp_0034). If you detect any non-baseline license entitlements for emp_0002, revoke them with revoked_at=2025-07-16T10:41:30+00:00.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_287fb8"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_287fb8",
                    "group_ids": [
                        "grp_marketing_719b",
                        "grp_marketing_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:40:00+00:00"
                },
            },
            {
                "name": "RevokeLicense",
                "arguments": {
                    "account_id": "acc_287fb8",
                    "employee_id": "emp_0002",
                    "license_id": "lic_adobe_cc",
                    "revoked_at": "2025-07-16T10:41:30+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_baacc3"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_baacc3",
                    "group_ids": [
                        "grp_marketing_719b",
                        "grp_marketing_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:41:00+00:00"
                }
            }
        ],
        "outputs": [
                "acc_287fb8",
                "acc_baacc3"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_70",
        "instruction": "Based on RBAC remediation scheduled for 2025-07-16, coordinate the alignment of Finance and Engineering accounts that have exhibited historical changes. Review Shawn Lewis (employee_id=emp_0033, Financial Analyst) and Zion Mitchell (employee_id=emp_0036, DevOps Engineer). Implement group alignment using the actor rbac_audit at the specified anchors 2025-07-16T10:45:00+00:00 (Finance) and 2025-07-16T10:46:00+00:00 (Engineering). Adhere to the offboarding policy: if a directory account is disabled, refrain from assigning or expanding licenses. Instead, document the situation with a validation record derived from the account_id and the Finance anchor, detailing the skipped licensing due to disabled status and confirming mailbox retention. For accounts that are enabled, reinstate baseline groups with a no-change write to ensure auditable alignment. Record posture validations within the anchor minute using deterministic identifiers derived from account_id and the anchor time to ensure reproducibility of outputs without laying out internal steps.Review Shawn Lewis (employee_id=emp_0033, Financial Analyst) and Zion Mitchell (employee_id=emp_0036, DevOps Engineer). Apply group alignment using actor rbac_audit at deterministic anchors 2025-07-16T10:45:00+00:00 (Finance) and 2025-07-16T10:46:00+00:00 (Engineering).Follow offboarding policy: if a directory account is disabled, you do not assign or expand licenses. Instead, you document the posture with a validation record that is derived from the account_id and the Finance anchor, explaining that licensing was skipped due to disabled status and confirming mailbox retention. For enabled accounts, you may reassert baseline groups as a no-change write to produce auditable alignment.Document posture validations within the anchor minute using deterministic identifiers derived from account_id and the anchor time to keep outputs reproducible without prescribing internal steps.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Finance",
                    "job_title": "Financial Analyst"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_f589dc"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_f589dc_2025_07_16_1045_skip_licensing",
                    "entity": "directory_accounts",
                    "entity_id": "acc_f589dc",
                    "field": "license_provisioning",
                    "rule": "skip_for_disabled_account",
                    "details": "licensing skipped due to directory.status='disabled'; mailbox retention verified",
                    "created_at": "2025-07-16T10:45:30+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Engineering",
                    "job_title": "DevOps Engineer"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "account_id": "acc_f9a6bc"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_f9a6bc",
                    "group_ids": [
                        "grp_engineering_4162",
                        "grp_engineering_all"
                    ],
                    "actor": "rbac_audit",
                    "timestamp": "2025-07-16T10:46:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_acc_f9a6bc_2025_07_16_1046",
                    "entity": "directory_accounts",
                    "entity_id": "acc_f9a6bc",
                    "field": "group_ids",
                    "rule": "rbac_baseline_alignment",
                    "details": "groups=['grp_engineering_4162','grp_engineering_all']",
                    "created_at": "2025-07-16T10:46:30+00:00"
                }
            }
        ],
        "outputs": [
                "acc_f589dc",
                "acc_f9a6bc"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_71",
        "instruction": "On 2025-07-16 you are required to handle an email service incident in accordance with the incident management policy. Ensure there is only one P1 incident of record anchored deterministically at 11:00Z. Swiftly adjust the handling status as per the policy, mark the affected ticket T5027 as On Hold, document the lifecycle with event=incident indicating a blocked state during the incident, and rigorously log the standard service desk health report. Take the report times from the anchor: started_at=anchor and completed_at=anchor+30s; source_ticket_window_days=30, compute run_id from started_at as rpt_YYYY_MM_DD_HHMMSS and output_path_pdf as s3://reports/ServiceDesk_Health_Report_{anchor_date}_{category}.pdf. Establish follow-up handling timestamps as anchor+60s and employ actor incident_coordinator for lifecycle handling. Calculate all other identifiers and timestamps deterministically from the 11:00Z anchor and the incident category (email) plus memo_id memo_inc_email_2025_07_16; do not hard-code database values.You must maintain a single P1 incident of record anchored deterministically at 11:00Z, transition handling status promptly per policy, place affected ticket T5027 On Hold, record lifecycle with event=incident reflecting a blocked state during the incident, and register the standard service desk health report deterministically. Derive report times from the anchor: started_at=anchor and completed_at=anchor+30s; source_ticket_window_days=30 and derive run_id from started_at as rpt_YYYY_MM_DD_HHMMSS and output_path_pdf as s3://reports/ServiceDesk_Health_Report_{anchor_date}_{category}.pdf. Derive follow\u2011up handling timestamps as anchor+60s and use actor incident_coordinator for lifecycle handling. You must derive all other identifiers and timestamps deterministically from the 11:00Z anchor and the incident category (email) and memo_id memo_inc_email_2025_07_16; do not hard\u2011code database values.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "JIRA-incident-email-2025_07_16_1100",
                    "issue_type": "Incident",
                    "summary": "incident=email;ticket=T5027;anchor=2025-07-16T11:00:00+00:00",
                    "priority": "P1",
                    "status": "New",
                    "created_at": "2025-07-16T11:00:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "JIRA-incident-email-2025_07_16_1100",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:01:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5027",
                    "status": "On Hold"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_email_2025_07_16_1100",
                    "memo_id": "memo_inc_email_2025_07_16",
                    "employee_ref": "incident_email",
                    "event": "incident",
                    "status": "in_progress",
                    "created_at": "2025-07-16T11:00:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_email_2025_07_16_1100",
                    "status": "blocked",
                    "timestamp": "2025-07-16T11:01:00+00:00",
                    "actor": "incident_coordinator"
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_110000",
                    "started_at": "2025-07-16T11:00:00+00:00",
                    "completed_at": "2025-07-16T11:00:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025_07_16_email.pdf"
                }
            }
        ],
        "outputs": [
                "JIRA-incident-email-2025_07_16_1100",
                "lcq_inc_email_2025_07_16_1100"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_72",
        "instruction": "You need to handle a network degradation according to the incident-management policy having one incident of record with deterministic anchors. Utilize: incident id=ITSD-1014 (summary=network_degradation_t5028, priority=P2), lifecycle id=lcq_inc_0002 (actor=incident_mgr, memo_id=memo_inc_0002, employee_ref=global_incident_network), backlog snapshot snap_2025_07_16_1107 over {On Hold, In Progress, New}, and health report run rpt_2025_07_16_1108 (window=30 days, output path s3://reports/ServiceDesk_Health_Report_2025-07-16_1108.pdf). Deterministic times: incident created_at=2025-07-16T11:05:00+00:00 and In Progress at 11:06:00; lifecycle created_at=2025-07-16T11:05:00+00:00 and blocked at 11:06:00; snapshot taken_at=2025-07-16T11:07:00+00:00; report started_at=11:08:00 and completed_at=11:08:30. Do not modify any service-desk ticket statuses. If the incident is absent, establish ITSD-1014 and set it to In Progress at 11:06:00.Use: incident id=ITSD-1014 (summary=network_degradation_t5028, priority=P2), lifecycle id=lcq_inc_0002 (actor=incident_mgr, memo_id=memo_inc_0002, employee_ref=global_incident_network), backlog snapshot snap_2025_07_16_1107 over {On Hold, In Progress, New}, and health report run rpt_2025_07_16_1108 (window=30 days, output path s3://reports/ServiceDesk_Health_Report_2025-07-16_1108.pdf).Deterministic times: incident created_at=2025-07-16T11:05:00+00:00 and In Progress at 11:06:00; lifecycle created_at=2025-07-16T11:05:00+00:00 and blocked at 11:06:00; snapshot taken_at=2025-07-16T11:07:00+00:00; report started_at=11:08:00 and completed_at=11:08:30. Do not alter any service-desk ticket statuses. If the incident is missing, create ITSD-1014 and set it to In Progress at 11:06:00.",
        "actions": [
            {
                "name": "FindJiraTickets",
                "arguments": {
                    "issue_type": "Incident",
                    "summary": "network_degradation_t5028",
                    "priority": "P2"
                },
            },
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1014",
                    "issue_type": "Incident",
                    "summary": "network_degradation_t5028",
                    "priority": "P2",
                    "status": "New",
                    "created_at": "2025-07-16T11:05:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1014",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:06:00+00:00"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0002",
                    "memo_id": "memo_inc_0002",
                    "employee_ref": "global_incident_network",
                    "event": "incident",
                    "status": "created",
                    "created_at": "2025-07-16T11:05:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0002",
                    "status": "blocked",
                    "timestamp": "2025-07-16T11:06:00+00:00",
                    "actor": "incident_mgr"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "On Hold"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "In Progress"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1107",
                    "taken_at": "2025-07-16T11:07:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1108",
                    "started_at": "2025-07-16T11:08:00+00:00",
                    "completed_at": "2025-07-16T11:08:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1108.pdf"
                }
            }
        ],
        "outputs": [
                "ITSD-1014",
                "lcq_inc_0002"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_73",
        "instruction": "Handle an MDM service disruption on 2025-07-16 in accordance with the incident-management policy. Utilize these deterministic values to maintain a single incident of record and ensure an auditable trail: incident id=ITSD-1015 with summary=mdm_service_disruption_t5013_t5053 and priority=P2 (created 2025-07-16T11:10:00+00:00, then In Progress 2025-07-16T11:11:00+00:00); lifecycle id=lcq_inc_0003 (created with event=incident and status=in_progress at 2025-07-16T11:10:00+00:00, then status=blocked at 2025-07-16T11:11:00+00:00 by actor incident_mgr, memo_id=memo_inc_0003, employee_ref=global_incident_mdm); snapshot id=snap_2025_07_16_1112 taken 2025-07-16T11:12:00+00:00 over {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1113 with started_at=2025-07-16T11:13:00+00:00, completed_at=2025-07-16T11:13:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1113.pdf. Apply the incident to impacted tickets T5013 and T5053 by placing them On Hold.Use these deterministic values for a single incident of record and an auditable trail: incident id=ITSD-1015 with summary=mdm_service_disruption_t5013_t5053 and priority=P2 (created 2025-07-16T11:10:00+00:00, then In Progress 2025-07-16T11:11:00+00:00); lifecycle id=lcq_inc_0003 (created with event=incident and status=in_progress at 2025-07-16T11:10:00+00:00, then status=blocked at 2025-07-16T11:11:00+00:00 by actor incident_mgr, memo_id=memo_inc_0003, employee_ref=global_incident_mdm); snapshot id=snap_2025_07_16_1112 taken 2025-07-16T11:12:00+00:00 over {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1113 with started_at=2025-07-16T11:13:00+00:00, completed_at=2025-07-16T11:13:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1113.pdf. Apply the incident to impacted tickets T5013 and T5053 by placing them On Hold.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1015",
                    "issue_type": "Incident",
                    "summary": "mdm_service_disruption_t5013_t5053",
                    "priority": "P2",
                    "status": "New",
                    "created_at": "2025-07-16T11:10:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1015",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:11:00+00:00"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0003",
                    "memo_id": "memo_inc_0003",
                    "employee_ref": "global_incident_mdm",
                    "event": "incident",
                    "status": "in_progress",
                    "created_at": "2025-07-16T11:10:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0003",
                    "status": "blocked",
                    "timestamp": "2025-07-16T11:11:00+00:00",
                    "actor": "incident_mgr"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1112",
                    "taken_at": "2025-07-16T11:12:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1113",
                    "started_at": "2025-07-16T11:13:00+00:00",
                    "completed_at": "2025-07-16T11:13:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1113.pdf"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5013",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5053",
                    "status": "On Hold"
                }
            }
        ],
        "outputs": [
                "ITSD-1015",
                "lcq_inc_0003"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_74",
        "instruction": "Handle an access provisioning outage on 2025-07-16 and adhere to the incident-management policy. Use deterministic values to ensure a single incident of record and an auditable trail: incident id=ITSD-1016 with summary=access_provisioning_outage_t5017_t5036 and priority=P1 (created 2025-07-16T11:15:00+00:00, then In Progress 2025-07-16T11:16:00+00:00); lifecycle id=lcq_inc_0004 (created with event=incident and status=created at 2025-07-16T11:15:00+00:00, then status=blocked at 2025-07-16T11:16:00+00:00 by actor incident_mgr, memo_id=memo_inc_0004, employee_ref=global_incident_access); snapshot id=snap_2025_07_16_1117 taken 2025-07-16T11:17:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1118 with started_at=2025-07-16T11:18:00+00:00, completed_at=2025-07-16T11:18:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1118.pdf. Apply the incident to tickets T5036 (Access Request) and T5017 (Account) by placing them On Hold.Use deterministic values to preserve a single incident of record and an auditable trail: incident id=ITSD-1016 with summary=access_provisioning_outage_t5017_t5036 and priority=P1 (created 2025-07-16T11:15:00+00:00, then In Progress 2025-07-16T11:16:00+00:00); lifecycle id=lcq_inc_0004 (created with event=incident and status=created at 2025-07-16T11:15:00+00:00, then status=blocked at 2025-07-16T11:16:00+00:00 by actor incident_mgr, memo_id=memo_inc_0004, employee_ref=global_incident_access); snapshot id=snap_2025_07_16_1117 taken 2025-07-16T11:17:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1118 with started_at=2025-07-16T11:18:00+00:00, completed_at=2025-07-16T11:18:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1118.pdf. Apply the incident to tickets T5036 (Access Request) and T5017 (Account) by placing them On Hold.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1016",
                    "issue_type": "Incident",
                    "summary": "access_provisioning_outage_t5017_t5036",
                    "priority": "P1",
                    "status": "New",
                    "created_at": "2025-07-16T11:15:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1016",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:16:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5017",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5036",
                    "status": "On Hold"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0004",
                    "memo_id": "memo_inc_0004",
                    "employee_ref": "global_incident_access",
                    "event": "incident",
                    "status": "created",
                    "created_at": "2025-07-16T11:15:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0004",
                    "status": "blocked",
                    "timestamp": "2025-07-16T11:16:00+00:00",
                    "actor": "incident_mgr"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1117",
                    "taken_at": "2025-07-16T11:17:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1118",
                    "started_at": "2025-07-16T11:18:00+00:00",
                    "completed_at": "2025-07-16T11:18:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1118.pdf"
                }
            }
        ],
        "outputs": [
                "ITSD-1016",
                "lcq_inc_0004"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_75",
        "instruction": "On 2025-07-16, handle a software distribution issue according to the incident-management policy. Utilize these deterministic values to maintain a single incident record and an auditable trail: incident id=ITSD-1017 with summary=software_distribution_issue_t5005_t5030 and priority=P2 (established 2025-07-16T11:20:00+00:00, then In Progress 2025-07-16T11:21:00+00:00); lifecycle id=lcq_inc_0005 (originated with event=incident and status=in_progress at 2025-07-16T11:20:00+00:00, subsequently status=blocked at 2025-07-16T11:21:00+00:00 by actor incident_mgr, memo_id=memo_inc_0005, employee_ref=global_incident_software); snapshot id=snap_2025_07_16_1122 captured 2025-07-16T11:22:00+00:00 with statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1123 with commenced_at=2025-07-16T11:23:00+00:00, finished_at=2025-07-16T11:23:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1123.pdf. Implement the incident on affected tickets T5005 and T5030 by setting them to On Hold.Use these deterministic values to keep a single incident of record and an auditable trail: incident id=ITSD-1017 with summary=software_distribution_issue_t5005_t5030 and priority=P2 (created 2025-07-16T11:20:00+00:00, then In Progress 2025-07-16T11:21:00+00:00); lifecycle id=lcq_inc_0005 (created with event=incident and status=in_progress at 2025-07-16T11:20:00+00:00, then status=blocked at 2025-07-16T11:21:00+00:00 by actor incident_mgr, memo_id=memo_inc_0005, employee_ref=global_incident_software); snapshot id=snap_2025_07_16_1122 taken 2025-07-16T11:22:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1123 with started_at=2025-07-16T11:23:00+00:00, completed_at=2025-07-16T11:23:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1123.pdf. Apply the incident to impacted tickets T5005 and T5030 by placing them On Hold.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1017",
                    "issue_type": "Incident",
                    "summary": "software_distribution_issue_t5005_t5030",
                    "priority": "P2",
                    "status": "New",
                    "created_at": "2025-07-16T11:20:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1017",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:21:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5005",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5030",
                    "status": "On Hold"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0005",
                    "memo_id": "memo_inc_0005",
                    "employee_ref": "global_incident_software",
                    "event": "incident",
                    "status": "in_progress",
                    "created_at": "2025-07-16T11:20:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0005",
                    "status": "blocked",
                    "timestamp": "2025-07-16T11:21:00+00:00",
                    "actor": "incident_mgr"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1122",
                    "taken_at": "2025-07-16T11:22:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1123",
                    "started_at": "2025-07-16T11:23:00+00:00",
                    "completed_at": "2025-07-16T11:23:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1123.pdf"
                }
            }
        ],
        "outputs": [
                "ITSD-1017",
                "lcq_inc_0005"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_76",
        "instruction": "On 2025-07-16, manage a directory synchronization incident in harmony with incident-management policy. Employ deterministic values: incident id=ITSD-1018 with summary=directory_sync_incident_t5009_t5010 and priority=P1 (instigated 2025-07-16T11:25:00+00:00, then In Progress 2025-07-16T11:26:00+00:00); lifecycle id=lcq_inc_0006 (started with event=incident and status=in_progress at 2025-07-16T11:25:00+00:00, then status=blocked at 2025-07-16T11:26:00+00:00 by actor incident_mgr, memo_id=memo_inc_0006, employee_ref=global_incident_directory); snapshot id=snap_2025_07_16_1127 recorded 2025-07-16T11:27:00+00:00 with statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1128 with initiated_at=2025-07-16T11:28:00+00:00, concluded_at=2025-07-16T11:28:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1128.pdf. Enforce the incident on tickets T5009 and T5010 by setting them to On Hold.Use deterministic values: incident id=ITSD-1018 with summary=directory_sync_incident_t5009_t5010 and priority=P1 (created 2025-07-16T11:25:00+00:00, then In Progress 2025-07-16T11:26:00+00:00); lifecycle id=lcq_inc_0006 (created with event=incident and status=in_progress at 2025-07-16T11:25:00+00:00, then status=blocked at 2025-07-16T11:26:00+00:00 by actor incident_mgr, memo_id=memo_inc_0006, employee_ref=global_incident_directory); snapshot id=snap_2025_07_16_1127 taken 2025-07-16T11:27:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1128 with started_at=2025-07-16T11:28:00+00:00, completed_at=2025-07-16T11:28:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1128.pdf. Apply the incident to tickets T5009 and T5010 by placing them On Hold.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1018",
                    "issue_type": "Incident",
                    "summary": "directory_sync_incident_t5009_t5010",
                    "priority": "P1",
                    "status": "New",
                    "created_at": "2025-07-16T11:25:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1018",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:26:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5009",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5010",
                    "status": "On Hold"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0006",
                    "memo_id": "memo_inc_0006",
                    "employee_ref": "global_incident_directory",
                    "event": "incident",
                    "status": "in_progress",
                    "created_at": "2025-07-16T11:25:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0006",
                    "status": "blocked",
                    "timestamp": "2025-07-16T11:26:00+00:00",
                    "actor": "incident_mgr"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1127",
                    "taken_at": "2025-07-16T11:27:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1128",
                    "started_at": "2025-07-16T11:28:00+00:00",
                    "completed_at": "2025-07-16T11:28:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1128.pdf"
                }
            }
        ],
        "outputs": [
                "ITSD-1018",
                "lcq_inc_0006"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_77",
        "instruction": "On 2025-07-16, make sure to manage a hardware vendor outage affecting device issues. Use deterministic values for maintaining a singular incident of record with an auditable trail: incident id=ITSD-1019 with summary=hardware_vendor_outage_t5037_t5048 and priority=P2 (created 2025-07-16T11:30:00+00:00, then In Progress 2025-07-16T11:31:00+00:00); lifecycle id=lcq_inc_0007 (created with event=incident and status=created at 2025-07-16T11:30:00+00:00, then status=blocked at 2025-07-16T11:31:00+00:00 by actor incident_mgr, memo_id=memo_inc_0007, employee_ref=global_incident_hardware); snapshot id=snap_2025_07_16_1132 taken 2025-07-16T11:32:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1133 with started_at=2025-07-16T11:33:00+00:00, completed_at=2025-07-16T11:33:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1133.pdf; apply the incident to tickets T5037 and T5048 by placing them On Hold.Use deterministic values to keep a single incident of record with an auditable trail: incident id=ITSD-1019 with summary=hardware_vendor_outage_t5037_t5048 and priority=P2 (created 2025-07-16T11:30:00+00:00, then In Progress 2025-07-16T11:31:00+00:00); lifecycle id=lcq_inc_0007 (created with event=incident and status=created at 2025-07-16T11:30:00+00:00, then status=blocked at 2025-07-16T11:31:00+00:00 by actor incident_mgr, memo_id=memo_inc_0007, employee_ref=global_incident_hardware); snapshot id=snap_2025_07_16_1132 taken 2025-07-16T11:32:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1133 with started_at=2025-07-16T11:33:00+00:00, completed_at=2025-07-16T11:33:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1133.pdf; apply the incident to tickets T5037 and T5048 by placing them On Hold.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1019",
                    "issue_type": "Incident",
                    "summary": "hardware_vendor_outage_t5037_t5048",
                    "priority": "P2",
                    "status": "New",
                    "created_at": "2025-07-16T11:30:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1019",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:31:00+00:00"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0007",
                    "memo_id": "memo_inc_0007",
                    "employee_ref": "global_incident_hardware",
                    "event": "incident",
                    "status": "created",
                    "created_at": "2025-07-16T11:30:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0007",
                    "status": "blocked",
                    "timestamp": "2025-07-16T11:31:00+00:00",
                    "actor": "incident_mgr"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1132",
                    "taken_at": "2025-07-16T11:32:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1133",
                    "started_at": "2025-07-16T11:33:00+00:00",
                    "completed_at": "2025-07-16T11:33:00+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1133.pdf"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5037",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5048",
                    "status": "On Hold"
                }
            }
        ],
        "outputs": [
                "ITSD-1019",
                "lcq_inc_0007"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_78",
        "instruction": "On 2025-07-16, you are responsible for managing a license provisioning disruption in accordance with the incident-management policy. Keep a single auditable record based on these deterministic facts (no tool specifics implied): incident id=ITSD-1020, summary=license_provisioning_incident_t5014_t5012, priority=P1; its creation is noted at 2025-07-16T11:35:00+00:00 and progression logged at 2025-07-16T11:36:00+00:00. Lifecycle id=lcq_inc_0008 is connected to memo_id=memo_inc_0008 and employee_ref=global_incident_licenses, maintaining in-progress control and a subsequent blocked status at the same respective times. Backlog monitoring uses a snapshot identifier snap_2025_07_16_1137 at 2025-07-16T11:37:00+00:00 scoped to {On Hold, In Progress, New}, and health reporting uses run_id=rpt_2025_07_16_1138 (window=30 days, output path s3://reports/ServiceDesk_Health_Report_2025-07-16_1138.pdf) at 11:38:00\u201311:38:30. Ensure incident controls are applied to affected records represented by tickets T5014 and T5012 consistent with policy.Maintain a single auditable record anchored by these deterministic facts (no tool specifics implied): incident id=ITSD-1020, summary=license_provisioning_incident_t5014_t5012, priority=P1; its creation is recorded at 2025-07-16T11:35:00+00:00 and progression captured at 2025-07-16T11:36:00+00:00. Lifecycle id=lcq_inc_0008 is attributed to memo_id=memo_inc_0008 and employee_ref=global_incident_licenses, with in-progress control and a subsequent blocked posture at the same respective times. Backlog monitoring references a snapshot identifier snap_2025_07_16_1137 at 2025-07-16T11:37:00+00:00 scoped to {On Hold, In Progress, New}, and health reporting references run_id=rpt_2025_07_16_1138 (window=30 days, output path s3://reports/ServiceDesk_Health_Report_2025-07-16_1138.pdf) at 11:38:00\u201311:38:30. You must ensure incident controls are applied to the impacted records represented by tickets T5014 and T5012 consistent with policy.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1020",
                    "issue_type": "Incident",
                    "summary": "license_provisioning_incident_t5014_t5012",
                    "priority": "P1",
                    "status": "New",
                    "created_at": "2025-07-16T11:35:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1020",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:36:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5014",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5012",
                    "status": "On Hold"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0008",
                    "memo_id": "memo_inc_0008",
                    "employee_ref": "global_incident_licenses",
                    "event": "incident",
                    "status": "in_progress",
                    "created_at": "2025-07-16T11:35:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0008",
                    "status": "blocked",
                    "timestamp": "2025-07-16T11:36:00+00:00",
                    "actor": "incident_policy"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1137",
                    "taken_at": "2025-07-16T11:37:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1138",
                    "started_at": "2025-07-16T11:38:00+00:00",
                    "completed_at": "2025-07-16T11:38:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1138.pdf"
                }
            }
        ],
        "outputs": [
                "ITSD-1020",
                "lcq_inc_0008"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_79",
        "instruction": "On 2025-07-16, you are required to handle an account access-control incident in accordance with incident-management policy. Use deterministic values to maintain a solitary incident of record with an auditable trail: incident id=ITSD-1021 with summary=account_access_incident_t5043_t5026 and priority=P2 (established on 2025-07-16T11:40:00+00:00, then transitioned to In Progress at 2025-07-16T11:41:00+00:00); lifecycle id=lcq_inc_0009 (initiated with the event=incident and status=in_progress at 2025-07-16T11:40:00+00:00, then moved to status=blocked at 2025-07-16T11:41:00+00:00 by actor incident_mgr, memo_id=memo_inc_0009, employee_ref=global_incident_account); snapshot id=snap_2025_07_16_1142 captured at 2025-07-16T11:42:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1143 which commenced at 2025-07-16T11:43:00+00:00 and concluded at 2025-07-16T11:43:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1143.pdf. The incident should be applied to tickets T5043 and T5026 by placing them On Hold.Use deterministic values to keep a single incident of record with an auditable trail: incident id=ITSD-1021 with summary=account_access_incident_t5043_t5026 and priority=P2 (created 2025-07-16T11:40:00+00:00, then In Progress 2025-07-16T11:41:00+00:00); lifecycle id=lcq_inc_0009 (created with event=incident and status=in_progress at 2025-07-16T11:40:00+00:00, then status=blocked at 2025-07-16T11:41:00+00:00 by actor incident_mgr, memo_id=memo_inc_0009, employee_ref=global_incident_account); snapshot id=snap_2025_07_16_1142 taken 2025-07-16T11:42:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1143 with started_at=2025-07-16T11:43:00+00:00, completed_at=2025-07-16T11:43:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1143.pdf. Apply the incident to tickets T5043 and T5026 by placing them On Hold.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1021",
                    "issue_type": "Incident",
                    "summary": "account_access_incident_t5043_t5026",
                    "priority": "P2",
                    "status": "New",
                    "created_at": "2025-07-16T11:40:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1021",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:41:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5043",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5026",
                    "status": "On Hold"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0009",
                    "memo_id": "memo_inc_0009",
                    "employee_ref": "global_incident_account",
                    "event": "incident",
                    "status": "in_progress",
                    "created_at": "2025-07-16T11:40:00+00:00"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0009",
                    "memo_id": "memo_inc_0009",
                    "employee_ref": "global_incident_account",
                    "event": "incident",
                    "status": "blocked",
                    "created_at": "2025-07-16T11:41:00+00:00"
                },
            },
            {
                "name": "RecordLifecycleAudit",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0009",
                    "event": "blocked",
                    "timestamp": "2025-07-16T11:41:00+00:00",
                    "actor": "incident_mgr"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "On Hold"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "In Progress"
                },
            },
            {
                "name": "FindTickets",
                "arguments": {
                    "status": "New"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1142",
                    "taken_at": "2025-07-16T11:42:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1143",
                    "started_at": "2025-07-16T11:43:00+00:00",
                    "completed_at": "2025-07-16T11:43:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1143.pdf"
                }
            }
        ],
        "outputs": [
                "ITSD-1021",
                "lcq_inc_0009"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_80",
        "instruction": "On 2025-07-16, you are needed to manage a general authentication timeout incident consistent with incident-management policy. Use deterministic values to uphold a single incident of record and an auditable trail: incident id=ITSD-1022 with summary=general_auth_timeouts_t5050_t5060 and priority=P2 (created on 2025-07-16T11:45:00+00:00, subsequently In Progress at 2025-07-16T11:46:00+00:00); lifecycle id=lcq_inc_0010 with memo_id=memo_inc_0010 and employee_ref=global_incident_general (formulated with event=incident and status=created at 2025-07-16T11:45:00+00:00, changed to in_progress at 2025-07-16T11:46:00+00:00 by actor incident_mgr, and completed at 2025-07-16T11:48:30+00:00 by actor incident_mgr); snapshot id=snap_2025_07_16_1147 taken at 2025-07-16T11:47:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1148 initiated at 2025-07-16T11:48:00+00:00 and finalized at 2025-07-16T11:48:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1148.pdf. The incident must be implemented to tickets T5050 and T5060 by placing them On Hold.Use deterministic values to keep a single incident of record and an auditable trail: incident id=ITSD-1022 with summary=general_auth_timeouts_t5050_t5060 and priority=P2 (created 2025-07-16T11:45:00+00:00, then In Progress 2025-07-16T11:46:00+00:00); lifecycle id=lcq_inc_0010 with memo_id=memo_inc_0010 and employee_ref=global_incident_general (created with event=incident and status=created at 2025-07-16T11:45:00+00:00, set to in_progress at 2025-07-16T11:46:00+00:00 by actor incident_mgr, and completed at 2025-07-16T11:48:30+00:00 by actor incident_mgr); snapshot id=snap_2025_07_16_1147 taken 2025-07-16T11:47:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1148 with started_at=2025-07-16T11:48:00+00:00, completed_at=2025-07-16T11:48:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1148.pdf. Apply the incident to tickets T5050 and T5060 by placing them On Hold.",
        "actions": [
            {
                "name": "CreateJiraTicket",
                "arguments": {
                    "jira_id": "ITSD-1022",
                    "issue_type": "Incident",
                    "summary": "general_auth_timeouts_t5050_t5060",
                    "priority": "P2",
                    "status": "New",
                    "created_at": "2025-07-16T11:45:00+00:00"
                },
            },
            {
                "name": "UpdateJiraStatus",
                "arguments": {
                    "jira_id": "ITSD-1022",
                    "status": "In Progress",
                    "updated_at": "2025-07-16T11:46:00+00:00"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5050",
                    "status": "On Hold"
                },
            },
            {
                "name": "UpdateTicketStatus",
                "arguments": {
                    "ticket_id": "T5060",
                    "status": "On Hold"
                },
            },
            {
                "name": "EnqueueLifecycleEvent",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0010",
                    "memo_id": "memo_inc_0010",
                    "employee_ref": "global_incident_general",
                    "event": "incident",
                    "status": "created",
                    "created_at": "2025-07-16T11:45:00+00:00"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0010",
                    "status": "in_progress",
                    "timestamp": "2025-07-16T11:46:00+00:00",
                    "actor": "incident_mgr"
                },
            },
            {
                "name": "TakeBacklogSnapshot",
                "arguments": {
                    "snapshot_id": "snap_2025_07_16_1147",
                    "taken_at": "2025-07-16T11:47:00+00:00",
                    "statuses_in_scope": [
                        "On Hold",
                        "In Progress",
                        "New"
                    ]
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1148",
                    "started_at": "2025-07-16T11:48:00+00:00",
                    "completed_at": "2025-07-16T11:48:30+00:00",
                    "source_ticket_window_days": 30,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1148.pdf"
                },
            },
            {
                "name": "UpdateLifecycleStatus",
                "arguments": {
                    "lifecycle_id": "lcq_inc_0010",
                    "status": "completed",
                    "timestamp": "2025-07-16T11:48:30+00:00",
                    "actor": "incident_mgr"
                }
            }
        ],
        "outputs": [
                "ITSD-1022",
                "lcq_inc_0010"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_81",
        "instruction": "On 2025-07-16, you are required to manage finance mailbox archiving according to the data-retention policy. Finance necessitates finance_7y archival while maintaining active mail services. Utilize deterministic values: for emp_0017, set archive_id=arch_2025_07_16_emp_0017 with mailbox_id=mbx_82aecf, archive_path=s3://corp-archives/mail/emp_0017/2025-07-16, created_at=2025-07-16T12:00:00+00:00; for emp_0029, apply archive_id=arch_2025_07_16_emp_0029 with mailbox_id=mbx_48efe8, archive_path=s3://corp-archives/mail/emp_0029/2025-07-16, created_at=2025-07-16T12:02:00+00:00. Check each mailbox and existing licenses before proceeding with archive creation.Finance requires finance_7y archival while preserving active mail service. Use deterministic values: for emp_0017 archive_id=arch_2025_07_16_emp_0017 with mailbox_id=mbx_82aecf, archive_path=s3://corp-archives/mail/emp_0017/2025-07-16, created_at=2025-07-16T12:00:00+00:00; for emp_0029 archive_id=arch_2025_07_16_emp_0029 with mailbox_id=mbx_48efe8, archive_path=s3://corp-archives/mail/emp_0029/2025-07-16, created_at=2025-07-16T12:02:00+00:00. Verify each mailbox and current licenses before writing archives.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0017",
                    "mailbox_id": "mbx_82aecf",
                    "employee_id": "emp_0017",
                    "archive_path": "s3://corp-archives/mail/emp_0017/2025-07-16",
                    "retention_policy": "finance_7y",
                    "created_at": "2025-07-16T12:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0029",
                    "mailbox_id": "mbx_48efe8",
                    "employee_id": "emp_0029",
                    "archive_path": "s3://corp-archives/mail/emp_0029/2025-07-16",
                    "retention_policy": "finance_7y",
                    "created_at": "2025-07-16T12:02:00+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0017",
                "arch_2025_07_16_emp_0029"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_82",
        "instruction": "On 2025-07-16, you should handle HR quarterly mailbox archiving in compliance with the data-retention policy. For HR, implement std_2y archives while ensuring mailboxes remain active. Employ deterministic values: for emp_0001, use archive_id=arch_2025_07_16_emp_0001 with mailbox_id=mbx_dc71c8, archive_path=s3://corp-archives/mail/emp_0001/2025-07-16, created_at=2025-07-16T12:04:00+00:00; for emp_0008, utilize archive_id=arch_2025_07_16_emp_0008 with mailbox_id=mbx_8abc91, archive_path=s3://corp-archives/mail/emp_0008/2025-07-16, created_at=2025-07-16T12:06:00+00:00. Validate mailbox details and current licenses before archiving. For audit purposes, log validation entries vld_arch_emp_0001_2025_07_16_120430 and vld_arch_emp_0008_2025_07_16_120630 at 12:04:30 and 12:06:30 respectively, linking each archive back to its corresponding mailbox and retention rule.For HR, apply std_2y archives while keeping mailboxes active. Use deterministic values: for emp_0001 use archive_id=arch_2025_07_16_emp_0001 with mailbox_id=mbx_dc71c8, archive_path=s3://corp-archives/mail/emp_0001/2025-07-16, created_at=2025-07-16T12:04:00+00:00; for emp_0008 use archive_id=arch_2025_07_16_emp_0008 with mailbox_id=mbx_8abc91, archive_path=s3://corp-archives/mail/emp_0008/2025-07-16, created_at=2025-07-16T12:06:00+00:00. Verify mailbox details and current licenses prior to archival.For auditability, record validation entries vld_arch_emp_0001_2025_07_16_120430 and vld_arch_emp_0008_2025_07_16_120630 at 12:04:30 and 12:06:30 respectively, linking each archive to its mailbox and retention rule.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0001",
                    "mailbox_id": "mbx_dc71c8",
                    "employee_id": "emp_0001",
                    "archive_path": "s3://corp-archives/mail/emp_0001/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:04:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_arch_emp_0001_2025_07_16_120430",
                    "entity": "data_archives",
                    "entity_id": "arch_2025_07_16_emp_0001",
                    "field": "retention_policy",
                    "rule": "archive_recorded",
                    "details": "mailbox=mbx_dc71c8;policy=std_2y",
                    "created_at": "2025-07-16T12:04:30+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0008",
                    "mailbox_id": "mbx_8abc91",
                    "employee_id": "emp_0008",
                    "archive_path": "s3://corp-archives/mail/emp_0008/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:06:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_arch_emp_0008_2025_07_16_120630",
                    "entity": "data_archives",
                    "entity_id": "arch_2025_07_16_emp_0008",
                    "field": "retention_policy",
                    "rule": "archive_recorded",
                    "details": "mailbox=mbx_8abc91;policy=std_2y",
                    "created_at": "2025-07-16T12:06:30+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0001",
                "arch_2025_07_16_emp_0008",
                "vld_arch_emp_0001_2025_07_16_120430",
                "vld_arch_emp_0008_2025_07_16_120630"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_83",
        "instruction": "On 2025-07-16, handle the archiving of mailboxes for employees currently on leave according to the retention policy. Implement std_2y archives and maintain the current mail status: for emp_0019, utilize archive_id=arch_2025_07_16_emp_0019 with mailbox_id=mbx_1d0980, path=s3://corp-archives/mail/emp_0019/2025-07-16, created_at=2025-07-16T12:08:00+00:00; for emp_0032, utilize archive_id=arch_2025_07_16_emp_0032 with mailbox_id=mbx_f06213, path=s3://corp-archives/mail/emp_0032/2025-07-16, created_at=2025-07-16T12:10:00+00:00. Confirm that mailboxes and licenses are valid before proceeding with the archival.Apply std_2y archives and leave mail status unchanged: for emp_0019 use archive_id=arch_2025_07_16_emp_0019 with mailbox_id=mbx_1d0980, path=s3://corp-archives/mail/emp_0019/2025-07-16, created_at=2025-07-16T12:08:00+00:00; for emp_0032 use archive_id=arch_2025_07_16_emp_0032 with mailbox_id=mbx_f06213, path=s3://corp-archives/mail/emp_0032/2025-07-16, created_at=2025-07-16T12:10:00+00:00. Validate mailbox and licenses prior to archival.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0019",
                    "mailbox_id": "mbx_1d0980",
                    "employee_id": "emp_0019",
                    "archive_path": "s3://corp-archives/mail/emp_0019/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:08:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0032",
                    "mailbox_id": "mbx_f06213",
                    "employee_id": "emp_0032",
                    "archive_path": "s3://corp-archives/mail/emp_0032/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:10:00+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0019",
                "arch_2025_07_16_emp_0032"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_84",
        "instruction": "On 2025-07-16, coordinate the archiving of engineering mailboxes in line with the data-retention policy. The engineering department follows the std_2y rule while leaving the service active. Base your actions on verified facts without suggesting specific tools: emp_0009 \u2192 archive_id=arch_2025_07_16_emp_0009 (mailbox mbx_9e0388) with path s3://corp-archives/mail/emp_0009/2025-07-16 at 2025-07-16T12:12:00+00:00; emp_0030 \u2192 archive_id=arch_2025_07_16_emp_0030 (mailbox mbx_db017d) with path s3://corp-archives/mail/emp_0030/2025-07-16 at 2025-07-16T12:14:00+00:00. Validate directory identity, mailbox details, current license entitlements, and app accounts before performing the archival, followed by the application of std_2y.Engineering applies the std_2y rule while keeping service active. Anchor to deterministic facts without prescribing tools: emp_0009 \u2192 archive_id=arch_2025_07_16_emp_0009 (mailbox mbx_9e0388) with path s3://corp-archives/mail/emp_0009/2025-07-16 at 2025-07-16T12:12:00+00:00; emp_0030 \u2192 archive_id=arch_2025_07_16_emp_0030 (mailbox mbx_db017d) with path s3://corp-archives/mail/emp_0030/2025-07-16 at 2025-07-16T12:14:00+00:00. You must validate directory identity, mailbox details, current license entitlements, and app accounts before archival, then apply std_2y.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0009"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0009"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0009"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0009"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0009"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0009",
                    "mailbox_id": "mbx_9e0388",
                    "employee_id": "emp_0009",
                    "archive_path": "s3://corp-archives/mail/emp_0009/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:12:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0030"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0030",
                    "mailbox_id": "mbx_db017d",
                    "employee_id": "emp_0030",
                    "archive_path": "s3://corp-archives/mail/emp_0030/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:14:00+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0009",
                "arch_2025_07_16_emp_0030"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_85",
        "instruction": "On 2025-07-16, handle the mailbox archiving for support managers according to the data-retention policy. Support adheres to the standard retention rule (std_2y) while services remain active. Base your tasks on deterministic facts without specifying tools: emp_0011 uses archive_id=arch_2025_07_16_emp_0011 (mailbox mbx_51e138) with path s3://corp-archives/mail/emp_0011/2025-07-16 and created_at=2025-07-16T12:16:00+00:00; emp_0038 uses archive_id=arch_2025_07_16_emp_0038 (mailbox mbx_839501) with path s3://corp-archives/mail/emp_0038/2025-07-16 and created_at=2025-07-16T12:18:00+00:00. Validate mailbox details and current entitlements prior to archival, and apply the std_2y policy.Support uses the standard retention rule (std_2y) while maintaining active service. Anchor the work to deterministic facts without prescribing tools: emp_0011 uses archive_id=arch_2025_07_16_emp_0011 (mailbox mbx_51e138) with path s3://corp-archives/mail/emp_0011/2025-07-16 and created_at=2025-07-16T12:16:00+00:00; emp_0038 uses archive_id=arch_2025_07_16_emp_0038 (mailbox mbx_839501) with path s3://corp-archives/mail/emp_0038/2025-07-16 and created_at=2025-07-16T12:18:00+00:00. You must validate mailbox details and current entitlements before performing archival, and apply the std_2y policy.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0011",
                    "mailbox_id": "mbx_51e138",
                    "employee_id": "emp_0011",
                    "archive_path": "s3://corp-archives/mail/emp_0011/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:16:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0038",
                    "mailbox_id": "mbx_839501",
                    "employee_id": "emp_0038",
                    "archive_path": "s3://corp-archives/mail/emp_0038/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:18:00+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0011",
                "arch_2025_07_16_emp_0038"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_86",
        "instruction": "On 2025-07-16, oversee the mailbox archiving for marketing leadership under the data-retention policy. Marketing leadership follows the std_2y rule while maintaining service. Rely on deterministic facts, avoiding the prescription of specific tools: emp_0012 \u2192 archive_id=arch_2025_07_16_emp_0012 (mailbox mbx_f63934) with path s3://corp-archives/mail/emp_0012/2025-07-16 at 2025-07-16T12:20:00+00:00; emp_0041 \u2192 archive_id=arch_2025_07_16_emp_0041 (mailbox mbx_6f9008) with path s3://corp-archives/mail/emp_0041/2025-07-16 at 2025-07-16T12:22:00+00:00. Confirm directory identity, mailbox details, current license entitlements, and app accounts before archival, then apply std_2y.Marketing leadership applies the std_2y rule while keeping service active. Anchor to deterministic facts without prescribing tools: emp_0012 \u2192 archive_id=arch_2025_07_16_emp_0012 (mailbox mbx_f63934) with path s3://corp-archives/mail/emp_0012/2025-07-16 at 2025-07-16T12:20:00+00:00; emp_0041 \u2192 archive_id=arch_2025_07_16_emp_0041 (mailbox mbx_6f9008) with path s3://corp-archives/mail/emp_0041/2025-07-16 at 2025-07-16T12:22:00+00:00.You must validate directory identity, mailbox details, current license entitlements, and app accounts before archival, then apply std_2y.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0012",
                    "mailbox_id": "mbx_f63934",
                    "employee_id": "emp_0012",
                    "archive_path": "s3://corp-archives/mail/emp_0012/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:20:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0041"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0041"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0041"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0041"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0041"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0041",
                    "mailbox_id": "mbx_6f9008",
                    "employee_id": "emp_0041",
                    "archive_path": "s3://corp-archives/mail/emp_0041/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:22:00+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0012",
                "arch_2025_07_16_emp_0041"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_87",
        "instruction": "On 2025-07-16, oversee the mailbox archiving for IT service staff in line with the data-retention policy. For IT, the standard retention rule (std_2y) is applied without altering mailbox status. Ground the policy application on deterministic facts: emp_0023 \u2192 archive_id=arch_2025_07_16_emp_0023 (mailbox mbx_696506) with path s3://corp-archives/mail/emp_0023/2025-07-16 at 2025-07-16T12:24:00+00:00; emp_0004 \u2192 archive_id=arch_2025_07_16_emp_0004 (mailbox mbx_38d007) with path s3://corp-archives/mail/emp_0004/2025-07-16 at 2025-07-16T12:26:00+00:00. Confirm the directory identity, mailbox specifications, current entitlements, and app accounts prior to executing archival, utilizing std_2y.IT uses the standard retention rule (std_2y) without changing mailbox status. Anchor to deterministic facts while applying policy: emp_0023 \u2192 archive_id=arch_2025_07_16_emp_0023 (mailbox mbx_696506) with path s3://corp-archives/mail/emp_0023/2025-07-16 at 2025-07-16T12:24:00+00:00; emp_0004 \u2192 archive_id=arch_2025_07_16_emp_0004 (mailbox mbx_38d007) with path s3://corp-archives/mail/emp_0004/2025-07-16 at 2025-07-16T12:26:00+00:00. You must validate directory identity, mailbox details, current entitlements, and app accounts before performing archival, applying std_2y.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0023"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0023"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0023"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0023"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0023"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0023",
                    "mailbox_id": "mbx_696506",
                    "employee_id": "emp_0023",
                    "archive_path": "s3://corp-archives/mail/emp_0023/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:24:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0004",
                    "mailbox_id": "mbx_38d007",
                    "employee_id": "emp_0004",
                    "archive_path": "s3://corp-archives/mail/emp_0004/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:26:00+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0023",
                "arch_2025_07_16_emp_0004"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_88",
        "instruction": "On 2025-07-16, carry out a Sales mailbox archiving session under the retention policy while maintaining active service. Implement std_2y for relevant Sales managers and check identity and license status before writing. Generate identifiers deterministically based on the date and employee_id (archive_id=arch_YYYY_MM_DD_emp_{employee_id}; archive_path=s3://corp-archives/mail/{employee_id}/YYYY-MM-DD), grounded to 12:28 and 12:30 UTC for emp_0013 and emp_0028 respectively. For audit purposes, document validation entries that link each archive to its mailbox and policy, 30 seconds after each created_at timestamp.Apply std_2y for in-scope Sales managers and validate identity and license posture before writing.Derive identifiers deterministically from the date and employee_id (archive_id=arch_YYYY_MM_DD_emp_{employee_id}; archive_path=s3://corp-archives/mail/{employee_id}/YYYY-MM-DD), anchored to 12:28 and 12:30 UTC for emp_0013 and emp_0028 respectively.For auditability, record validation entries linking each archive to its mailbox and policy at +30s after each created_at.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0013",
                    "mailbox_id": "mbx_78fb5c",
                    "employee_id": "emp_0013",
                    "archive_path": "s3://corp-archives/mail/emp_0013/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:28:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_arch_emp_0013_2025_07_16_122830",
                    "entity": "data_archives",
                    "entity_id": "arch_2025_07_16_emp_0013",
                    "field": "retention_policy",
                    "rule": "archive_recorded",
                    "details": "mailbox=mbx_78fb5c;policy=std_2y",
                    "created_at": "2025-07-16T12:28:30+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0028",
                    "mailbox_id": "mbx_81d8d5",
                    "employee_id": "emp_0028",
                    "archive_path": "s3://corp-archives/mail/emp_0028/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:30:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_arch_emp_0028_2025_07_16_123030",
                    "entity": "data_archives",
                    "entity_id": "arch_2025_07_16_emp_0028",
                    "field": "retention_policy",
                    "rule": "archive_recorded",
                    "details": "mailbox=mbx_81d8d5;policy=std_2y",
                    "created_at": "2025-07-16T12:30:30+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0013",
                "arch_2025_07_16_emp_0028",
                "vld_arch_emp_0013_2025_07_16_122830",
                "vld_arch_emp_0028_2025_07_16_123030"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_89",
        "instruction": "On 2025-07-16, manage the operations leadership mailbox archiving in accordance with the data-retention policy. Operations employs the standard retention rule (std_2y) while keeping the mail service active. Base your actions on deterministic facts without dictating tool operations: emp_0035 \u2192 archive_id=arch_2025_07_16_emp_0035 (mailbox mbx_d89d5c) with path s3://corp-archives/mail/emp_0035/2025-07-16 at 2025-07-16T12:32:00+00:00; emp_0042 \u2192 archive_id=arch_2025_07_16_emp_0042 (mailbox mbx_f76658) with path s3://corp-archives/mail/emp_0042/2025-07-16 at 2025-07-16T12:34:00+00:00. Verify directory identity, mailbox details, current license entitlements, and app accounts prior to the archival process, and proceed to apply std_2y.Operations applies the standard retention rule (std_2y) while maintaining active mail service. Anchor to deterministic facts without prescribing tool operations: emp_0035 \u2192 archive_id=arch_2025_07_16_emp_0035 (mailbox mbx_d89d5c) with path s3://corp-archives/mail/emp_0035/2025-07-16 at 2025-07-16T12:32:00+00:00; emp_0042 \u2192 archive_id=arch_2025_07_16_emp_0042 (mailbox mbx_f76658) with path s3://corp-archives/mail/emp_0042/2025-07-16 at 2025-07-16T12:34:00+00:00. You must validate directory identity, mailbox details, current license entitlements, and app accounts before performing archival, and then apply std_2y.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0035",
                    "mailbox_id": "mbx_d89d5c",
                    "employee_id": "emp_0035",
                    "archive_path": "s3://corp-archives/mail/emp_0035/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:32:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0042"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0042"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0042"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0042"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0042"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0042",
                    "mailbox_id": "mbx_f76658",
                    "employee_id": "emp_0042",
                    "archive_path": "s3://corp-archives/mail/emp_0042/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:34:00+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0035",
                "arch_2025_07_16_emp_0042"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_90",
        "instruction": "On 2025-07-16, you have to initiate a general data-retention sweep across various departments to ensure policy-compliant archives. Apply std_2y for emp_0040 (Engineering) and emp_0020 (HR). Deterministic parameters: emp_0040 archive_id=arch_2025_07_16_emp_0040 (mbx_54337a) path=s3://corp-archives/mail/emp_0040/2025-07-16 created_at=2025-07-16T12:36:00+00:00; emp_0020 archive_id=arch_2025_07_16_emp_0020 (mbx_401a71) path=s3://corp-archives/mail/emp_0020/2025-07-16 created_at=2025-07-16T12:38:00+00:00. Ensure confirmation of mailbox and licenses before executing the archiving. For audit purposes, make sure to record validation entries that associate each archive with its mailbox and policy at +30s after each created_at.Apply std_2y for emp_0040 (Engineering) and emp_0020 (HR). Deterministic parameters: emp_0040 archive_id=arch_2025_07_16_emp_0040 (mbx_54337a) path=s3://corp-archives/mail/emp_0040/2025-07-16 created_at=2025-07-16T12:36:00+00:00; emp_0020 archive_id=arch_2025_07_16_emp_0020 (mbx_401a71) path=s3://corp-archives/mail/emp_0020/2025-07-16 created_at=2025-07-16T12:38:00+00:00. Confirm mailbox and licenses before writing archives.For auditability, record validation entries linking each archive to its mailbox and policy at +30s after each created_at.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0040",
                    "mailbox_id": "mbx_54337a",
                    "employee_id": "emp_0040",
                    "archive_path": "s3://corp-archives/mail/emp_0040/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:36:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_arch_emp_0040_2025_07_16_123630",
                    "entity": "data_archives",
                    "entity_id": "arch_2025_07_16_emp_0040",
                    "field": "retention_policy",
                    "rule": "archive_recorded",
                    "details": "mailbox=mbx_54337a;policy=std_2y",
                    "created_at": "2025-07-16T12:36:30+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetMailbox",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "ArchiveMailbox",
                "arguments": {
                    "archive_id": "arch_2025_07_16_emp_0020",
                    "mailbox_id": "mbx_401a71",
                    "employee_id": "emp_0020",
                    "archive_path": "s3://corp-archives/mail/emp_0020/2025-07-16",
                    "retention_policy": "std_2y",
                    "created_at": "2025-07-16T12:38:00+00:00"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "vld_arch_emp_0020_2025_07_16_123830",
                    "entity": "data_archives",
                    "entity_id": "arch_2025_07_16_emp_0020",
                    "field": "retention_policy",
                    "rule": "archive_recorded",
                    "details": "mailbox=mbx_401a71;policy=std_2y",
                    "created_at": "2025-07-16T12:38:30+00:00"
                }
            }
        ],
        "outputs": [
                "arch_2025_07_16_emp_0040",
                "arch_2025_07_16_emp_0020",
                "vld_arch_emp_0040_2025_07_16_123630",
                "vld_arch_emp_0020_2025_07_16_123830"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_91",
        "instruction": "By 2025-07-16, you are tasked with synchronizing Engineering app accounts to observed peer baselines without disrupting access. Utilize emp_0009 and emp_0036 as reference points to derive the Engineering baseline since they possess app_github, app_slack, app_confluence, app_jira. Verify directory identity against current app accounts, then supply only the lacking Engineering apps with deterministic identifiers: for emp_0037 (Software Engineer), include the absent TaskTrack account as appacc_2025_07_16_emp_0037_jira with created_at=2025-07-16T13:00:00+00:00; for emp_0040 (Software Engineer), add solely the missing WikiSpace account as appacc_2025_07_16_emp_0040_confluence with created_at=2025-07-16T13:04:00+00:00, without altering existing apps.Derive the Engineering baseline from existing Engineering peers: use emp_0009 and emp_0036 as anchors (they hold app_github, app_slack, app_confluence, app_jira).You must validate directory identity and current app accounts, then provision only missing Engineering apps with deterministic identifiers: for emp_0037 (Software Engineer) add the missing TaskTrack account only as appacc_2025_07_16_emp_0037_jira with created_at=2025-07-16T13:00:00+00:00; for emp_0040 (Software Engineer) add only the missing WikiSpace account as appacc_2025_07_16_emp_0040_confluence with created_at=2025-07-16T13:04:00+00:00, leaving existing apps unchanged.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0009"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0009"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0036"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0037"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0037"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0037"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0037",
                    "app_id": "app_jira"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_2025_07_16_emp_0037_jira",
                    "employee_id": "emp_0037",
                    "app_id": "app_jira",
                    "status": "active",
                    "created_at": "2025-07-16T13:00:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0040"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0040",
                    "app_id": "app_confluence"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_2025_07_16_emp_0040_confluence",
                    "employee_id": "emp_0040",
                    "app_id": "app_confluence",
                    "status": "active",
                    "created_at": "2025-07-16T13:04:00+00:00"
                }
            }
        ],
        "outputs": [
                "appacc_2025_07_16_emp_0037_jira",
                "appacc_2025_07_16_emp_0040_confluence"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_92",
        "instruction": "You are required to coordinate Sales app coverage for Sales Managers in line with policy while ensuring accounts remain active. Use peer Sales Manager emp_0028 to set the standard Sales manager app set including {app_salesforce, app_confluence, app_github}. Verify the identity, prevent duplicates, and adhere to baseline license capacity strictly for baseline licenses. For emp_0013, supply only the indispensable Sales apps from that set and maintain existing collaboration apps (Slack, TaskTrack) as is. Record determinate writes to 2025\u201107\u201116: allocate CloudCRM at 13:06:00Z, initiate the CodeHub app account at 13:06:30Z, and start the WikiSpace app account at 13:07:00Z.Use peer Sales Manager emp_0028 to anchor the expected Sales manager app set as {app_salesforce, app_confluence, app_github}. Confirm identity, avoid duplicates, and honor baseline license capacity only for baseline licenses. For emp_0013, provision only the missing Sales apps from that set and leave existing collaboration apps (Slack, TaskTrack) unchanged. Anchor writes deterministically to 2025\u201107\u201116: assign CloudCRM at 13:06:00Z, create the CodeHub app account at 13:06:30Z, and create the WikiSpace app account at 13:07:00Z.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0028"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0013",
                    "app_id": "app_salesforce"
                },
            },
            {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "needed_count": 1,
                    "jira_id": "JIRA-lic_salesforce-emp_0013-align",
                    "priority": "P3",
                    "created_at": "2025-07-16T13:06:00+00:00"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_emp_0013_lic_salesforce_2025_07_16",
                    "account_id": "acc_78fb5c",
                    "employee_id": "emp_0013",
                    "license_id": "lic_salesforce",
                    "assigned_at": "2025-07-16T13:06:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_emp_0013_salesforce_2025_07_16_1306",
                    "employee_id": "emp_0013",
                    "app_id": "app_salesforce",
                    "status": "active",
                    "created_at": "2025-07-16T13:06:00+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0013",
                    "app_id": "app_github"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_emp_0013_github_2025_07_16_130630",
                    "employee_id": "emp_0013",
                    "app_id": "app_github",
                    "status": "active",
                    "created_at": "2025-07-16T13:06:30+00:00"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0013",
                    "app_id": "app_confluence"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_emp_0013_confluence_2025_07_16_1307",
                    "employee_id": "emp_0013",
                    "app_id": "app_confluence",
                    "status": "active",
                    "created_at": "2025-07-16T13:07:00+00:00"
                }
            }
        ],
        "outputs": [
                "lca_emp_0013_lic_salesforce_2025_07_16",
                "appacc_emp_0013_salesforce_2025_07_16_1306",
                "appacc_emp_0013_github_2025_07_16_130630",
                "appacc_emp_0013_confluence_2025_07_16_1307"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_93",
        "instruction": "Handle ticketing coverage required by Support Managers. You need to align Support leadership's stance by implementing policy\u2014derive baseline RBAC groups from rbac_group_map (do not name them here), verify identity and baseline license posture/capacity, and include only what is missing. Use emp_0038 (Support Manager) as the peer anchor and reconcile emp_0011 while maintaining service active. Record writes to a fixed audit window on 2025-07-16: apply any necessary RBAC alignment at 13:08:05Z by actor rbac_alignment, and register TaskTrack only if it is missing at 13:08:00Z using deterministic identifiers (appacc_2025_07_16_emp_0011_jira, created_at=2025-07-16T13:08:00+00:00).Use emp_0038 (Support Manager) as the peer anchor and reconcile emp_0011 while keeping service active. Anchor writes to a fixed 2025-07-16 audit window: apply any necessary RBAC alignment at 13:08:05Z by actor rbac_alignment, and register TaskTrack only if it is absent at 13:08:00Z using deterministic identifiers (appacc_2025_07_16_emp_0011_jira, created_at=2025-07-16T13:08:00+00:00).",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0038"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Support",
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_51e138",
                    "group_ids": [
                        "grp_support_ada3",
                        "grp_support_all"
                    ],
                    "actor": "rbac_alignment",
                    "timestamp": "2025-07-16T13:08:05+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0011",
                    "app_id": "app_jira"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_2025_07_16_emp_0011_jira",
                    "employee_id": "emp_0011",
                    "app_id": "app_jira",
                    "status": "active",
                    "created_at": "2025-07-16T13:08:00+00:00"
                }
            }
        ],
        "outputs": [
                "appacc_2025_07_16_emp_0011_jira"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_94",
        "instruction": "Coordinate cross-functional collaboration for Marketing Content Strategists; it is necessary to align app coverage with peer usage for Sales-related tasks while preserving current access. Use peers like emp_0012, emp_0018, and emp_0021 who hold app_salesforce to establish the baseline. Validate RBAC baseline for Marketing/Content Strategist, confirm CloudCRM is included in the baseline license bundle, check current app set and license coverage, and ensure license capacity before documenting. For emp_0024 (Content Strategist), provision only the missing CloudCRM app account using deterministic identifiers\u2014appacc_2025_07_16_emp_0024_salesforce with created_at=2025-07-16T13:10:00+00:00\u2014while keeping existing licenses unchanged if lic_salesforce is already present.Use peers like emp_0012, emp_0018, and emp_0021 who hold app_salesforce to anchor the baseline. Validate RBAC baseline for Marketing/Content Strategist, confirm CloudCRM is part of the baseline license bundle, verify current app set and license coverage, and ensure license capacity before writing.For emp_0024 (Content Strategist), provision only the missing CloudCRM app account using deterministic identifiers\u2014appacc_2025_07_16_emp_0024_salesforce with created_at=2025-07-16T13:10:00+00:00\u2014while leaving existing licenses unchanged if lic_salesforce is already present.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0018"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0018"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_salesforce"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0024"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_2025_07_16_emp_0024_salesforce",
                    "employee_id": "emp_0024",
                    "app_id": "app_salesforce",
                    "status": "active",
                    "created_at": "2025-07-16T13:10:00+00:00"
                }
            }
        ],
        "outputs": [
                "appacc_2025_07_16_emp_0024_salesforce"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_95",
        "instruction": "In operations roles, collaborative efforts must happen in real time. Handle TeamChat reconciliation for Operations where TaskTrack/WikiSpace are already integrated. Utilize emp_0019 and emp_0035 as peer anchors (both possess TeamChat). Confirm the RBAC baseline for Operations/Ops Coordinator, ensure TeamChat is included in the baseline bundle, assess existing app set and license coverage, and verify capacity from the license inventory before proceeding. For emp_0010 (Ops Coordinator), only provision the TeamChat app account that is missing using deterministic identifiers: appacc_2025_07_16_emp_0010_slack with created_at=2025-07-16T13:12:00+00:00; keep existing licenses unchanged if lic_slack_ent is already assigned.Use emp_0019 and emp_0035 as peer anchors (both have TeamChat). Validate RBAC baseline for Operations/Ops Coordinator, verify TeamChat is in the baseline bundle, check existing app set and license coverage, and confirm capacity from license inventory before writing.For emp_0010 (Ops Coordinator), provision only the missing TeamChat app account with deterministic identifiers: appacc_2025_07_16_emp_0010_slack with created_at=2025-07-16T13:12:00+00:00; leave existing licenses unchanged if lic_slack_ent is already assigned.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0035"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Operations",
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0010",
                    "app_id": "app_slack"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_2025_07_16_emp_0010_slack",
                    "employee_id": "emp_0010",
                    "app_id": "app_slack",
                    "status": "active",
                    "created_at": "2025-07-16T13:12:00+00:00"
                }
            }
        ],
        "outputs": [
                "appacc_2025_07_16_emp_0010_slack"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_96",
        "instruction": "Finance leaders must engage in cross-team collaboration. Manage Finance app coverage by enforcing policy: establish the Accounting Manager baseline from rbac_group_map, verify identity and current app status, and only remediate missing elements while maintaining active services. Employ emp_0017 (Controller) solely as a peer reference for expected coverage (do not duplicate identifiers). Anchor any audit/write timestamps to the directory account created_at of the target (for emp_0029: 2023-05-01T09:00:00+00:00). If TeamChat, WikiSpace, and TaskTrack are already present for emp_0029, a single validation entry must be recorded linking the observed app_account_ids and no changes should be made.Use emp_0017 (Controller) only as a peer reference for expected coverage (do not copy identifiers). Anchor any audit/write timestamps to the target\u2019s directory account created_at (for emp_0029: 2023-05-01T09:00:00+00:00). If TeamChat, WikiSpace, and TaskTrack are already present for emp_0029, you must record a single validation entry linking the observed app_account_ids and make no changes.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0017"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Finance",
                    "job_title": "Accounting Manager"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0029"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0029",
                    "app_id": "app_slack"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0029",
                    "app_id": "app_confluence"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0029",
                    "app_id": "app_jira"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "val_2025_07_16_emp_0029_apps_present",
                    "entity": "employee",
                    "entity_id": "emp_0029",
                    "field": "app_accounts",
                    "rule": "no duplicate provisioning when target apps already present",
                    "details": "TeamChat, WikiSpace, and TaskTrack already active (appacc_9a342b, appacc_71843b, appacc_78c078); no upsert performed.",
                    "created_at": "2023-05-01T09:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "val_2025_07_16_emp_0029_apps_present"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_97",
        "instruction": "HR Recruiters work jointly with Engineering and Marketing; you must manage CodeHub coverage for emp_0020 under RBAC and licensing policy while maintaining uninterrupted access. Use peers emp_0001 and emp_0008 (both have CodeHub) to verify the expected coverage; validate identity and role, confirm capacity for lic_github_ent, prevent duplicates, and source any write timestamps from the CodeHub inventory audit time (2025-07-15T08:00:00+00:00). If CodeHub coverage is not present for emp_0020, you must provide it; otherwise, make no changes.Use peers emp_0001 and emp_0008 (both hold CodeHub) to confirm the expected coverage; validate identity and role, ensure capacity for lic_github_ent, avoid duplicates, and source any write timestamps from the CodeHub inventory audit time (2025-07-15T08:00:00+00:00).If CodeHub coverage is missing for emp_0020, you must provision it; otherwise make no change.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "HR",
                    "job_title": "Recruiter"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0020"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0020",
                    "app_id": "app_github"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "AssignLicense",
                "arguments": {
                    "assignment_id": "lca_2025_07_16_emp_0020_github",
                    "account_id": "acc_401a71",
                    "employee_id": "emp_0020",
                    "license_id": "lic_github_ent",
                    "assigned_at": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_2025_07_16_emp_0020_github",
                    "employee_id": "emp_0020",
                    "app_id": "app_github",
                    "status": "active",
                    "created_at": "2025-07-15T08:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "lca_2025_07_16_emp_0020_github",
                "appacc_2025_07_16_emp_0020_github"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_98",
        "instruction": "You need to align TeamChat coverage for Marketing Design Leads following policy guidelines, ensuring any valid access is retained. Assess anchors emp_0012, emp_0018, and emp_0034 against the Marketing/Design Lead baseline: base your decisions on RBAC mapping and license capacity, avoiding ad-hoc approaches. If an individual is not a Design Lead, document the role mismatch at the fixed 13:20Z anchor; do not provision. When the actual Design Lead\u2019s TeamChat and baseline groups are already met, record the state via an auditable, deterministic baseline write aligned to the TeamChat audit anchor (2025-07-15T08:00:00+00:00) rather than duplicating access. Utilize the standard service-desk reporting policy for documentation (13:21Z run anchors and a 14-day ticket window).Evaluate anchors emp_0012, emp_0018, and emp_0034 against the Marketing/Design Lead baseline: base decisions on RBAC mapping and license capacity, not ad\u2011hoc steps.When a person is not a Design Lead, document the role mismatch at the fixed 13:20Z anchor; do not provision. When the actual Design Lead\u2019s TeamChat and baseline groups are already satisfied, capture the state via an auditable, deterministic baseline write aligned to the TeamChat audit anchor (2025-07-15T08:00:00+00:00) rather than duplicating access.Use the standard service\u2011desk reporting policy for documentation (13:21Z run anchors and a 14\u2011day ticket window).",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0018"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0018"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "val_2025_07_16_emp_0018_not_design_lead",
                    "entity": "employee",
                    "entity_id": "emp_0018",
                    "field": "job_title",
                    "rule": "expected 'Design Lead' for anchor role check",
                    "details": "Anchor job_title='Content Strategist' not 'Design Lead'.",
                    "created_at": "2025-07-16T13:20:00+00:00"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "val_2025_07_16_emp_0034_not_design_lead",
                    "entity": "employee",
                    "entity_id": "emp_0034",
                    "field": "job_title",
                    "rule": "expected 'Design Lead' for anchor role check",
                    "details": "Anchor job_title='Content Strategist' not 'Design Lead'.",
                    "created_at": "2025-07-16T13:20:00+00:00"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_slack"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_f63934",
                    "group_ids": [
                        "grp_marketing_c05f",
                        "grp_marketing_all"
                    ],
                    "actor": "rbac_alignment",
                    "timestamp": "2025-07-15T08:00:00+00:00"
                },
            },
            {
                "name": "GenerateServiceDeskHealthReport",
                "arguments": {
                    "run_id": "rpt_2025_07_16_1321",
                    "started_at": "2025-07-16T13:21:00+00:00",
                    "completed_at": "2025-07-16T13:21:00+00:00",
                    "source_ticket_window_days": 14,
                    "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1321.pdf"
                }
            }
        ],
        "outputs": [
                "val_2025_07_16_emp_0018_not_design_lead",
                "val_2025_07_16_emp_0034_not_design_lead"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_99",
        "instruction": "Ensure the Marketing team collaborates using TeamChat. Align the app coverage of another Design Lead to match that of peers while maintaining access. Utilize peers emp_0012, emp_0018, and emp_0034 (who all possess TeamChat). Validate the RBAC baseline for Marketing/Design Lead, confirm TeamChat's coverage, and assess license capacity prior to any writing action. For emp_0021 (Design Lead), provide TeamChat only if it is absent; if TeamChat is already present, avoid creating a duplicate and instead log a deterministic validation entry val_2025_07_16_emp_0021_slack_present at 2025-07-16T13:22:05+00:00 to confirm baseline satisfaction.Use peers emp_0012, emp_0018, and emp_0034 (all hold TeamChat). Validate RBAC baseline for Marketing/Design Lead, verify TeamChat is in coverage, and check license capacity before any write. For emp_0021 (Design Lead), provision TeamChat only if missing; if TeamChat is already present, you must not create a duplicate and instead record a deterministic validation entry val_2025_07_16_emp_0021_slack_present at 2025-07-16T13:22:05+00:00 documenting baseline satisfaction.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0018"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0018"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "Marketing",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0021"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_slack"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "RecordValidationIssue",
                "arguments": {
                    "issue_id": "val_2025_07_16_emp_0021_slack_present",
                    "entity": "employee",
                    "entity_id": "emp_0021",
                    "field": "app_accounts",
                    "rule": "no duplicate provisioning when TeamChat already present",
                    "details": "TeamChat already active (appacc_0d93c2). Skipped provisioning per policy.",
                    "created_at": "2025-07-16T13:22:05+00:00"
                }
            }
        ],
        "outputs": [
                "val_2025_07_16_emp_0021_slack_present"
        ]
    }
    ,
    {
        "annotator": it6,
        "user_id": "it_v6_task_100",
        "instruction": "HR leadership necessitates ticket participation in certain workflows. Reconcile TaskTrack coverage for HR by using an HR peer as a basis while continuing active service. Choose emp_0008 (HRBP) as a reference point (has TaskTrack). Validate directory identity, align RBAC groups to adhere to the HRBP baseline, verify license status and capacity for baseline tools, and ensure TaskTrack is added only if it is not already present. Derive timestamps for any write operations from the target's directory account created_at (for emp_0001: 2024-02-09T09:00:00+00:00) and use deterministic identifiers without generating random values or duplicating existing app accounts.Use emp_0008 (HRBP) as a reference (holds TaskTrack). You must validate directory identity, align RBAC groups to the HRBP baseline, verify license posture and capacity for baseline tools, and ensure TaskTrack is present only if missing.Derive any write timestamps from the target's directory account created_at (for emp_0001: 2024-02-09T09:00:00+00:00) and use deterministic identifiers; do not generate random values or duplicate existing app accounts.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetBaselineForRole",
                "arguments": {
                    "department": "HR",
                    "job_title": "HRBP"
                },
            },
            {
                "name": "SetAccountGroups",
                "arguments": {
                    "account_id": "acc_dc71c8",
                    "group_ids": [
                        "grp_hr_82f8",
                        "grp_hr_all"
                    ],
                    "actor": "rbac_alignment",
                    "timestamp": "2024-02-09T09:00:00+00:00"
                },
            },
            {
                "name": "GetLicenseAssignments",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "GetLicenseInventory",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "GetAppAccounts",
                "arguments": {
                    "employee_id": "emp_0001",
                    "app_id": "app_jira"
                },
            },
            {
                "name": "UpsertAppAccount",
                "arguments": {
                    "app_account_id": "appacc_emp_0001_jira",
                    "employee_id": "emp_0001",
                    "app_id": "app_jira",
                    "status": "active",
                    "created_at": "2024-02-09T09:00:00+00:00"
                }
            }
        ],
        "outputs": [
                "appacc_emp_0001_jira"
        ]
    }
]
