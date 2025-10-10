from typing import List

from domains.dto import Task, Action


TASKS: List[Task] = [
    Task(
        annotator="it6",
        user_id="it_v6_task_01",
        instruction=(
            "You are completing onboarding for Marketing’s new Content Strategist, Elliot Lewis (employee_id=emp_0024). "
            "You must align RBAC to the role baseline and ensure the default license bundle from the RBAC map is present (lic_m365_e3, lic_salesforce, lic_slack_ent). "
            "You must provision a managed laptop selected from in_stock inventory using the policy tie‑breakers and track a deterministic pickup workflow. "
            "If capacity allows, you must add Adobe Creative Cloud as an optional license. You must provision Slack and Confluence app accounts. "
            "Anchor all writes to the 2025-07-16 onboarding window: lifecycle at 09:00Z, groups at 09:05Z, licenses at 09:06–09:09Z, device workflow at 09:10Z/10:00Z, apps at 09:12Z, completion at 10:05Z."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00024", "memo_id": "memo_onb_0024", "employee_ref": "emp_0024", "event": "onboarding", "status": "queued", "created_at": "2025-07-16T09:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_9071d5", "group_ids": [], "actor": "service_desk", "timestamp": "2025-07-16T09:05:00+00:00"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_9071d5", "group_ids": ["grp_marketing_719b", "grp_marketing_all"], "actor": "service_desk", "timestamp": "2025-07-16T09:05:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0024", "priority": "P2", "created_at": "2025-07-16T09:06:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0024_lic_m365_e3", "account_id": "acc_9071d5", "employee_id": "emp_0024", "license_id": "lic_m365_e3", "assigned_at": "2025-07-16T09:06:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_salesforce", "needed_count": 1, "jira_id": "JIRA-lic_salesforce-emp_0024", "priority": "P2", "created_at": "2025-07-16T09:07:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0024_lic_salesforce", "account_id": "acc_9071d5", "employee_id": "emp_0024", "license_id": "lic_salesforce", "assigned_at": "2025-07-16T09:07:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0024", "priority": "P2", "created_at": "2025-07-16T09:08:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0024_lic_slack_ent", "account_id": "acc_9071d5", "employee_id": "emp_0024", "license_id": "lic_slack_ent", "assigned_at": "2025-07-16T09:08:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_adobe_cc", "needed_count": 1, "jira_id": "JIRA-lic_adobe_cc-emp_0024", "priority": "P2", "created_at": "2025-07-16T09:09:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0024_lic_adobe_cc", "account_id": "acc_9071d5", "employee_id": "emp_0024", "license_id": "lic_adobe_cc", "assigned_at": "2025-07-16T09:09:00+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0024"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0024_1", "employee_id": "emp_0024", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0024_1", "created_at": "2025-07-16T09:10:00+00:00", "completed_at": "2025-07-16T10:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0024_slack", "employee_id": "emp_0024", "app_id": "app_slack", "status": "active", "created_at": "2025-07-16T09:12:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0024_conf", "employee_id": "emp_0024", "app_id": "app_confluence", "status": "active", "created_at": "2025-07-16T09:12:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00024", "status": "completed", "timestamp": "2025-07-16T10:05:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "lic_adobe_cc", "acc_9071d5"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_02",
        instruction=(
            "You are finishing onboarding for Cameron Wilson (employee_id=emp_0011, Support Manager)."
            "You must apply baseline RBAC, ensure core licenses, provision an in_stock laptop with MDM pickup, and add Jira app access and use timestamps 2025-07-16T11:02:00+00:00 for all tiem realted things deterministically."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00011", "memo_id": "memo_onb_emp_0011", "employee_ref": "emp_0011", "event": "onboarding", "status": "queued", "created_at": "2025-07-16T11:02:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Support", "job_title": "Support Manager"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"], "actor": "service_desk", "timestamp": "2025-07-16T11:02:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0011", "priority": "P2", "created_at": "2025-07-16T11:02:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0011_lic_m365_e3", "account_id": "acc_51e138", "employee_id": "emp_0011", "license_id": "lic_m365_e3", "assigned_at": "2025-07-16T11:02:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0011", "priority": "P2", "created_at": "2025-07-16T11:02:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0011_lic_slack_ent", "account_id": "acc_51e138", "employee_id": "emp_0011", "license_id": "lic_slack_ent", "assigned_at": "2025-07-16T11:02:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0011"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0011_1", "employee_id": "emp_0011", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0011_1", "created_at": "2025-07-16T11:02:00+00:00", "completed_at": "2025-07-16T11:02:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0011_jira", "employee_id": "emp_0011", "app_id": "app_jira", "status": "active", "created_at": "2025-07-16T11:02:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00011", "status": "completed", "timestamp": "2025-07-16T11:02:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "acc_51e138"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_03",
        instruction=(
            "You must complete onboarding hardware for Jordan Garcia (employee_id=emp_0002, Marketing Content Strategist)."
            "You will align RBAC, assign the baseline license bundle, provide an in_stock laptop with pickup workflow, and confirm Slack & Confluence app accounts."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00002", "memo_id": "memo_onb_emp_0002", "employee_ref": "emp_0002", "event": "onboarding", "status": "queued", "created_at": "2025-07-16T13:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0002"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0002"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_287fb8", "group_ids": ["grp_marketing_719b", "grp_marketing_all"], "actor": "service_desk", "timestamp": "2025-07-16T13:02:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0002", "priority": "P2", "created_at": "2025-07-16T13:02:30+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0002_lic_m365_e3", "account_id": "acc_287fb8", "employee_id": "emp_0002", "license_id": "lic_m365_e3", "assigned_at": "2025-07-16T13:02:35+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_salesforce", "needed_count": 1, "jira_id": "JIRA-lic_salesforce-emp_0002", "priority": "P2", "created_at": "2025-07-16T13:02:40+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0002_lic_salesforce", "account_id": "acc_287fb8", "employee_id": "emp_0002", "license_id": "lic_salesforce", "assigned_at": "2025-07-16T13:02:45+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0002", "priority": "P2", "created_at": "2025-07-16T13:02:50+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0002_lic_slack_ent", "account_id": "acc_287fb8", "employee_id": "emp_0002", "license_id": "lic_slack_ent", "assigned_at": "2025-07-16T13:02:55+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0002"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0002_1", "employee_id": "emp_0002", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0002_1", "created_at": "2025-07-16T13:05:00+00:00", "completed_at": "2025-07-16T14:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0002_slack", "employee_id": "emp_0002", "app_id": "app_slack", "status": "active", "created_at": "2025-07-16T13:06:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0002_conf", "employee_id": "emp_0002", "app_id": "app_confluence", "status": "active", "created_at": "2025-07-16T13:06:30+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00002", "status": "completed", "timestamp": "2025-07-16T14:05:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "acc_287fb8"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_04",
        instruction=(
            "You will provision HR Recruiter Logan Harris (employee_id=emp_0020) with baseline groups, baseline licenses, a laptop, and the Slack app account."
            "Follow in_stock selection policy; track provisioning with a deterministic pickup code."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00020", "memo_id": "memo_onb_emp_0020", "employee_ref": "emp_0020", "event": "onboarding", "status": "queued", "created_at": "2025-07-16T15:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_baseline_for_role", kwargs={"department": "HR", "job_title": "Recruiter"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_401a71", "group_ids": ["grp_hr_92d4", "grp_hr_all"], "actor": "service_desk", "timestamp": "2025-07-16T15:02:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0020", "priority": "P2", "created_at": "2025-07-16T15:02:30+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0020_lic_m365_e3", "account_id": "acc_401a71", "employee_id": "emp_0020", "license_id": "lic_m365_e3", "assigned_at": "2025-07-16T15:02:35+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0020", "priority": "P2", "created_at": "2025-07-16T15:02:40+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0020_lic_slack_ent", "account_id": "acc_401a71", "employee_id": "emp_0020", "license_id": "lic_slack_ent", "assigned_at": "2025-07-16T15:02:45+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0020"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0020_1", "employee_id": "emp_0020", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0020_1", "created_at": "2025-07-16T15:05:00+00:00", "completed_at": "2025-07-16T16:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0020_slack", "employee_id": "emp_0020", "app_id": "app_slack", "status": "active", "created_at": "2025-07-16T15:06:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00020", "status": "completed", "timestamp": "2025-07-16T16:05:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "acc_401a71"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_05",
        instruction=(
            "You must finalize onboarding for Operations Manager Zion Green (employee_id=emp_0035): baseline RBAC, baseline licenses, laptop provisioning, Slack & Jira app access."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00035", "memo_id": "memo_onb_emp_0035", "employee_ref": "emp_0035", "event": "onboarding", "status": "queued", "created_at": "2025-07-16T17:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0035"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0035"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Operations", "job_title": "Operations Manager"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_d89d5c", "group_ids": ["grp_operations_9079", "grp_operations_all"], "actor": "service_desk", "timestamp": "2025-07-16T17:02:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0035", "priority": "P2", "created_at": "2025-07-16T17:02:30+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0035_lic_m365_e3", "account_id": "acc_d89d5c", "employee_id": "emp_0035", "license_id": "lic_m365_e3", "assigned_at": "2025-07-16T17:02:35+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0035", "priority": "P2", "created_at": "2025-07-16T17:02:40+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0035_lic_slack_ent", "account_id": "acc_d89d5c", "employee_id": "emp_0035", "license_id": "lic_slack_ent", "assigned_at": "2025-07-16T17:02:45+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0035"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0035_1", "employee_id": "emp_0035", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0035_1", "created_at": "2025-07-16T17:05:00+00:00", "completed_at": "2025-07-16T18:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0035_slack", "employee_id": "emp_0035", "app_id": "app_slack", "status": "active", "created_at": "2025-07-16T17:06:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0035_jira", "employee_id": "emp_0035", "app_id": "app_jira", "status": "active", "created_at": "2025-07-16T17:06:30+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00035", "status": "completed", "timestamp": "2025-07-16T18:05:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "acc_d89d5c"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_06",
        instruction=(
            "You must onboard Engineering Software Engineer Sasha Baker (employee_id=emp_0037) with baseline groups, baseline licenses, a laptop, and GitHub/Jira app access."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00037", "memo_id": "memo_onb_emp_0037", "employee_ref": "emp_0037", "event": "onboarding", "status": "queued", "created_at": "2025-07-17T09:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0037"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0037"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_451983", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"], "actor": "service_desk", "timestamp": "2025-07-17T09:02:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0037", "priority": "P2", "created_at": "2025-07-17T09:02:30+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0037_lic_m365_e3", "account_id": "acc_451983", "employee_id": "emp_0037", "license_id": "lic_m365_e3", "assigned_at": "2025-07-17T09:02:35+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_github_ent", "needed_count": 1, "jira_id": "JIRA-lic_github_ent-emp_0037", "priority": "P2", "created_at": "2025-07-17T09:02:40+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0037_lic_github_ent", "account_id": "acc_451983", "employee_id": "emp_0037", "license_id": "lic_github_ent", "assigned_at": "2025-07-17T09:02:45+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0037", "priority": "P2", "created_at": "2025-07-17T09:02:50+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0037_lic_slack_ent", "account_id": "acc_451983", "employee_id": "emp_0037", "license_id": "lic_slack_ent", "assigned_at": "2025-07-17T09:02:55+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0037"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0037_1", "employee_id": "emp_0037", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0037_1", "created_at": "2025-07-17T09:05:00+00:00", "completed_at": "2025-07-17T10:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0037_gh", "employee_id": "emp_0037", "app_id": "app_github", "status": "active", "created_at": "2025-07-17T09:06:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0037_jira", "employee_id": "emp_0037", "app_id": "app_jira", "status": "active", "created_at": "2025-07-17T09:06:30+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00037", "status": "completed", "timestamp": "2025-07-17T10:05:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "acc_451983"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_07",
        instruction=(
            "You will onboard Sales Manager Riley Johnson (employee_id=emp_0006) by issuing a managed phone from in_stock, creating a deterministic pickup workflow, and enabling Slack & Salesforce apps, including baseline licenses."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00006", "memo_id": "memo_onb_emp_0006", "employee_ref": "emp_0006", "event": "onboarding", "status": "queued", "created_at": "2025-07-17T11:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0006"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0006"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Sales", "job_title": "Sales Manager"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0006", "priority": "P2", "created_at": "2025-07-17T11:02:30+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0006_lic_m365_e3", "account_id": "acc_e7e9ee", "employee_id": "emp_0006", "license_id": "lic_m365_e3", "assigned_at": "2025-07-17T11:02:35+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_salesforce", "needed_count": 1, "jira_id": "JIRA-lic_salesforce-emp_0006", "priority": "P2", "created_at": "2025-07-17T11:02:40+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0006_lic_salesforce", "account_id": "acc_e7e9ee", "employee_id": "emp_0006", "license_id": "lic_salesforce", "assigned_at": "2025-07-17T11:02:45+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0006", "priority": "P2", "created_at": "2025-07-17T11:02:50+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0006_lic_slack_ent", "account_id": "acc_e7e9ee", "employee_id": "emp_0006", "license_id": "lic_slack_ent", "assigned_at": "2025-07-17T11:02:55+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "phone", "status": "in_stock", "mdm_enrolled": True}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0016", "employee_id": "emp_0006"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0006_1", "employee_id": "emp_0006", "asset_id": "ast_0016", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0006_1", "created_at": "2025-07-17T11:05:00+00:00", "completed_at": "2025-07-17T12:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0006_slack", "employee_id": "emp_0006", "app_id": "app_slack", "status": "active", "created_at": "2025-07-17T11:06:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0006_sf", "employee_id": "emp_0006", "app_id": "app_salesforce", "status": "active", "created_at": "2025-07-17T11:06:30+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00006", "status": "completed", "timestamp": "2025-07-17T12:05:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0016", "acc_e7e9ee"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_08",
        instruction=(
            "You must complete onboarding for Finance Controller Blake Martin (employee_id=emp_0017) by issuing a laptop per policy, "
            "assigning baseline licenses, creating a mailbox with finance retention, and provisioning Confluence and Jira app accounts."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00017", "memo_id": "memo_onb_emp_0017", "employee_ref": "emp_0017", "event": "onboarding", "status": "queued", "created_at": "2025-07-17T13:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0017"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0017"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Finance", "job_title": "Controller"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0017", "priority": "P2", "created_at": "2025-07-17T13:02:30+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0017_lic_m365_e3", "account_id": "acc_82aecf", "employee_id": "emp_0017", "license_id": "lic_m365_e3", "assigned_at": "2025-07-17T13:02:35+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0017", "priority": "P2", "created_at": "2025-07-17T13:02:40+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0017_lic_slack_ent", "account_id": "acc_82aecf", "employee_id": "emp_0017", "license_id": "lic_slack_ent", "assigned_at": "2025-07-17T13:02:45+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0017"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0017_1", "employee_id": "emp_0017", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0017_1", "created_at": "2025-07-17T13:05:00+00:00", "completed_at": "2025-07-17T14:00:00+00:00"}),
            Action(name="create_mailbox", kwargs={"mailbox_id": "mbx_onb_0017", "employee_id": "emp_0017", "address": "blake.martin@example.com", "retention_policy": "finance_7y", "created_at": "2025-07-17T13:05:30+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0017_conf", "employee_id": "emp_0017", "app_id": "app_confluence", "status": "active", "created_at": "2025-07-17T13:06:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0017_jira", "employee_id": "emp_0017", "app_id": "app_jira", "status": "active", "created_at": "2025-07-17T13:06:30+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00017", "status": "completed", "timestamp": "2025-07-17T14:05:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "acc_82aecf"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_09",
        instruction=(
            "You must bring River Scott (employee_id=emp_0031, Marketing Content Strategist) to baseline. "
            "You must derive RBAC memberships from the RBAC baseline for Marketing/Content Strategist and ensure the role’s default license bundle is assigned. "
            "You must provision a managed laptop selected from in_stock inventory using the policy tie‑breakers with a deterministic pickup workflow, and you must provision app accounts for the baseline collaboration and sales apps (Slack and Salesforce). "
            "You must derive all write timestamps deterministically from emp_0031’s directory account created_at (2023-07-18T09:00:00+00:00); do not introduce other times."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00031", "memo_id": "memo_onb_emp_0031", "employee_ref": "emp_0031", "event": "onboarding", "status": "queued", "created_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_351bb4", "group_ids": ["grp_marketing_719b", "grp_marketing_all"], "actor": "service_desk", "timestamp": "2023-07-18T09:00:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0031", "priority": "P2", "created_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0031_lic_m365_e3", "account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_m365_e3", "assigned_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_salesforce", "needed_count": 1, "jira_id": "JIRA-lic_salesforce-emp_0031", "priority": "P2", "created_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0031_lic_salesforce", "account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_salesforce", "assigned_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0031", "priority": "P2", "created_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0031_lic_slack_ent", "account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_slack_ent", "assigned_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0031"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0031_1", "employee_id": "emp_0031", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0031_1", "created_at": "2023-07-18T09:00:00+00:00", "completed_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0031_slack", "employee_id": "emp_0031", "app_id": "app_slack", "status": "active", "created_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0031_sf", "employee_id": "emp_0031", "app_id": "app_salesforce", "status": "active", "created_at": "2023-07-18T09:00:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00031", "status": "completed", "timestamp": "2023-07-18T09:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "acc_351bb4"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_10",
        instruction=(
            "You must complete onboarding for Kai Young (employee_id=emp_0027, Marketing Growth Marketer): baseline groups, baseline licenses, "
            "Adobe optional license if capacity, laptop per policy, and app accounts for all licensed apps (Slack, Salesforce, Adobe)."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_onb_00027", "memo_id": "memo_onb_emp_0027", "employee_ref": "emp_0027", "event": "onboarding", "status": "queued", "created_at": "2025-07-17T17:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0027"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0027"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Growth Marketer"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_5494f2", "group_ids": ["grp_marketing_231e", "grp_marketing_all"], "actor": "service_desk", "timestamp": "2025-07-17T17:02:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0027", "priority": "P2", "created_at": "2025-07-17T17:02:30+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0027_lic_m365_e3", "account_id": "acc_5494f2", "employee_id": "emp_0027", "license_id": "lic_m365_e3", "assigned_at": "2025-07-17T17:02:35+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_salesforce", "needed_count": 1, "jira_id": "JIRA-lic_salesforce-emp_0027", "priority": "P2", "created_at": "2025-07-17T17:02:40+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0027_lic_salesforce", "account_id": "acc_5494f2", "employee_id": "emp_0027", "license_id": "lic_salesforce", "assigned_at": "2025-07-17T17:02:45+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0027", "priority": "P2", "created_at": "2025-07-17T17:02:50+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0027_lic_slack_ent", "account_id": "acc_5494f2", "employee_id": "emp_0027", "license_id": "lic_slack_ent", "assigned_at": "2025-07-17T17:02:55+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_adobe_cc", "needed_count": 1, "jira_id": "JIRA-lic_adobe_cc-emp_0027", "priority": "P2", "created_at": "2025-07-17T17:03:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0027_lic_adobe_cc", "account_id": "acc_5494f2", "employee_id": "emp_0027", "license_id": "lic_adobe_cc", "assigned_at": "2025-07-17T17:04:00+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0027"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_onb_0027_1", "employee_id": "emp_0027", "asset_id": "ast_0013", "process": "provisioning", "status": "completed", "pickup_code": "pc_dwf_onb_0027_1", "created_at": "2025-07-17T17:05:00+00:00", "completed_at": "2025-07-17T18:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0027_slack", "employee_id": "emp_0027", "app_id": "app_slack", "status": "active", "created_at": "2025-07-17T17:06:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0027_sf", "employee_id": "emp_0027", "app_id": "app_salesforce", "status": "active", "created_at": "2025-07-17T17:06:30+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0027_adobe", "employee_id": "emp_0027", "app_id": "app_adobe_cc", "status": "active", "created_at": "2025-07-17T17:07:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_onb_00027", "status": "completed", "timestamp": "2025-07-17T18:05:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013", "lic_adobe_cc", "acc_5494f2"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_11",
        instruction=(
            "You must offboard Operations Manager Remy White (employee_id=emp_0019) under standard policy. "
            "Anchor all writes deterministically to the directory account created_at (2023-10-24T09:00:00+00:00); derive identifiers from stable IDs only. "
            "Apply identity disable, align RBAC to empty with audited removals, revoke active baseline licenses, honor mailbox retention (std_2y), and reflect Slack app access based on current state. "
            "Record manager notification and complete the lifecycle; do not enumerate steps beyond these policy outcomes."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_offb_00019", "memo_id": "memo_offb_emp_0019", "employee_ref": "emp_0019", "event": "offboarding", "status": "queued", "created_at": "2023-10-24T09:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0019"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0019"}),
            Action(name="update_directory_account_status", kwargs={"account_id": "acc_1d0980", "status": "disabled", "disabled_at": "2023-10-24T09:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_1d0980", "group_ids": ["grp_operations_9079"], "actor": "service_desk", "timestamp": "2023-10-24T09:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_1d0980", "group_ids": ["grp_operations_all"], "actor": "service_desk", "timestamp": "2023-10-24T09:00:00+00:00"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_1d0980", "group_ids": [], "actor": "service_desk", "timestamp": "2023-10-24T09:00:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0019"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_1d0980", "employee_id": "emp_0019", "license_id": "lic_slack_ent", "revoked_at": "2023-10-24T09:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_1d0980", "employee_id": "emp_0019", "license_id": "lic_m365_e3", "revoked_at": "2023-10-24T09:00:00+00:00"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0019"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_offb_emp_0019", "mailbox_id": "mbx_1d0980", "employee_id": "emp_0019", "archive_path": "s3://corp-archives/mail/emp_0019/2023-10-24", "retention_policy": "std_2y", "created_at": "2023-10-24T09:00:00+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0019", "app_id": "app_slack"}),
            Action(name="disable_app_account", kwargs={"app_account_id": "appacc_fef353", "disabled_at": "2023-10-24T09:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00019", "event": "manager_notified", "timestamp": "2023-10-24T09:00:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_offb_00019", "status": "completed", "timestamp": "2023-10-24T09:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["acc_1d0980", "mbx_1d0980"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_12",
        instruction=(
            "You must offboard Marketing Growth Marketer Shawn Torres (employee_id=emp_0032) under standard policy, anchored deterministically to the directory account created_at (2023-12-24T09:00:00+00:00). "
            "Derive identifiers from the employee id; ensure RBAC changes are auditable, license posture is corrected, device handling is recorded deterministically, retention is honored, and app access changes reflect current state for collaboration and productivity apps."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_offb_00032", "memo_id": "memo_offb_emp_0032", "employee_ref": "emp_0032", "event": "offboarding", "status": "queued", "created_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0032"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0032"}),
            Action(name="update_directory_account_status", kwargs={"account_id": "acc_f06213", "status": "disabled", "disabled_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_f06213", "group_ids": ["grp_marketing_231e"], "actor": "service_desk", "timestamp": "2023-12-24T09:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_f06213", "group_ids": ["grp_marketing_all"], "actor": "service_desk", "timestamp": "2023-12-24T09:00:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0032"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_f06213", "employee_id": "emp_0032", "license_id": "lic_salesforce", "revoked_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_f06213", "employee_id": "emp_0032", "license_id": "lic_slack_ent", "revoked_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_f06213", "employee_id": "emp_0032", "license_id": "lic_m365_e3", "revoked_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0032"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00032", "event": "device_none_assigned", "timestamp": "2023-12-24T09:00:00+00:00", "actor": "service_desk"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0032", "app_id": "app_slack"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00032", "event": "app_slack_none", "timestamp": "2023-12-24T09:00:00+00:00", "actor": "service_desk"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0032"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00032", "event": "no_m365_app_account", "timestamp": "2023-12-24T09:00:00+00:00", "actor": "service_desk"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0032"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_offb_emp_0032", "mailbox_id": "mbx_f06213", "employee_id": "emp_0032", "archive_path": "s3://corp-archives/mail/emp_0032/2023-12-24", "retention_policy": "std_2y", "created_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0032", "app_id": "app_salesforce"}),
            Action(name="disable_app_account", kwargs={"app_account_id": "appacc_dfb864", "disabled_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0032", "app_id": "app_github"}),
            Action(name="disable_app_account", kwargs={"app_account_id": "appacc_f69e6a", "disabled_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0032", "app_id": "app_confluence"}),
            Action(name="disable_app_account", kwargs={"app_account_id": "appacc_6fc5eb", "disabled_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0032", "app_id": "app_jira"}),
            Action(name="disable_app_account", kwargs={"app_account_id": "appacc_7b53ec", "disabled_at": "2023-12-24T09:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00032", "event": "manager_notified", "timestamp": "2023-12-24T09:00:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_offb_00032", "status": "completed", "timestamp": "2023-12-24T09:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["acc_f06213", "mbx_f06213"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_13",
        instruction=(
            "You must offboard Marketing Content Strategist Elliot Lewis (employee_id=emp_0024) in line with identity, RBAC, licensing, device, and retention policy. "
            "Anchor all writes deterministically to 2025-07-20 and derive identifiers and pickup codes from employee_id and anchors. Within the anchored window, you must use the anchor timestamp (11:00:00Z) for all writes; only the scheduled device return entry uses its due time (2025-07-27T17:00:00+00:00) as created_at by policy. "
            "Do not hard‑code database internals beyond policy‑required anchors and due times."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_offb_00024", "memo_id": "memo_offb_emp_0024", "employee_ref": "emp_0024", "event": "offboarding", "status": "queued", "created_at": "2025-07-20T11:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0024"}),
            Action(name="update_directory_account_status", kwargs={"account_id": "acc_9071d5", "status": "disabled", "disabled_at": "2025-07-20T11:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_9071d5", "group_ids": ["grp_marketing_719b"], "actor": "service_desk", "timestamp": "2025-07-20T11:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_9071d5", "group_ids": ["grp_marketing_all"], "actor": "service_desk", "timestamp": "2025-07-20T11:00:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0024"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_9071d5", "employee_id": "emp_0024", "license_id": "lic_salesforce", "revoked_at": "2025-07-20T11:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_9071d5", "employee_id": "emp_0024", "license_id": "lic_slack_ent", "revoked_at": "2025-07-20T11:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_9071d5", "employee_id": "emp_0024", "license_id": "lic_m365_e3", "revoked_at": "2025-07-20T11:00:00+00:00"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0024"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_ret_emp_0024_ast_0056_req", "employee_id": "emp_0024", "asset_id": "ast_0056", "process": "return", "status": "requested", "pickup_code": "pc_ret_emp_0024_ast_0056", "created_at": "2025-07-20T11:00:00+00:00", "completed_at": None}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_ret_emp_0024_ast_0056_due", "employee_id": "emp_0024", "asset_id": "ast_0056", "process": "return_due", "status": "scheduled", "pickup_code": "pc_ret_emp_0024_ast_0056", "created_at": "2025-07-27T17:00:00+00:00", "completed_at": None}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0024"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_offb_emp_0024", "mailbox_id": "mbx_9071d5", "employee_id": "emp_0024", "archive_path": "s3://corp-archives/mail/emp_0024/2025-07-20", "retention_policy": "std_2y", "created_at": "2025-07-20T11:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00024", "event": "manager_notified", "timestamp": "2025-07-20T11:00:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_offb_00024", "status": "completed", "timestamp": "2025-07-20T11:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0056", "mbx_9071d5"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_14",
        instruction=(
            "You must perform license posture maintenance for Marketing’s Content Strategist Wyatt Hill (employee_id=emp_0034). "
            "Anchor all writes to the license audit time 2025-07-15T08:00:00+00:00. You must deterministically revoke any active baseline licenses from the directory account and reflect inventory updates. "
            "Do not modify RBAC, devices, or mailboxes. You must register a deterministic Jira maintenance record (priority=P2, status=Closed) derived from the anchor and employee id."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0034"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0034"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0034"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_baacc3", "employee_id": "emp_0034", "license_id": "lic_slack_ent", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_baacc3", "employee_id": "emp_0034", "license_id": "lic_m365_e3", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_baacc3", "employee_id": "emp_0034", "license_id": "lic_salesforce", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_salesforce"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "JIRA-lic_maint-emp_0034-2025_07_15_0800", "issue_type": "Maintenance", "summary": "license_maintenance_emp_0034_2025_07_15_0800", "priority": "P2", "status": "Closed", "created_at": "2025-07-15T08:00:00+00:00", "updated_at": "2025-07-15T08:00:00+00:00"}),
        ],
        outputs=["acc_baacc3"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_15",
        instruction=(
            "You must offboard Engineering DevOps Engineer Nico Adams (employee_id=emp_0036) under identity, RBAC, licensing, device, and retention policy. "
            "Anchor all writes deterministically to the directory account created_at (2024-06-21T09:00:00+00:00). Use a single scheduled device return entry at due 2025-07-29T17:00:00+00:00 (policy: the scheduled return uses the due time as created_at), apply std_2y mailbox retention with a path derived from the anchor date, and ensure RBAC/license posture and lifecycle handling are compliant. "
            "Derive the workflow identifier and pickup code deterministically from employee_id and asset_id; do not rely on random values or hard‑coded database internals."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_offb_00036", "memo_id": "memo_offb_emp_0036", "employee_ref": "emp_0036", "event": "offboarding", "status": "queued", "created_at": "2024-06-21T09:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0036"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0036"}),
            Action(name="update_directory_account_status", kwargs={"account_id": "acc_f9a6bc", "status": "disabled", "disabled_at": "2024-06-21T09:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_f9a6bc", "group_ids": ["grp_engineering_4162"], "actor": "service_desk", "timestamp": "2024-06-21T09:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_f9a6bc", "group_ids": ["grp_engineering_all"], "actor": "service_desk", "timestamp": "2024-06-21T09:00:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0036"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_github_ent", "revoked_at": "2024-06-21T09:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_slack_ent", "revoked_at": "2024-06-21T09:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_m365_e3", "revoked_at": "2024-06-21T09:00:00+00:00"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0036"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_ret_emp_0036_ast_0055_due", "employee_id": "emp_0036", "asset_id": "ast_0055", "process": "return_due", "status": "scheduled", "pickup_code": "pc_ret_emp_0036_ast_0055", "created_at": "2025-07-29T17:00:00+00:00", "completed_at": None}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0036"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_offb_emp_0036", "mailbox_id": "mbx_f9a6bc", "employee_id": "emp_0036", "archive_path": "s3://corp-archives/mail/emp_0036/2024-06-21", "retention_policy": "std_2y", "created_at": "2024-06-21T09:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00036", "event": "manager_notified", "timestamp": "2024-06-21T09:00:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_offb_00036", "status": "completed", "timestamp": "2024-06-21T09:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0055", "mbx_f9a6bc"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_16",
        instruction=(
            "You must offboard Support Manager Drew Nelson (employee_id=emp_0039) in accordance with identity, RBAC, licensing, device, and retention policy."
            " You must anchor all writes to 2025-07-20T14:00:00+00:00 and you must schedule the assigned device return due on 2025-07-30T17:00:00+00:00 (the scheduled entry uses the due time as its created_at)."
            " You must apply std_2y mailbox retention with an archive path derived from the anchor date, and you must ensure all directory access changes are auditable."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_offb_00039", "memo_id": "memo_offb_emp_0039", "employee_ref": "emp_0039", "event": "offboarding", "status": "queued", "created_at": "2025-07-20T14:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0039"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0039"}),
            Action(name="update_directory_account_status", kwargs={"account_id": "acc_c42c15", "status": "disabled", "disabled_at": "2025-07-20T14:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_c42c15", "group_ids": ["grp_support_ada3"], "actor": "service_desk", "timestamp": "2025-07-20T14:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_c42c15", "group_ids": ["grp_support_all"], "actor": "service_desk", "timestamp": "2025-07-20T14:00:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0039"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_c42c15", "employee_id": "emp_0039", "license_id": "lic_slack_ent", "revoked_at": "2025-07-20T14:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_c42c15", "employee_id": "emp_0039", "license_id": "lic_m365_e3", "revoked_at": "2025-07-20T14:00:00+00:00"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0039"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_ret_0039_1", "employee_id": "emp_0039", "asset_id": "ast_0010", "process": "return_due", "status": "scheduled", "pickup_code": None, "created_at": "2025-07-30T17:00:00+00:00", "completed_at": None}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0039"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_offb_emp_0039", "mailbox_id": "mbx_c42c15", "employee_id": "emp_0039", "archive_path": "s3://corp-archives/mail/emp_0039/2025-07-20", "retention_policy": "std_2y", "created_at": "2025-07-20T14:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00039", "event": "manager_notified", "timestamp": "2025-07-20T14:00:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_offb_00039", "status": "completed", "timestamp": "2025-07-20T14:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0010", "mbx_c42c15"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_17",
        instruction=(
            "You are offboarding Sales Manager Lane Allen (employee_id=emp_0028)."
            "Disable sign‑in, clear groups, revoke Salesforce/Slack/M365, request dock return (due by 2025-07-30 17:00 UTC), archive mailbox (std_2y), and disable Slack app account."
            "Use deterministic anchors: lifecycle_id=lcq_offb_00028; memo_id=memo_offb_emp_0028; archive_id=arch_offb_emp_0028; archive_path=s3://corp-archives/mail/emp_0028/2025-07-20; all writes anchored to 2025-07-20: created_at=15:00:00Z, disabled_at=15:01:00Z, groups timestamp=15:02:00Z, revoke Salesforce=15:03:00Z, revoke Slack=15:03:30Z, revoke M365=15:04:00Z; return request created_at=15:04:30Z with workflow_id=dwf_ret_0028_1 and pickup_code=pc_ret_0028_1; schedule the return at due_ts=2025-07-30T17:00:00+00:00 as a second entry workflow_id=dwf_ret_0028_2 with the same pickup_code; archive created_at=15:05:00Z, Slack app disable at 15:05:30Z, manager_notified=15:06:00Z, completed=15:07:00Z."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_offb_00028", "memo_id": "memo_offb_emp_0028", "employee_ref": "emp_0028", "event": "offboarding", "status": "queued", "created_at": "2025-07-20T15:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0028"}),
            Action(name="update_directory_account_status", kwargs={"account_id": "acc_81d8d5", "status": "disabled", "disabled_at": "2025-07-20T15:01:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_81d8d5", "group_ids": ["grp_sales_4bcb", "grp_sales_all"], "actor": "service_desk", "timestamp": "2025-07-20T15:02:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0028"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_81d8d5", "employee_id": "emp_0028", "license_id": "lic_salesforce", "revoked_at": "2025-07-20T15:03:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_81d8d5", "employee_id": "emp_0028", "license_id": "lic_slack_ent", "revoked_at": "2025-07-20T15:03:30+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_81d8d5", "employee_id": "emp_0028", "license_id": "lic_m365_e3", "revoked_at": "2025-07-20T15:04:00+00:00"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0028"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_ret_0028_1", "employee_id": "emp_0028", "asset_id": "ast_0028", "process": "return", "status": "requested", "pickup_code": "pc_ret_0028_1", "created_at": "2025-07-20T15:04:30+00:00", "completed_at": None}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_ret_0028_2", "employee_id": "emp_0028", "asset_id": "ast_0028", "process": "return_due", "status": "scheduled", "pickup_code": "pc_ret_0028_1", "created_at": "2025-07-30T17:00:00+00:00", "completed_at": None}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0028"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_offb_emp_0028", "mailbox_id": "mbx_81d8d5", "employee_id": "emp_0028", "archive_path": "s3://corp-archives/mail/emp_0028/2025-07-20", "retention_policy": "std_2y", "created_at": "2025-07-20T15:05:00+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0028", "app_id": "app_slack"}),
            Action(name="disable_app_account", kwargs={"app_account_id": "appacc_a3d740", "disabled_at": "2025-07-20T15:05:30+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00028", "event": "manager_notified", "timestamp": "2025-07-20T15:06:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_offb_00028", "status": "completed", "timestamp": "2025-07-20T15:07:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0028", "mbx_81d8d5"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_18",
        instruction=(
            "You must perform license posture maintenance for Engineering’s DevOps Engineer Noel Wright (employee_id=emp_0030) under license‑governance policy. "
            "Anchor all writes to the license audit time 2025-07-15T08:00:00+00:00. Validate current assignments, operate strictly within capacity, and record the change deterministically. "
            "You must revoke collaboration licenses that are not required for the role (Slack Enterprise and Microsoft 365 E3). Do not modify RBAC, mailbox, devices, or app accounts. "
            "Register a maintenance record in Jira with issue_type=Maintenance and priority=P2, following New→In Progress→Resolved at the anchor."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0030"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_db017d", "employee_id": "emp_0030", "license_id": "lic_slack_ent", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_db017d", "employee_id": "emp_0030", "license_id": "lic_m365_e3", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "JIRA-lic_cleanup-emp_0030-2025_07_15_0800", "issue_type": "Maintenance", "summary": "license_revoke;licenses=lic_slack_ent,lic_m365_e3;employee=emp_0030;audit=2025-07-15T08:00:00+00:00", "priority": "P2", "status": "New", "created_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "JIRA-lic_cleanup-emp_0030-2025_07_15_0800", "status": "In Progress", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "JIRA-lic_cleanup-emp_0030-2025_07_15_0800", "status": "Resolved", "updated_at": "2025-07-15T08:00:00+00:00"}),
        ],
        outputs=["lic_slack_ent", "lic_m365_e3"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_19",
        instruction=(
            "You must offboard Marketing Content Strategist River Scott (employee_id=emp_0031) under identity, RBAC, licensing, device, and retention policy. "
            "Anchor all writes deterministically to 2025-07-20 and derive identifiers from inputs. Within the anchored window, you must use the anchor timestamp (17:00:00Z) for all writes; archive the mailbox under std_2y with a path derived from the anchor date (s3://corp-archives/mail/emp_0031/2025-07-20). "
            "Execute device handling deterministically; if no devices are assigned you must record that deterministically at the anchor time."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_offb_00031", "memo_id": "memo_offb_emp_0031", "employee_ref": "emp_0031", "event": "offboarding", "status": "queued", "created_at": "2025-07-20T17:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0031"}),
            Action(name="update_directory_account_status", kwargs={"account_id": "acc_351bb4", "status": "disabled", "disabled_at": "2025-07-20T17:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_351bb4", "group_ids": ["grp_marketing_719b"], "actor": "service_desk", "timestamp": "2025-07-20T17:00:00+00:00"}),
            Action(name="remove_account_groups", kwargs={"account_id": "acc_351bb4", "group_ids": ["grp_marketing_all"], "actor": "service_desk", "timestamp": "2025-07-20T17:00:00+00:00"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_351bb4", "group_ids": [], "actor": "service_desk", "timestamp": "2025-07-20T17:00:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0031"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0031"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00031", "event": "device_none_assigned", "timestamp": "2025-07-20T17:00:00+00:00", "actor": "service_desk"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_salesforce", "revoked_at": "2025-07-20T17:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_salesforce"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_adobe_cc", "revoked_at": "2025-07-20T17:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_slack_ent", "revoked_at": "2025-07-20T17:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_m365_e3", "revoked_at": "2025-07-20T17:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0031"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_offb_emp_0031", "mailbox_id": "mbx_351bb4", "employee_id": "emp_0031", "archive_path": "s3://corp-archives/mail/emp_0031/2025-07-20", "retention_policy": "std_2y", "created_at": "2025-07-20T17:00:00+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0031", "app_id": "app_slack"}),
            Action(name="disable_app_account", kwargs={"app_account_id": "appacc_14cdf3", "disabled_at": "2025-07-20T17:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_offb_00031", "event": "manager_notified", "timestamp": "2025-07-20T17:00:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_offb_00031", "status": "completed", "timestamp": "2025-07-20T17:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["mbx_351bb4", "acc_351bb4"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_20",
        instruction=(
            "You must correct Finance license posture for Accounting Manager Micah King (employee_id=emp_0029) under license‑governance policy. "
            "Anchor all writes to the license audit time 2025-07-15T08:00:00+00:00. You must validate current assignments, operate strictly within capacity, and record the change as deterministic maintenance. "
            "You must revoke only the collaboration licenses that are not required for the role (Slack Enterprise and Microsoft 365 E3) and document the change in Jira; you must not modify RBAC, mailbox, devices, or app accounts. "
            "In Jira, you must create a maintenance record with issue_type=Maintenance and priority=P2 and follow the status transitions New→In Progress→Resolved at the anchor time."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0029"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_48efe8", "employee_id": "emp_0029", "license_id": "lic_slack_ent", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_48efe8", "employee_id": "emp_0029", "license_id": "lic_m365_e3", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "JIRA-lic_cleanup-emp_0029-2025_07_15_0800", "issue_type": "Maintenance", "summary": "license_revoke;licenses=lic_slack_ent,lic_m365_e3;employee=emp_0029;audit=2025-07-15T08:00:00+00:00", "priority": "P2", "status": "New", "created_at": "2025-07-15T08:00:00+00:00", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "JIRA-lic_cleanup-emp_0029-2025_07_15_0800", "status": "In Progress", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "JIRA-lic_cleanup-emp_0029-2025_07_15_0800", "status": "Resolved", "updated_at": "2025-07-15T08:00:00+00:00"}),
        ],
        outputs=["lic_slack_ent", "lic_m365_e3"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_21",
        instruction=(
            "You must rebalance Adobe Creative Cloud seats by reclaiming one from River Scott (employee_id=emp_0031) and assigning it to Elliot Lewis (employee_id=emp_0024) in line with license governance. "
            "Anchor all writes to the Adobe CC audit time 2025-07-15T08:00:00+00:00. Ensure inventory and assignments are validated, capacity is honored (open a shortage ticket if required), and record the operation as deterministic license maintenance (lifecycle + Jira)."
        ),
        actions=[
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_rebalance_2025_07_15", "memo_id": "memo_lic_adobe_cc_rebalance_2025_07_15", "employee_ref": "lic_adobe_cc", "event": "license_maintenance", "status": "queued", "created_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_rebalance_2025_07_15", "event": "started", "timestamp": "2025-07-15T08:00:00+00:00", "actor": "service_desk"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0031"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_adobe_cc", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0024"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_adobe_cc", "needed_count": 1, "jira_id": "JIRA-lic_adobe_cc-rebalance-emp_0031-to-emp_0024-2025_07_15_0800", "priority": "P3", "created_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0024_lic_adobe_cc_2025_07_15", "account_id": "acc_9071d5", "employee_id": "emp_0024", "license_id": "lic_adobe_cc", "assigned_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "JIRA-lic_adobe_cc-rebalance-emp_0031-to-emp_0024-2025_07_15_0800", "issue_type": "Incident", "summary": "license_id=lic_adobe_cc;action=rebalance;from=emp_0031;to=emp_0024;audit=2025-07-15T08:00:00+00:00", "priority": "P3", "status": "New", "created_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "JIRA-lic_adobe_cc-rebalance-emp_0031-to-emp_0024-2025_07_15_0800", "status": "In Progress", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "JIRA-lic_adobe_cc-rebalance-emp_0031-to-emp_0024-2025_07_15_0800", "status": "Resolved", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_rebalance_2025_07_15", "status": "completed", "timestamp": "2025-07-15T08:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["lic_adobe_cc", "acc_9071d5"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_22",
        instruction=(
            "You must reduce active Slack and M365 consumption by revoking seats from on‑leave employees (emp_0004 and emp_0032)."
            "Validate assignments, and use each license's audit timestamp as the deterministic change time."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0004"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0004"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0004"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_38d007", "employee_id": "emp_0004", "license_id": "lic_slack_ent", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0032"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0032"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0032"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_f06213", "employee_id": "emp_0032", "license_id": "lic_slack_ent", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_38d007", "employee_id": "emp_0004", "license_id": "lic_m365_e3", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_f06213", "employee_id": "emp_0032", "license_id": "lic_m365_e3", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
        ],
        outputs=["lic_slack_ent", "lic_m365_e3"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_23",
        instruction=(
            "You must align Adobe CC reservation posture for July onboarding: increase reserved capacity by one seat if and only if inventory shows reserved_seats below the target buffer of 4."
            "Use deterministic anchors from the Adobe CC audit (2025-07-15T08:00:00+00:00), record lifecycle using the license id as the subject, and set the reservation reason deterministically to reason=buffer_2025_07_15. Track the maintenance under ITSD-1013 (License Maintenance, P3, Resolved)."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_2025_07_15", "memo_id": "memo_lic_adobe_cc_2025_07_15", "employee_ref": "lic_adobe_cc", "event": "license_maintenance", "status": "queued", "created_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_2025_07_15", "event": "started", "timestamp": "2025-07-15T08:00:00+00:00", "actor": "service_desk"}),
            Action(name="reserve_license", kwargs={"license_id": "lic_adobe_cc", "count": 1, "reason": "buffer_2025_07_15"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_2025_07_15", "event": "reserved_to_4", "timestamp": "2025-07-15T08:00:00+00:00", "actor": "service_desk"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1013", "issue_type": "License Maintenance", "summary": "license_id=lic_adobe_cc;action=reservation_set;from=3;to=4;reserve=1;reason=buffer_2025_07_15", "priority": "P3", "status": "Resolved", "created_at": "2025-07-15T08:00:00+00:00", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_2025_07_15", "status": "completed", "timestamp": "2025-07-15T08:00:00+00:00", "actor": "service_desk"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
        ],
        outputs=["lic_adobe_cc"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_24",
        instruction=(
            "You must provision Microsoft 365 E5 for DevOps Engineer Nico Adams (emp_0036) and Software Engineer Sasha Baker (emp_0037) in accordance with license governance."
            "Validate available capacity and anchor assignment timestamps to the license audit (2025-07-15T08:00:00+00:00). Track under ITSD-1018 (License Maintenance, P3, Done)."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e5"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0036"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0036"}),
            Action(name="get_license_assignments", kwargs={}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_00106", "account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_m365_e5", "assigned_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0037"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0037"}),
            Action(name="get_license_assignments", kwargs={}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_00107", "account_id": "acc_451983", "employee_id": "emp_0037", "license_id": "lic_m365_e5", "assigned_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e5"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1018", "issue_type": "License Maintenance", "summary": "tracking=ITSD-1018;license=lic_m365_e5;op=assign;to=emp_0036,emp_0037;audit=2025-07-15T08:00:00+00:00", "priority": "P3", "status": "Done", "created_at": "2025-07-15T08:00:00+00:00", "updated_at": "2025-07-15T08:00:00+00:00"}),
        ],
        outputs=["lic_m365_e5"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_25",
        instruction=(
            "You must free two GitHub Enterprise seats by revoking licenses from Noel Wright (employee_id=emp_0030) and Evan Carter (employee_id=emp_0040)."
            "Validate their assignments first and use the GitHub license audit time for deterministic timestamps."
            "Log the reclaim in Jira as ITSD-1017 (issue_type='License Maintenance', priority='P3', status='Done')."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_github_ent"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0030"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_db017d", "employee_id": "emp_0030", "license_id": "lic_github_ent", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0040"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_54337a", "employee_id": "emp_0040", "license_id": "lic_github_ent", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1017", "issue_type": "License Maintenance", "summary": "license_id=lic_github_ent;action=revoke;revoke_from=emp_0030,emp_0040;count=2", "priority": "P3", "status": "Done", "created_at": "2025-07-15T08:00:00+00:00", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_github_ent"}),
        ],
        outputs=["lic_github_ent"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_26",
        instruction=(
            "You must ensure compliant Salesforce access for Ops Manager Jules Perez (employee_id=emp_0042) under license governance: operate within capacity, avoid duplicate grants, and anchor all write timestamps to the Salesforce audit time (2025-07-15T08:00:00+00:00)."
            "Track this under ITSD-1014 (License Maintenance, P3, Done). If capacity allows, assign directly without trimming reservations to avoid ambiguity in final state."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_salesforce"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0042"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0042"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0042"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_00106", "account_id": "acc_f76658", "employee_id": "emp_0042", "license_id": "lic_salesforce", "assigned_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1014", "issue_type": "License Maintenance", "summary": "tracking=ITSD-1014;license=lic_salesforce;op=assign;to=emp_0042;audit=2025-07-15T08:00:00+00:00", "priority": "P3", "status": "Resolved", "created_at": "2025-07-15T08:00:00+00:00", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_salesforce"}),
        ],
        outputs=["lic_salesforce", "acc_f76658"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_27",
        instruction=(
            "You must align Microsoft 365 E5 reservation posture with the pilot threshold of 2 by trimming reservations only if current reserved_seats exceed 2."
            "Use the E5 audit anchor (2025-07-15T08:00:00+00:00) for deterministic timing and capture a before/after inventory read for auditability. Track under ITSD-1015 (License Maintenance, P3, Resolved)."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e5"}),
            Action(name="release_license_reservation", kwargs={"license_id": "lic_m365_e5", "count": 2}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e5"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1015", "issue_type": "License Maintenance", "summary": "tracking=ITSD-1015;license=lic_m365_e5;op=reservation_trim;to=2;audit=2025-07-15T08:00:00+00:00", "priority": "P3", "status": "Resolved", "created_at": "2025-07-15T08:00:00+00:00", "updated_at": "2025-07-15T08:00:00+00:00"}),
        ],
        outputs=["lic_m365_e5"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_28",
        instruction=(
            "You must reallocate Adobe CC within Marketing by reclaiming one from Finley Robinson (employee_id=emp_0025) and assigning it to Dakota Jackson (employee_id=emp_0016)."
            "Validate assignments and use the audit timestamp for deterministic times."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="find_employees", kwargs={"department": "Marketing", "status": "active"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0025"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0025"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0025"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_1e8432", "employee_id": "emp_0025", "license_id": "lic_adobe_cc", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0016"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0016"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0016"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_00063", "account_id": "acc_0099f1", "employee_id": "emp_0016", "license_id": "lic_adobe_cc", "assigned_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
        ],
        outputs=["lic_adobe_cc", "acc_0099f1"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_29",
        instruction=(
            "You must expand Adobe CC availability for content work by assigning Adobe CC to Skyler Sanchez (employee_id=emp_0021) and Kai Young (employee_id=emp_0027) under license‑governance policy."
            "Anchor all writes to the Adobe CC audit (2025-07-15T08:00:00+00:00). Verify capacity deterministically via inventory reads and derive new assignment identifiers as the next sequential values after the current maximum in the assignments table at the audit anchor."
            "Record a lightweight license‑maintenance run at the same anchor for auditability; do not raise escalations when capacity suffices."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="get_license_assignments", kwargs={}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_expand_2025_07_15", "memo_id": "memo_lic_adobe_cc_expand_2025_07_15", "employee_ref": "lic_adobe_cc", "event": "license_maintenance", "status": "queued", "created_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_expand_2025_07_15", "event": "started", "timestamp": "2025-07-15T08:00:00+00:00", "actor": "service_desk"}),

            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0021"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_00106", "account_id": "acc_43980f", "employee_id": "emp_0021", "license_id": "lic_adobe_cc", "assigned_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0027"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0027"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0027"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_00107", "account_id": "acc_5494f2", "employee_id": "emp_0027", "license_id": "lic_adobe_cc", "assigned_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_lic_adobe_cc_expand_2025_07_15", "event": "completed", "timestamp": "2025-07-15T08:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["lic_adobe_cc"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_30",
        instruction=(
            "You must combine Adobe cleanup with forward planning by revoking Adobe CC from River Scott (employee_id=emp_0031) and Finley Robinson (employee_id=emp_0025), then reserving 2 seats for upcoming content projects using reason 'content_projects_q3'."
            "Validate assignments first and keep times deterministic via the audit timestamp. Record this under tracking_id ITSD-1016 (License Maintenance, P3, Done)."
        ),
        actions=[
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0031"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_351bb4", "employee_id": "emp_0031", "license_id": "lic_adobe_cc", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0025"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0025"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0025"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_1e8432", "employee_id": "emp_0025", "license_id": "lic_adobe_cc", "revoked_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="reserve_license", kwargs={"license_id": "lic_adobe_cc", "count": 2, "reason": "content_projects_q3"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1016", "issue_type": "License Maintenance", "summary": "license_id=lic_adobe_cc;action=revoke+reserve;revoke_from=emp_0031,emp_0025;reserve=2;reason=content_projects_q3", "priority": "P3", "status": "Done", "created_at": "2025-07-15T08:00:00+00:00", "updated_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_adobe_cc"}),
        ],
        outputs=["lic_adobe_cc"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_31",
        instruction=(
            "You must provide a compliant in-stock laptop to Skyler Sanchez (employee_id=emp_0021) per tie-breaker policy, complete MDM enrollment deterministically, and verify the asset is assigned and managed and use the timestamp 2023-06-10T09:00:00+00:00 for all time realated things."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0021"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_hw_emp_0021", "memo_id": "memo_hw_emp_0021", "employee_ref": "emp_0021", "event": "hardware_provision", "status": "queued", "created_at": "2023-06-10T09:00:00+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0021"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0021_ast_0013", "employee_id": "emp_0021", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_mdm_emp_0021_ast_0013", "created_at": "2023-06-10T09:00:00+00:00", "completed_at": "2023-06-10T09:00:00+00:00"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0021"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "assigned_to": "emp_0021", "mdm_enrolled": True}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_hw_emp_0021", "status": "completed", "timestamp": "2023-06-10T09:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_32",
        instruction=(
            "You must issue a managed phone to Sales Manager Emerson Thomas (employee_id=emp_0013)."
            "Choose an in_stock phone per policy, enroll it via MDM, and verify the assignment."
            "Track with workflow_id=dwf_asset_emp_0013_1 and pickup_code=pc_dwf_asset_emp_0013_1; created_at=2025-07-18T10:05:00+00:00; mdm_enroll at 2025-07-18T10:10:00+00:00."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0013"}),
            Action(name="find_assets", kwargs={"asset_type": "phone", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0016", "employee_id": "emp_0013"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_asset_emp_0013_1", "employee_id": "emp_0013", "asset_id": "ast_0016", "process": "mdm", "status": "completed", "pickup_code": "pc_dwf_asset_emp_0013_1", "created_at": "2025-07-18T10:05:00+00:00", "completed_at": "2025-07-18T10:10:00+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "phone", "assigned_to": "emp_0013"}),
        ],
        outputs=["ast_0016"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_33",
        instruction=(
            "You must verify device compliance for Dakota Jackson (employee_id=emp_0016) under asset and RBAC policy: the assigned phone must be MDM‑managed, RBAC groups must match baseline for Marketing/Content Strategist, licenses must reflect the baseline bundle, and mailbox should be active."
            "Anchor all writes to 2025-07-18T11:10:00+00:00 for determinism; use lifecycle_id=lcq_devcomp_emp_0016_2025_07_18 and memo_id=memo_devcomp_emp_0016_2025_07_18 for auditable tracking."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0016"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0016"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_0099f1", "group_ids": ["grp_marketing_719b", "grp_marketing_all"], "actor": "service_desk", "timestamp": "2025-07-18T11:10:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0016"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0016"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0016"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0016_ast_0022", "employee_id": "emp_0016", "asset_id": "ast_0022", "process": "mdm", "status": "completed", "pickup_code": "pc_mdm_emp_0016_ast_0022", "created_at": "2025-07-18T11:10:00+00:00", "completed_at": "2025-07-18T11:10:00+00:00"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18", "memo_id": "memo_devcomp_emp_0016_2025_07_18", "employee_ref": "emp_0016", "event": "device_compliance", "status": "queued", "created_at": "2025-07-18T11:10:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18", "event": "rbac_verified", "timestamp": "2025-07-18T11:10:00+00:00", "actor": "service_desk"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18", "event": "licenses_verified", "timestamp": "2025-07-18T11:10:00+00:00", "actor": "service_desk"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18", "event": "mailbox_verified", "timestamp": "2025-07-18T11:10:00+00:00", "actor": "service_desk"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18", "event": "mdm_verified", "timestamp": "2025-07-18T11:10:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_devcomp_emp_0016_2025_07_18", "status": "completed", "timestamp": "2025-07-18T11:10:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0022"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_34",
        instruction=(
            "You must provide an in-stock laptop to Kendall Clark (employee_id=emp_0022) per policy, complete MDM enrollment deterministically, and verify it is assigned and managed."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0022"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0022"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0022"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Operations", "job_title": "Ops Coordinator"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_51ba73", "group_ids": ["grp_operations_772e", "grp_operations_all"], "actor": "service_desk", "timestamp": "2025-01-21T09:00:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_m365_e3", "needed_count": 1, "jira_id": "JIRA-lic_m365_e3-emp_0022", "priority": "P2", "created_at": "2025-01-21T09:00:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0022_lic_m365_e3", "account_id": "acc_51ba73", "employee_id": "emp_0022", "license_id": "lic_m365_e3", "assigned_at": "2025-01-21T09:00:00+00:00"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_slack_ent", "needed_count": 1, "jira_id": "JIRA-lic_slack_ent-emp_0022", "priority": "P2", "created_at": "2025-01-21T09:00:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0022_lic_slack_ent", "account_id": "acc_51ba73", "employee_id": "emp_0022", "license_id": "lic_slack_ent", "assigned_at": "2025-01-21T09:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_onb_0022_slack", "employee_id": "emp_0022", "app_id": "app_slack", "status": "active", "created_at": "2025-01-21T09:00:00+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0022"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0022_ast_0013", "employee_id": "emp_0022", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_mdm_emp_0022_ast_0013", "created_at": "2025-01-21T09:00:00+00:00", "completed_at": "2025-01-21T09:00:00+00:00"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0022"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "assigned_to": "emp_0022", "mdm_enrolled": True}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_35",
        instruction=(
            "You must schedule a device return and coordinated MDM wipe for Noel Wright’s assigned phone (employee_id=emp_0030) at the specified due time at=2025-07-25T17:00:00+00:00; do not change ownership until the collection completes."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0030"}),
            Action(name="find_assets", kwargs={"asset_type": "phone", "assigned_to": "emp_0030", "mdm_enrolled": True}),
            Action(name="request_asset_return", kwargs={"asset_id": "ast_0014", "employee_id": "emp_0030", "due_ts": "2025-07-25T17:00:00+00:00", "workflow_id": "wf_ret_ast_0014"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_ret_ast_0014", "employee_id": "emp_0030", "asset_id": "ast_0014", "process": "return", "status": "requested", "pickup_code": "pc_ret_ast_0014", "created_at": "2025-07-25T17:00:00+00:00"}),
            Action(name="schedule_mdm_action", kwargs={"asset_id": "ast_0014", "when": "2025-07-25T17:00:00+00:00", "action": "wipe", "workflow_id": "wf_ret_ast_0014"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_ret_emp_0030_ast_0014", "memo_id": "memo_ret_emp_0030_ast_0014", "employee_ref": "emp_0030", "event": "return", "status": "queued", "created_at": "2025-07-25T17:00:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_ret_emp_0030_ast_0014", "event": "return_scheduled", "timestamp": "2025-07-25T17:00:00+00:00", "actor": "service_desk"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_ret_emp_0030_ast_0014", "event": "wipe_scheduled", "timestamp": "2025-07-25T17:00:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0014"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_36",
        instruction=(
            "You must schedule managed phone returns for Accounting Manager Micah King (employee_id=emp_0029) for both assigned phones with deterministic due times."
            "Create return workflows for each device and schedule MDM wipes at the respective due times; do not change ownership until collection is completed."
            "Use due_ts=2025-07-26T17:00:00+00:00 for ast_0039 and due_ts=2025-07-26T17:30:00+00:00 for ast_0049."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0029"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0029"}),
            Action(name="request_asset_return", kwargs={"asset_id": "ast_0039", "employee_id": "emp_0029", "due_ts": "2025-07-26T17:00:00+00:00", "workflow_id": "wf_ret_emp_0029_ast_0039"}),
            Action(name="schedule_mdm_action", kwargs={"asset_id": "ast_0039", "when": "2025-07-26T17:00:00+00:00", "action": "wipe", "workflow_id": "wf_ret_emp_0029_ast_0039"}),
            Action(name="request_asset_return", kwargs={"asset_id": "ast_0049", "employee_id": "emp_0029", "due_ts": "2025-07-26T17:30:00+00:00", "workflow_id": "wf_ret_emp_0029_ast_0049"}),
            Action(name="schedule_mdm_action", kwargs={"asset_id": "ast_0049", "when": "2025-07-26T17:30:00+00:00", "action": "wipe", "workflow_id": "wf_ret_emp_0029_ast_0049"}),
        ],
        outputs=["ast_0039", "ast_0049"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_37",
        instruction=(
            "You must provision a compliant managed laptop for Support Manager Briar Gonzalez (employee_id=emp_0038) in accordance with onboarding hardware policy. "
            "Ensure RBAC matches the Support/Support Manager baseline with audited changes, baseline licenses are present, the mailbox is active, and the laptop is assigned and MDM‑managed. "
            "Anchor workflow writes to 2025-07-18T13:05:00+00:00 (MDM completion at 13:10) and track the activity deterministically."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Support", "job_title": "Support Manager"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_hw_emp_0038", "memo_id": "memo_hw_emp_0038", "employee_ref": "emp_0038", "event": "hardware_provision", "status": "queued", "created_at": "2025-07-18T13:05:00+00:00"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_839501", "group_ids": ["grp_support_ada3", "grp_support_all"], "actor": "service_desk", "timestamp": "2025-07-18T13:05:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0038"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0038"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_asset_emp_0038_ast_0013", "employee_id": "emp_0038", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_dwf_asset_emp_0038_ast_0013", "created_at": "2025-07-18T13:05:00+00:00", "completed_at": "2025-07-18T13:10:00+00:00"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "assigned_to": "emp_0038", "mdm_enrolled": True}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_hw_emp_0038", "event": "rbac_verified", "timestamp": "2025-07-18T13:05:00+00:00", "actor": "service_desk"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_hw_emp_0038", "event": "licenses_verified", "timestamp": "2025-07-18T13:05:00+00:00", "actor": "service_desk"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_hw_emp_0038", "event": "mdm_completed", "timestamp": "2025-07-18T13:10:00+00:00", "actor": "service_desk"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_hw_emp_0038", "status": "completed", "timestamp": "2025-07-18T13:10:00+00:00", "actor": "service_desk"}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_38",
        instruction=(
            "You must provide an in-stock laptop to Peyton Taylor (employee_id=emp_0014) per policy, complete MDM enrollment deterministically, and verify it is assigned and managed."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0014"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0014"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0014"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0014"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_asset_emp_0014_ast_0013", "employee_id": "emp_0014", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_dwf_asset_emp_0014_ast_0013", "created_at": "2024-10-13T09:00:00+00:00", "completed_at": "2024-10-13T09:00:00+00:00"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_hw_emp_0014", "memo_id": "memo_hw_emp_0014", "employee_ref": "emp_0014", "event": "hardware_provision", "status": "queued", "created_at": "2024-10-13T09:00:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_hw_emp_0014", "status": "completed", "timestamp": "2024-10-13T09:00:00+00:00", "actor": "service_desk"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0014"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "assigned_to": "emp_0014", "mdm_enrolled": True}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_39",
        instruction=(
            "You must issue an in-stock phone to Rowan Lopez (employee_id=emp_0010) per tie-breaker policy, complete MDM enrollment deterministically, and verify the managed assignment."
            "Derive any workflow timestamps from the employee's directory account created_at (2023-11-10T09:00:00+00:00); do not invent other times."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0010"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0010"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0010"}),
            Action(name="find_assets", kwargs={"asset_type": "phone", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0016", "employee_id": "emp_0010"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "dwf_asset_emp_0010_ast_0016", "employee_id": "emp_0010", "asset_id": "ast_0016", "process": "mdm", "status": "completed", "pickup_code": "pc_dwf_asset_emp_0010_ast_0016", "created_at": "2023-11-10T09:00:00+00:00", "completed_at": "2023-11-10T09:00:00+00:00"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0010"}),
            Action(name="find_assets", kwargs={"asset_type": "phone", "assigned_to": "emp_0010"}),
        ],
        outputs=["ast_0016"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_40",
        instruction=(
            "You must issue an in-stock laptop to Jesse Walker (employee_id=emp_0026) per policy, complete MDM enrollment deterministically, and verify the assigned managed state."
            "Derive any workflow timestamps from the employee's directory account created_at (2025-05-15T09:00:00+00:00); do not invent other times."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0026"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0026"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0026"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0026_ast_0013", "employee_id": "emp_0026", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_mdm_emp_0026_ast_0013", "created_at": "2025-05-15T09:00:00+00:00", "completed_at": "2025-05-15T09:00:00+00:00"}),
        ],
        outputs=["ast_0013"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_41",
        instruction=(
            "You are responsible for first‑response on 2025‑07‑16 at 09:00 UTC. You must ensure every Urgent ticket currently in New is being actively worked per policy by advancing New → In Progress."
            "Operate with auditability using deterministic anchors derived from the 09:00 cutoff: record the post‑triage backlog state (snapshot_id=snap_2025_07_16_0900 at 2025-07-16T09:00:00+00:00 for {New, Open, In Progress, On Hold}) and register the health report (run_id=rpt_2025_07_16_0902, started_at=2025-07-16T09:01:00+00:00, completed_at=2025-07-16T09:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf)."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "New", "priority": "Urgent"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5002", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5009", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5011", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5048", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5049", "status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_0900", "taken_at": "2025-07-16T09:00:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_0902", "started_at": "2025-07-16T09:01:00+00:00", "completed_at": "2025-07-16T09:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf"}),
        ],
        outputs=["snap_2025_07_16_0900"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_42",
        instruction=(
            "You are finalizing all tickets currently in Resolved status by closing them using their existing closed_at timestamps."
            "Explicitly close T5022, T5033, T5040, T5041, T5045, T5047, and T5064."
            "Then capture a backlog snapshot using snapshot_id=snap_2025_07_16_1200 and taken_at=2025-07-16T12:00:00+00:00 for statuses {New, Open, In Progress, On Hold}; register the service‑desk health report with run_id=rpt_2025_07_16_1202 (started_at=2025-07-16T12:01:00+00:00, completed_at=2025-07-16T12:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_noon_close.pdf); and append daily metrics for 2025-07-16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "Resolved"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5022", "status": "Closed", "closed_at": "2025-07-11T11:24:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5033", "status": "Closed", "closed_at": "2025-07-11T15:22:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5040", "status": "Closed", "closed_at": "2025-07-09T16:11:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5041", "status": "Closed", "closed_at": "2025-07-10T13:44:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5045", "status": "Closed", "closed_at": "2025-07-07T11:40:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5047", "status": "Closed", "closed_at": "2025-07-11T14:17:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5064", "status": "Closed", "closed_at": "2025-07-10T15:30:00+00:00"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1200", "taken_at": "2025-07-16T12:00:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1202", "started_at": "2025-07-16T12:01:00+00:00", "completed_at": "2025-07-16T12:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_noon_close.pdf"}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["snap_2025_07_16_1200"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_43",
        instruction=(
            "Per escalation policy, you must ensure that all Urgent tickets in On Hold at the 2025-07-16 13:00 UTC cutoff are escalated and have work initiated within five minutes."
            "Operate under policy rather than steps: escalation is evidenced by creating an escalation record tied to the ticket reference and transitioning its handling state to In Progress; document the resulting backlog state for {New, Open, In Progress, On Hold} at 13:05Z and register the standard daily health report in the same window."
            "Use the standard reporting policy parameters deterministically: a 30‑day source window and the canonical output path name 'ServiceDesk_Health_Report_YYYY‑MM‑DD_escalation.pdf' under s3://reports/, anchored to 13:06Z for the run. Anchor identifiers to the 13:05Z/13:06Z window; avoid redundant lookups and do not compute daily aggregates in this run."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "On Hold", "priority": "Urgent"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "SLA-T5017", "issue_type": "SLA Escalation", "summary": "Escalate ticket T5017 (Urgent On Hold)", "priority": "P1", "status": "New", "created_at": "2025-07-16T13:00:00+00:00", "updated_at": "2025-07-16T13:00:00+00:00"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "SLA-T5029", "issue_type": "SLA Escalation", "summary": "Escalate ticket T5029 (Urgent On Hold)", "priority": "P1", "status": "New", "created_at": "2025-07-16T13:00:00+00:00", "updated_at": "2025-07-16T13:00:00+00:00"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "SLA-T5036", "issue_type": "SLA Escalation", "summary": "Escalate ticket T5036 (Urgent On Hold)", "priority": "P1", "status": "New", "created_at": "2025-07-16T13:00:00+00:00", "updated_at": "2025-07-16T13:00:00+00:00"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "SLA-T5058", "issue_type": "SLA Escalation", "summary": "Escalate ticket T5058 (Urgent On Hold)", "priority": "P1", "status": "New", "created_at": "2025-07-16T13:00:00+00:00", "updated_at": "2025-07-16T13:00:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "SLA-T5017", "status": "In Progress", "updated_at": "2025-07-16T13:05:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "SLA-T5029", "status": "In Progress", "updated_at": "2025-07-16T13:05:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "SLA-T5036", "status": "In Progress", "updated_at": "2025-07-16T13:05:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "SLA-T5058", "status": "In Progress", "updated_at": "2025-07-16T13:05:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5017", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5029", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5036", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5058", "status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1305", "taken_at": "2025-07-16T13:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1306", "started_at": "2025-07-16T13:05:30+00:00", "completed_at": "2025-07-16T13:06:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_escalation.pdf"}),
        ],
        outputs=["SLA-T5017", "SLA-T5029", "SLA-T5036", "SLA-T5058"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_44",
        instruction=(
            "Per triage policy, you must ensure that by the 2025-07-16 14:00 UTC cutoff, all High‑priority tickets remaining in New or Open are actively worked (In Progress)."
            "Operate with auditability: record the post‑triage backlog state, produce a health report for governance, and refresh daily metrics for 2025‑07‑16 using deterministic identifiers derived from the cutoff time: snapshot_id=snap_2025_07_16_1400 at 2025-07-16T14:00:00+00:00 and report run_id=rpt_2025_07_16_1406 (started_at=2025-07-16T14:05:30+00:00, completed_at=2025-07-16T14:06:30+00:00, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_triage.pdf)."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "New", "priority": "High"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5014", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5020", "status": "In Progress"}),
            Action(name="find_tickets", kwargs={"status": "Open", "priority": "High"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5035", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5060", "status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1400", "taken_at": "2025-07-16T14:00:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1406", "started_at": "2025-07-16T14:05:30+00:00", "completed_at": "2025-07-16T14:06:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_triage.pdf"}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["snap_2025_07_16_1400"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_45",
        instruction=(
            "Per first‑response policy on 2025‑07‑16, you must ensure that all Urgent tickets currently in New and any New Software tickets are actively being worked (In Progress) by 15:00 UTC."
            "Capture the post‑triage backlog snapshot using snapshot_id=snap_2025_07_16_1500 at 2025-07-16T15:00:00+00:00 over statuses {New, Open, In Progress, On Hold}; register the health report using run_id=rpt_2025_07_16_1502 (started_at=2025-07-16T15:01:00+00:00, completed_at=2025-07-16T15:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf); and recompute daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "New", "priority": "Urgent"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5002", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5009", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5011", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5048", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5049", "status": "In Progress"}),
            Action(name="find_tickets", kwargs={"status": "New", "category": "Software"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5046", "status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1500", "taken_at": "2025-07-16T15:00:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1502", "started_at": "2025-07-16T15:01:00+00:00", "completed_at": "2025-07-16T15:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_first_response.pdf"}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["snap_2025_07_16_1500"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_46",
        instruction=(
            "On 2025-07-16, you must complete incident hygiene for 'Password reset needed' cases by closing applicable tickets that are in progress, using a deterministic closed_at (2025-07-16T16:45:00+00:00)."
            "Operate with governance: register the daily health report with run_id=rpt_2025_07_16_1647 (started_at=2025-07-16T16:46:00+00:00, completed_at=2025-07-16T16:47:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_password_resets.pdf); keep identifiers and timestamps anchored to the same date."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5005", "status": "Resolved"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5006", "status": "Resolved"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5030", "status": "Resolved"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5005", "status": "Closed", "closed_at": "2025-07-16T16:45:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5006", "status": "Closed", "closed_at": "2025-07-16T16:45:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5030", "status": "Closed", "closed_at": "2025-07-16T16:45:00+00:00"}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1647", "started_at": "2025-07-16T16:46:00+00:00", "completed_at": "2025-07-16T16:47:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_password_resets.pdf"}),
        ],
        outputs=["rpt_2025_07_16_1647"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_47",
        instruction=(
            "Per MDM backlog policy on 2025-07-16, you must ensure all MDM tickets in On Hold or Open are actively being worked (In Progress) by the 17:00 UTC cutoff, and preserve an auditable trail with deterministic anchors (snapshot and report identifiers/times)."
            "Do not introduce parameters beyond those explicitly anchored below; avoid unspecified report windows."
            "Use snapshot_id=snap_2025_07_16_1700 at 2025-07-16T17:00:00+00:00 and register the health report with run_id=rpt_2025_07_16_1701 (started_at=2025-07-16T17:00:00+00:00, completed_at=2025-07-16T17:01:00+00:00, source_ticket_window_days=14, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_mdm_1701.pdf)."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "On Hold", "category": "MDM"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5053", "status": "In Progress"}),
            Action(name="find_tickets", kwargs={"status": "Open", "category": "MDM"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5013", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5035", "status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1700", "taken_at": "2025-07-16T17:00:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1701", "started_at": "2025-07-16T17:00:00+00:00", "completed_at": "2025-07-16T17:01:00+00:00", "source_ticket_window_days": 14, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_mdm_1701.pdf"}),
        ],
        outputs=["snap_2025_07_16_1700"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_48",
        instruction=(
            "You are responsible for the daily service‑desk health reporting for 2025-07-16. You must produce the report using run_id=rpt_2025_07_16_1700 (started_at=2025-07-16T17:00:00+00:00, completed_at=2025-07-16T17:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16.pdf)."
            "You must capture a pre‑run backlog snapshot using snapshot_id=snap_2025_07_16_1655 at 2025-07-16T16:55:00+00:00 and a post‑run snapshot using snapshot_id=snap_2025_07_16_1705 at 2025-07-16T17:05:00+00:00 for statuses {New, Open, In Progress, On Hold}, and recompute daily metrics for 2025-07-16."
        ),
        actions=[
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1655", "taken_at": "2025-07-16T16:55:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1700", "started_at": "2025-07-16T17:00:00+00:00", "completed_at": "2025-07-16T17:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1705", "taken_at": "2025-07-16T17:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1700"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_49",
        instruction=(
            "On 2025‑07‑16 you must govern MDM incident handling for Micah King (employee_id=emp_0029) under established incident and reporting policies. "
            "For this date, the policy anchors are: incidents open at 17:10Z and close at 18:00Z (priority High, category MDM); take the backlog snapshot at 17:12Z while incidents are still open (statuses {New, In Progress}); and the daily health report horizon is 18:06–18:07Z with a 30‑day ticket window and the canonical report path. You must derive identifiers and subjects deterministically from stable IDs and refresh daily metrics for the date."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0029"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_incident_mdm_emp_0029_2025_07_16", "event": "mdm_window_applied_open_17_10_close_18_00", "timestamp": "2025-07-16T17:10:00+00:00", "actor": "incident_policy"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0029"}),
            Action(name="create_ticket", kwargs={"ticket_id": "T_mdm_emp_0029_ast_0039", "employee_id": "emp_0029", "category": "MDM", "priority": "High", "status": "New", "subject": "mdm_wipe_ast_0039", "opened_at": "2025-07-16T17:10:00+00:00", "related_asset_id": "ast_0039"}),
            Action(name="create_ticket", kwargs={"ticket_id": "T_mdm_emp_0029_ast_0049", "employee_id": "emp_0029", "category": "MDM", "priority": "High", "status": "New", "subject": "mdm_wipe_ast_0049", "opened_at": "2025-07-16T17:10:00+00:00", "related_asset_id": "ast_0049"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1712", "taken_at": "2025-07-16T17:12:00+00:00", "statuses_in_scope": ["New", "In Progress"]}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T_mdm_emp_0029_ast_0039", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T_mdm_emp_0029_ast_0039", "status": "Resolved"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T_mdm_emp_0029_ast_0039", "status": "Closed", "closed_at": "2025-07-16T18:00:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T_mdm_emp_0029_ast_0049", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T_mdm_emp_0029_ast_0049", "status": "Resolved"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T_mdm_emp_0029_ast_0049", "status": "Closed", "closed_at": "2025-07-16T18:00:00+00:00"}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1807", "started_at": "2025-07-16T18:06:00+00:00", "completed_at": "2025-07-16T18:07:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_mdm_wipes.pdf"}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1807"],
    ),
    Task(
        annotator="it6",
        user_id="it_v6_task_50",
        instruction=(
            "As Per backlog policy, you must ensure that by 2025-07-16 18:30 UTC, Access Request tickets lingering in New or On Hold are actively being worked (In Progress)."
            "Operate with auditability using deterministic anchors derived from the cutoff: take a snapshot at 18:30 (snapshot_id=snap_2025_07_16_1830 for {New, Open, In Progress, On Hold}), register the health report (run_id=rpt_2025_07_16_1832, started_at=2025-07-16T18:31:00+00:00, completed_at=2025-07-16T18:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_access.pdf), and refresh daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"category": "Access Request", "status": "New"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5002", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5059", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5063", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5014", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5020", "status": "In Progress"}),
            Action(name="find_tickets", kwargs={"category": "Access Request", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5021", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5031", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5036", "status": "In Progress"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5058", "status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1830", "taken_at": "2025-07-16T18:30:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1832", "started_at": "2025-07-16T18:31:00+00:00", "completed_at": "2025-07-16T18:32:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_access.pdf"}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1832"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_51",
        instruction=(
            "You must conduct the early‑morning health check on 2025‑07‑16 under standard reporting policy. Anchor all writes to the 07:30Z window and use deterministic identifiers derived from the anchor. "
            "Pre‑run snapshot: snapshot_id=snap_2025_07_16_0725 at 2025-07-16T07:25:00+00:00 for {New, Open, In Progress, On Hold}. "
            "Report run: run_id=rpt_2025_07_16_0732 with started_at=2025-07-16T07:30:00+00:00, completed_at=2025-07-16T07:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_0732.pdf. "
            "Post‑run snapshot: snapshot_id=snap_2025_07_16_0735 at 2025-07-16T07:35:00+00:00 for the same statuses. Record one validation entry referencing the run and both snapshots."
        ),
        actions=[
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_0725", "taken_at": "2025-07-16T07:25:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_0732", "started_at": "2025-07-16T07:30:00+00:00", "completed_at": "2025-07-16T07:32:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_0732.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_0735", "taken_at": "2025-07-16T07:35:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_2025_07_16_0732_morning_check", "entity": "report", "entity_id": "rpt_2025_07_16_0732", "field": "morning_health_check", "rule": "reporting_policy", "details": "pre=snap_2025_07_16_0725; post=snap_2025_07_16_0735", "created_at": "2025-07-16T07:32:00+00:00"}),
        ],
        outputs=["rpt_2025_07_16_0732"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_52",
        instruction=(
            "You must perform a mid‑morning service‑desk review on 2025‑07‑16. You must inspect High priority tickets and items in In Progress, capture snapshots, and produce the health report using run_id=rpt_2025_07_16_1102 (started_at=2025-07-16T11:00:00+00:00, completed_at=2025-07-16T11:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1102.pdf)."
            "You must record pre‑run snapshot_id=snap_2025_07_16_1055 at 2025-07-16T10:55:00+00:00 and post‑run snapshot_id=snap_2025_07_16_1105 at 2025-07-16T11:05:00+00:00 for {New, Open, In Progress, On Hold}, and recompute daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"priority": "High"}),
            Action(name="find_tickets", kwargs={"status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1055", "taken_at": "2025-07-16T10:55:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1102", "started_at": "2025-07-16T11:00:00+00:00", "completed_at": "2025-07-16T11:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1102.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1105", "taken_at": "2025-07-16T11:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1102"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_53",
        instruction=(
            "You must run a category‑focused midday report on 2025‑07‑16. You must inspect Access Request and MDM tickets across New and On Hold, capture snapshots, and produce the health report using run_id=rpt_2025_07_16_1232 (started_at=2025-07-16T12:30:00+00:00, completed_at=2025-07-16T12:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1232.pdf)."
            "You must record pre‑run snapshot_id=snap_2025_07_16_1225 at 2025-07-16T12:25:00+00:00 and post‑run snapshot_id=snap_2025_07_16_1235 at 2025-07-16T12:35:00+00:00 for statuses {New, Open, In Progress, On Hold}, and recompute daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"category": "Access Request", "status": "New"}),
            Action(name="find_tickets", kwargs={"category": "Access Request", "status": "On Hold"}),
            Action(name="find_tickets", kwargs={"category": "MDM", "status": "New"}),
            Action(name="find_tickets", kwargs={"category": "MDM", "status": "On Hold"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1225", "taken_at": "2025-07-16T12:25:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1232", "started_at": "2025-07-16T12:30:00+00:00", "completed_at": "2025-07-16T12:32:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1232.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1235", "taken_at": "2025-07-16T12:35:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1232"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_54",
        instruction=(
            "You must run an afternoon SLA oversight on 2025‑07‑16: review active SLA escalation records (issue_type=SLA Escalation, status=In Progress) and Urgent tickets on On Hold, then produce the health report using run_id=rpt_2025_07_16_1502 (started_at=2025-07-16T15:00:00+00:00, completed_at=2025-07-16T15:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1502.pdf)."
            "Record the backlog state immediately before and after the run with snapshot_id=snap_2025_07_16_1455 (taken_at=2025-07-16T14:55:00+00:00) and snapshot_id=snap_2025_07_16_1505 (taken_at=2025-07-16T15:05:00+00:00) for statuses {New, Open, In Progress, On Hold}. Register a validation entry issue_id=vld_2025_07_16_1502_sla_oversight referencing the run and snapshots, and recompute daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_jira_tickets", kwargs={"issue_type": "SLA Escalation", "status": "In Progress"}),
            Action(name="find_tickets", kwargs={"status": "On Hold", "priority": "Urgent"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1455", "taken_at": "2025-07-16T14:55:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1502", "started_at": "2025-07-16T15:00:00+00:00", "completed_at": "2025-07-16T15:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1502.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1505", "taken_at": "2025-07-16T15:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_2025_07_16_1502_sla_oversight", "entity": "report", "entity_id": "rpt_2025_07_16_1502", "field": "sla_oversight", "rule": "reporting_policy", "details": "pre=snap_2025_07_16_1455; post=snap_2025_07_16_1505", "created_at": "2025-07-16T15:02:00+00:00"}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1502"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_55",
        instruction=(
            "You must run a priority‑focused afternoon review on 2025‑07‑16. You must inspect High and Urgent tickets, capture snapshots, and produce the health report using run_id=rpt_2025_07_16_1602 (started_at=2025-07-16T16:00:00+00:00, completed_at=2025-07-16T16:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1602.pdf)."
            "You must record pre/post snapshots (snap_2025_07_16_1555 at 2025-07-16T15:55:00+00:00 and snap_2025_07_16_1605 at 2025-07-16T16:05:00+00:00 for statuses {New, Open, In Progress, On Hold})."
            "To ensure date‑bounded metrics, you must log two deterministic review markers at 16:00Z attributed to the review owner (employee_id=emp_0023, the Service Desk Analyst), both in category 'Service Desk'. Derive ticket_ids as T2025_07_16_1600_high and T2025_07_16_1600_urgent, and derive subjects from the run_id as rpt_2025_07_16_1602_high and rpt_2025_07_16_1602_urgent; close only the High marker at 16:02Z. Then recompute daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"priority": "Urgent"}),
            Action(name="find_tickets", kwargs={"priority": "High"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1555", "taken_at": "2025-07-16T15:55:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="create_ticket", kwargs={"ticket_id": "T2025_07_16_1600_high", "employee_id": "emp_0023", "category": "Service Desk", "priority": "High", "status": "New", "subject": "rpt_2025_07_16_1602_high", "opened_at": "2025-07-16T16:00:00+00:00"}),
            Action(name="create_ticket", kwargs={"ticket_id": "T2025_07_16_1600_urgent", "employee_id": "emp_0023", "category": "Service Desk", "priority": "Urgent", "status": "New", "subject": "rpt_2025_07_16_1602_urgent", "opened_at": "2025-07-16T16:00:00+00:00"}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1602", "started_at": "2025-07-16T16:00:00+00:00", "completed_at": "2025-07-16T16:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1602.pdf"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T2025_07_16_1600_high", "status": "Closed", "closed_at": "2025-07-16T16:02:00+00:00"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1605", "taken_at": "2025-07-16T16:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1602"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_56",
        instruction=(
            "Per reporting policy, you must produce a category audit slice on 2025‑07‑16 that reviews Software and Account tickets across New and In Progress states. Use run_id=rpt_2025_07_16_1632 (started_at=2025-07-16T16:30:00+00:00, completed_at=2025-07-16T16:32:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1632.pdf), and record the backlog state immediately before and after the run with snapshot_id=snap_2025_07_16_1625 (16:25 UTC) and snapshot_id=snap_2025_07_16_1635 (16:35 UTC) for statuses {New, Open, In Progress, On Hold}."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"category": "Software", "status": "New"}),
            Action(name="find_tickets", kwargs={"category": "Software", "status": "In Progress"}),
            Action(name="find_tickets", kwargs={"category": "Account", "status": "In Progress"}),
            Action(name="find_tickets", kwargs={"category": "Account", "status": "New"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1625", "taken_at": "2025-07-16T16:25:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1632", "started_at": "2025-07-16T16:30:00+00:00", "completed_at": "2025-07-16T16:32:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1632.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1635", "taken_at": "2025-07-16T16:35:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
        ],
        outputs=["rpt_2025_07_16_1632"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_57",
        instruction=(
            "You have to Run an On Hold queue focus on 2025‑07‑16 under reporting policy: examine On Hold tickets across categories, preserve a pre/post view, and produce the daily health report using deterministic anchors."
            "Use run_id=rpt_2025_07_16_1702 (started_at=2025-07-16T17:00:00+00:00, completed_at=2025-07-16T17:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1702.pdf) and snapshots snap_2025_07_16_1655 (16:55) and snap_2025_07_16_1705 (17:05) over {New, Open, In Progress, On Hold}."
            "Register one validation entry that references the report and both snapshots after the post snapshot is captured, with created_at equal to the post snapshot taken_at (2025-07-16T17:05:00+00:00); recompute daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "On Hold"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1655", "taken_at": "2025-07-16T16:55:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1702", "started_at": "2025-07-16T17:00:00+00:00", "completed_at": "2025-07-16T17:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1702.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1705", "taken_at": "2025-07-16T17:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_2025_07_16_1702_on_hold_focus", "entity": "report", "entity_id": "rpt_2025_07_16_1702", "field": "on_hold_focus", "rule": "reporting_policy", "details": "pre=snap_2025_07_16_1655; post=snap_2025_07_16_1705", "created_at": "2025-07-16T17:05:00+00:00"}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1702"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_58",
        instruction=(
            "You must run an evening New‑ticket focus on 2025‑07‑16. You must inspect New tickets by category (Software, Account), capture snapshots, and produce the health report using run_id=rpt_2025_07_16_1802 (started_at=2025-07-16T18:00:00+00:00, completed_at=2025-07-16T18:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1802.pdf)."
            "You must save pre/post snapshots (snap_2025_07_16_1755 at 2025-07-16T17:55:00+00:00 and snap_2025_07_16_1805 at 2025-07-16T18:05:00+00:00 for statuses {New, Open, In Progress, On Hold}) and recompute daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "New", "category": "Software"}),
            Action(name="find_tickets", kwargs={"status": "New", "category": "Account"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1755", "taken_at": "2025-07-16T17:55:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1802", "started_at": "2025-07-16T18:00:00+00:00", "completed_at": "2025-07-16T18:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1802.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1805", "taken_at": "2025-07-16T18:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1802"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_59",
        instruction=(
            "You must run a late‑evening hold/priority sweep on 2025‑07‑16. You must inspect On Hold and Urgent tickets, capture snapshots, and produce the health report using run_id=rpt_2025_07_16_1902 (started_at=2025-07-16T19:00:00+00:00, completed_at=2025-07-16T19:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1902.pdf)."
            "You must record snapshots (snap_2025_07_16_1855 at 2025-07-16T18:55:00+00:00 and snap_2025_07_16_1905 at 2025-07-16T19:05:00+00:00 for statuses {New, Open, In Progress, On Hold}) and recompute daily metrics for 2025‑07‑16."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "On Hold"}),
            Action(name="find_tickets", kwargs={"priority": "Urgent"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1855", "taken_at": "2025-07-16T18:55:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1902", "started_at": "2025-07-16T19:00:00+00:00", "completed_at": "2025-07-16T19:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1902.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1905", "taken_at": "2025-07-16T19:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="recompute_daily_metrics", kwargs={"date": "2025-07-16"}),
        ],
        outputs=["rpt_2025_07_16_1902"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_60",
        instruction=(
            "Per end‑of‑day reporting policy for 2025‑07‑16, you must review Open and In Progress queues, record the backlog state immediately before and after the run, and produce the final service‑desk health report."
            "Use run_id=rpt_2025_07_16_2002 (started_at=2025-07-16T20:00:00+00:00, completed_at=2025-07-16T20:02:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_2002.pdf), and capture snapshots with snapshot_id=snap_2025_07_16_1955 (19:55 UTC) and snapshot_id=snap_2025_07_16_2005 (20:05 UTC) for statuses {New, Open, In Progress, On Hold}."
        ),
        actions=[
            Action(name="find_tickets", kwargs={"status": "Open"}),
            Action(name="find_tickets", kwargs={"status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1955", "taken_at": "2025-07-16T19:55:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_2002", "started_at": "2025-07-16T20:00:00+00:00", "completed_at": "2025-07-16T20:02:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_2002.pdf"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_2005", "taken_at": "2025-07-16T20:05:00+00:00", "statuses_in_scope": ["New", "Open", "In Progress", "On Hold"]}),
        ],
        outputs=["rpt_2025_07_16_2002"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_61",
        instruction=(
            "Per RBAC review policy dated 2025-07-16, you must ensure Marketing accounts reflect baseline group membership for their roles."
            "You must review River Scott (employee_id=emp_0031, job_title=Content Strategist) and Skyler Sanchez (employee_id=emp_0021, job_title=Design Lead), align their directory accounts to the Marketing baselines derived from the role map, and ensure the alignment is auditable. Use actor rbac_audit and fixed anchors 2025-07-16T10:00:00+00:00 (emp_0031) and 2025-07-16T10:01:00+00:00 (emp_0021). Do not modify licenses, devices, or mailboxes."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0031"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_351bb4", "group_ids": ["grp_marketing_719b", "grp_marketing_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Design Lead"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_43980f", "group_ids": ["grp_marketing_c05f", "grp_marketing_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:01:00+00:00"}),
        ],
        outputs=["acc_351bb4", "acc_43980f"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_62",
        instruction=(
            "Per RBAC review policy dated 2025-07-16, you must ensure HR accounts reflect baseline group membership for their roles."
            "You must review Avery Lee (employee_id=emp_0001, job_title=HRBP) and Peyton Taylor (employee_id=emp_0014, job_title=HR Generalist), align their directory accounts to HR baselines, and register the remediation."
            "Use deterministic audit anchors on 2025-07-16: apply group alignment for emp_0001 at 10:05:00Z and for emp_0014 at 10:06:00Z by actor rbac_audit; then record validation entries with IDs vld_acc_dc71c8_2025_07_16_1007 at 10:07:00Z and vld_acc_88c4f4_2025_07_16_1007 at 10:07:30Z capturing the exact groups after alignment."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_baseline_for_role", kwargs={"department": "HR", "job_title": "HRBP"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_dc71c8", "group_ids": ["grp_hr_82f8", "grp_hr_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:05:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0014"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0014"}),
            Action(name="get_baseline_for_role", kwargs={"department": "HR", "job_title": "HR Generalist"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_88c4f4", "group_ids": ["grp_hr_a74e", "grp_hr_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:06:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_dc71c8_2025_07_16_1007", "entity": "directory_accounts", "entity_id": "acc_dc71c8", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_hr_82f8','grp_hr_all']", "created_at": "2025-07-16T10:07:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_88c4f4_2025_07_16_1007", "entity": "directory_accounts", "entity_id": "acc_88c4f4", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_hr_a74e','grp_hr_all']", "created_at": "2025-07-16T10:07:30+00:00"}),
        ],
        outputs=["vld_acc_dc71c8_2025_07_16_1007", "vld_acc_88c4f4_2025_07_16_1007"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_63",
        instruction=(
            "Per RBAC review policy dated 2025-07-16, you must ensure Support accounts reflect baseline access and posture, not just groups."
            "Review Jesse Walker (employee_id=emp_0026) and Briar Gonzalez (employee_id=emp_0038), align groups to the Support/Support Manager baseline at fixed anchors (10:10Z and 10:11Z, actor rbac_audit), and verify baseline posture across license bundle and mailbox retention."
            "Document the verified posture deterministically using validation records derived from account_id and the anchor time; do not open escalation tickets unless drift is detected."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0026"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0026"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Support", "job_title": "Support Manager"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_bac647", "group_ids": ["grp_support_ada3", "grp_support_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:10:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_bac647"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0026"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_bac647_2025_07_16_1010_posture", "entity": "directory_accounts", "entity_id": "acc_bac647", "field": "posture", "rule": "support_baseline_verified", "details": "licenses=['lic_slack_ent','lic_m365_e3']; mailbox_retention=std_2y", "created_at": "2025-07-16T10:10:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Support", "job_title": "Support Manager"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_839501", "group_ids": ["grp_support_ada3", "grp_support_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:11:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_839501"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0038"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_839501_2025_07_16_1011_posture", "entity": "directory_accounts", "entity_id": "acc_839501", "field": "posture", "rule": "support_baseline_verified", "details": "licenses=['lic_slack_ent','lic_m365_e3']; mailbox_retention=std_2y", "created_at": "2025-07-16T10:11:00+00:00"}),
        ],
        outputs=["acc_bac647", "acc_839501", "vld_acc_bac647_2025_07_16_1010_posture", "vld_acc_839501_2025_07_16_1011_posture"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_64",
        instruction=(
            "Per RBAC review policy dated 2025-07-16, you must ensure Engineering accounts reflect baseline group membership for their roles."
            "You must review Noel Wright (employee_id=emp_0030, DevOps Engineer) and Evan Carter (employee_id=emp_0040, Software Engineer), align their directory accounts to Engineering baselines, and ensure the alignment is auditable. Use actor rbac_audit with fixed audit timestamps 2025-07-16T10:15:00+00:00 (for emp_0030) and 2025-07-16T10:16:00+00:00 (for emp_0040). Also verify that each account holds the default license bundle for Engineering (lic_m365_e3, lic_github_ent, lic_slack_ent) and that their mailboxes have standard retention (std_2y). For auditability, record validation entries vld_acc_db017d_2025_07_16_1015 and vld_acc_54337a_2025_07_16_1016 at 10:15:30 and 10:16:30 respectively, reflecting the aligned group_ids."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Engineering", "job_title": "DevOps Engineer"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_db017d"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0030"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_db017d", "group_ids": ["grp_engineering_4162", "grp_engineering_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:15:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_db017d_2025_07_16_1015", "entity": "directory_accounts", "entity_id": "acc_db017d", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_engineering_4162','grp_engineering_all']", "created_at": "2025-07-16T10:15:30+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_54337a"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0040"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_54337a", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:16:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_54337a_2025_07_16_1016", "entity": "directory_accounts", "entity_id": "acc_54337a", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_engineering_cbaf','grp_engineering_all']", "created_at": "2025-07-16T10:16:30+00:00"}),
        ],
        outputs=["acc_db017d", "acc_54337a", "vld_acc_db017d_2025_07_16_1015", "vld_acc_54337a_2025_07_16_1016"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_65",
        instruction=(
            "Per RBAC review policy dated 2025-07-16, you must ensure Finance accounts reflect baseline group membership for their roles."
            "Review Blake Martin (employee_id=emp_0017, Controller) and Micah King (employee_id=emp_0029, Accounting Manager); align their directory accounts to Finance baselines and register the remediation using actor rbac_audit."
            "Anchor audit timestamps at 2025-07-16T10:20:00+00:00 (emp_0017) and 2025-07-16T10:21:00+00:00 (emp_0029). Verify Finance license posture and mailbox retention for both accounts."
            "For auditability, write validation records that reflect the aligned group_ids, deriving deterministic identifiers from the account_id and the corresponding anchor time (without inventing any uncontrolled values)."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0017"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0017"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Finance", "job_title": "Controller"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_82aecf"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0017"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_82aecf", "group_ids": ["grp_finance_c147", "grp_finance_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:20:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_82aecf_2025_07_16_1020", "entity": "directory_accounts", "entity_id": "acc_82aecf", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_finance_c147','grp_finance_all']", "created_at": "2025-07-16T10:20:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Finance", "job_title": "Accounting Manager"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_48efe8"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0029"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_48efe8", "group_ids": ["grp_finance_5d50", "grp_finance_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:21:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_48efe8_2025_07_16_1021", "entity": "directory_accounts", "entity_id": "acc_48efe8", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_finance_5d50','grp_finance_all']", "created_at": "2025-07-16T10:21:00+00:00"}),
        ],
        outputs=["acc_82aecf", "acc_48efe8", "vld_acc_82aecf_2025_07_16_1020", "vld_acc_48efe8_2025_07_16_1021"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_66",
        instruction=(
            "Per RBAC review policy dated 2025-07-16, you must ensure Operations accounts reflect baseline group membership for their roles."
            "You must review Rowan Lopez (employee_id=emp_0010, Ops Coordinator) and Hayden Moore (employee_id=emp_0015, Supply Chain Analyst), align their directory accounts to Operations baselines, and ensure the alignment is auditable. Use actor rbac_audit and the fixed audit timestamps 2025-07-16T10:25:00+00:00 (for emp_0010) and 2025-07-16T10:26:00+00:00 (for emp_0015)."
            "Also verify license posture via license-assignments and mailbox retention for both accounts. For auditability, record validation entries vld_acc_4d16c0_2025_07_16_1025 and vld_acc_3818d8_2025_07_16_1026 at 10:25:30 and 10:26:30 respectively, reflecting the aligned group_ids."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0010"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0010"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Operations", "job_title": "Ops Coordinator"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_4d16c0"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0010"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_4d16c0", "group_ids": ["grp_operations_772e", "grp_operations_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:25:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_4d16c0_2025_07_16_1025", "entity": "directory_accounts", "entity_id": "acc_4d16c0", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_operations_772e','grp_operations_all']", "created_at": "2025-07-16T10:25:30+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0015"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0015"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Operations", "job_title": "Supply Chain Analyst"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_3818d8"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0015"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_3818d8", "group_ids": ["grp_operations_dcb3", "grp_operations_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:26:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_3818d8_2025_07_16_1026", "entity": "directory_accounts", "entity_id": "acc_3818d8", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_operations_dcb3','grp_operations_all']", "created_at": "2025-07-16T10:26:30+00:00"}),
        ],
        outputs=["acc_4d16c0", "acc_3818d8", "vld_acc_4d16c0_2025_07_16_1025", "vld_acc_3818d8_2025_07_16_1026"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_67",
        instruction=(
            "Per RBAC review policy dated 2025-07-16, you must ensure IT accounts reflect the baseline access posture for their roles."
            "You must review Morgan Nguyen (employee_id=emp_0004, Systems Engineer) and Devin Ramirez (employee_id=emp_0023, Service Desk Analyst). You must align directory groups to the IT baselines using actor rbac_audit at fixed anchors within the 10:30Z window to remove ambiguity: assign the earlier audit to the lower employee_id at 2025-07-16T10:30:00+00:00 and the later audit at 2025-07-16T10:31:00+00:00."
            "You must verify each account holds its baseline license bundle and standard mailbox retention; when posture is already satisfied, you must emit an auditable no‑change group write. You must record validation entries with created_at=audit+30s and issue_id format vld_acc_<account_id>_YYYY_MM_DD_HHMM to make outputs unique and reproducible."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0004"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0004"}),
            Action(name="get_baseline_for_role", kwargs={"department": "IT", "job_title": "Systems Engineer"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_38d007"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_github_ent"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0004"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_38d007", "group_ids": ["grp_it_6b89", "grp_it_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:30:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_38d007_2025_07_16_1030", "entity": "directory_accounts", "entity_id": "acc_38d007", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_it_6b89','grp_it_all']; licenses=['lic_m365_e3','lic_github_ent','lic_slack_ent']; mailbox_retention=std_2y", "created_at": "2025-07-16T10:30:30+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0023"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0023"}),
            Action(name="get_baseline_for_role", kwargs={"department": "IT", "job_title": "Service Desk Analyst"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_696506"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_github_ent"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0023"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_696506", "group_ids": ["grp_it_2990", "grp_it_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:31:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_696506_2025_07_16_1031", "entity": "directory_accounts", "entity_id": "acc_696506", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_it_2990','grp_it_all']; licenses=['lic_m365_e3','lic_github_ent','lic_slack_ent']; mailbox_retention=std_2y", "created_at": "2025-07-16T10:31:30+00:00"}),
        ],
        outputs=["acc_38d007", "acc_696506", "vld_acc_38d007_2025_07_16_1030", "vld_acc_696506_2025_07_16_1031"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_68",
        instruction=(
            "Per RBAC review policy dated 2025-07-16, you must ensure Sales accounts reflect baseline group membership for their roles."
            "You must review Emerson Thomas (employee_id=emp_0013, Sales Manager) and Lane Allen (employee_id=emp_0028, Sales Manager), align their directory accounts to Sales baselines, and ensure the alignment is auditable. Use actor rbac_audit with fixed audit timestamps 2025-07-16T10:35:00+00:00 (for emp_0013) and 2025-07-16T10:36:00+00:00 (for emp_0028). Also verify that each account holds the default Sales license bundle (lic_m365_e3, lic_salesforce, lic_slack_ent), that their mailboxes use standard retention (std_2y), and that their assigned assets are recorded."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Sales", "job_title": "Sales Manager"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_78fb5c"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0013"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0013"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_78fb5c", "group_ids": ["grp_sales_4bcb", "grp_sales_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:35:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Sales", "job_title": "Sales Manager"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_81d8d5"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0028"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0028"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_81d8d5", "group_ids": ["grp_sales_4bcb", "grp_sales_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:36:00+00:00"}),
        ],
        outputs=["acc_78fb5c", "acc_81d8d5"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_69",
        instruction=(
            "Per RBAC remediation on 2025-07-16, you must reassert Marketing baselines to prevent drift."
            "You must review Jordan Garcia (employee_id=emp_0002, Content Strategist) and Wyatt Hill (employee_id=emp_0034, Content Strategist), reapply baselines, and ensure alignment is auditable. Use actor rbac_audit and fixed audit timestamps 2025-07-16T10:40:00+00:00 (for emp_0002) and 2025-07-16T10:41:00+00:00 (for emp_0034). If you detect any non-baseline license entitlements for emp_0002, revoke them with revoked_at=2025-07-16T10:41:30+00:00."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0002"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0002"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_287fb8"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_287fb8", "group_ids": ["grp_marketing_719b", "grp_marketing_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:40:00+00:00"}),
            Action(name="revoke_license", kwargs={"account_id": "acc_287fb8", "employee_id": "emp_0002", "license_id": "lic_adobe_cc", "revoked_at": "2025-07-16T10:41:30+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0034"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0034"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_baacc3"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_baacc3", "group_ids": ["grp_marketing_719b", "grp_marketing_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:41:00+00:00"}),
        ],
        outputs=["acc_287fb8", "acc_baacc3"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_70",
        instruction=(
            "Per RBAC remediation on 2025-07-16, you must align Finance and Engineering accounts that show historical changes."
            "Review Tatum Ng (employee_id=emp_0033, Financial Analyst) and Nico Adams (employee_id=emp_0036, DevOps Engineer). Apply group alignment using actor rbac_audit at deterministic anchors 2025-07-16T10:45:00+00:00 (Finance) and 2025-07-16T10:46:00+00:00 (Engineering)."
            "Follow offboarding policy: if a directory account is disabled, you do not assign or expand licenses. Instead, you document the posture with a validation record that is derived from the account_id and the Finance anchor, explaining that licensing was skipped due to disabled status and confirming mailbox retention. For enabled accounts, you may reassert baseline groups as a no-change write to produce auditable alignment."
            "Document posture validations within the anchor minute using deterministic identifiers derived from account_id and the anchor time to keep outputs reproducible without prescribing internal steps."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0033"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0033"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_f589dc"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0033"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_f589dc_2025_07_16_1045_skip_licensing", "entity": "directory_accounts", "entity_id": "acc_f589dc", "field": "license_provisioning", "rule": "skip_for_disabled_account", "details": "licensing skipped due to directory.status='disabled'; mailbox retention verified", "created_at": "2025-07-16T10:45:30+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0036"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0036"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Engineering", "job_title": "DevOps Engineer"}),
            Action(name="get_license_assignments", kwargs={"account_id": "acc_f9a6bc"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_f9a6bc", "group_ids": ["grp_engineering_4162", "grp_engineering_all"], "actor": "rbac_audit", "timestamp": "2025-07-16T10:46:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_acc_f9a6bc_2025_07_16_1046", "entity": "directory_accounts", "entity_id": "acc_f9a6bc", "field": "group_ids", "rule": "rbac_baseline_alignment", "details": "groups=['grp_engineering_4162','grp_engineering_all']", "created_at": "2025-07-16T10:46:30+00:00"}),
        ],
        outputs=["acc_f589dc", "acc_f9a6bc"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_71",
        instruction=(
            "On 2025-07-16 you must coordinate an email service incident under incident‑management policy. "
            "You must maintain a single P1 incident of record anchored deterministically at 11:00Z, transition handling status promptly per policy, place affected ticket T5027 On Hold, "
            "record lifecycle with event=incident reflecting a blocked state during the incident, and register the standard service desk health report deterministically. "
            "Derive report times from the anchor: started_at=anchor and completed_at=anchor+30s; source_ticket_window_days=30 and derive run_id from started_at as rpt_YYYY_MM_DD_HHMMSS and output_path_pdf as s3://reports/ServiceDesk_Health_Report_{anchor_date}_{category}.pdf. "
            "Derive follow‑up handling timestamps as anchor+60s and use actor incident_coordinator for lifecycle handling. "
            "You must derive all other identifiers and timestamps deterministically from the 11:00Z anchor and the incident category (email) and memo_id memo_inc_email_2025_07_16; do not hard‑code database values."
        ),
        actions=[
            Action(name="create_jira_ticket", kwargs={"jira_id": "JIRA-incident-email-2025_07_16_1100", "issue_type": "Incident", "summary": "incident=email;ticket=T5027;anchor=2025-07-16T11:00:00+00:00", "priority": "P1", "status": "New", "created_at": "2025-07-16T11:00:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "JIRA-incident-email-2025_07_16_1100", "status": "In Progress", "updated_at": "2025-07-16T11:01:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5027", "status": "On Hold"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_email_2025_07_16_1100", "memo_id": "memo_inc_email_2025_07_16", "employee_ref": "incident_email", "event": "incident", "status": "in_progress", "created_at": "2025-07-16T11:00:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_email_2025_07_16_1100", "status": "blocked", "timestamp": "2025-07-16T11:01:00+00:00", "actor": "incident_coordinator"}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_110000", "started_at": "2025-07-16T11:00:00+00:00", "completed_at": "2025-07-16T11:00:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025_07_16_email.pdf"}),
        ],
        outputs=["JIRA-incident-email-2025_07_16_1100", "lcq_inc_email_2025_07_16_1100"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_72",
        instruction=(
            "You have to Coordinate a network degradation per incident-management policy with one incident of record and deterministic anchors."
            "Use: incident id=ITSD-1014 (summary=network_degradation_t5028, priority=P2), lifecycle id=lcq_inc_0002 (actor=incident_mgr, memo_id=memo_inc_0002, employee_ref=global_incident_network), backlog snapshot snap_2025_07_16_1107 over {On Hold, In Progress, New}, and health report run rpt_2025_07_16_1108 (window=30 days, output path s3://reports/ServiceDesk_Health_Report_2025-07-16_1108.pdf)."
            "Deterministic times: incident created_at=2025-07-16T11:05:00+00:00 and In Progress at 11:06:00; lifecycle created_at=2025-07-16T11:05:00+00:00 and blocked at 11:06:00; snapshot taken_at=2025-07-16T11:07:00+00:00; report started_at=11:08:00 and completed_at=11:08:30. Do not alter any service-desk ticket statuses. If the incident is missing, create ITSD-1014 and set it to In Progress at 11:06:00."
        ),
        actions=[
            Action(name="find_jira_tickets", kwargs={"issue_type": "Incident", "summary": "network_degradation_t5028", "priority": "P2"}),
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1014", "issue_type": "Incident", "summary": "network_degradation_t5028", "priority": "P2", "status": "New", "created_at": "2025-07-16T11:05:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1014", "status": "In Progress", "updated_at": "2025-07-16T11:06:00+00:00"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0002", "memo_id": "memo_inc_0002", "employee_ref": "global_incident_network", "event": "incident", "status": "created", "created_at": "2025-07-16T11:05:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0002", "status": "blocked", "timestamp": "2025-07-16T11:06:00+00:00", "actor": "incident_mgr"}),
            Action(name="find_tickets", kwargs={"status": "On Hold"}),
            Action(name="find_tickets", kwargs={"status": "In Progress"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1107", "taken_at": "2025-07-16T11:07:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1108", "started_at": "2025-07-16T11:08:00+00:00", "completed_at": "2025-07-16T11:08:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1108.pdf"}),
        ],
        outputs=["ITSD-1014", "lcq_inc_0002"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_73",
        instruction=(
            "On 2025-07-16 you must coordinate an MDM service disruption consistent with incident-management policy."
            "Use these deterministic values for a single incident of record and an auditable trail: incident id=ITSD-1015 with summary=mdm_service_disruption_t5013_t5053 and priority=P2 (created 2025-07-16T11:10:00+00:00, then In Progress 2025-07-16T11:11:00+00:00); lifecycle id=lcq_inc_0003 (created with event=incident and status=in_progress at 2025-07-16T11:10:00+00:00, then status=blocked at 2025-07-16T11:11:00+00:00 by actor incident_mgr, memo_id=memo_inc_0003, employee_ref=global_incident_mdm); snapshot id=snap_2025_07_16_1112 taken 2025-07-16T11:12:00+00:00 over {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1113 with started_at=2025-07-16T11:13:00+00:00, completed_at=2025-07-16T11:13:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1113.pdf. Apply the incident to impacted tickets T5013 and T5053 by placing them On Hold."
        ),
        actions=[
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1015", "issue_type": "Incident", "summary": "mdm_service_disruption_t5013_t5053", "priority": "P2", "status": "New", "created_at": "2025-07-16T11:10:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1015", "status": "In Progress", "updated_at": "2025-07-16T11:11:00+00:00"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0003", "memo_id": "memo_inc_0003", "employee_ref": "global_incident_mdm", "event": "incident", "status": "in_progress", "created_at": "2025-07-16T11:10:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0003", "status": "blocked", "timestamp": "2025-07-16T11:11:00+00:00", "actor": "incident_mgr"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1112", "taken_at": "2025-07-16T11:12:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1113", "started_at": "2025-07-16T11:13:00+00:00", "completed_at": "2025-07-16T11:13:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1113.pdf"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5013", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5053", "status": "On Hold"}),
        ],
        outputs=["ITSD-1015", "lcq_inc_0003"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_74",
        instruction=(
            "On 2025-07-16 you must coordinate an access provisioning outage consistent with incident-management policy."
            "Use deterministic values to preserve a single incident of record and an auditable trail: incident id=ITSD-1016 with summary=access_provisioning_outage_t5017_t5036 and priority=P1 (created 2025-07-16T11:15:00+00:00, then In Progress 2025-07-16T11:16:00+00:00); lifecycle id=lcq_inc_0004 (created with event=incident and status=created at 2025-07-16T11:15:00+00:00, then status=blocked at 2025-07-16T11:16:00+00:00 by actor incident_mgr, memo_id=memo_inc_0004, employee_ref=global_incident_access); snapshot id=snap_2025_07_16_1117 taken 2025-07-16T11:17:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1118 with started_at=2025-07-16T11:18:00+00:00, completed_at=2025-07-16T11:18:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1118.pdf. Apply the incident to tickets T5036 (Access Request) and T5017 (Account) by placing them On Hold."
        ),
        actions=[
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1016", "issue_type": "Incident", "summary": "access_provisioning_outage_t5017_t5036", "priority": "P1", "status": "New", "created_at": "2025-07-16T11:15:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1016", "status": "In Progress", "updated_at": "2025-07-16T11:16:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5017", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5036", "status": "On Hold"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0004", "memo_id": "memo_inc_0004", "employee_ref": "global_incident_access", "event": "incident", "status": "created", "created_at": "2025-07-16T11:15:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0004", "status": "blocked", "timestamp": "2025-07-16T11:16:00+00:00", "actor": "incident_mgr"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1117", "taken_at": "2025-07-16T11:17:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1118", "started_at": "2025-07-16T11:18:00+00:00", "completed_at": "2025-07-16T11:18:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1118.pdf"}),
        ],
        outputs=["ITSD-1016", "lcq_inc_0004"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_75",
        instruction=(
            "On 2025-07-16 you must coordinate a software distribution issue in accordance with incident-management policy."
            "Use these deterministic values to keep a single incident of record and an auditable trail: incident id=ITSD-1017 with summary=software_distribution_issue_t5005_t5030 and priority=P2 (created 2025-07-16T11:20:00+00:00, then In Progress 2025-07-16T11:21:00+00:00); lifecycle id=lcq_inc_0005 (created with event=incident and status=in_progress at 2025-07-16T11:20:00+00:00, then status=blocked at 2025-07-16T11:21:00+00:00 by actor incident_mgr, memo_id=memo_inc_0005, employee_ref=global_incident_software); snapshot id=snap_2025_07_16_1122 taken 2025-07-16T11:22:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1123 with started_at=2025-07-16T11:23:00+00:00, completed_at=2025-07-16T11:23:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1123.pdf. Apply the incident to impacted tickets T5005 and T5030 by placing them On Hold."
        ),
        actions=[
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1017", "issue_type": "Incident", "summary": "software_distribution_issue_t5005_t5030", "priority": "P2", "status": "New", "created_at": "2025-07-16T11:20:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1017", "status": "In Progress", "updated_at": "2025-07-16T11:21:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5005", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5030", "status": "On Hold"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0005", "memo_id": "memo_inc_0005", "employee_ref": "global_incident_software", "event": "incident", "status": "in_progress", "created_at": "2025-07-16T11:20:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0005", "status": "blocked", "timestamp": "2025-07-16T11:21:00+00:00", "actor": "incident_mgr"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1122", "taken_at": "2025-07-16T11:22:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1123", "started_at": "2025-07-16T11:23:00+00:00", "completed_at": "2025-07-16T11:23:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1123.pdf"}),
        ],
        outputs=["ITSD-1017", "lcq_inc_0005"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_76",
        instruction=(
            "On 2025-07-16 you must coordinate a directory synchronization incident consistent with incident-management policy."
            "Use deterministic values: incident id=ITSD-1018 with summary=directory_sync_incident_t5009_t5010 and priority=P1 (created 2025-07-16T11:25:00+00:00, then In Progress 2025-07-16T11:26:00+00:00); lifecycle id=lcq_inc_0006 (created with event=incident and status=in_progress at 2025-07-16T11:25:00+00:00, then status=blocked at 2025-07-16T11:26:00+00:00 by actor incident_mgr, memo_id=memo_inc_0006, employee_ref=global_incident_directory); snapshot id=snap_2025_07_16_1127 taken 2025-07-16T11:27:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1128 with started_at=2025-07-16T11:28:00+00:00, completed_at=2025-07-16T11:28:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1128.pdf. Apply the incident to tickets T5009 and T5010 by placing them On Hold."
        ),
        actions=[
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1018", "issue_type": "Incident", "summary": "directory_sync_incident_t5009_t5010", "priority": "P1", "status": "New", "created_at": "2025-07-16T11:25:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1018", "status": "In Progress", "updated_at": "2025-07-16T11:26:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5009", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5010", "status": "On Hold"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0006", "memo_id": "memo_inc_0006", "employee_ref": "global_incident_directory", "event": "incident", "status": "in_progress", "created_at": "2025-07-16T11:25:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0006", "status": "blocked", "timestamp": "2025-07-16T11:26:00+00:00", "actor": "incident_mgr"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1127", "taken_at": "2025-07-16T11:27:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1128", "started_at": "2025-07-16T11:28:00+00:00", "completed_at": "2025-07-16T11:28:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1128.pdf"}),
        ],
        outputs=["ITSD-1018", "lcq_inc_0006"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_77",
        instruction=(
            "On 2025-07-16 you must coordinate a hardware vendor outage affecting device issues."
            "Use deterministic values to keep a single incident of record with an auditable trail: incident id=ITSD-1019 with summary=hardware_vendor_outage_t5037_t5048 and priority=P2 (created 2025-07-16T11:30:00+00:00, then In Progress 2025-07-16T11:31:00+00:00); lifecycle id=lcq_inc_0007 (created with event=incident and status=created at 2025-07-16T11:30:00+00:00, then status=blocked at 2025-07-16T11:31:00+00:00 by actor incident_mgr, memo_id=memo_inc_0007, employee_ref=global_incident_hardware); snapshot id=snap_2025_07_16_1132 taken 2025-07-16T11:32:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1133 with started_at=2025-07-16T11:33:00+00:00, completed_at=2025-07-16T11:33:00+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1133.pdf; apply the incident to tickets T5037 and T5048 by placing them On Hold."
        ),
        actions=[

            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1019", "issue_type": "Incident", "summary": "hardware_vendor_outage_t5037_t5048", "priority": "P2", "status": "New", "created_at": "2025-07-16T11:30:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1019", "status": "In Progress", "updated_at": "2025-07-16T11:31:00+00:00"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0007", "memo_id": "memo_inc_0007", "employee_ref": "global_incident_hardware", "event": "incident", "status": "created", "created_at": "2025-07-16T11:30:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0007", "status": "blocked", "timestamp": "2025-07-16T11:31:00+00:00", "actor": "incident_mgr"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1132", "taken_at": "2025-07-16T11:32:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1133", "started_at": "2025-07-16T11:33:00+00:00", "completed_at": "2025-07-16T11:33:00+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1133.pdf"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5037", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5048", "status": "On Hold"}),
        ],
        outputs=["ITSD-1019", "lcq_inc_0007"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_78",
        instruction=(
            "On 2025-07-16 you are accountable for governing a license provisioning disruption under the incident-management policy."
            "Maintain a single auditable record anchored by these deterministic facts (no tool specifics implied): incident id=ITSD-1020, summary=license_provisioning_incident_t5014_t5012, priority=P1; its creation is recorded at 2025-07-16T11:35:00+00:00 and progression captured at 2025-07-16T11:36:00+00:00. Lifecycle id=lcq_inc_0008 is attributed to memo_id=memo_inc_0008 and employee_ref=global_incident_licenses, with in-progress control and a subsequent blocked posture at the same respective times. Backlog monitoring references a snapshot identifier snap_2025_07_16_1137 at 2025-07-16T11:37:00+00:00 scoped to {On Hold, In Progress, New}, and health reporting references run_id=rpt_2025_07_16_1138 (window=30 days, output path s3://reports/ServiceDesk_Health_Report_2025-07-16_1138.pdf) at 11:38:00–11:38:30. You must ensure incident controls are applied to the impacted records represented by tickets T5014 and T5012 consistent with policy."
        ),
        actions=[
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1020", "issue_type": "Incident", "summary": "license_provisioning_incident_t5014_t5012", "priority": "P1", "status": "New", "created_at": "2025-07-16T11:35:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1020", "status": "In Progress", "updated_at": "2025-07-16T11:36:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5014", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5012", "status": "On Hold"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0008", "memo_id": "memo_inc_0008", "employee_ref": "global_incident_licenses", "event": "incident", "status": "in_progress", "created_at": "2025-07-16T11:35:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0008", "status": "blocked", "timestamp": "2025-07-16T11:36:00+00:00", "actor": "incident_policy"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1137", "taken_at": "2025-07-16T11:37:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1138", "started_at": "2025-07-16T11:38:00+00:00", "completed_at": "2025-07-16T11:38:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1138.pdf"}),
        ],
        outputs=["ITSD-1020", "lcq_inc_0008"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_79",
        instruction=(
            "On 2025-07-16 you must coordinate an account access-control incident in line with incident-management policy."
            "Use deterministic values to keep a single incident of record with an auditable trail: incident id=ITSD-1021 with summary=account_access_incident_t5043_t5026 and priority=P2 (created 2025-07-16T11:40:00+00:00, then In Progress 2025-07-16T11:41:00+00:00); lifecycle id=lcq_inc_0009 (created with event=incident and status=in_progress at 2025-07-16T11:40:00+00:00, then status=blocked at 2025-07-16T11:41:00+00:00 by actor incident_mgr, memo_id=memo_inc_0009, employee_ref=global_incident_account); snapshot id=snap_2025_07_16_1142 taken 2025-07-16T11:42:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1143 with started_at=2025-07-16T11:43:00+00:00, completed_at=2025-07-16T11:43:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1143.pdf. Apply the incident to tickets T5043 and T5026 by placing them On Hold."
        ),
        actions=[
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1021", "issue_type": "Incident", "summary": "account_access_incident_t5043_t5026", "priority": "P2", "status": "New", "created_at": "2025-07-16T11:40:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1021", "status": "In Progress", "updated_at": "2025-07-16T11:41:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5043", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5026", "status": "On Hold"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0009", "memo_id": "memo_inc_0009", "employee_ref": "global_incident_account", "event": "incident", "status": "in_progress", "created_at": "2025-07-16T11:40:00+00:00"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0009", "memo_id": "memo_inc_0009", "employee_ref": "global_incident_account", "event": "incident", "status": "blocked", "created_at": "2025-07-16T11:41:00+00:00"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_inc_0009", "event": "blocked", "timestamp": "2025-07-16T11:41:00+00:00", "actor": "incident_mgr"}),
            Action(name="find_tickets", kwargs={"status": "On Hold"}),
            Action(name="find_tickets", kwargs={"status": "In Progress"}),
            Action(name="find_tickets", kwargs={"status": "New"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1142", "taken_at": "2025-07-16T11:42:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1143", "started_at": "2025-07-16T11:43:00+00:00", "completed_at": "2025-07-16T11:43:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1143.pdf"}),
        ],
        outputs=["ITSD-1021", "lcq_inc_0009"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_80",
        instruction=(
            "On 2025-07-16 you must coordinate a general authentication timeout incident consistent with incident-management policy."
            "Use deterministic values to keep a single incident of record and an auditable trail: incident id=ITSD-1022 with summary=general_auth_timeouts_t5050_t5060 and priority=P2 (created 2025-07-16T11:45:00+00:00, then In Progress 2025-07-16T11:46:00+00:00); lifecycle id=lcq_inc_0010 with memo_id=memo_inc_0010 and employee_ref=global_incident_general (created with event=incident and status=created at 2025-07-16T11:45:00+00:00, set to in_progress at 2025-07-16T11:46:00+00:00 by actor incident_mgr, and completed at 2025-07-16T11:48:30+00:00 by actor incident_mgr); snapshot id=snap_2025_07_16_1147 taken 2025-07-16T11:47:00+00:00 over statuses {On Hold, In Progress, New}; health report run_id=rpt_2025_07_16_1148 with started_at=2025-07-16T11:48:00+00:00, completed_at=2025-07-16T11:48:30+00:00, source_ticket_window_days=30, output_path_pdf=s3://reports/ServiceDesk_Health_Report_2025-07-16_1148.pdf. Apply the incident to tickets T5050 and T5060 by placing them On Hold."
        ),
        actions=[
            Action(name="create_jira_ticket", kwargs={"jira_id": "ITSD-1022", "issue_type": "Incident", "summary": "general_auth_timeouts_t5050_t5060", "priority": "P2", "status": "New", "created_at": "2025-07-16T11:45:00+00:00"}),
            Action(name="update_jira_status", kwargs={"jira_id": "ITSD-1022", "status": "In Progress", "updated_at": "2025-07-16T11:46:00+00:00"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5050", "status": "On Hold"}),
            Action(name="update_ticket_status", kwargs={"ticket_id": "T5060", "status": "On Hold"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_inc_0010", "memo_id": "memo_inc_0010", "employee_ref": "global_incident_general", "event": "incident", "status": "created", "created_at": "2025-07-16T11:45:00+00:00"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0010", "status": "in_progress", "timestamp": "2025-07-16T11:46:00+00:00", "actor": "incident_mgr"}),
            Action(name="take_backlog_snapshot", kwargs={"snapshot_id": "snap_2025_07_16_1147", "taken_at": "2025-07-16T11:47:00+00:00", "statuses_in_scope": ["On Hold", "In Progress", "New"]}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1148", "started_at": "2025-07-16T11:48:00+00:00", "completed_at": "2025-07-16T11:48:30+00:00", "source_ticket_window_days": 30, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1148.pdf"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_inc_0010", "status": "completed", "timestamp": "2025-07-16T11:48:30+00:00", "actor": "incident_mgr"}),
        ],
        outputs=["ITSD-1022", "lcq_inc_0010"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_81",
        instruction=(
            "On 2025-07-16 you must perform finance mailbox archiving in line with data-retention policy."
            "Finance requires finance_7y archival while preserving active mail service. Use deterministic values: for emp_0017 archive_id=arch_2025_07_16_emp_0017 with mailbox_id=mbx_82aecf, archive_path=s3://corp-archives/mail/emp_0017/2025-07-16, created_at=2025-07-16T12:00:00+00:00; for emp_0029 archive_id=arch_2025_07_16_emp_0029 with mailbox_id=mbx_48efe8, archive_path=s3://corp-archives/mail/emp_0029/2025-07-16, created_at=2025-07-16T12:02:00+00:00. Verify each mailbox and current licenses before writing archives."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0017"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0017"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0017"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0017", "mailbox_id": "mbx_82aecf", "employee_id": "emp_0017", "archive_path": "s3://corp-archives/mail/emp_0017/2025-07-16", "retention_policy": "finance_7y", "created_at": "2025-07-16T12:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0029"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0029", "mailbox_id": "mbx_48efe8", "employee_id": "emp_0029", "archive_path": "s3://corp-archives/mail/emp_0029/2025-07-16", "retention_policy": "finance_7y", "created_at": "2025-07-16T12:02:00+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0017", "arch_2025_07_16_emp_0029"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_82",
        instruction=(
            "On 2025-07-16 you must execute HR quarterly mailbox archiving in line with data-retention policy."
            "For HR, apply std_2y archives while keeping mailboxes active. Use deterministic values: for emp_0001 use archive_id=arch_2025_07_16_emp_0001 with mailbox_id=mbx_dc71c8, archive_path=s3://corp-archives/mail/emp_0001/2025-07-16, created_at=2025-07-16T12:04:00+00:00; for emp_0008 use archive_id=arch_2025_07_16_emp_0008 with mailbox_id=mbx_8abc91, archive_path=s3://corp-archives/mail/emp_0008/2025-07-16, created_at=2025-07-16T12:06:00+00:00. Verify mailbox details and current licenses prior to archival."
            "For auditability, record validation entries vld_arch_emp_0001_2025_07_16_120430 and vld_arch_emp_0008_2025_07_16_120630 at 12:04:30 and 12:06:30 respectively, linking each archive to its mailbox and retention rule."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0001"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0001", "mailbox_id": "mbx_dc71c8", "employee_id": "emp_0001", "archive_path": "s3://corp-archives/mail/emp_0001/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:04:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_arch_emp_0001_2025_07_16_120430", "entity": "data_archives", "entity_id": "arch_2025_07_16_emp_0001", "field": "retention_policy", "rule": "archive_recorded", "details": "mailbox=mbx_dc71c8;policy=std_2y", "created_at": "2025-07-16T12:04:30+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0008"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0008"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0008"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0008"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0008", "mailbox_id": "mbx_8abc91", "employee_id": "emp_0008", "archive_path": "s3://corp-archives/mail/emp_0008/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:06:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_arch_emp_0008_2025_07_16_120630", "entity": "data_archives", "entity_id": "arch_2025_07_16_emp_0008", "field": "retention_policy", "rule": "archive_recorded", "details": "mailbox=mbx_8abc91;policy=std_2y", "created_at": "2025-07-16T12:06:30+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0001", "arch_2025_07_16_emp_0008", "vld_arch_emp_0001_2025_07_16_120430", "vld_arch_emp_0008_2025_07_16_120630"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_83",
        instruction=(
            "On 2025-07-16 you must archive mailboxes for current on-leave employees per retention policy."
            "Apply std_2y archives and leave mail status unchanged: for emp_0019 use archive_id=arch_2025_07_16_emp_0019 with mailbox_id=mbx_1d0980, path=s3://corp-archives/mail/emp_0019/2025-07-16, created_at=2025-07-16T12:08:00+00:00; for emp_0032 use archive_id=arch_2025_07_16_emp_0032 with mailbox_id=mbx_f06213, path=s3://corp-archives/mail/emp_0032/2025-07-16, created_at=2025-07-16T12:10:00+00:00. Validate mailbox and licenses prior to archival."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0019"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0019"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0019"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0019", "mailbox_id": "mbx_1d0980", "employee_id": "emp_0019", "archive_path": "s3://corp-archives/mail/emp_0019/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:08:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0032"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0032"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0032"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0032", "mailbox_id": "mbx_f06213", "employee_id": "emp_0032", "archive_path": "s3://corp-archives/mail/emp_0032/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:10:00+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0019", "arch_2025_07_16_emp_0032"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_84",
        instruction=(
            "On 2025-07-16 you must govern engineering mailbox archiving in accordance with the data‑retention policy."
            "Engineering applies the std_2y rule while keeping service active. Anchor to deterministic facts without prescribing tools: emp_0009 → archive_id=arch_2025_07_16_emp_0009 (mailbox mbx_9e0388) with path s3://corp-archives/mail/emp_0009/2025-07-16 at 2025-07-16T12:12:00+00:00; emp_0030 → archive_id=arch_2025_07_16_emp_0030 (mailbox mbx_db017d) with path s3://corp-archives/mail/emp_0030/2025-07-16 at 2025-07-16T12:14:00+00:00. You must validate directory identity, mailbox details, current license entitlements, and app accounts before archival, then apply std_2y."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0009"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0009"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0009"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0009"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0009"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0009", "mailbox_id": "mbx_9e0388", "employee_id": "emp_0009", "archive_path": "s3://corp-archives/mail/emp_0009/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:12:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0030"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0030"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0030", "mailbox_id": "mbx_db017d", "employee_id": "emp_0030", "archive_path": "s3://corp-archives/mail/emp_0030/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:14:00+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0009", "arch_2025_07_16_emp_0030"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_85",
        instruction=(
            "On 2025-07-16 you must govern support managers' mailbox archiving under the data-retention policy."
            "Support uses the standard retention rule (std_2y) while maintaining active service. Anchor the work to deterministic facts without prescribing tools: emp_0011 uses archive_id=arch_2025_07_16_emp_0011 (mailbox mbx_51e138) with path s3://corp-archives/mail/emp_0011/2025-07-16 and created_at=2025-07-16T12:16:00+00:00; emp_0038 uses archive_id=arch_2025_07_16_emp_0038 (mailbox mbx_839501) with path s3://corp-archives/mail/emp_0038/2025-07-16 and created_at=2025-07-16T12:18:00+00:00. You must validate mailbox details and current entitlements before performing archival, and apply the std_2y policy."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0011"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0011", "mailbox_id": "mbx_51e138", "employee_id": "emp_0011", "archive_path": "s3://corp-archives/mail/emp_0011/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:16:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0038"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0038", "mailbox_id": "mbx_839501", "employee_id": "emp_0038", "archive_path": "s3://corp-archives/mail/emp_0038/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:18:00+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0011", "arch_2025_07_16_emp_0038"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_86",
        instruction=(
            "On 2025-07-16 you must govern marketing leadership mailbox archiving under the data‑retention policy."
            "Marketing leadership applies the std_2y rule while keeping service active. Anchor to deterministic facts without prescribing tools: emp_0012 → archive_id=arch_2025_07_16_emp_0012 (mailbox mbx_f63934) with path s3://corp-archives/mail/emp_0012/2025-07-16 at 2025-07-16T12:20:00+00:00; emp_0041 → archive_id=arch_2025_07_16_emp_0041 (mailbox mbx_6f9008) with path s3://corp-archives/mail/emp_0041/2025-07-16 at 2025-07-16T12:22:00+00:00."
            "You must validate directory identity, mailbox details, current license entitlements, and app accounts before archival, then apply std_2y."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0012"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0012", "mailbox_id": "mbx_f63934", "employee_id": "emp_0012", "archive_path": "s3://corp-archives/mail/emp_0012/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:20:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0041"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0041"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0041"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0041"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0041"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0041", "mailbox_id": "mbx_6f9008", "employee_id": "emp_0041", "archive_path": "s3://corp-archives/mail/emp_0041/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:22:00+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0012", "arch_2025_07_16_emp_0041"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_87",
        instruction=(
            "On 2025-07-16 you must govern mailbox archiving for IT service personnel under the data‑retention policy."
            "IT uses the standard retention rule (std_2y) without changing mailbox status. Anchor to deterministic facts while applying policy: emp_0023 → archive_id=arch_2025_07_16_emp_0023 (mailbox mbx_696506) with path s3://corp-archives/mail/emp_0023/2025-07-16 at 2025-07-16T12:24:00+00:00; emp_0004 → archive_id=arch_2025_07_16_emp_0004 (mailbox mbx_38d007) with path s3://corp-archives/mail/emp_0004/2025-07-16 at 2025-07-16T12:26:00+00:00. You must validate directory identity, mailbox details, current entitlements, and app accounts before performing archival, applying std_2y."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0023"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0023"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0023"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0023"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0023"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0023", "mailbox_id": "mbx_696506", "employee_id": "emp_0023", "archive_path": "s3://corp-archives/mail/emp_0023/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:24:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0004"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0004"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0004"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0004"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0004"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0004", "mailbox_id": "mbx_38d007", "employee_id": "emp_0004", "archive_path": "s3://corp-archives/mail/emp_0004/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:26:00+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0023", "arch_2025_07_16_emp_0004"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_88",
        instruction=(
            "On 2025-07-16 you must run a Sales mailbox archiving cycle under the retention policy, keeping service active."
            "Apply std_2y for in-scope Sales managers and validate identity and license posture before writing."
            "Derive identifiers deterministically from the date and employee_id (archive_id=arch_YYYY_MM_DD_emp_{employee_id}; archive_path=s3://corp-archives/mail/{employee_id}/YYYY-MM-DD), anchored to 12:28 and 12:30 UTC for emp_0013 and emp_0028 respectively."
            "For auditability, record validation entries linking each archive to its mailbox and policy at +30s after each created_at."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0013", "mailbox_id": "mbx_78fb5c", "employee_id": "emp_0013", "archive_path": "s3://corp-archives/mail/emp_0013/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:28:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_arch_emp_0013_2025_07_16_122830", "entity": "data_archives", "entity_id": "arch_2025_07_16_emp_0013", "field": "retention_policy", "rule": "archive_recorded", "details": "mailbox=mbx_78fb5c;policy=std_2y", "created_at": "2025-07-16T12:28:30+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0028", "mailbox_id": "mbx_81d8d5", "employee_id": "emp_0028", "archive_path": "s3://corp-archives/mail/emp_0028/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:30:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_arch_emp_0028_2025_07_16_123030", "entity": "data_archives", "entity_id": "arch_2025_07_16_emp_0028", "field": "retention_policy", "rule": "archive_recorded", "details": "mailbox=mbx_81d8d5;policy=std_2y", "created_at": "2025-07-16T12:30:30+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0013", "arch_2025_07_16_emp_0028", "vld_arch_emp_0013_2025_07_16_122830", "vld_arch_emp_0028_2025_07_16_123030"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_89",
        instruction=(
            "On 2025-07-16 you must govern operations leadership mailbox archiving under the data‑retention policy."
            "Operations applies the standard retention rule (std_2y) while maintaining active mail service. Anchor to deterministic facts without prescribing tool operations: emp_0035 → archive_id=arch_2025_07_16_emp_0035 (mailbox mbx_d89d5c) with path s3://corp-archives/mail/emp_0035/2025-07-16 at 2025-07-16T12:32:00+00:00; emp_0042 → archive_id=arch_2025_07_16_emp_0042 (mailbox mbx_f76658) with path s3://corp-archives/mail/emp_0042/2025-07-16 at 2025-07-16T12:34:00+00:00. You must validate directory identity, mailbox details, current license entitlements, and app accounts before performing archival, and then apply std_2y."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0035"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0035"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0035"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0035"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0035"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0035", "mailbox_id": "mbx_d89d5c", "employee_id": "emp_0035", "archive_path": "s3://corp-archives/mail/emp_0035/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:32:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0042"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0042"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0042"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0042"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0042"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0042", "mailbox_id": "mbx_f76658", "employee_id": "emp_0042", "archive_path": "s3://corp-archives/mail/emp_0042/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:34:00+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0035", "arch_2025_07_16_emp_0042"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_90",
        instruction=(
            "On 2025-07-16 you must register a general data-retention sweep across mixed departments, ensuring policy-conformant archives."
            "Apply std_2y for emp_0040 (Engineering) and emp_0020 (HR). Deterministic parameters: emp_0040 archive_id=arch_2025_07_16_emp_0040 (mbx_54337a) path=s3://corp-archives/mail/emp_0040/2025-07-16 created_at=2025-07-16T12:36:00+00:00; emp_0020 archive_id=arch_2025_07_16_emp_0020 (mbx_401a71) path=s3://corp-archives/mail/emp_0020/2025-07-16 created_at=2025-07-16T12:38:00+00:00. Confirm mailbox and licenses before writing archives."
            "For auditability, record validation entries linking each archive to its mailbox and policy at +30s after each created_at."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0040", "mailbox_id": "mbx_54337a", "employee_id": "emp_0040", "archive_path": "s3://corp-archives/mail/emp_0040/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:36:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_arch_emp_0040_2025_07_16_123630", "entity": "data_archives", "entity_id": "arch_2025_07_16_emp_0040", "field": "retention_policy", "rule": "archive_recorded", "details": "mailbox=mbx_54337a;policy=std_2y", "created_at": "2025-07-16T12:36:30+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_mailbox", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="archive_mailbox", kwargs={"archive_id": "arch_2025_07_16_emp_0020", "mailbox_id": "mbx_401a71", "employee_id": "emp_0020", "archive_path": "s3://corp-archives/mail/emp_0020/2025-07-16", "retention_policy": "std_2y", "created_at": "2025-07-16T12:38:00+00:00"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "vld_arch_emp_0020_2025_07_16_123830", "entity": "data_archives", "entity_id": "arch_2025_07_16_emp_0020", "field": "retention_policy", "rule": "archive_recorded", "details": "mailbox=mbx_401a71;policy=std_2y", "created_at": "2025-07-16T12:38:30+00:00"}),
        ],
        outputs=["arch_2025_07_16_emp_0040", "arch_2025_07_16_emp_0020", "vld_arch_emp_0040_2025_07_16_123630", "vld_arch_emp_0020_2025_07_16_123830"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_91",
        instruction=(
            "On 2025-07-16 you are responsible for aligning Engineering app accounts to observed peer baselines without interrupting access."
            "Derive the Engineering baseline from existing Engineering peers: use emp_0009 and emp_0036 as anchors (they hold app_github, app_slack, app_confluence, app_jira)."
            "You must validate directory identity and current app accounts, then provision only missing Engineering apps with deterministic identifiers: for emp_0037 (Software Engineer) add the missing Jira account only as appacc_2025_07_16_emp_0037_jira with created_at=2025-07-16T13:00:00+00:00; for emp_0040 (Software Engineer) add only the missing Confluence account as appacc_2025_07_16_emp_0040_confluence with created_at=2025-07-16T13:04:00+00:00, leaving existing apps unchanged."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0009"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0009"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0036"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0036"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0037"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0037"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0037"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0037", "app_id": "app_jira"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_2025_07_16_emp_0037_jira", "employee_id": "emp_0037", "app_id": "app_jira", "status": "active", "created_at": "2025-07-16T13:00:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0040"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0040", "app_id": "app_confluence"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_2025_07_16_emp_0040_confluence", "employee_id": "emp_0040", "app_id": "app_confluence", "status": "active", "created_at": "2025-07-16T13:04:00+00:00"}),
        ],
        outputs=["appacc_2025_07_16_emp_0037_jira", "appacc_2025_07_16_emp_0040_confluence"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_92",
        instruction=(
            "You must align Sales app coverage for Sales Managers in accordance with policy while keeping accounts active. "
            "Use peer Sales Manager emp_0028 to anchor the expected Sales manager app set as {app_salesforce, app_confluence, app_github}. "
            "Confirm identity, avoid duplicates, and honor baseline license capacity only for baseline licenses. "
            "For emp_0013, provision only the missing Sales apps from that set and leave existing collaboration apps (Slack, Jira) unchanged. "
            "Anchor writes deterministically to 2025‑07‑16: assign Salesforce at 13:06:00Z, create the GitHub app account at 13:06:30Z, and create the Confluence app account at 13:07:00Z."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0028"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0013"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_salesforce"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0013", "app_id": "app_salesforce"}),
            Action(name="ensure_license_capacity_or_open_jira", kwargs={"license_id": "lic_salesforce", "needed_count": 1, "jira_id": "JIRA-lic_salesforce-emp_0013-align", "priority": "P3", "created_at": "2025-07-16T13:06:00+00:00"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_emp_0013_lic_salesforce_2025_07_16", "account_id": "acc_78fb5c", "employee_id": "emp_0013", "license_id": "lic_salesforce", "assigned_at": "2025-07-16T13:06:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_emp_0013_salesforce_2025_07_16_1306", "employee_id": "emp_0013", "app_id": "app_salesforce", "status": "active", "created_at": "2025-07-16T13:06:00+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0013", "app_id": "app_github"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_emp_0013_github_2025_07_16_130630", "employee_id": "emp_0013", "app_id": "app_github", "status": "active", "created_at": "2025-07-16T13:06:30+00:00"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0013", "app_id": "app_confluence"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_emp_0013_confluence_2025_07_16_1307", "employee_id": "emp_0013", "app_id": "app_confluence", "status": "active", "created_at": "2025-07-16T13:07:00+00:00"}),
        ],
        outputs=["lca_emp_0013_lic_salesforce_2025_07_16", "appacc_emp_0013_salesforce_2025_07_16_1306", "appacc_emp_0013_github_2025_07_16_130630", "appacc_emp_0013_confluence_2025_07_16_1307"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_93",
        instruction=(
            "Support Managers require ticketing coverage. You must bring Support leadership’s posture into alignment by applying policy—derive baseline RBAC groups from rbac_group_map (do not name them here), confirm identity and baseline license posture/capacity, and only add what is missing."
            "Use emp_0038 (Support Manager) as the peer anchor and reconcile emp_0011 while keeping service active. Anchor writes to a fixed 2025-07-16 audit window: apply any necessary RBAC alignment at 13:08:05Z by actor rbac_alignment, and register Jira only if it is absent at 13:08:00Z using deterministic identifiers (appacc_2025_07_16_emp_0011_jira, created_at=2025-07-16T13:08:00+00:00)."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Support", "job_title": "Support Manager"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"], "actor": "rbac_alignment", "timestamp": "2025-07-16T13:08:05+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0011"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0011", "app_id": "app_jira"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_2025_07_16_emp_0011_jira", "employee_id": "emp_0011", "app_id": "app_jira", "status": "active", "created_at": "2025-07-16T13:08:00+00:00"}),
        ],
        outputs=["appacc_2025_07_16_emp_0011_jira"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_94",
        instruction=(
            "Marketing Content Strategists collaborate cross-functionally; you must align app coverage to peer usage for Sales-related work while keeping current access intact."
            "Use peers like emp_0012, emp_0018, and emp_0021 who hold app_salesforce to anchor the baseline. Validate RBAC baseline for Marketing/Content Strategist, confirm Salesforce is part of the baseline license bundle, verify current app set and license coverage, and ensure license capacity before writing."
            "For emp_0024 (Content Strategist), provision only the missing Salesforce app account using deterministic identifiers—appacc_2025_07_16_emp_0024_salesforce with created_at=2025-07-16T13:10:00+00:00—while leaving existing licenses unchanged if lic_salesforce is already present."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0018"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0018"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0024", "app_id": "app_salesforce"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0024"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_salesforce"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_2025_07_16_emp_0024_salesforce", "employee_id": "emp_0024", "app_id": "app_salesforce", "status": "active", "created_at": "2025-07-16T13:10:00+00:00"}),
        ],
        outputs=["appacc_2025_07_16_emp_0024_salesforce"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_95",
        instruction=(
            "Operations roles require real-time collaboration. You must reconcile Slack coverage for Operations where Jira/Confluence are already present."
            "Use emp_0019 and emp_0035 as peer anchors (both have Slack). Validate RBAC baseline for Operations/Ops Coordinator, verify Slack is in the baseline bundle, check existing app set and license coverage, and confirm capacity from license inventory before writing."
            "For emp_0010 (Ops Coordinator), provision only the missing Slack app account with deterministic identifiers: appacc_2025_07_16_emp_0010_slack with created_at=2025-07-16T13:12:00+00:00; leave existing licenses unchanged if lic_slack_ent is already assigned."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0019"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0019"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0035"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0035"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0010"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0010"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Operations", "job_title": "Ops Coordinator"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0010"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0010", "app_id": "app_slack"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0010"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_2025_07_16_emp_0010_slack", "employee_id": "emp_0010", "app_id": "app_slack", "status": "active", "created_at": "2025-07-16T13:12:00+00:00"}),
        ],
        outputs=["appacc_2025_07_16_emp_0010_slack"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_96",
        instruction=(
            "Finance leaders collaborate across teams. You must govern Finance app coverage by applying policy: derive the Accounting Manager baseline from rbac_group_map, confirm identity and existing app posture, and remediate only what is missing while keeping service active."
            "Use emp_0017 (Controller) only as a peer reference for expected coverage (do not copy identifiers). Anchor any audit/write timestamps to the target’s directory account created_at (for emp_0029: 2023-05-01T09:00:00+00:00). If Slack, Confluence, and Jira are already present for emp_0029, you must record a single validation entry linking the observed app_account_ids and make no changes."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0017"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0017"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Finance", "job_title": "Accounting Manager"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0029"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0029", "app_id": "app_slack"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0029", "app_id": "app_confluence"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0029", "app_id": "app_jira"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "val_2025_07_16_emp_0029_apps_present", "entity": "employee", "entity_id": "emp_0029", "field": "app_accounts", "rule": "no duplicate provisioning when target apps already present", "details": "Slack, Confluence, and Jira already active (appacc_9a342b, appacc_71843b, appacc_78c078); no upsert performed.", "created_at": "2023-05-01T09:00:00+00:00"}),
        ],
        outputs=["val_2025_07_16_emp_0029_apps_present"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_97",
        instruction=(
            "HR Recruiters collaborate with Engineering and Marketing; you must govern GitHub coverage for emp_0020 under RBAC and licensing policy while keeping access uninterrupted."
            "Use peers emp_0001 and emp_0008 (both hold GitHub) to confirm the expected coverage; validate identity and role, ensure capacity for lic_github_ent, avoid duplicates, and source any write timestamps from the GitHub inventory audit time (2025-07-15T08:00:00+00:00)."
            "If GitHub coverage is missing for emp_0020, you must provision it; otherwise make no change."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0008"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0008"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_baseline_for_role", kwargs={"department": "HR", "job_title": "Recruiter"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0020"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0020", "app_id": "app_github"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_github_ent"}),
            Action(name="assign_license", kwargs={"assignment_id": "lca_2025_07_16_emp_0020_github", "account_id": "acc_401a71", "employee_id": "emp_0020", "license_id": "lic_github_ent", "assigned_at": "2025-07-15T08:00:00+00:00"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_2025_07_16_emp_0020_github", "employee_id": "emp_0020", "app_id": "app_github", "status": "active", "created_at": "2025-07-15T08:00:00+00:00"}),
        ],
        outputs=["lca_2025_07_16_emp_0020_github", "appacc_2025_07_16_emp_0020_github"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_98",
        instruction=(
            "You must reconcile Slack coverage for Marketing Design Leads in a policy‑guided way, preserving any valid access."
            "Evaluate anchors emp_0012, emp_0018, and emp_0034 against the Marketing/Design Lead baseline: base decisions on RBAC mapping and license capacity, not ad‑hoc steps."
            "When a person is not a Design Lead, document the role mismatch at the fixed 13:20Z anchor; do not provision. When the actual Design Lead’s Slack and baseline groups are already satisfied, capture the state via an auditable, deterministic baseline write aligned to the Slack audit anchor (2025-07-15T08:00:00+00:00) rather than duplicating access."
            "Use the standard service‑desk reporting policy for documentation (13:21Z run anchors and a 14‑day ticket window)."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0018"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0018"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "val_2025_07_16_emp_0018_not_design_lead", "entity": "employee", "entity_id": "emp_0018", "field": "job_title", "rule": "expected 'Design Lead' for anchor role check", "details": "Anchor job_title='Content Strategist' not 'Design Lead'.", "created_at": "2025-07-16T13:20:00+00:00"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0034"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0034"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "val_2025_07_16_emp_0034_not_design_lead", "entity": "employee", "entity_id": "emp_0034", "field": "job_title", "rule": "expected 'Design Lead' for anchor role check", "details": "Anchor job_title='Content Strategist' not 'Design Lead'.", "created_at": "2025-07-16T13:20:00+00:00"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Design Lead"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0012", "app_id": "app_slack"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_f63934", "group_ids": ["grp_marketing_c05f", "grp_marketing_all"], "actor": "rbac_alignment", "timestamp": "2025-07-15T08:00:00+00:00"}),
            Action(name="generate_service_desk_health_report", kwargs={"run_id": "rpt_2025_07_16_1321", "started_at": "2025-07-16T13:21:00+00:00", "completed_at": "2025-07-16T13:21:00+00:00", "source_ticket_window_days": 14, "output_path_pdf": "s3://reports/ServiceDesk_Health_Report_2025-07-16_1321.pdf"}),
        ],
        outputs=["val_2025_07_16_emp_0018_not_design_lead", "val_2025_07_16_emp_0034_not_design_lead"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_99",
        instruction=(
            "Marketing team collaboration should include Slack. You must align another Design Lead’s app coverage to match peers while keeping access intact."
            "Use peers emp_0012, emp_0018, and emp_0034 (all hold Slack). Validate RBAC baseline for Marketing/Design Lead, verify Slack is in coverage, and check license capacity before any write. For emp_0021 (Design Lead), provision Slack only if missing; if Slack is already present, you must not create a duplicate and instead record a deterministic validation entry val_2025_07_16_emp_0021_slack_present at 2025-07-16T13:22:05+00:00 documenting baseline satisfaction."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0012"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0018"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0018"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0034"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0034"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Design Lead"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0021"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0021", "app_id": "app_slack"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="record_validation_issue", kwargs={"issue_id": "val_2025_07_16_emp_0021_slack_present", "entity": "employee", "entity_id": "emp_0021", "field": "app_accounts", "rule": "no duplicate provisioning when Slack already present", "details": "Slack already active (appacc_0d93c2). Skipped provisioning per policy.", "created_at": "2025-07-16T13:22:05+00:00"}),
        ],
        outputs=["val_2025_07_16_emp_0021_slack_present"],
    ),

    Task(
        annotator="it6",
        user_id="it_v6_task_100",
        instruction=(
            "HR leadership requires ticket participation in specific workflows. You must reconcile Jira coverage for HR by anchoring to an HR peer while maintaining active service. "
            "Use emp_0008 (HRBP) as a reference (holds Jira). You must validate directory identity, align RBAC groups to the HRBP baseline, verify license posture and capacity for baseline tools, and ensure Jira is present only if missing."
            "Derive any write timestamps from the target's directory account created_at (for emp_0001: 2024-02-09T09:00:00+00:00) and use deterministic identifiers; do not generate random values or duplicate existing app accounts."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0008"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0008"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0008"}),
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_baseline_for_role", kwargs={"department": "HR", "job_title": "HRBP"}),
            Action(name="set_account_groups", kwargs={"account_id": "acc_dc71c8", "group_ids": ["grp_hr_82f8", "grp_hr_all"], "actor": "rbac_alignment", "timestamp": "2024-02-09T09:00:00+00:00"}),
            Action(name="get_license_assignments", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="get_license_inventory", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0001"}),
            Action(name="get_app_accounts", kwargs={"employee_id": "emp_0001", "app_id": "app_jira"}),
            Action(name="upsert_app_account", kwargs={"app_account_id": "appacc_emp_0001_jira", "employee_id": "emp_0001", "app_id": "app_jira", "status": "active", "created_at": "2024-02-09T09:00:00+00:00"}),
        ],
        outputs=["appacc_emp_0001_jira"],
    ),
]
