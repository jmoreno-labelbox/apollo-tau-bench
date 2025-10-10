from domains.dto import Task, Action
TASKS = [
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_001",
        instruction=(
            "Your task is to perform a full, compliant offboarding for Morgan Nguyen (employee_id 'emp_0004') for lifecycle_id 'lcq_00040'. "
            "You must follow the complete, policy-driven offboarding sequence, including handling cases where no hardware is assigned."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0004"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_38d007", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00040", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_38d007"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_38d007", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00040", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_38d007"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0004"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00009"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00040", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00009"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00010"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00040", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00010"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00011"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00040", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00011"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0004"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00040", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0004"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0004"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00040", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_38d007"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_38d007"],
    ),
        Task(
annotator="v2",
user_id="It_Help_Desk_V2_002",
instruction=("You must offboard terminated employee Riley Johnson (employee_id 'emp_0006') for lifecycle_id 'lcq_00019'. Follow standard termination policy to securely deprovision access, revoke licenses, and schedule asset return."),
actions=[
Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0006"}),
Action(name="set_directory_account_status", kwargs={"account_id": "acc_e7e9ee", "status": "inactive"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00019", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_e7e9ee"}}),
Action(name="remove_user_from_groups", kwargs={"account_id": "acc_e7e9ee", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00019", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_e7e9ee"}}),
Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0006"}),
Action(name="revoke_license", kwargs={"assignment_id": "lca_00014"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00019", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00014"}}),
Action(name="revoke_license", kwargs={"assignment_id": "lca_00015"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00019", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00015"}}),
Action(name="revoke_license", kwargs={"assignment_id": "lca_00016"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00019", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00016"}}),
Action(name="archive_mailbox", kwargs={"employee_id": "emp_0006"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00019", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0006"}}),
Action(name="get_user_asset", kwargs={"employee_id": "emp_0006"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00019", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_e7e9ee"}}),
],
outputs=["acc_e7e9ee"],
),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_003",
instruction=("You must offboard Cameron Wilson (employee_id 'emp_0011') for lifecycle_id 'lcq_00023'. Employee has no assigned hardware. You should follow standard termination policy for software-only user."),
actions=[
Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0011"}),
Action(name="set_directory_account_status", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00023", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}}),
Action(name="remove_user_from_groups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00023", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}}),
Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0011"}),
Action(name="revoke_license", kwargs={"assignment_id": "lca_00024"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00023", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}}),
Action(name="revoke_license", kwargs={"assignment_id": "lca_00025"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00023", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}}),
Action(name="archive_mailbox", kwargs={"employee_id": "emp_0011"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00023", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}}),
Action(name="get_user_asset", kwargs={"employee_id": "emp_0011"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00023", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}}),
],
outputs=["acc_51e138"],
),
        
Task(
annotator="v2",
user_id="It_Help_Desk_V2_004",
instruction=("You must process the onboarding for the new IT Manager, Taylor Patel (hr-217), for lifecycle_id 'lcq_00016'. Follow standard onboarding procedures to provision software access, but report any hardware shortages encountered during the process."),
actions=[
Action(name="create_directory_account", kwargs={"legal_name": "Taylor Patel", "hr_id": "hr-217", "department": "IT", "job_title": "IT Manager"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00016", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_taylorp217"}}),
Action(name="lookup_role_profile", kwargs={"department": "IT", "job_title": "IT Manager"}),
Action(name="add_user_to_groups", kwargs={"account_id": "acc_taylorp217", "group_ids": ["grp_it_a6e7", "grp_it_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00016", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_taylorp217"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="assign_license", kwargs={"account_id": "acc_taylorp217", "employee_id": "emp_217", "license_id": "lic_m365_e3"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00016", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_taylorp217", "employee_id": "emp_217", "license_id": "lic_github_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00016", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_github_ent"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_taylorp217", "employee_id": "emp_217", "license_id": "lic_slack_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00016", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_217"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00016", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_217", "asset_id": "ast_0013"}}),
Action(name="create_device_workflow", kwargs={"employee_id": "emp_217", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00016", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_taylorp217"],
),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_005",
        instruction=(
            "You need to generate the monthly Service Desk Health Report for lifecycle 'lcq_00090'. "
            "Analyze ticket data from the last 30 days and provide comprehensive metrics to management."
        ),
        actions=[
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00090", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 30, "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="export_recent_tickets", kwargs={"days": 30}),
            Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00090", "event": "MONTHLY_REPORT_GENERATED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_006",
instruction=("You are to perform a full, compliant onboarding for the new DevOps Engineer, Casey Smith (hr-219), in Engineering for lifecycle_id 'lcq_00018'. Follow standard policy to fully provision the user with appropriate access, groups, licenses, and hardware."),
actions=[
Action(name="create_directory_account", kwargs={"legal_name": "Casey Smith", "hr_id": "hr-219", "department": "Engineering", "job_title": "DevOps Engineer"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00018", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_caseys219"}}),
Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "DevOps Engineer"}),
Action(name="add_user_to_groups", kwargs={"account_id": "acc_caseys219", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00018", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_caseys219"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="assign_license", kwargs={"account_id": "acc_caseys219", "employee_id": "emp_219", "license_id": "lic_m365_e3"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00018", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_caseys219", "license_id": "lic_m365_e3"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_caseys219", "employee_id": "emp_219", "license_id": "lic_github_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00018", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_caseys219", "license_id": "lic_github_ent"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_caseys219", "employee_id": "emp_219", "license_id": "lic_slack_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00018", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_caseys219", "license_id": "lic_slack_ent"}}),
Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_219"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00018", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_219", "asset_id": "ast_0013"}}),
Action(name="create_device_workflow", kwargs={"employee_id": "emp_219", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00018", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_caseys219"],
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_007",
        instruction=(
            "Your task is to perform a standard onboarding for the new Account Executive, Jordan Garcia (hr-216), in the Sales department for lifecycle_id 'lcq_00014'. "
            "You must follow the complete, policy-compliant procedure to provision their account, groups, all required licenses, and a standard laptop."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Jordan Garcia", "hr_id": "hr-216", "department": "Sales", "job_title": "Account Executive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00014", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordang216"}}),
            Action(name="lookup_role_profile", kwargs={"department": "Sales", "job_title": "Account Executive"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_jordang216", "group_ids": ["grp_sales_6744", "grp_sales_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00014", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_jordang216"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00014", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_salesforce"}),
            Action(name="assign_license", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_salesforce"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00014", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_salesforce"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00014", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_216"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00014", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_216_ast_0013", "employee_id": "emp_216", "asset_id": "ast_0013", "process": "onboarding"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00014", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_216_ast_0013"}}),
        ],
        outputs=["acc_jordang216"],
    ),

Task(
annotator="v2",
user_id="It_Help_Desk_V2_008",
instruction=("You must onboard new Financial Analyst Parker Davis (hr-220) in Finance for lifecycle_id 'lcq_00020'. Role requires M365 E5 license in addition to standard bundle. Create ticket for license shortage if needed."),
actions=[
Action(name="create_directory_account", kwargs={"legal_name": "Parker Davis", "hr_id": "hr-220", "department": "Finance", "job_title": "Financial Analyst"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00020", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_parkerd220"}}),
Action(name="lookup_role_profile", kwargs={"department": "Finance", "job_title": "Financial Analyst"}),
Action(name="add_user_to_groups", kwargs={"account_id": "acc_parkerd220", "group_ids": ["grp_finance_7304", "grp_finance_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00020", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_parkerd220"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="assign_license", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_m365_e3"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00020", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_m365_e3"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_slack_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00020", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_slack_ent"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e5"}),
Action(name="assign_license", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_m365_e5"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e5", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00020", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_m365_e5"}}),
Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_220"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00020", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_220", "asset_id": "ast_0013"}}),
Action(name="create_device_workflow", kwargs={"employee_id": "emp_220", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00020", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_parkerd220"],
),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_009",
        instruction=(
            "You are handling an offboarding exception for Quinn Martinez (employee_id 'emp_0009') for lifecycle_id 'lcq_00021'. "
            "Your task is to ensure the account is inactive and then complete the standard termination workflow. Since you will find no assigned hardware, the process will conclude after the software deprovisioning steps."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0009"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_9e0388", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00021", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_9e0388"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_9e0388", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00021", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_9e0388"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0009"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00019"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00021", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00019"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00020"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00021", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00020"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00021"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00021", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00021"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0009"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00021", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0009"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0009"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00021", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_9e0388"}}),
        ],
        outputs=["acc_9e0388"],
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_010",
instruction=("You must onboard new Sales Ops Analyst Rowan Lopez (hr-221) in Sales for lifecycle_id 'lcq_00022'. You should follow standard policy for sales role provisioning including optional Adobe Creative Cloud license."),
actions=[
Action(name="create_directory_account", kwargs={"legal_name": "Rowan Lopez", "hr_id": "hr-221", "department": "Sales", "job_title": "Sales Ops Analyst"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00022", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rowanl221"}}),
Action(name="lookup_role_profile", kwargs={"department": "Sales", "job_title": "Sales Ops Analyst"}),
Action(name="add_user_to_groups", kwargs={"account_id": "acc_rowanl221", "group_ids": ["grp_sales_5040", "grp_sales_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00022", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_rowanl221"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="assign_license", kwargs={"account_id": "acc_rowanl221", "employee_id": "emp_221", "license_id": "lic_m365_e3"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00022", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_rowanl221", "license_id": "lic_m365_e3"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_salesforce"}),
Action(name="assign_license", kwargs={"account_id": "acc_rowanl221", "employee_id": "emp_221", "license_id": "lic_salesforce"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00022", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_rowanl221", "license_id": "lic_salesforce"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_rowanl221", "employee_id": "emp_221", "license_id": "lic_slack_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00022", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_rowanl221", "license_id": "lic_slack_ent"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_adobe_cc"}),
Action(name="assign_license", kwargs={"account_id": "acc_rowanl221", "employee_id": "emp_221", "license_id": "lic_adobe_cc"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_adobe_cc", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00022", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_rowanl221", "license_id": "lic_adobe_cc"}}),
Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_221"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00022", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_221", "asset_id": "ast_0013"}}),
Action(name="create_device_workflow", kwargs={"employee_id": "emp_221", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00022", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_rowanl221"],
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_011",
        instruction=(
            "Your task is to perform a full, compliant offboarding for terminated employee Parker Davis (employee_id 'emp_0007') for lifecycle_id 'lcq_00015'. "
            "You must follow all standard security protocols to securely deprovision user access and handle their assets according to policy."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0007"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_e2a5e9", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00015", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_e2a5e9"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_e2a5e9", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00015", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_e2a5e9"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0007"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00015", "event": "LICENSE_VERIFICATION_COMPLETE", "details": {"active_licenses_found": 0}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0007"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00015", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0007"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0007"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00015", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"assets_found": 0}}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00015", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_e2a5e9"}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_return_emp_0007_none", "employee_id": "emp_0007", "asset_id": "none", "process": "device_return"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00015", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0007_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_e2a5e9"],
    ),

    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_012",
        instruction=(
            "Your task is to onboard the new HRBP, Reese Anderson (hr-222), in the HR department for lifecycle_id 'lcq_00024'. "
            "You find that their required hardware, a '16-inch MacBook Pro', is out of stock. "
            "You must provision all their software access and then escalate the hardware shortage by creating a Jira ticket."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Reese Anderson", "hr_id": "hr-222", "department": "HR", "job_title": "HRBP"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00024", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_reesea222"}}),
            Action(name="lookup_role_profile", kwargs={"department": "HR", "job_title": "HRBP"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_reesea222", "group_ids": ["grp_hr_82f8", "grp_hr_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00024", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_reesea222"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_reesea222", "employee_id": "emp_222", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00024", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_reesea222", "employee_id": "emp_222", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00024", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
            Action(name="find_available_asset", kwargs={"asset_type": "16-inch MacBook Pro"}),
            Action(
                name="create_jira_ticket",
                kwargs={
                    "issue_type": "Hardware Shortage",
                    "summary": "HARDWARE_SHORTAGE: lcq_00024 - 16-inch MacBook Pro",
                },
            ),
            Action(
                name="create_audit_record",
                kwargs={"lifecycle_id": "lcq_00024", "event": "JIRA_TICKET_CREATED", "details": {"jira_id": "ITSD-1013"}},
            ),
        ],
        outputs=["ITSD-1013"],
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_013",
instruction=("You must handle the offboarding exception for Emerson Thomas (employee_id 'emp_0013') for lifecycle_id 'lcq_00025'. Initial employee ID lookup may fail. You should use UPN fallback to complete standard termination process."),
actions=[
Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0013"}),
Action(name="set_directory_account_status", kwargs={"account_id": "acc_78fb5c", "status": "inactive"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00025", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_78fb5c"}}),
Action(name="remove_user_from_groups", kwargs={"account_id": "acc_78fb5c", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00025", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_78fb5c"}}),
Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0013"}),
Action(name="revoke_license", kwargs={"assignment_id": "lca_00029"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00025", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00029"}}),
Action(name="revoke_license", kwargs={"assignment_id": "lca_00030"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00025", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00030"}}),
Action(name="revoke_license", kwargs={"assignment_id": "lca_00031"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00025", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00031"}}),
Action(name="archive_mailbox", kwargs={"employee_id": "emp_0013"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00025", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0013"}}),
Action(name="get_user_asset", kwargs={"employee_id": "emp_0013"}),
Action(name="create_device_workflow", kwargs={"employee_id": "emp_0013", "asset_id": "ast_0033", "process": "offboarding_return"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00025", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "return_code": "RT0022"}}),
],
outputs=["acc_78fb5c"],
),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_014",
instruction=("You must onboard new Content Strategist Peyton Taylor (hr-223) in Marketing for lifecycle_id 'lcq_00026'. Role requires Adobe Creative Cloud license. You should create ticket for license shortage if needed."),
actions=[
Action(name="create_directory_account", kwargs={"legal_name": "Peyton Taylor", "hr_id": "hr-223", "department": "Marketing", "job_title": "Content Strategist"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00026", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_peytont223"}}),
Action(name="lookup_role_profile", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
Action(name="add_user_to_groups", kwargs={"account_id": "acc_peytont223", "group_ids": ["grp_marketing_719b", "grp_marketing_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00026", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_peytont223"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="assign_license", kwargs={"account_id": "acc_peytont223", "employee_id": "emp_223", "license_id": "lic_m365_e3"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00026", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_peytont223", "license_id": "lic_m365_e3"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_peytont223", "employee_id": "emp_223", "license_id": "lic_slack_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00026", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_peytont223", "license_id": "lic_slack_ent"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_salesforce"}),
Action(name="assign_license", kwargs={"account_id": "acc_peytont223", "employee_id": "emp_223", "license_id": "lic_salesforce"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00026", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_peytont223", "license_id": "lic_salesforce"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_adobe_cc"}),
Action(name="assign_license", kwargs={"account_id": "acc_peytont223", "employee_id": "emp_223", "license_id": "lic_adobe_cc"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_adobe_cc", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00026", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_peytont223", "license_id": "lic_adobe_cc"}}),
Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_223"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00026", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_223", "asset_id": "ast_0013"}}),
Action(name="create_device_workflow", kwargs={"employee_id": "emp_223", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00026", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_peytont223"],
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_015",
        instruction=(
            "Your task is to offboard terminated employee Hayden Moore (employee_id 'emp_0015') for lifecycle_id 'lcq_00027'. "
            "You must follow standard termination policy to securely deprovision access. Since you will find no hardware assigned, your workflow should conclude after auditing this fact."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0015"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_3818d8", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00027", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_3818d8", "group_ids": ["grp_operations_dcb3", "grp_operations_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00027", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0015"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00034"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00027", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00034"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00035"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00027", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00035"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0015"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00027", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0015"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0015"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00027", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_3818d8"}}),
        ],
        outputs=["acc_3818d8"],
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_016",
instruction=("You must onboard new Senior Software Engineer Dakota Jackson (hr-224) in Engineering for lifecycle_id 'lcq_00028'. You should follow standard policy to fully provision the user with appropriate access, groups, licenses, and hardware."),
actions=[
Action(name="create_directory_account", kwargs={"legal_name": "Dakota Jackson", "hr_id": "hr-224", "department": "Engineering", "job_title": "Senior Software Engineer"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00028", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_dakotaj224"}}),
Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "Senior Software Engineer"}),
Action(name="add_user_to_groups", kwargs={"account_id": "acc_dakotaj224", "group_ids": ["grp_engineering_639b", "grp_engineering_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00028", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_dakotaj224"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="assign_license", kwargs={"account_id": "acc_dakotaj224", "employee_id": "emp_224", "license_id": "lic_m365_e3"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00028", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_dakotaj224", "license_id": "lic_m365_e3"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_dakotaj224", "employee_id": "emp_224", "license_id": "lic_github_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00028", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_dakotaj224", "license_id": "lic_github_ent"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_dakotaj224", "employee_id": "emp_224", "license_id": "lic_slack_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00028", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_dakotaj224", "license_id": "lic_slack_ent"}}),
Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_224"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00028", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_224", "asset_id": "ast_0013"}}),
Action(name="create_device_workflow", kwargs={"employee_id": "emp_224", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00028", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_dakotaj224"],
),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_017",
        instruction=(
            "You must handle an offboarding exception for an employee for lifecycle_id 'lcq_00029'. "
            "You have been given the employee ID 'emp_0999' and UPN 'blake.martin@company.com', but you find that neither exists in the directory. "
            "Your task is to confirm both lookups fail and then escalate by creating an 'identity_not_found' Jira ticket."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0999"}),
            Action(
                name="create_audit_record",
                kwargs={
                    "lifecycle_id": "lcq_00029",
                    "event": "LOOKUP_FAILED",
                    "details": {"lookup_value": "emp_0999"},
                },
            ),
            Action(
                name="get_user_by_upn_or_hr_id",
                kwargs={"user_lookup": "blake.martin@company.com"},
            ),
            Action(
                name="create_audit_record",
                kwargs={
                    "lifecycle_id": "lcq_00029",
                    "event": "LOOKUP_FAILED",
                    "details": {"lookup_value": "blake.martin@company.com"},
                },
            ),
            Action(
                name="create_jira_ticket",
                kwargs={
                    "issue_type": "identity_not_found",
                    "summary": "OFFBOARDING_FAILURE: lcq_00029 - IDENTITY_NOT_FOUND",
                },
            ),
            Action(
                name="create_audit_record",
                kwargs={
                    "lifecycle_id": "lcq_00029",
                    "event": "OFFBOARDING_BLOCKED",
                    "details": {"reason": "identity_not_found", "jira_id": "ITSD-1013"},
                },
            ),
        ],
        outputs=["ITSD-1013"],
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_018",
instruction=("You are onboarding a new 'QA Engineer', Sawyer Thompson (hr-225), in 'Engineering' for lifecycle_id 'lcq_00030'. The goal is to fully provision the user. You must create the account ('acc_sawyert225'), assign all role-based groups and licenses, and provision a laptop ('ast_0013'). You must ensure every action is audited."),
actions=[
Action(name="create_directory_account", kwargs={"legal_name": "Sawyer Thompson", "hr_id": "hr-225", "department": "Engineering", "job_title": "QA Engineer"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00030", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_sawyert225"}}),
Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "QA Engineer"}),
Action(name="add_user_to_groups", kwargs={"account_id": "acc_sawyert225", "group_ids": ["grp_engineering_addd", "grp_engineering_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00030", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_sawyert225"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="assign_license", kwargs={"account_id": "acc_sawyert225", "employee_id": "emp_225", "license_id": "lic_m365_e3"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00030", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_sawyert225", "license_id": "lic_m365_e3"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_sawyert225", "employee_id": "emp_225", "license_id": "lic_github_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00030", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_sawyert225", "license_id": "lic_github_ent"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_sawyert225", "employee_id": "emp_225", "license_id": "lic_slack_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00030", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_sawyert225", "license_id": "lic_slack_ent"}}),
Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_225"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00030", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_225", "asset_id": "ast_0013"}}),
Action(name="create_device_workflow", kwargs={"employee_id": "emp_225", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00030", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_sawyert225"],
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_019",
    instruction=(
        "For lifecycle 'lcq_00052', your task is to investigate a reported service desk performance degradation. "
        "Compare the current ticket KPIs against the last successful report run. If the number of open P1 tickets has increased, "
        "escalate by creating a P1 'Incident' ticket summarizing the change."
    ),
    actions=[
        Action(name="get_last_report_run", kwargs={}),
        Action(name="export_recent_tickets", kwargs={"days": 30}),
        Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(name="compare_ticket_kpis", kwargs={
            "previous_kpis": {"total_open": 45, "avg_age_open_hours": 22.0, "avg_ttr_mins": 1300, "pct_closed_1d": 65.0, "p1_open_count": 4},
            "current_kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5},
        }),
        Action(name="create_jira_ticket", kwargs={
            "issue_type": "Incident",
            "summary": "PERFORMANCE_DEGRADATION: lcq_00052 | P1_TICKET_INCREASE: 1",
            "priority": "P1",
        }),
        Action(name="create_audit_record", kwargs={
            "lifecycle_id": "lcq_00052",
            "event": "INCIDENT_ESCALATED",
            "details": {"issue_type": "Incident", "reason": "P1 ticket count increased", "jira_id": "ITSD-1013"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
    ],
    outputs=["ITSD-1013"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_020",
    instruction=(
        "Your task is to onboard a new 'Support Specialist', Logan Harris (hr-226), in the 'Support' department for lifecycle_id 'lcq_00032'. "
        "You must follow the full, standard procedure to provision their account, role-based groups, licenses, and a laptop, ensuring every IAM action is audited."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Logan Harris", "hr_id": "hr-226", "department": "Support", "job_title": "Support Specialist"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00032", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_loganh226"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Support", "job_title": "Support Specialist"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_loganh226", "group_ids": ["grp_support_a407", "grp_support_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00032", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_loganh226"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="assign_license", kwargs={"account_id": "acc_loganh226", "employee_id": "emp_226", "license_id": "lic_m365_e3"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00032", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_loganh226", "employee_id": "emp_226", "license_id": "lic_slack_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00032", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_226"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00032", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_226_ast_0013", "employee_id": "emp_226", "asset_id": "ast_0013", "process": "onboarding"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00032", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_226_ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_loganh226"],
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_021",
        instruction=(
            "You need to generate the monthly Service Desk Health Report for lifecycle 'lcq_00105'. "
            "Provide comprehensive performance metrics based on recent ticket activity for management review. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00105", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 30, "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="export_recent_tickets", kwargs={"days": 30}),
            Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00105", "event": "MONTHLY_REPORT_GENERATED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00105", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00105", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_022",
    instruction=("You are onboarding a new 'Support Manager', Kendall Clark (hr-227), in 'Support' for lifecycle_id 'lcq_00034'. Complete the standard onboarding process to provision their account, role-based access, and hardware."),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Kendall Clark", "hr_id": "hr-227", "department": "Support", "job_title": "Support Manager"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00034", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_kendallc227"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Support", "job_title": "Support Manager"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_kendallc227", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00034", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_kendallc227"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="assign_license", kwargs={"account_id": "acc_kendallc227", "employee_id": "emp_227", "license_id": "lic_m365_e3"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00034", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_kendallc227", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_kendallc227", "employee_id": "emp_227", "license_id": "lic_slack_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00034", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_kendallc227", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_227"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00034", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_227", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_227_ast_0013", "employee_id": "emp_227", "asset_id": "ast_0013", "process": "onboarding"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00034", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_227_ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_kendallc227"],
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_023",
    instruction=("You must offboard the terminated employee Devin Ramirez (employee_id 'emp_0023') for lifecycle_id 'lcq_00035'. Your goal is to securely deprovision all access and assets, including their account ('acc_696506'), licenses, and assigned hardware ('ast_0041'), ensuring every step is audited."),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0023"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_696506", "status": "inactive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00035", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_696506"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_696506", "group_ids": ["grp_it_2990", "grp_it_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00035", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_696506"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0023"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00053"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00035", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00053"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00054"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00035", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00054"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00055"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00035", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00055"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="archive_mailbox", kwargs={"employee_id": "emp_0023"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00035", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0023"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="request_asset_return", kwargs={"asset_id": "ast_0041", "employee_id": "emp_0023", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0023_ast_0041"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00035", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0023_ast_0041"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_696506"],
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_024",
    instruction=("You are onboarding a new 'Operations Manager', Elliot Lewis (hr-228), in 'Operations' for lifecycle_id 'lcq_00036'. The goal is to fully provision the user. You must create the account ('acc_elliotl228'), assign all role-based groups and licenses, and provision a laptop ('ast_0013'). You must ensure every action is audited."),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Elliot Lewis", "hr_id": "hr-228", "department": "Operations", "job_title": "Operations Manager"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00036", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_elliotl228"}}),
        Action(name="lookup_role_profile", kwargs={"department": "Operations", "job_title": "Operations Manager"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_elliotl228", "group_ids": ["grp_operations_9079", "grp_operations_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00036", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_elliotl228"}}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="assign_license", kwargs={"account_id": "acc_elliotl228", "employee_id": "emp_228", "license_id": "lic_m365_e3"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00036", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_elliotl228", "license_id": "lic_m365_e3"}}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_elliotl228", "employee_id": "emp_228", "license_id": "lic_slack_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00036", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_elliotl228", "license_id": "lic_slack_ent"}}),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_228"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00036", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_228", "asset_id": "ast_0013"}}),
        Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_228_ast_0013", "employee_id": "emp_228", "asset_id": "ast_0013", "process": "onboarding"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00036", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_228_ast_0013"}}),
    ],
    outputs=["acc_elliotl228"],
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_025",
    instruction=(
        "Due to a compliance audit requirement, you must execute a comprehensive offboarding for Cameron Wilson (employee_id 'emp_0011') for lifecycle_id 'lcq_00080'. "
        "This requires strict adherence to our data retention policies and complete access deprovisioning to meet regulatory standards."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0011"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0011"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00024"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00025"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}}),
        Action(name="archive_mailbox", kwargs={"employee_id": "emp_0011"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}}),
        Action(name="get_user_asset", kwargs={"employee_id": "emp_0011"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}}),
        Action(name="create_device_workflow", kwargs={"workflow_id": "wf_return_emp_0011_none", "employee_id": "emp_0011", "asset_id": "none", "process": "device_return"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0011_none", "devices_scheduled": 0}}),
    ],
    outputs=["acc_51e138"],
),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_026",
        instruction=(
            "You are an IT manager. For lifecycle_id 'lcq_00038', your task is to generate the standard daily Service Desk Health Report for the last 30 days. "
            "You must follow the complete, standard procedure to produce the final PDF and CSV reports, save the metrics, and notify the management team."
        ),
        actions=[
            Action(name="export_recent_tickets", kwargs={"days": 30}),
            Action(
                name="calculate_ticket_kpis",
                kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"},
            ),
            Action(
                name="generate_health_report_pdf",
                kwargs={"kpis": { "total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5 }},
            ),
            Action(
                name="save_report_to_metrics_db",
                kwargs={"kpis": { "total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5 }},
            ),
            Action(
                name="notify_team_of_report",
                kwargs={
                    "pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf",
                    "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv",
                },
            ),
            Action(
                name="create_audit_record",
                kwargs={
                    "lifecycle_id": "lcq_00038",
                    "event": "REPORT_GENERATED",
                    "details": {"report_type": "daily_health_check", "run_id": "run_20250815"},
                },
            ),
        ],
        outputs=["run_20250815"],
    ),
                    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_027",
        instruction=(
            "You are an IT automation engineer. Your task is to re-enable the directory account for re-hired employee Parker Davis ('acc_e2a5e9'). "
            "You must then fully provision them with the standard groups, license bundle, and a standard laptop for their role as a 'Systems Engineer' in 'IT' for lifecycle_id 'lcq_00039'."
        ),
        actions=[
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_e2a5e9", "status": "enabled"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00039", "event": "ACCOUNT_ENABLED", "details": {"account_id": "acc_e2a5e9"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "IT", "job_title": "Systems Engineer"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_e2a5e9", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00039", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_e2a5e9"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_e2a5e9", "employee_id": "emp_0007", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_e2a5e9", "employee_id": "emp_0007", "license_id": "lic_github_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_e2a5e9", "employee_id": "emp_0007", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00039", "event": "LICENSES_ASSIGNED_COMPLETE", "details": {"account_id": "acc_e2a5e9"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0007"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00039", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_device_workflow", kwargs={"employee_id": "emp_0007", "asset_id": "ast_0013", "process": "onboarding"}),
        ],
        outputs=["acc_e2a5e9"],
    ),
    Task(
annotator="v2",
user_id="It_Help_Desk_V2_028",
instruction=("You are onboarding a new Software Engineer, Avery Lee (hr-215), in the Engineering department for lifecycle_id 'lcq_00013'. Follow the standard onboarding process: create their directory account, assign appropriate role-based groups and licenses, provision a laptop, and ensure all major events are properly audited throughout the process."),
actions=[
Action(name="create_directory_account", kwargs={"legal_name": "Avery Lee", "hr_id": "hr-215", "department": "Engineering", "job_title": "Software Engineer"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_averyl215", "upn": "avery.lee@company.com"}}),
Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "Software Engineer"}),
Action(name="add_user_to_groups", kwargs={"account_id": "acc_averyl215", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_averyl215", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="assign_license", kwargs={"account_id": "acc_averyl215", "employee_id": "emp_215", "license_id": "lic_m365_e3"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averyl215", "license_id": "lic_m365_e3"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_averyl215", "employee_id": "emp_215", "license_id": "lic_github_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averyl215", "license_id": "lic_github_ent"}}),
Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="assign_license", kwargs={"account_id": "acc_averyl215", "employee_id": "emp_215", "license_id": "lic_slack_ent"}),
Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averyl215", "license_id": "lic_slack_ent"}}),
Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_215"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_215", "asset_id": "ast_0013"}}),
Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_215_ast_0013", "employee_id": "emp_215", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_215_ast_0013", "pickup_code": "PU0013"}}),
],
outputs=["acc_averyl215"],
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_029",
        instruction=(
            "Your task is to process a role change for Morgan Nguyen (employee_id 'emp_0004') for lifecycle_id 'lcq_00041'. "
            "They are moving from 'Systems Engineer' to 'Identity Engineer' within the 'IT' department. You must fully deprovision their old access and provision all access for the new role, ensuring every IAM step is audited."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0004"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_38d007", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00041", "event": "OLD_GROUPS_REMOVED", "details": {"account_id": "acc_38d007"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0004"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00009"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00009"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00010"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00010"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00011"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00011"}}),
            Action(name="lookup_role_profile", kwargs={"department": "IT", "job_title": "Identity Engineer"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_38d007", "group_ids": ["grp_it_b55e", "grp_it_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00041", "event": "NEW_GROUPS_ASSIGNED", "details": {"account_id": "acc_38d007"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_38d007", "employee_id": "emp_0004", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_38d007", "employee_id": "emp_0004", "license_id": "lic_github_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_github_ent"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_38d007", "employee_id": "emp_0004", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
        ],
        outputs=["acc_38d007"],
    ),

            Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_030",
    instruction=(
        "You are an IT manager. For lifecycle 'lcq_00042', your task is to generate the quarterly service desk report covering the last 90 days. "
        "This quarterly review requires comprehensive performance metrics but no PDF documentation. "
        "Ensure all data is properly archived in the metrics database for executive reporting."
    ),
    actions=[
        Action(name="export_recent_tickets", kwargs={"days": 90}),
        Action(
            name="calculate_ticket_kpis",
            kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"},
        ),
        Action(
            name="save_report_to_metrics_db",
            kwargs={"kpis": { "total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5 }},
        ),
        Action(
            name="create_audit_record",
            kwargs={
                "lifecycle_id": "lcq_00042",
                "event": "REPORT_GENERATED",
                "details": {"report_type": "quarterly_health_check", "run_id": "run_20250815"},
                "timestamp": "2025-08-15T13:00:00Z",
            },
        ),
    ],
    outputs=["run_20250815"],
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_031",
    instruction=(
        "You are onboarding a contractor, 'Alex Kirby' (hr-901), as a 'Systems Engineer' in IT for lifecycle 'lcq_00043'. "
        "Handle the contractor onboarding process including account provisioning and group assignments. "
        "Contractors receive directory accounts which provide email access, but no licensed software or hardware assets."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Alex Kirby", "hr_id": "hr-901", "department": "IT", "job_title": "Systems Engineer"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00043", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_alexk901"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "IT", "job_title": "Systems Engineer"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_alexk901", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00043", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_alexk901"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_alexk901"],
),
            Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_032",
        instruction=(
            "Your task is to offboard employee 'emp_0016' (Dakota Jackson) for lifecycle 'lcq_00044'. "
            "You must follow the complete and immutable offboarding sequence: disable their account, remove groups, revoke all assigned licenses, "
            "archive their mailbox, and schedule the return of their asset, ensuring every step is audited."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0016"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_0099f1", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00044", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_0099f1"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(
                name="remove_user_from_groups",
                kwargs={
                    "account_id": "acc_0099f1",
                    "group_ids": ["grp_marketing_719b", "grp_marketing_all"],
                },
            ),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00044", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_0099f1"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0016"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00036"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00044", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00036"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00037"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00044", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00037"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00038"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00044", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00038"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0016"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00044", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0016"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0016"}),
            Action(
                name="create_device_workflow",
                kwargs={
                    "workflow_id": "wf_return_emp_0016_ast_0022",
                    "employee_id": "emp_0016",
                    "asset_id": "ast_0022",
                    "process": "offboarding_return",
                },
            ),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00044", "event": "DEVICE_RETURN_SCHEDULED", "details": {"asset_id": "ast_0022"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_0099f1"],
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_033",
        instruction=(
            "You are onboarding a new VIP, 'Jordan Rivera' (hr-235), who is an 'Executive VP' in the 'Executive' department for lifecycle 'lcq_00045'. "
            "You discover that their role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket with P3 priority."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Jordan Rivera", "hr_id": "hr-235", "department": "Executive", "job_title": "Executive VP"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00045", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordanr235"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "Executive", "job_title": "Executive VP"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00045 - MISSING_ROLE_PROFILE 'Executive VP'", "priority": "P3"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00045", "event": "ONBOARDING_BLOCKED", "details": {"reason": "Missing role profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013"],
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_034",
        instruction=(
            "You are performing a software-only onboarding for a new 'Recruiter', 'Sam Jones' (hr-230), in 'HR' for lifecycle 'lcq_00046'. "
            "Your task is to create their account and assign their standard software bundle, ensuring each IAM step is audited and compliant."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Sam Jones", "hr_id": "hr-230", "department": "HR", "job_title": "Recruiter"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00046", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_samj230"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "HR", "job_title": "Recruiter"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_samj230", "group_ids": ["grp_hr_92d4", "grp_hr_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00046", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_samj230"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_samj230", "employee_id": "emp_230", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00046", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_samj230", "employee_id": "emp_230", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00046", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_samj230"],
    ),
        Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_035",
    instruction=(
        "You are investigating a critical report generation process failure for lifecycle 'lcq_00047'. "
        "Your task is to perform a comprehensive incident analysis by comparing KPIs from the last successful report run with current ticket data. "
        "You must archive the analysis findings in the metrics database and escalate through a P1 Jira incident ticket."
    ),
    actions=[
        Action(name="get_last_report_run", kwargs={}),
        Action(name="export_recent_tickets", kwargs={"days": 30}),
        Action(
            name="calculate_ticket_kpis",
            kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"},
        ),
        Action(
            name="compare_ticket_kpis",
            kwargs={
                "previous_kpis": {"total_open": 45, "avg_age_open_hours": 22.0, "avg_ttr_mins": 1300, "pct_closed_1d": 65.0, "p1_open_count": 4},
                "current_kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5},
            },
        ),
        Action(
            name="save_report_to_metrics_db",
            kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}},
        ),
        Action(
            name="create_audit_record",
            kwargs={
                "lifecycle_id": "lcq_00047",
                "event": "INCIDENT_RESPONSE_INITIATED",
                "details": {"incident_type": "report_generation_failure", "analysis_completed": True},
                "timestamp": "2025-08-15T13:00:00Z",
            },
        ),
        Action(
            name="create_jira_ticket",
            kwargs={
                "issue_type": "Incident",
                "summary": "INCIDENT lcq_00047: REPORTING_FAILURE | ANALYSIS: Open tickets changed by 1. P1 tickets changed by 1.",
                "priority": "P1",
            },
        ),
        Action(
            name="create_audit_record",
            kwargs={
                "lifecycle_id": "lcq_00047",
                "event": "INCIDENT_ESCALATED",
                "details": {"issue_type": "Incident", "jira_id": "ITSD-1013", "analysis_summary": "KPI comparison complete. Open tickets changed by 1. P1 tickets changed by 1."},
                "timestamp": "2025-08-15T13:00:00Z",
            },
        ),
    ],
    outputs=["ITSD-1013"],
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_036",
    instruction=(
        "As the IT director, you must prepare the executive quarterly Service Desk Health Report for lifecycle 'lcq_00106'. "
        "The board requires a comprehensive analysis of all operational metrics from the past 90 days with clear visualization of performance trends. "
        "Remember to use the standard distribution list for executive communications if no specific recipient is provided."
    ),
    actions=[
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00106", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 90, "report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="export_recent_tickets", kwargs={"days": 90}),
        Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
        Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
        Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00106", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00106", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["run_20250815"],
),
    
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_037",
        instruction=(
            "For lifecycle 'lcq_00049', you must offboard the terminated employee 'emp_0017' (Blake Martin). "
            "Your task is to follow the complete, policy-driven offboarding sequence, ensuring you deprovision their account, groups, licenses, and mailbox, auditing every IAM step. This user has no hardware assigned."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0017"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_82aecf", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00049", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_82aecf"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_82aecf", "group_ids": ["grp_finance_c147", "grp_finance_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00049", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_82aecf"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0017"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00039"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00049", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00039"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00040"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00049", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00040"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0017"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00049", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0017"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0017"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00049", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_82aecf"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_82aecf"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_038",
    instruction=(
        "You are asked to investigate a potential security issue. A manager has requested an audit to confirm the successful offboarding of terminated employee 'emp_0029' (Micah King) for lifecycle 'lcq_00050'. "
        "You need to investigate their account and fully remediate any active access found according to security policy. "
        "You must document your findings and all remediation actions taken in a formal ticket."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0029"}),
        Action(name="get_user_asset", kwargs={"employee_id": "emp_0029"}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0029"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_48efe8", "status": "inactive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00050", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_48efe8"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_48efe8", "group_ids": ["grp_finance_5d50", "grp_finance_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00050", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_48efe8"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00071"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00050", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00071"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00072"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00050", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00072"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="archive_mailbox", kwargs={"employee_id": "emp_0029"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00050", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0029"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="create_device_workflow", kwargs={"employee_id": "emp_0029", "asset_id": "ast_0039", "process": "offboarding_return", "workflow_id": "wf_return_emp_0029_ast_0039"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00050", "event": "DEVICE_RETURN_SCHEDULED", "details": {"asset_id": "ast_0039"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(
            name="create_jira_ticket",
            kwargs={
                "issue_type": "Task",
                "summary": "OFFBOARDING_SECURITY_AUDIT: lcq_00050 - emp_0029",
                "priority": "P3",
            },
        ),
        Action(
            name="create_audit_record",
            kwargs={
                "lifecycle_id": "lcq_00050",
                "event": "SECURITY_AUDIT_REMEDIATED",
                "details": {"employee_id": "emp_0029", "action_taken": "FULL_OFFBOARDING_COMPLETED", "jira_id": "ITSD-1013"},
                "timestamp": "2025-08-15T13:00:00Z",
            },
        ),
    ],
    outputs=["ITSD-1013"],
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_039",
        instruction=(
            "For lifecycle 'lcq_00051', you are onboarding a new 'Accounting Manager', 'Alex Ray' (hr-231), in 'Finance'. "
            "Your task is to provision their account and software access. The user has requested a 'Dell Latitude 7440', "
            "but you find that none are in stock. You must create a ticket for the hardware shortage."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Alex Ray", "hr_id": "hr-231", "department": "Finance", "job_title": "Accounting Manager"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00051", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_alexr231"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "Finance", "job_title": "Accounting Manager"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_alexr231", "group_ids": ["grp_finance_5d50", "grp_finance_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00051", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_alexr231"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_alexr231", "employee_id": "emp_231", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00051", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_alexr231", "employee_id": "emp_231", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00051", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="find_available_asset", kwargs={"asset_type": "Dell Latitude 7440"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "Hardware Shortage", "summary": "HARDWARE_SHORTAGE: lcq_00051 - Dell Latitude 7440"}),
        ],
        outputs=["ITSD-1013"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_040",
        instruction=(
            "Your task is to perform a full, compliant offboarding for Remy White (employee_id 'emp_0019') for lifecycle_id 'lcq_00031'. "
            "Your goal is to securely deprovision all access and assets according to standard offboarding procedures. "
            "You must find the user's account ('acc_1d0980'), disable it, remove them from groups, find and revoke their license assignments, "
            "archive their mailbox, and schedule the return of their asset ('ast_0031'). You must ensure every IAM step is audited."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0019"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_1d0980", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00031", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_1d0980"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_1d0980", "group_ids": ["grp_operations_9079", "grp_operations_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00031", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_1d0980"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0019"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00044"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00031", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00044"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00045"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00031", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00045"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0019"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00031", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0019"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0019"}),
            Action(
                name="create_device_workflow",
                kwargs={
                    "employee_id": "emp_0019",
                    "asset_id": "ast_0031",
                    "process": "offboarding_return",
                },
            ),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00031", "event": "DEVICE_WORKFLOW_CREATED", "details": {"asset_id": "ast_0031"}}),
        ],
        outputs=["acc_1d0980"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_041",
    instruction=(
        "You have a high-priority request to onboard Taylor Reed (hr-229), a new senior Account Executive in the Sales department for lifecycle 'lcq_00107'. "
        "The VP of Sales has flagged this as urgent with a same-day completion requirement to meet client commitments. "
        "Ensure all standard procedures are followed with particular attention to license provisioning and immediate hardware assignment."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Taylor Reed", "hr_id": "hr-229", "department": "Sales", "job_title": "Account Executive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00107", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_taylorr229", "default_email": "it-management-dl@company.com"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Sales", "job_title": "Account Executive"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_taylorr229", "group_ids": ["grp_sales_6744", "grp_sales_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00107", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_taylorr229", "group_ids": ["grp_sales_6744", "grp_sales_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="assign_license", kwargs={"account_id": "acc_taylorr229", "license_id": "lic_m365_e3"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00107", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_taylorr229", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_salesforce"}),
        Action(name="assign_license", kwargs={"account_id": "acc_taylorr229", "license_id": "lic_salesforce"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00107", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_taylorr229", "license_id": "lic_salesforce"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_taylorr229", "license_id": "lic_slack_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00107", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_taylorr229", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_229", "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00107", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_229", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_taylorr229"],
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_042",
    instruction=(
        "Your task is to offboard employee 'emp_0027' (Kai Young) for lifecycle 'lcq_00054' according to standard termination policy. "
        "The process must include fully deprovisioning their account, groups, and all licenses. You discover they have no assigned hardware, which must be audited to complete the process."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0027"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_5494f2", "status": "inactive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00054", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_5494f2"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_5494f2", "group_ids": ["grp_marketing_231e", "grp_marketing_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00054", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_5494f2"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0027"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00065"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00054", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00065"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00066"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00054", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00066"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00067"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00054", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00067"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="archive_mailbox", kwargs={"employee_id": "emp_0027"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00054", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0027"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_asset", kwargs={"employee_id": "emp_0027"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00054", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_5494f2"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_5494f2"],
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_043",
    instruction=(
        "Your task is to onboard a new 'VP of Product', 'Riley Kim' (hr-236), in the 'Product' department for lifecycle 'lcq_00055'. "
        "You create their account but discover that their role profile is not defined in the system. You must escalate this by creating a P2 ticket that details the lifecycle ID and the specific missing role."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Riley Kim", "hr_id": "hr-236", "department": "Product", "job_title": "VP of Product"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00055", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyk236"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Product", "job_title": "VP of Product"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "MISSING_ROLE_PROFILE: lcq_00055 | department: Product | job_title: VP of Product", "priority": "P2"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00055", "event": "ONBOARDING_BLOCKED", "details": {"reason": "Missing role profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_044",
        instruction=(
            "Your task is to perform a software-only offboarding for 'emp_0011' (Cameron Wilson) for lifecycle 'lcq_00056', "
            "ensuring the process follows the complete, immutable offboarding policy, including hardware verification."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0011"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00056", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00056", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00024"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00056", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00025"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00056", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00056", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0011"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00056", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_51e138"],
    ),

    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_045",
    instruction=(
        "Your goal is to fully provision a new 'Controller', 'Morgan Kai' (hr-233), in 'Finance' for lifecycle 'lcq_00057'. "
        "This involves creating their account, assigning groups, all required licenses, and a standard laptop according to the immutable onboarding policy."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Morgan Kai", "hr_id": "hr-233", "department": "Finance", "job_title": "Controller"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00057", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_morgank233"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Finance", "job_title": "Controller"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_morgank233", "group_ids": ["grp_finance_c147", "grp_finance_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00057", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_morgank233"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="assign_license", kwargs={"account_id": "acc_morgank233", "employee_id": "emp_233", "license_id": "lic_m365_e3"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00057", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_morgank233", "employee_id": "emp_233", "license_id": "lic_slack_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00057", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_233"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00057", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_233"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_morgank233"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_046",
    instruction=(
        "Your task is to handle a complex re-onboarding for employee 'emp_0007' (Parker Davis) for lifecycle 'lcq_00058', who is returning to a new, undefined role as a 'Lead DevOps Engineer' in 'Engineering'. "
        "You must re-activate their account and then address two distinct blockers: the new role is missing a profile, and the standard temporary license ('lic_m365_e5') is also out of stock. You need to escalate both issues."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0007"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_e2a5e9", "status": "enabled"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00058", "event": "ACCOUNT_REACTIVATED", "details": {"account_id": "acc_e2a5e9"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "Lead DevOps Engineer"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "Task", "summary": "PROVISIONING_BLOCKED: lcq_00058 - MISSING_ROLE_PROFILE 'Lead DevOps Engineer'"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00058", "event": "ONBOARDING_BLOCKED", "details": {"reason": "Missing role profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "License Shortage", "summary": "LICENSE_SHORTAGE: lcq_00058 - M365 E5 license unavailable for temporary assignment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00058", "event": "TEMP_LICENSE_PROVISIONING_BLOCKED", "details": {"license_id": "lic_m365_e5", "jira_id": "ITSD-1014"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013", "ITSD-1014"],
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_047",
        instruction=(
            "Your task is to handle an asset replacement for employee 'emp_0018' for lifecycle 'lcq_00059'. "
            "You must unassign their old device, 'ast_0004', and provision the designated replacement, 'ast_0013'."
        ),
        actions=[
            Action(name="assign_asset", kwargs={"asset_id": "ast_0004", "employee_id": None}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0018"}),
            Action(name="create_device_workflow", kwargs={"employee_id": "emp_0018", "asset_id": "ast_0013", "process": "onboarding"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00059", "event": "ASSET_SWAP_COMPLETED", "details": {"employee_id": "emp_0018", "old_asset": "ast_0004", "new_asset": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["dwf_00022"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_048",
    instruction=(
        "For lifecycle 'lcq_00060', you must offboard 'emp_0029' (Micah King). "
        "The goal is to securely deprovision all access and assets according to standard termination procedures."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0029"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_48efe8", "status": "inactive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00060", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_48efe8"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_48efe8", "group_ids": ["grp_finance_5d50", "grp_finance_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00060", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_48efe8"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0029"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00071"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00060", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00071"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00072"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00060", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00072"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="archive_mailbox", kwargs={"employee_id": "emp_0029"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00060", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0029"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_asset", kwargs={"employee_id": "emp_0029"}),
        Action(name="create_device_workflow", kwargs={"workflow_id": "wf_return_emp_0029_ast_0039", "employee_id": "emp_0029", "asset_id": "ast_0039", "process": "offboarding_return"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00060", "event": "DEVICE_RETURN_SCHEDULED", "details": {"asset_id": "ast_0039"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_48efe8"],
),
            Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_049",
        instruction=(
            "An identity sync process has failed, possibly due to employee 'emp_0030'. "
            "For lifecycle 'lcq_00061', your task is to investigate the user's assigned groups and remediate their access by removing them. "
            "You must then disable the account and escalate to the appropriate teams for further analysis."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0030"}),
            Action(name="get_user_group_memberships", kwargs={"account_id": "acc_db017d"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_db017d", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00061", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_db017d"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_db017d", "status": "disabled"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00061", "event": "ACCOUNT_ACCESS_SUSPENDED", "details": {"account_id": "acc_db017d"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "Incident", "summary": "INCIDENT: lcq_00061 - Account acc_db017d disabled for sync investigation", "priority": "P2"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "Task", "summary": "TASK: lcq_00061 - Forensic analysis for acc_db017d", "priority": "P1"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00061", "event": "INCIDENT_RESPONSE_INITIATED", "details": {"account_id": "acc_db017d", "jira_ids": ["ITSD-1013", "ITSD-1014"]}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013", "ITSD-1014"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_050",
    instruction=(
        "You need to onboard new Systems Engineer Finley Blue (hr-234) in the IT department for lifecycle 'lcq_00062'. "
        "Follow standard onboarding procedures to provision their account, assign appropriate role-based access, and prepare hardware."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Finley Blue", "hr_id": "hr-234", "department": "IT", "job_title": "Systems Engineer"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00062", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_finleyb234"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "IT", "job_title": "Systems Engineer"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_finleyb234", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00062", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_finleyb234", "group_ids": ["grp_it_6b89", "grp_it_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="assign_license", kwargs={"account_id": "acc_finleyb234", "license_id": "lic_m365_e3"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00062", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_finleyb234", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_finleyb234", "license_id": "lic_github_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00062", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_finleyb234", "license_id": "lic_github_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_finleyb234", "license_id": "lic_slack_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00062", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_finleyb234", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_234"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00062", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_234", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_finleyb234"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_051",
    instruction=(
        "Your task is to handle the onboarding of a new 'Legal Counsel', 'Kai Chen' (hr-237), based on a request from HR (memo_102). A key part of the process is to create an entry in the lifecycle queue. During the process, you find their role profile is not defined. Your goal is to escalate this blocker appropriately."
    ),
    actions=[
        Action(name="add_memo_to_lifecycle_queue", kwargs={"memo_id": "memo_102", "hr_id": "hr-237", "event_type": "onboarding"}),
        Action(name="create_directory_account", kwargs={"legal_name": "Kai Chen", "hr_id": "hr-237", "department": "Legal", "job_title": "Legal Counsel"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_kaic237"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Legal", "job_title": "Legal Counsel"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00013 - MISSING_ROLE_PROFILE", "priority": "P2"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00013", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
),
        Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_052",
    instruction=(
        "Your task is to perform a full, policy-compliant offboarding for employee 'emp_0025' (Finley Robinson) under the lifecycle context 'lcq_00064'. Your goal is to deprovision all access for their account ('acc_1e8432'), which includes removing groups, revoking their four assigned licenses (Salesforce, Adobe, Slack, M365), archiving their mailbox, and scheduling the return of their laptop ('ast_0044'). You must ensure every IAM action is audited."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0025"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_1e8432", "status": "inactive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00064", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_1e8432"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_1e8432", "group_ids": ["grp_marketing_719b", "grp_marketing_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00064", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_1e8432"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0025"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00059"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00064", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00059"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00060"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_adobe_cc", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00064", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00060"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00061"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00064", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00061"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00062"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00064", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00062"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="archive_mailbox", kwargs={"employee_id": "emp_0025"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00064", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0025"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_asset", kwargs={"employee_id": "emp_0025"}),
        Action(name="request_asset_return", kwargs={"asset_id": "ast_0044", "employee_id": "emp_0025", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0025_ast_0044"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00064", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0025_ast_0044"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0025_ast_0044"],
),

Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_053",
    instruction=(
        "As an IT manager, your task is to generate the daily Service Desk Health Report for lifecycle 'lcq_00065'. "
        "Your goal is to produce the final PDF and CSV reports, save the resulting metrics for historical tracking, and notify the management team at 'it-management-dl@company.com'."
    ),
    actions=[
        Action(name="export_recent_tickets", kwargs={"days": 30}),
        Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
        Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
        Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(
            name="create_audit_record",
            kwargs={
                "lifecycle_id": "lcq_00065",
                "event": "DAILY_HEALTH_REPORT_GENERATED",
                "details": {"run_id": "run_20250815", "notified_group": "it-management-dl@company.com"},
                "timestamp": "2025-08-15T13:00:00Z"
            }
        ),
    ],
    outputs=["run_20250815"],
),

Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_054",
    instruction=(
        "Your task is to perform a full, policy-compliant offboarding for employee 'emp_0020' (River Allen) for lifecycle 'lcq_00066'. "
        "You must disable their account, remove their groups, find and revoke all of their assigned licenses, and archive their mailbox. You must ensure all IAM actions are audited."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0020"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_401a71", "status": "inactive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00066", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_401a71"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_401a71", "group_ids": ["grp_hr_92d4", "grp_hr_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00066", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_401a71"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0020"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00046"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00066", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00046"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00047"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00066", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00047"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="archive_mailbox", kwargs={"employee_id": "emp_0020"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00066", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0020"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_asset", kwargs={"employee_id": "emp_0020"}),
        Action(name="request_asset_return", kwargs={"asset_id": "ast_0011", "employee_id": "emp_0020", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0020_ast_0011"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00066", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0020_ast_0011"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0020_ast_0011"],
),

    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_055",
    instruction=(
        "Your task is to perform a full, policy-compliant onboarding for a new 'IT Support Specialist', 'Morgan Casey' (hr-240), under lifecycle context 'lcq_00067'. "
        "You must create their account, and then attempt to assign role-based groups and standard licenses for their role, and provision a laptop. "
        "However, you'll find the role profile doesn't exist, so you must follow policy by creating a Jira ticket to have the profile defined and block further onboarding steps until this is resolved."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Morgan Casey", "hr_id": "hr-240", "department": "IT", "job_title": "IT Support Specialist"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00067", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_morganc240"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "IT", "job_title": "IT Support Specialist"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00067 - MISSING_ROLE_PROFILE"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00067", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_056",
    instruction=(
        "Your task is to perform a full, policy-compliant onboarding for a new 'IT Help Desk Analyst', 'Jamie Bell' (hr-239), under lifecycle context 'lcq_00068'. "
        "You must create their account, and then attempt to assign role-based groups and standard licenses for their role, and provision a laptop. "
        "However, you'll find the role profile doesn't exist, so you must follow policy by creating a Jira ticket to have the profile defined and block further onboarding steps until this is resolved."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Jamie Bell", "hr_id": "hr-239", "department": "IT", "job_title": "IT Help Desk Analyst"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00068", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jamieb239"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "IT", "job_title": "IT Help Desk Analyst"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00068 - MISSING_ROLE_PROFILE"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00068", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_057",
    instruction=(
        "You need to handle an onboarding for VP of Operations Casey Morgan (hr-229) in the Operations department for lifecycle 'lcq_00105'. "
        "Process their account creation and escalate any missing role profile issues through proper channels. "
        "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Casey Morgan", "hr_id": "hr-229", "department": "Operations", "job_title": "VP of Operations", "default_email": "it-management-dl@company.com"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00105", "event": "EXECUTIVE_ACCOUNT_CREATED", "details": {"account_id": "acc_caseym229", "default_email": "it-management-dl@company.com"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Operations", "job_title": "VP of Operations"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00105 - MISSING_ROLE_PROFILE"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00105", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
    ),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_058",
    instruction=(
        "You need to offboard terminated employee Devin Ramirez (employee_id 'emp_0023') for lifecycle 'lcq_00070'. "
        "Follow standard termination protocols to securely deprovision access, revoke licenses, and schedule asset return."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0023"}),
        Action(name="set_directory_account_status", kwargs={"account_id": "acc_696506", "status": "inactive"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00070", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_696506"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_696506", "group_ids": ["grp_it_2990", "grp_it_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00070", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_696506"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0023"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00053"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00070", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00053"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00054"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00070", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00054"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00055"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00070", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00055"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="archive_mailbox", kwargs={"employee_id": "emp_0023"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00070", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0023"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="request_asset_return", kwargs={"asset_id": "ast_0041", "employee_id": "emp_0023", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0023_ast_0041"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00070", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0023_ast_0041"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0023_ast_0041"],
),

Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_059",
    instruction=(
        "An employee, 'emp_0026' (Charlie Garcia), has a broken laptop ('ast_0052'). As part of "
        "lifecycle 'lcq_00071', your task is to handle the asset swap. Your goal is to get them a working "
        "device, but you find there are no 'laptop_loaner' devices available. You must escalate the shortage "
        "by creating a P2 Jira ticket."
    ),
    actions=[
        Action(name="get_user_asset", kwargs={"employee_id": "emp_0026"}),
        Action(name="unassign_asset", kwargs={"asset_id": "ast_0052"}),
        Action(name="create_audit_record", kwargs={
            "lifecycle_id": "lcq_00071",
            "event": "BROKEN_ASSET_UNASSIGNED",
            "details": {"asset_id": "ast_0052"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop_loaner"}),
        Action(name="create_jira_ticket", kwargs={
            "issue_type": "Hardware Shortage",
            "priority": "P2"
        }),
        Action(name="create_audit_record", kwargs={
            "lifecycle_id": "lcq_00071",
            "event": "JIRA_TICKET_CREATED",
            "details": {"issue_type": "Hardware Shortage", "jira_id": "ITSD-1013"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
    ],
    outputs=["ITSD-1013"],
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_060",
    instruction=(
        "You must handle an internal role transfer for Jules Perez (employee_id 'emp_0042') moving from 'Operations Manager' in Operations to 'Business Intelligence Manager' in Operations for lifecycle 'lcq_role_emp_0042'. Company policy requires complete access transition with continuous audit compliance and proper license management."
    ),
    actions=[
        Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0042"}),
        Action(name="get_user_group_memberships", kwargs={"account_id": "acc_43980f"}),
        Action(name="remove_user_from_groups", kwargs={"account_id": "acc_43980f", "group_ids": ["grp_operations_9079", "grp_operations_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "PROMOTION_OLD_GROUPS_REMOVED", "details": {"account_id": "acc_43980f"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0042"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00048"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00048"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00049"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00049"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="revoke_license", kwargs={"assignment_id": "lca_00050"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00050"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Operations", "job_title": "Business Intelligence Manager"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ROLE_TRANSFER_BLOCKED: lcq_role_emp_0042 - MISSING_ROLE_PROFILE", "priority": "P2"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
),


    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_061",
    instruction=(
        "You need to conduct a compliance check for Dakota Jackson (employee_id=emp_0016). Your task is to verify "
        "that their assigned phone is under MDM, with a creation date of 2025-07-18T11:10:00+00:00. "
        "Additionally, you must validate their directory account status, group memberships against the RBAC baseline, "
        "and active license assignments. You should confirm the asset remains correctly assigned and log any issues. "
        "Record all steps in the lifecycle audit log."
    ),
    actions=[
        Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0016"}),
        Action(name="get_directory_account", kwargs={"employee_id": "emp_0016"}),
        Action(name="create_audit_record", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "ACCOUNT_STATUS_VERIFIED",
            "details": {"account_id": "acc_0099f1", "status": "enabled"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="get_user_group_memberships", kwargs={"account_id": "acc_0099f1"}),
        Action(name="get_baseline_for_role", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
        Action(name="create_audit_record", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "GROUPS_ASSIGNED",
            "details": {"actual_groups": ["grp_marketing_719b", "grp_marketing_all"], "baseline": ["grp_marketing_719b", "grp_marketing_all"]},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="get_license_assignments", kwargs={"employee_id": "emp_0016"}),
        Action(name="create_audit_record", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "LICENSE_VERIFICATION_COMPLETE",
            "details": {"assignments": ["lic_salesforce", "lic_slack_ent", "lic_m365_e3"], "expected": ["lic_salesforce", "lic_slack_ent", "lic_m365_e3"]},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="find_assets", kwargs={
            "assigned_to": "emp_0016",
            "asset_type": "phone",
            "mdm_enrolled": True
        }),
        Action(name="create_audit_record", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "ASSET_VERIFICATION_COMPLETE",
            "details": {"asset_id": "ast_0022", "asset_type": "phone", "mdm_enrolled": True},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="create_audit_record", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "ASSET_VERIFICATION_COMPLETE",
            "details": {"asset_id": "ast_0022", "expected_date": "2025-07-18T11:10:00+00:00", "actual_date": "2022-07-27", "status": "mismatch"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="record_lifecycle_audit", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "COMPLIANCE_CHECK_COMPLETED",
            "timestamp": "2025-08-15T13:00:00Z",
            "actor": "system"
        }),
    ],
    outputs=["lcq_compliance_emp_0016"],
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_062",
        instruction=(
            "Your objective is to issue a standard company laptop to Kendall Clark (employee_id=emp_0022) from the available inventory for lifecycle 'lcq_hw_emp_0022'. Company policy requires consistent asset allocation using the lowest available asset ID. Ensure the device undergoes complete MDM enrollment and verify successful assignment and management status. Handle any hardware shortages by creating appropriate escalation tickets."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0022"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0022"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0022"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_hw_emp_0022", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0022"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0022_ast_0013", "employee_id": "emp_0022", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_mdm_emp_0022_ast_0013", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
            Action(name="update_asset_status", kwargs={"asset_id": "ast_0013", "status": "READY FOR PICKUP", "mdm_enrolled": True}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_hw_emp_0022", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_mdm_emp_0022_ast_0013", "pickup_code": "pc_mdm_emp_0022_ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_hw_emp_0022", "memo_id": "memo_hw_emp_0022", "employee_ref": "emp_0022", "event": "hardware_provision", "status": "completed", "created_at": "2025-08-15T13:00:00Z"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "assigned_to": "emp_0022", "mdm_enrolled": True}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_063",
    instruction=(
        "Process the return of the phone assigned to Noel Wright (employee_id=emp_0030). You are required to schedule the device return and a corresponding MDM wipe for exactly 2025-08-15T13:00:00Z. The asset's ownership should not be modified until the collection process is fully completed."
    ),
    actions=[
        Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0030"}),
        Action(name="find_assets", kwargs={"asset_type": "phone", "assigned_to": "emp_0030", "mdm_enrolled": True}),
        Action(name="request_asset_return", kwargs={"asset_id": "ast_0014", "employee_id": "emp_0030", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0030_ast_0014"}),
        Action(name="schedule_mdm_action", kwargs={"asset_id": "ast_0014", "when": "2025-08-15T13:00:00Z", "action": "wipe", "workflow_id": "wf_return_emp_0030_ast_0014"}),
        Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_return_emp_0030", "memo_id": "memo_return_emp_0030", "employee_ref": "emp_0030", "event": "return", "status": "queued", "created_at": "2025-08-15T13:00:00Z"}),
        Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_return_emp_0030", "event": "DEVICE_WORKFLOW_CREATED", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
    ],
    outputs=["wf_return_emp_0030_ast_0014"],
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_064",
    instruction=(
        "Handle the return of two managed phones for Micah King, an Accounting Manager (employee_id=emp_0029). Your task is to create distinct return workflows and schedule MDM wipes for each device at their specified deterministic due times. Asset 'ast_0039' is due at 2025-07-26T17:00:00+00:00, and 'ast_0049' is due at 2025-07-26T17:30:00+00:00. Do not alter ownership records until the collection is confirmed."
    ),
    actions=[
        Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0029"}),
        Action(name="get_directory_account", kwargs={"employee_id": "emp_0029"}),
        Action(name="find_assets", kwargs={"assigned_to": "emp_0029"}),
        Action(name="request_asset_return", kwargs={"asset_id": "ast_0039", "employee_id": "emp_0029", "due_ts": "2025-07-26T17:00:00+00:00", "workflow_id": "wf_return_emp_0029_ast_0039"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_return_emp_0029", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0029_ast_0039"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="schedule_mdm_action", kwargs={"asset_id": "ast_0039", "when": "2025-07-26T17:00:00+00:00", "action": "wipe", "workflow_id": "wf_return_emp_0029_ast_0039"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_return_emp_0029", "event": "DEVICE_SECURITY_WIPE_SCHEDULED", "details": {"workflow_id": "wf_return_emp_0029_ast_0039"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="request_asset_return", kwargs={"asset_id": "ast_0049", "employee_id": "emp_0029", "due_ts": "2025-07-26T17:30:00+00:00", "workflow_id": "wf_return_emp_0029_ast_0049"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_return_emp_0029", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0029_ast_0049"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="schedule_mdm_action", kwargs={"asset_id": "ast_0049", "when": "2025-07-26T17:30:00+00:00", "action": "wipe", "workflow_id": "wf_return_emp_0029_ast_0049"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_return_emp_0029", "event": "DEVICE_SECURITY_WIPE_SCHEDULED", "details": {"workflow_id": "wf_return_emp_0029_ast_0049"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0029_ast_0039", "wf_return_emp_0029_ast_0049"],
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_065",
    instruction=(
        "You must provision a managed laptop for Support Manager Briar Gonzalez (employee_id=emp_0038) for lifecycle 'lcq_hardware_provision_emp_0038'. Company policy requires consistent asset allocation using the lowest available asset ID and full MDM compliance for all issued devices."
    ),
    actions=[
        Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0038"}),
        Action(name="get_directory_account", kwargs={"employee_id": "emp_0038"}),
        Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0038"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0038", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0038"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0038_ast_0013", "employee_id": "emp_0038", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0038", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_mdm_emp_0038_ast_0013", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ast_0013"],
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_066",
        instruction=(
            "You must issue a laptop from company stock to Peyton Taylor (employee_id=emp_0014). Company policy mandates consistent asset allocation using the lowest available asset ID and requires all devices to be fully enrolled in MDM with complete lifecycle tracking. Verify the final provisioning meets all management and assignment requirements."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0014"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0014"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0014"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0014", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0014"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0014_ast_0013", "employee_id": "emp_0014", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0014", "memo_id": "memo_hardware_provision_emp_0014", "employee_ref": "emp_0014", "event": "hardware_provision", "status": "queued", "created_at": "2025-08-15T13:00:00Z"}),
            Action(name="update_lifecycle_status", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0014", "status": "completed", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
            Action(name="find_assets", kwargs={"assigned_to": "emp_0014"}),
            Action(name="find_assets", kwargs={"asset_type": "laptop", "assigned_to": "emp_0014", "mdm_enrolled": True}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_067",
        instruction=(
            "You must begin onboarding for new Senior Marketing Analyst River Chen (hr-240) in Marketing for lifecycle 'lcq_ob_emp_0040'. You discover that their role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "River Chen", "hr_id": "hr-240", "department": "Marketing", "job_title": "Senior Marketing Analyst"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_riverc240"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "Marketing", "job_title": "Senior Marketing Analyst"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_ob_emp_0040 - MISSING_ROLE_PROFILE"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "AUDIT_BLOCKED", "details": {"reason": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013"],
    ),
            Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_068",
        instruction=(
            "You must securely offboard terminated employee Harper Mitchell (employee_id 'emp_0041') for lifecycle 'lcq_off_emp_0041'. Company policy mandates complete access revocation, license reclamation, and asset recovery. Ensure comprehensive audit trail and handle any deprovisioning exceptions through proper escalation."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0041"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_6f9008", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_6f9008"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_6f9008", "group_ids": ["grp_marketing_719b", "grp_marketing_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_6f9008"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0041"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00101"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00101"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00102"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00102"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00103"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00103"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0041"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0041"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0041"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"employee_id": "emp_0041", "assets_found": 0}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_6f9008"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_return_emp_0041_none", "employee_id": "emp_0041", "asset_id": "none", "process": "device_return"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0041_none", "devices_scheduled": 0}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_6f9008"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_069",
    instruction=(
        "You need to onboard new Senior Software Engineer Avery Morgan (hr-238) in the Engineering department for lifecycle 'lcq_00072'. "
        "Follow standard onboarding procedures to provision their account, assign appropriate role-based access, and prepare hardware."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Avery Morgan", "hr_id": "hr-238", "department": "Engineering", "job_title": "Senior Software Engineer"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_averym238"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "Senior Software Engineer"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_averym238", "group_ids": ["grp_engineering_639b", "grp_engineering_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_averym238", "group_ids": ["grp_engineering_639b", "grp_engineering_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="assign_license", kwargs={"account_id": "acc_averym238", "license_id": "lic_m365_e3"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averym238", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_averym238", "license_id": "lic_slack_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averym238", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
        Action(name="assign_license", kwargs={"account_id": "acc_averym238", "license_id": "lic_github_ent"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averym238", "license_id": "lic_github_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_238"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_238", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_averym238"],
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_070",
        instruction=(
            "You must provision a laptop for DevOps Engineer Nico Adams (employee_id=emp_0036) for lifecycle 'lcq_spec_emp_emp_0036'. Role requires GitHub Enterprise, Microsoft 365 E3, and Slack Enterprise licenses. Company policy mandates consistent allocation procedures with comprehensive tracking and escalation for resource constraints."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0036"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0036"}),
            Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "DevOps Engineer"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_f9a6bc", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_f9a6bc", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_github_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_github_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0036"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0036"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0036_ast_0013", "employee_id": "emp_0036", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
            Action(name="update_asset_status", kwargs={"asset_id": "ast_0013", "status": "READY FOR PICKUP", "mdm_enrolled": True}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "memo_id": "memo_spec_emp_emp_0036", "employee_ref": "emp_0036", "event": "hardware_provision", "status": "completed", "created_at": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_071",
        instruction=(
            "You must handle a critical asset replacement for Briar Gonzalez (employee_id=emp_0038) whose laptop 'ast_0002' has failed for lifecycle 'lcq_replace_emp_0038'. Company policy requires immediate replacement with proper asset lifecycle management. Handle any inventory shortages through emergency procurement escalation."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0038"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0038"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "ASSET_FAILURE_REPORTED", "details": {"asset_id": "ast_0002", "employee_id": "emp_0038", "failure_type": "hardware_malfunction"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0038"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"asset_id": "ast_0002", "current_status": "assigned"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="unassign_asset", kwargs={"asset_id": "ast_0002"}),
            Action(name="update_asset_status", kwargs={"asset_id": "ast_0002", "status": "broken"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "BROKEN_ASSET_UNASSIGNED", "details": {"asset_id": "ast_0002", "unassignment_reason": "hardware_failure"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "REPLACEMENT_ASSET_LOCATED", "details": {"replacement_asset_id": "ast_0013", "asset_type": "laptop"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0038"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "REPLACEMENT_ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0038"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_mdm_emp_0038_ast_0013", "employee_id": "emp_0038", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_dwf_replace_emp_0038_ast_0013", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
            Action(name="update_asset_status", kwargs={"asset_id": "ast_0013", "status": "READY FOR PICKUP", "mdm_enrolled": True}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "REPLACEMENT_DEVICE_READY", "details": {"asset_id": "ast_0013", "mdm_status": "enrolled"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="enqueue_lifecycle_event", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "memo_id": "memo_replace_emp_0038", "employee_ref": "emp_0038", "event": "hardware_provision", "status": "completed", "created_at": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_072",
        instruction=(
            "You must conduct a compliance audit verification for Logan Park (employee_id=emp_0045) for lifecycle 'lcq_audit_emp_0045'. Company policy requires validation of directory account status, group memberships against RBAC baseline, active license assignments, and asset management compliance. Document all findings with comprehensive audit trails."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0045"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "AUDIT_INITIATED", "details": {"employee_id": "emp_0045", "audit_type": "compliance_verification"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_directory_account", kwargs={"employee_id": "emp_0045"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "ACCOUNT_STATUS_VERIFIED", "details": {"employee_id": "emp_0045", "account_status": "not_found"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "identity_not_found", "summary": "AUDIT_BLOCKED: lcq_audit_emp_0045 - EMPLOYEE_NOT_FOUND"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "identity_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "AUDIT_BLOCKED", "details": {"employee_id": "emp_0045", "reason": "employee_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "COMPLIANCE_AUDIT_FAILED", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
        ],
        outputs=["lcq_audit_emp_0045"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_073",
        instruction=(
            "You must process a contractor conversion for Alex Reed (hr-0046) transitioning from contractor to full-time 'Security Analyst' in IT for lifecycle 'lcq_convert_emp_0046'. The employee record cannot be found in the directory. Company policy requires identity verification before proceeding with any provisioning."
        ),
        actions=[
            Action(name="get_employee_by_id", kwargs={"employee_id": "emp_0046"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_INITIATED", "details": {"employee_id": "emp_0046", "legal_name": "Alex Reed"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "identity_not_found", "summary": "CONTRACTOR_CONVERSION_BLOCKED: lcq_convert_emp_0046 - EMPLOYEE_NOT_FOUND"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "identity_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_FAILED", "details": {"reason": "employee_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="record_lifecycle_audit", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_FAILED", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
        ],
        outputs=["ITSD-1013"],
    ),
            Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_074",
        instruction=(
            "You are onboarding a new Marketing Specialist, Riley Walker (hr-245), in the Marketing department for lifecycle_id 'lcq_00079'. "
            "You discover that their role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Riley Walker", "hr_id": "hr-245", "department": "Marketing", "job_title": "Marketing Specialist"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00079", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyw245"}}),
            Action(name="lookup_role_profile", kwargs={"department": "Marketing", "job_title": "Marketing Specialist"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00079 - MISSING_ROLE_PROFILE"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00079", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_075",
        instruction=(
            "Your task is to perform a full, compliant offboarding for terminated employee Cameron Wilson (employee_id 'emp_0011') for lifecycle_id 'lcq_00080'. "
            "You must follow all standard security protocols to securely deprovision user access and handle their assets according to policy."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0011"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00024"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00025"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0011"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_return_emp_0011_none", "employee_id": "emp_0011", "asset_id": "none", "process": "device_return"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00080", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0011_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_51e138"],
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_076",
        instruction=(
            "You are handling an onboarding for Blake Thompson (hr-246) in the 'Operations' department as a 'Operations Coordinator' for lifecycle_id 'lcq_00081'. "
            "You discover this role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Blake Thompson", "hr_id": "hr-246", "department": "Operations", "job_title": "Operations Coordinator"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00081", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_blaket246"}}),
            Action(name="lookup_role_profile", kwargs={"department": "Operations", "job_title": "Operations Coordinator"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00081 - MISSING_ROLE_PROFILE"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00081", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}}),
        ],
        outputs=["ITSD-1013"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_077",
        instruction=(
            "You need to generate the monthly Service Desk Health Report for lifecycle 'lcq_00104'. "
            "Provide comprehensive performance metrics based on recent ticket activity for management review. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00104", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 30, "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="export_recent_tickets", kwargs={"days": 30}),
            Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00104", "event": "MONTHLY_REPORT_GENERATED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00104", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00104", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_078",
        instruction=(
            "You must offboard terminated employee Riley Johnson (employee_id 'emp_0006') for lifecycle_id 'lcq_00083'. "
            "Follow standard termination policy to securely deprovision access, revoke licenses, and handle asset return."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0006"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_e7e9ee", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00083", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_e7e9ee"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_e7e9ee", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00083", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_e7e9ee"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0006"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00014"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00083", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00014"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00015"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00083", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00015"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00016"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00083", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00016"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0006"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00083", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0006"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0006"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00083", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_e7e9ee"}}),
        ],
        outputs=["acc_e7e9ee"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_079",
        instruction=(
            "You must perform a full, compliant offboarding for terminated employee Cameron Wilson (employee_id 'emp_0011') "
            "for lifecycle_id 'lcq_00084'. You must follow all standard security protocols to securely deprovision user access "
            "and handle their assets according to policy."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0011"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00084", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00084", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00024"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00084", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00025"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00084", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00084", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0011"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00084", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"assets_found": 0}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_return_emp_0011_none", "employee_id": "emp_0011", "asset_id": "none", "process": "device_return"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00084", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0011_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_51e138"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_080",
        instruction=(
            "You must offboard terminated employee Hayden Moore (employee_id 'emp_0015') for lifecycle_id 'lcq_00085'. "
            "Employee has no assigned hardware. You should follow standard termination policy for software-only user."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0015"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_3818d8", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00085", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_3818d8", "group_ids": ["grp_operations_dcb3", "grp_operations_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00085", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0015"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00034"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00085", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00034"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00035"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00085", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00035"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0015"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00085", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0015"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0015"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00085", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"assets_found": 0}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_return_emp_0015_none", "employee_id": "emp_0015", "asset_id": "none", "process": "device_return"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00085", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0015_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_3818d8"],
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_081",
        instruction=(
            "You must onboard new Financial Analyst Parker Davis (hr-220) in Finance for lifecycle_id 'lcq_00086'. "
            "Role requires M365 E5 license in addition to standard bundle. Create ticket for license shortage if needed."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Parker Davis", "hr_id": "hr-220", "department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00086", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_parkerd220"}}),
            Action(name="lookup_role_profile", kwargs={"department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_parkerd220", "group_ids": ["grp_finance_7304", "grp_finance_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00086", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_parkerd220"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00086", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_m365_e3"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00086", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_slack_ent"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e5"}),
            Action(name="assign_license", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_m365_e5"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e5", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00086", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_m365_e5"}}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_220"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00086", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_220", "asset_id": "ast_0013"}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_220_ast_0013", "employee_id": "emp_220", "asset_id": "ast_0013", "process": "onboarding", "status": "pending"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00086", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_220_ast_0013", "pickup_code": "PU0013"}}),
        ],
        outputs=["acc_parkerd220"],
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_082",
        instruction=(
            "Your task is to perform a standard onboarding for the new Account Executive, Jordan Garcia (hr-216), in the Sales department for lifecycle_id 'lcq_00087'. "
            "You must follow the complete, policy-compliant procedure to provision their account, groups, all required licenses, and a standard laptop."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Jordan Garcia", "hr_id": "hr-216", "department": "Sales", "job_title": "Account Executive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00087", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordang216"}}),
            Action(name="lookup_role_profile", kwargs={"department": "Sales", "job_title": "Account Executive"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_jordang216", "group_ids": ["grp_sales_6744", "grp_sales_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00087", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_jordang216"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00087", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_salesforce"}),
            Action(name="assign_license", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_salesforce"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00087", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_salesforce"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00087", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_216"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00087", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_216_ast_0013", "employee_id": "emp_216", "asset_id": "ast_0013", "process": "onboarding", "status": "pending_pickup"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00087", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_216_ast_0013"}}),
        ],
        outputs=["acc_jordang216"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_083",
    instruction=(
        "You need to onboard Blake Thompson (hr-246) as an Operations Coordinator in the Operations department for lifecycle 'lcq_00088'. "
        "Handle the standard onboarding process and any blockers that arise according to established policies."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Blake Thompson", "hr_id": "hr-246", "department": "Operations", "job_title": "Operations Coordinator"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00088", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_blaket246"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Operations", "job_title": "Operations Coordinator"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00088 - MISSING_ROLE_PROFILE"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00088", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_084",
        instruction=(
            "You must onboard new Software Engineer Maya Patel (hr-301) in Engineering for lifecycle_id 'lcq_00089'. "
            "Follow standard onboarding procedure to provision account, groups, licenses, and hardware."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Maya Patel", "hr_id": "hr-301", "department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00089", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_mayap301"}}),
            Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_mayap301", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00089", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_mayap301"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_mayap301", "employee_id": "emp_301", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00089", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_mayap301", "license_id": "lic_m365_e3"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_mayap301", "employee_id": "emp_301", "license_id": "lic_github_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00089", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_mayap301", "license_id": "lic_github_ent"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_mayap301", "employee_id": "emp_301", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00089", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_mayap301", "license_id": "lic_slack_ent"}}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_301"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00089", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_301", "asset_id": "ast_0013"}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_301_ast_0013", "employee_id": "emp_301", "asset_id": "ast_0013", "process": "onboarding", "status": "pending"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00089", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_301_ast_0013", "pickup_code": "PU0013"}}),
        ],
        outputs=["acc_mayap301"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_085",
    instruction=(
        "You are handling an onboarding for Sam Chen (hr-302) in the 'HR' department as a 'HR Specialist' for lifecycle_id 'lcq_00090'. "
        "Follow the standard onboarding process to provision account and check resource availability. "
        "During the process, you discover the role profile is not defined and must escalate appropriately."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Sam Chen", "hr_id": "hr-302", "department": "HR", "job_title": "HR Specialist"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00090", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_samc302"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "HR", "job_title": "HR Specialist"}),
        Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00090 - MISSING_ROLE_PROFILE"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00090", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_086",
        instruction=(
            "You must onboard new Support Manager Alex Rodriguez (hr-303) in Support for lifecycle_id 'lcq_00091'. "
            "Complete standard onboarding with appropriate role-based access and hardware provisioning."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Alex Rodriguez", "hr_id": "hr-303", "department": "Support", "job_title": "Support Manager"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00091", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_alexr303"}}),
            Action(name="lookup_role_profile", kwargs={"department": "Support", "job_title": "Support Manager"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_alexr303", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00091", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_alexr303"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_alexr303", "employee_id": "emp_303", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00091", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexr303", "license_id": "lic_m365_e3"}}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_alexr303", "employee_id": "emp_303", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00091", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexr303", "license_id": "lic_slack_ent"}}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_303"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00091", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_303", "asset_id": "ast_0013"}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_303_ast_0013", "employee_id": "emp_303", "asset_id": "ast_0013", "process": "onboarding", "status": "pending"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00091", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_303_ast_0013", "pickup_code": "PU0013"}}),
        ],
        outputs=["acc_alexr303"],
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_087",
        instruction=(
            "You need to generate the weekly Service Desk Health Report for lifecycle 'lcq_00092'. "
            "Provide comprehensive performance metrics based on recent ticket activity for management review. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00092", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 7, "report_type": "weekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="export_recent_tickets", kwargs={"days": 7}),
            Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00092", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "weekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00092", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "weekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_088",
        instruction=(
            "You need to generate the monthly Service Desk Health Report for lifecycle 'lcq_00093'. "
            "Analyze ticket data from the last 30 days and provide comprehensive metrics to management."
        ),
        actions=[
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00093", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 30, "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="export_recent_tickets", kwargs={"days": 30}),
            Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00093", "event": "MONTHLY_REPORT_GENERATED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_089",
        instruction=(
            "You need to create the bi-weekly Service Desk Health Report for lifecycle 'lcq_00094'. "
            "Export last 14 days of ticket data, calculate performance metrics, and distribute to stakeholders."
        ),
        actions=[
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00094", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 14, "report_type": "biweekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="export_recent_tickets", kwargs={"days": 14}),
            Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15","timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00094", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "biweekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_090",
        instruction=(
            "You need to onboard new Software Engineer Alex Kim (hr-225) in the Engineering department for lifecycle 'lcq_00095'. "
            "Follow standard onboarding procedures to provision their account, assign appropriate role-based access, and prepare hardware. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Alex Kim", "hr_id": "hr-225", "department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00095", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_alexk225", "default_email": "it-management-dl@company.com"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_alexk225", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00095", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_alexk225", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_alexk225", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00095", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexk225", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_alexk225", "license_id": "lic_github_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00095", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexk225", "license_id": "lic_github_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_alexk225", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00095", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexk225", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_225"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00095", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_225", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_alexk225"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_091",
        instruction=(
            "You need to offboard terminated employee Quinn Martinez (employee_id 'emp_0009') for lifecycle 'lcq_00096'. "
            "Follow standard termination procedures to securely deprovision user access and handle the termination process."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0009"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_9e0388", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00096", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_9e0388"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_9e0388", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00096", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_9e0388"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0009"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00019"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00096", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00019"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00020"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00096", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00020"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00021"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00096", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00021"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0009"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00096", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0009"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0009"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00096", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_9e0388"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_9e0388"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_092",
        instruction=(
            "You need to handle an onboarding for Riley Chen (hr-226) in the 'Legal' department as a 'Legal Analyst' for lifecycle 'lcq_00097'. "
            "Process their account creation and escalate any missing role profile issues through proper channels."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Riley Chen", "hr_id": "hr-226", "department": "Legal", "job_title": "Legal Analyst"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00097", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyc226"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "Legal", "job_title": "Legal Analyst"}),
            Action(name="create_jira_ticket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00097 - MISSING_ROLE_PROFILE"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00097", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013"],
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_093",
        instruction=(
            "You need to offboard terminated employee Riley Johnson (employee_id 'emp_0006') for lifecycle 'lcq_00098'. "
            "Follow standard termination protocols to securely deprovision access, revoke licenses, and schedule asset return."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0006"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_e7e9ee", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00098", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_e7e9ee"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_e7e9ee", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00098", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_e7e9ee"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0006"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00014"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00098", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00014"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00015"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00098", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00015"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00016"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00098", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00016"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0006"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00098", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0006"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0006"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00098", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_e7e9ee"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_e7e9ee"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_094",
        instruction=(
            "You need to generate the quarterly Service Desk Health Report for lifecycle 'lcq_00099'. "
            "Provide comprehensive performance analysis based on last 90 days of ticket activity for executive review. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00099", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 90, "report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="export_recent_tickets", kwargs={"days": 90}),
            Action(name="calculate_ticket_kpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="generate_health_report_pdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="save_report_to_metrics_db", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="notify_team_of_report", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00099", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00099", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_095",
        instruction=(
            "You need to onboard new Account Executive Morgan Taylor (hr-227) in the Sales department for lifecycle 'lcq_00100'. "
            "Follow standard onboarding procedures to provision their account, assign appropriate role-based access, and prepare hardware. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Morgan Taylor", "hr_id": "hr-227", "department": "Sales", "job_title": "Account Executive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00100", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_morgant227", "default_email": "it-management-dl@company.com"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "Sales", "job_title": "Account Executive"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_morgant227", "group_ids": ["grp_sales_6744", "grp_sales_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00100", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_morgant227", "group_ids": ["grp_sales_6744", "grp_sales_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_morgant227", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00100", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_morgant227", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_salesforce"}),
            Action(name="assign_license", kwargs={"account_id": "acc_morgant227", "license_id": "lic_salesforce"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00100", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_morgant227", "license_id": "lic_salesforce"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_morgant227", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00100", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_morgant227", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_227", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00100", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_227", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_morgant227"],
    ),

    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_096",
        instruction=(
            "You need to offboard terminated employee Emerson Thomas (employee_id 'emp_0013') for lifecycle 'lcq_00101'. "
            "Follow standard termination protocols to securely deprovision access, revoke licenses, and schedule asset return."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0013"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_78fb5c", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00101", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_78fb5c"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_78fb5c", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00101", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_78fb5c"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0013"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00029"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00101", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00029"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00030"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00101", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00030"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00031"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00101", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00031"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0013"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00101", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0013"}),
            Action(name="request_asset_return", kwargs={"asset_id": "ast_0033", "employee_id": "emp_0013", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0013_ast_0033"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00101", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0013_ast_0033"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["wf_return_emp_0013_ast_0033"],
    ),

    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_097",
        instruction=(
            "You need to onboard new Financial Analyst Jordan Lee (hr-228) in the Finance department for lifecycle 'lcq_00102'. "
            "Follow standard onboarding procedures and handle any license shortage issues through proper escalation channels."
        ),
        actions=[
            Action(name="create_directory_account", kwargs={"legal_name": "Jordan Lee", "hr_id": "hr-228", "department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00102", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordanl228"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_jordanl228", "group_ids": ["grp_finance_7304", "grp_finance_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00102", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_jordanl228", "group_ids": ["grp_finance_7304", "grp_finance_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="assign_license", kwargs={"account_id": "acc_jordanl228", "license_id": "lic_m365_e3"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00102", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_jordanl228", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="assign_license", kwargs={"account_id": "acc_jordanl228", "license_id": "lic_slack_ent"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00102", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_jordanl228", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
            Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_228"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00102", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_228", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_jordanl228"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_098",
        instruction=(
            "You need to offboard terminated employee Cameron Wilson (employee_id 'emp_0011') for lifecycle 'lcq_00103'. "
            "Follow standard termination procedures to securely deprovision user access and handle the termination process."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0011"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00103", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00103", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00024"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00103", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00025"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00103", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00103", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0011"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00103", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_51e138"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_099",
        instruction=(
            "You must offboard terminated employee Hayden Moore (employee_id 'emp_0015') for lifecycle_id 'lcq_00082'. "
            "Employee has no assigned hardware. You should follow standard termination policy for software-only user."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0015"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_3818d8", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00082", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_3818d8", "group_ids": ["grp_operations_dcb3", "grp_operations_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00082", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0015"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00034"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00082", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00034"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00035"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00082", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00035"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0015"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00082", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0015"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0015"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00082", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"assets_found": 0}}),
            Action(name="create_device_workflow", kwargs={"workflow_id": "wf_return_emp_0015_none", "employee_id": "emp_0015", "asset_id": "none", "process": "device_return"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00082", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0015_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_3818d8"],
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_100",
        instruction=(
            "Your task is to perform a full, policy-compliant software-only offboarding for employee 'Kai Young' (emp_0027) for lifecycle 'lcq_00072'. "
            "You must disable their account, remove their groups, find and revoke all of their assigned licenses (Salesforce, Slack, M365), and archive their mailbox. "
            "The process is complete after you verify they have no assigned hardware. You must ensure all IAM actions are audited."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0027"}),
            Action(name="set_directory_account_status", kwargs={"account_id": "acc_5494f2", "status": "inactive"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_5494f2"}}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_5494f2", "group_ids": ["grp_marketing_231e", "grp_marketing_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_5494f2"}}),
            Action(name="get_user_license_assignments", kwargs={"employee_id": "emp_0027"}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00065"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00065"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00066"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00066"}}),
            Action(name="revoke_license", kwargs={"assignment_id": "lca_00067"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00067"}}),
            Action(name="archive_mailbox", kwargs={"employee_id": "emp_0027"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0027"}}),
            Action(name="get_user_asset", kwargs={"employee_id": "emp_0027"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00072", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_5494f2"}}),
        ],
        outputs=["acc_5494f2"],
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_101",
    instruction=(
        "You are onboarding an intern, 'Chris Green' (hr-902), in the 'Marketing' department as a 'Growth Marketer' for lifecycle 'lcq_00048'. "
        "Your task is to follow the complete, standard onboarding procedure: create their account, assign groups, provision the required M365 E3 license, and assign a standard laptop, auditing all actions."
    ),
    actions=[
        Action(name="create_directory_account", kwargs={"legal_name": "Chris Green", "hr_id": "hr-902", "department": "Marketing", "job_title": "Growth Marketer"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00048", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_chrisg902"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="lookup_role_profile", kwargs={"department": "Marketing", "job_title": "Growth Marketer"}),
        Action(name="add_user_to_groups", kwargs={"account_id": "acc_chrisg902", "group_ids": ["grp_marketing_231e", "grp_marketing_all"]}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00048", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_chrisg902"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="assign_license", kwargs={"account_id": "acc_chrisg902", "employee_id": "emp_902", "license_id": "lic_m365_e3"}),
        Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00048", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="find_available_asset", kwargs={"asset_type": "laptop"}),
        Action(name="assign_asset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_902"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00048", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="create_device_workflow", kwargs={"workflow_id": "wf_onboard_emp_902_ast_0013", "employee_id": "emp_902", "asset_id": "ast_0013", "process": "onboarding"}),
        Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00048", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_902_ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_chrisg902"],
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_102",
        instruction=(
            "Employee 'emp_0022' (Kendall Clark) is being promoted from 'Ops Coordinator' to 'Operations Manager' for lifecycle 'lcq_00053'. "
            "Your task is to update their role-based access. You must remove their old group memberships, assign the new ones, and provision the required 'M365 E5' license for their new role."
        ),
        actions=[
            Action(name="get_user_by_upn_or_hr_id", kwargs={"user_lookup": "emp_0022"}),
            Action(name="remove_user_from_groups", kwargs={"account_id": "acc_51ba73", "group_ids": ["grp_operations_772e", "grp_operations_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00053", "event": "PROMOTION_OLD_GROUPS_REMOVED", "details": {"account_id": "acc_51ba73"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="lookup_role_profile", kwargs={"department": "Operations", "job_title": "Operations Manager"}),
            Action(name="add_user_to_groups", kwargs={"account_id": "acc_51ba73", "group_ids": ["grp_operations_9079", "grp_operations_all"]}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00053", "event": "PROMOTION_NEW_GROUPS_ASSIGNED", "details": {"account_id": "acc_51ba73"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="check_license_availability", kwargs={"license_id": "lic_m365_e5"}),
            Action(name="assign_license", kwargs={"account_id": "acc_51ba73", "employee_id": "emp_0022", "license_id": "lic_m365_e5"}),
            Action(name="update_license_inventory", kwargs={"license_id": "lic_m365_e5", "operation": "increment"}),
            Action(name="create_audit_record", kwargs={"lifecycle_id": "lcq_00053", "event": "PROMOTION_NEW_LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e5"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_51ba73"],
    ),

]