from tau_bench.types import Action, Task
TASKS = [
Task(
annotator="0",
user_id="it-help-desk-v4-001",
instruction=("You are onboarding a new Software Engineer, Jamie Chen (hr-215), in the Engineering department for lifecycle_id 'lcq_00013'. Follow the standard onboarding process: create their directory account, assign appropriate role-based groups and licenses, provision a laptop, and ensure all major events are properly audited throughout the process."),
actions=[
Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Jamie Chen", "hr_id": "hr-215", "department": "Engineering", "job_title": "Software Engineer"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_averyl215", "upn": "avery.lee@company.com"}}),
Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "Software Engineer"}),
Action(name="AddUserToGroups", kwargs={"account_id": "acc_averyl215", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_averyl215", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_averyl215", "employee_id": "emp_215", "license_id": "lic_m365_e3"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averyl215", "license_id": "lic_m365_e3"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_averyl215", "employee_id": "emp_215", "license_id": "lic_github_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averyl215", "license_id": "lic_github_ent"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_averyl215", "employee_id": "emp_215", "license_id": "lic_slack_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averyl215", "license_id": "lic_slack_ent"}}),
Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_215"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_215", "asset_id": "ast_0013"}}),
Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_215_ast_0013", "employee_id": "emp_215", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_215_ast_0013", "pickup_code": "PU0013"}}),
],
outputs=["acc_averyl215"],
),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-002",
        instruction=(
            "Coordinate a standard onboarding for the new Account Executive, Casey Liu (hr-216), in the Sales department for lifecycle_id 'lcq_00014'. Follow the complete, policy-compliant procedure to provision their account, groups, all required licenses, and a standard laptop."
            "You must follow the complete, policy-compliant procedure to provision their account, groups, all required licenses, and a standard laptop."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Casey Liu", "hr_id": "hr-216", "department": "Sales", "job_title": "Account Executive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00014", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordang216"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Sales", "job_title": "Account Executive"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_jordang216", "group_ids": ["grp_sales_6744", "grp_sales_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00014", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_jordang216"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00014", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_salesforce"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_salesforce"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00014", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_salesforce"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00014", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_216"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00014", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_216_ast_0013", "employee_id": "emp_216", "asset_id": "ast_0013", "process": "onboarding"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00014", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_216_ast_0013"}}),
        ],
        outputs=["acc_jordang216"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-003",
        instruction=(
            "Your responsibility is to handle a complete, compliant offboarding for terminated employee Jordan Kim (employee_id 'emp_0007') for lifecycle_id 'lcq_00015'. Adhere to all standard security protocols to securely remove user access and manage their assets in line with policy."
            "You must follow all standard security protocols to securely deprovision user access and handle their assets according to policy."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0007"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_e2a5e9", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00015", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_e2a5e9"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_e2a5e9", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00015", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_e2a5e9"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0007"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00015", "event": "LICENSE_VERIFICATION_COMPLETE", "details": {"active_licenses_found": 0}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0007"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00015", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0007"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0007"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00015", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"assets_found": 0}}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00015", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_e2a5e9"}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_return_emp_0007_none", "employee_id": "emp_0007", "asset_id": "none", "process": "device_return"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00015", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0007_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_e2a5e9"],
    ),
Task(
annotator="0",
user_id="it-help-desk-v4-004",
instruction=("You must process the onboarding for the new IT Manager, Drew Kumar (hr-217), for lifecycle_id 'lcq_00016'. Follow standard onboarding procedures to provision software access, but report any hardware shortages encountered during the process."),
actions=[
Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Drew Kumar", "hr_id": "hr-217", "department": "IT", "job_title": "IT Manager"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00016", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_taylorp217"}}),
Action(name="LookupRoleProfile", kwargs={"department": "IT", "job_title": "IT Manager"}),
Action(name="AddUserToGroups", kwargs={"account_id": "acc_taylorp217", "group_ids": ["grp_it_a6e7", "grp_it_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00016", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_taylorp217"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_taylorp217", "employee_id": "emp_217", "license_id": "lic_m365_e3"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00016", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_taylorp217", "employee_id": "emp_217", "license_id": "lic_github_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00016", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_github_ent"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_taylorp217", "employee_id": "emp_217", "license_id": "lic_slack_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00016", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_217"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00016", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_217", "asset_id": "ast_0013"}}),
Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_217", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00016", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_taylorp217"],
),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-005",
        instruction=(
            "Generate the monthly Service Desk Health Report for lifecycle 'lcq_00090'. Examine ticket data from the past 30 days and present detailed metrics to management."
            "Analyze ticket data from the last 30 days and provide comprehensive metrics to management."
        ),
        actions=[
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00090", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 30, "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ExportRecentTickets", kwargs={"days": 30}),
            Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00090", "event": "MONTHLY_REPORT_GENERATED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
Task(
annotator="0",
user_id="it-help-desk-v4-006",
instruction=("You are to perform a full, compliant onboarding for the new DevOps Engineer, Robin Jones (hr-219), in Engineering for lifecycle_id 'lcq_00018'. Follow standard policy to fully provision the user with appropriate access, groups, licenses, and hardware."),
actions=[
Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Robin Jones", "hr_id": "hr-219", "department": "Engineering", "job_title": "DevOps Engineer"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00018", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_caseys219"}}),
Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "DevOps Engineer"}),
Action(name="AddUserToGroups", kwargs={"account_id": "acc_caseys219", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00018", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_caseys219"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_caseys219", "employee_id": "emp_219", "license_id": "lic_m365_e3"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00018", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_caseys219", "license_id": "lic_m365_e3"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_caseys219", "employee_id": "emp_219", "license_id": "lic_github_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00018", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_caseys219", "license_id": "lic_github_ent"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_caseys219", "employee_id": "emp_219", "license_id": "lic_slack_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00018", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_caseys219", "license_id": "lic_slack_ent"}}),
Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_219"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00018", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_219", "asset_id": "ast_0013"}}),
Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_219", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00018", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_caseys219"],
),
Task(
annotator="0",
user_id="it-help-desk-v4-007",
instruction=("You must offboard terminated employee Alex Park (employee_id 'emp_0006') for lifecycle_id 'lcq_00019'. Follow standard termination policy to securely deprovision access, revoke licenses, and schedule asset return."),
actions=[
Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0006"}),
Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_e7e9ee", "status": "inactive"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00019", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_e7e9ee"}}),
Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_e7e9ee", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00019", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_e7e9ee"}}),
Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0006"}),
Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00014"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00019", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00014"}}),
Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00015"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00019", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00015"}}),
Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00016"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00019", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00016"}}),
Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0006"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00019", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0006"}}),
Action(name="GetUserAsset", kwargs={"employee_id": "emp_0006"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00019", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_e7e9ee"}}),
],
outputs=["acc_e7e9ee"],
),
Task(
annotator="0",
user_id="it-help-desk-v4-008",
instruction=("You must onboard new Financial Analyst Jordan Kim (hr-220) in Finance for lifecycle_id 'lcq_00020'. Role requires M365 E5 license in addition to standard bundle. Create ticket for license shortage if needed."),
actions=[
Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Jordan Kim", "hr_id": "hr-220", "department": "Finance", "job_title": "Financial Analyst"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00020", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_parkerd220"}}),
Action(name="LookupRoleProfile", kwargs={"department": "Finance", "job_title": "Financial Analyst"}),
Action(name="AddUserToGroups", kwargs={"account_id": "acc_parkerd220", "group_ids": ["grp_finance_7304", "grp_finance_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00020", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_parkerd220"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_m365_e3"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00020", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_m365_e3"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_slack_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00020", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_slack_ent"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e5"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_m365_e5"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e5", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00020", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_m365_e5"}}),
Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_220"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00020", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_220", "asset_id": "ast_0013"}}),
Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_220", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00020", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_parkerd220"],
),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-009",
        instruction=(
            "You are responsible for an offboarding exception for Taylor Singh (employee_id 'emp_0009') concerning lifecycle_id 'lcq_00021'. Your job is to deactivate the account and subsequently execute the normal termination workflow. As no hardware has been assigned, finish the process after the software deprovisioning steps."
            "Your task is to ensure the account is inactive and then complete the standard termination workflow. Since you will find no assigned hardware, the process will conclude after the software deprovisioning steps."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0009"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_9e0388", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00021", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_9e0388"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_9e0388", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00021", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_9e0388"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0009"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00019"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00021", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00019"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00020"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00021", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00020"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00021"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00021", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00021"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0009"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00021", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0009"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0009"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00021", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_9e0388"}}),
        ],
        outputs=["acc_9e0388"],
    ),
Task(
annotator="0",
user_id="it-help-desk-v4-010",
instruction=("You must onboard new Sales Ops Analyst Avery Zhang (hr-221) in Sales for lifecycle_id 'lcq_00022'. You should follow standard policy for sales role provisioning including optional CreativeWorks Creative Cloud license."),
actions=[
Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Avery Zhang", "hr_id": "hr-221", "department": "Sales", "job_title": "Sales Ops Analyst"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00022", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rowanl221"}}),
Action(name="LookupRoleProfile", kwargs={"department": "Sales", "job_title": "Sales Ops Analyst"}),
Action(name="AddUserToGroups", kwargs={"account_id": "acc_rowanl221", "group_ids": ["grp_sales_5040", "grp_sales_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00022", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_rowanl221"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_rowanl221", "employee_id": "emp_221", "license_id": "lic_m365_e3"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00022", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_rowanl221", "license_id": "lic_m365_e3"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_salesforce"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_rowanl221", "employee_id": "emp_221", "license_id": "lic_salesforce"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00022", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_rowanl221", "license_id": "lic_salesforce"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_rowanl221", "employee_id": "emp_221", "license_id": "lic_slack_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00022", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_rowanl221", "license_id": "lic_slack_ent"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_adobe_cc"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_rowanl221", "employee_id": "emp_221", "license_id": "lic_adobe_cc"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_adobe_cc", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00022", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_rowanl221", "license_id": "lic_adobe_cc"}}),
Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_221"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00022", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_221", "asset_id": "ast_0013"}}),
Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_221", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00022", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_rowanl221"],
),
Task(
annotator="0",
user_id="it-help-desk-v4-011",
instruction=("You must offboard Riley Wang (employee_id 'emp_0011') for lifecycle_id 'lcq_00023'. Employee has no assigned hardware. You should follow standard termination policy for software-only user."),
actions=[
Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0011"}),
Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00023", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}}),
Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00023", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}}),
Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0011"}),
Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00024"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00023", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}}),
Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00025"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00023", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}}),
Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0011"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00023", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}}),
Action(name="GetUserAsset", kwargs={"employee_id": "emp_0011"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00023", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}}),
],
outputs=["acc_51e138"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-012",
        instruction=(
            "Coordinate the onboarding of the new HRBP, Quinn Miller (hr-222), in the HR department for lifecycle_id 'lcq_00024'. Note that their required hardware, a '16-inch OrionBook Pro', is currently out of stock. You need to provide all necessary software access and subsequently create a TaskTrack ticket to report the hardware shortage."
            "You find that their required hardware, a '16-inch OrionBook Pro', is out of stock. "
            "You must provision all their software access and then escalate the hardware shortage by creating a TaskTrack ticket."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Quinn Miller", "hr_id": "hr-222", "department": "HR", "job_title": "HRBP"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00024", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_reesea222"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "HR", "job_title": "HRBP"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_reesea222", "group_ids": ["grp_hr_82f8", "grp_hr_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00024", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_reesea222"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_reesea222", "employee_id": "emp_222", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00024", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_reesea222", "employee_id": "emp_222", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00024", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "16-inch OrionBook Pro"}),
            Action(
                name="CreateJiraTicket",
                kwargs={
                    "issue_type": "Hardware Shortage",
                    "summary": "HARDWARE_SHORTAGE: lcq_00024 - 16-inch OrionBook Pro",
                },
            ),
            Action(
                name="CreateAuditRecord",
                kwargs={"lifecycle_id": "lcq_00024", "event": "JIRA_TICKET_CREATED", "details": {"jira_id": "ITSD-1013"}},
            ),
        ],
        outputs=["ITSD-1013"],
    ),
Task(
annotator="0",
user_id="it-help-desk-v4-013",
instruction=("You must handle the offboarding exception for Cameron Patel (employee_id 'emp_0013') for lifecycle_id 'lcq_00025'. Initial employee ID lookup may fail. You should use UPN fallback to complete standard termination process."),
actions=[
Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0013"}),
Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_78fb5c", "status": "inactive"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00025", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_78fb5c"}}),
Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_78fb5c", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00025", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_78fb5c"}}),
Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0013"}),
Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00029"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00025", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00029"}}),
Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00030"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00025", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00030"}}),
Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00031"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00025", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00031"}}),
Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0013"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00025", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0013"}}),
Action(name="GetUserAsset", kwargs={"employee_id": "emp_0013"}),
Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_0013", "asset_id": "ast_0033", "process": "offboarding_return"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00025", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "return_code": "RT0022"}}),
],
outputs=["acc_78fb5c"],
),
Task(
annotator="0",
user_id="it-help-desk-v4-014",
instruction=("You must onboard new Content Strategist Emerson Davis (hr-223) in Marketing for lifecycle_id 'lcq_00026'. Role requires CreativeWorks Creative Cloud license. You should create ticket for license shortage if needed."),
actions=[
Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Emerson Davis", "hr_id": "hr-223", "department": "Marketing", "job_title": "Content Strategist"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00026", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_peytont223"}}),
Action(name="LookupRoleProfile", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
Action(name="AddUserToGroups", kwargs={"account_id": "acc_peytont223", "group_ids": ["grp_marketing_719b", "grp_marketing_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00026", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_peytont223"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_peytont223", "employee_id": "emp_223", "license_id": "lic_m365_e3"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00026", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_peytont223", "license_id": "lic_m365_e3"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_peytont223", "employee_id": "emp_223", "license_id": "lic_slack_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00026", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_peytont223", "license_id": "lic_slack_ent"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_salesforce"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_peytont223", "employee_id": "emp_223", "license_id": "lic_salesforce"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00026", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_peytont223", "license_id": "lic_salesforce"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_adobe_cc"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_peytont223", "employee_id": "emp_223", "license_id": "lic_adobe_cc"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_adobe_cc", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00026", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_peytont223", "license_id": "lic_adobe_cc"}}),
Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_223"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00026", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_223", "asset_id": "ast_0013"}}),
Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_223", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00026", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_peytont223"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-015",
        instruction=(
            "Handle the offboarding process for terminated employee Peyton Shah (employee_id 'emp_0015') concerning lifecycle_id 'lcq_00027'. Follow the standard termination procedure to securely deprovision access. Since no hardware is assigned, your procedure should end after verifying this."
            "You must follow standard termination policy to securely deprovision access. Since you will find no hardware assigned, your workflow should conclude after auditing this fact."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0015"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_3818d8", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00027", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_3818d8", "group_ids": ["grp_operations_dcb3", "grp_operations_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00027", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0015"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00034"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00027", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00034"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00035"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00027", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00035"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0015"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00027", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0015"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0015"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00027", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_3818d8"}}),
        ],
        outputs=["acc_3818d8"],
    ),
Task(
annotator="0",
user_id="it-help-desk-v4-016",
instruction=("You must onboard new Senior Software Engineer Hayden Brown (hr-224) in Engineering for lifecycle_id 'lcq_00028'. You should follow standard policy to fully provision the user with appropriate access, groups, licenses, and hardware."),
actions=[
Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Hayden Brown", "hr_id": "hr-224", "department": "Engineering", "job_title": "Senior Software Engineer"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00028", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_dakotaj224"}}),
Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "Senior Software Engineer"}),
Action(name="AddUserToGroups", kwargs={"account_id": "acc_dakotaj224", "group_ids": ["grp_engineering_639b", "grp_engineering_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00028", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_dakotaj224"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_dakotaj224", "employee_id": "emp_224", "license_id": "lic_m365_e3"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00028", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_dakotaj224", "license_id": "lic_m365_e3"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_dakotaj224", "employee_id": "emp_224", "license_id": "lic_github_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00028", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_dakotaj224", "license_id": "lic_github_ent"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_dakotaj224", "employee_id": "emp_224", "license_id": "lic_slack_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00028", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_dakotaj224", "license_id": "lic_slack_ent"}}),
Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_224"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00028", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_224", "asset_id": "ast_0013"}}),
Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_224", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00028", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_dakotaj224"],
),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-017",
        instruction=(
            "You are required to address an offboarding exception for an employee linked to lifecycle_id 'lcq_00029'. Provided with the employee ID 'emp_0999' and UPN 'blake.martin@company.com', verify that neither entry appears in the directory. Your job is to confirm that both searches are unsuccessful and then raise the issue by creating an 'identity_not_found' TaskTrack ticket."
            "You have been given the employee ID 'emp_0999' and UPN 'blake.martin@company.com', but you find that neither exists in the directory. "
            "Your task is to confirm both lookups fail and then escalate by creating an 'identity_not_found' TaskTrack ticket."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0999"}),
            Action(
                name="CreateAuditRecord",
                kwargs={
                    "lifecycle_id": "lcq_00029",
                    "event": "LOOKUP_FAILED",
                    "details": {"lookup_value": "emp_0999"},
                },
            ),
            Action(
                name="GetUserByUpnOrHrId",
                kwargs={"user_lookup": "blake.martin@company.com"},
            ),
            Action(
                name="CreateAuditRecord",
                kwargs={
                    "lifecycle_id": "lcq_00029",
                    "event": "LOOKUP_FAILED",
                    "details": {"lookup_value": "blake.martin@company.com"},
                },
            ),
            Action(
                name="CreateJiraTicket",
                kwargs={
                    "issue_type": "identity_not_found",
                    "summary": "OFFBOARDING_FAILURE: lcq_00029 - IDENTITY_NOT_FOUND",
                },
            ),
            Action(
                name="CreateAuditRecord",
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
annotator="0",
user_id="it-help-desk-v4-018",
instruction=("You are onboarding a new 'QA Engineer', Blake Anderson (hr-225), in 'Engineering' for lifecycle_id 'lcq_00030'. The goal is to fully provision the user. You must create the account ('acc_sawyert225'), assign all role-based groups and licenses, and provision a laptop ('ast_0013'). You must ensure every action is audited."),
actions=[
Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Blake Anderson", "hr_id": "hr-225", "department": "Engineering", "job_title": "QA Engineer"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00030", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_sawyert225"}}),
Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "QA Engineer"}),
Action(name="AddUserToGroups", kwargs={"account_id": "acc_sawyert225", "group_ids": ["grp_engineering_addd", "grp_engineering_all"]}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00030", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_sawyert225"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_sawyert225", "employee_id": "emp_225", "license_id": "lic_m365_e3"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00030", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_sawyert225", "license_id": "lic_m365_e3"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_sawyert225", "employee_id": "emp_225", "license_id": "lic_github_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00030", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_sawyert225", "license_id": "lic_github_ent"}}),
Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
Action(name="AssignLicense", kwargs={"account_id": "acc_sawyert225", "employee_id": "emp_225", "license_id": "lic_slack_ent"}),
Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00030", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_sawyert225", "license_id": "lic_slack_ent"}}),
Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_225"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00030", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_225", "asset_id": "ast_0013"}}),
Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_225", "asset_id": "ast_0013", "process": "onboarding"}),
Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00030", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "dwf_00022", "pickup_code": "PU0022"}}),
],
outputs=["acc_sawyert225"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-019",
        instruction=(
            "You are responsible for coordinating a complete and compliant offboarding for Sawyer Harris (employee_id 'emp_0019') for lifecycle_id 'lcq_00031'. Your objective is to securely deprovision all access and assets following standard offboarding procedures. Begin by locating the user's account ('acc_1d0980'), disabling it, removing them from groups, identifying and revoking their license assignments, archiving their mailbox, and arranging the return of their asset ('ast_0031'). Ensure that each IAM step is audited."
            "Your goal is to securely deprovision all access and assets according to standard offboarding procedures. "
            "You must find the user's account ('acc_1d0980'), disable it, remove them from groups, find and revoke their license assignments, "
            "archive their mailbox, and schedule the return of their asset ('ast_0031'). You must ensure every IAM step is audited."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0019"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_1d0980", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00031", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_1d0980"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_1d0980", "group_ids": ["grp_operations_9079", "grp_operations_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00031", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_1d0980"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0019"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00044"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00031", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00044"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00045"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00031", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00045"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0019"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00031", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0019"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0019"}),
            Action(
                name="CreateDeviceWorkflow",
                kwargs={
                    "employee_id": "emp_0019",
                    "asset_id": "ast_0031",
                    "process": "offboarding_return",
                },
            ),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00031", "event": "DEVICE_WORKFLOW_CREATED", "details": {"asset_id": "ast_0031"}}),
        ],
        outputs=["acc_1d0980"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-020",
    instruction=(
        "You are tasked with handling the onboarding of a new 'Support Specialist', Remy Clark (hr-226), in the 'Support' department for lifecycle_id 'lcq_00032'. Be sure to follow the entire standard procedure to provision their account, role-based groups, licenses, and a laptop, ensuring every IAM action is audited."
        "You must follow the full, standard procedure to provision their account, role-based groups, licenses, and a laptop, ensuring every IAM action is audited."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Remy Clark", "hr_id": "hr-226", "department": "Support", "job_title": "Support Specialist"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00032", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_loganh226"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Support", "job_title": "Support Specialist"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_loganh226", "group_ids": ["grp_support_a407", "grp_support_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00032", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_loganh226"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_loganh226", "employee_id": "emp_226", "license_id": "lic_m365_e3"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00032", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_loganh226", "employee_id": "emp_226", "license_id": "lic_slack_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00032", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_226"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00032", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_226_ast_0013", "employee_id": "emp_226", "asset_id": "ast_0013", "process": "onboarding"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00032", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_226_ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_loganh226"],
),
Task(
        annotator="0",
        user_id="it-help-desk-v4-021",
        instruction=(
            "Handle the creation of the monthly Service Desk Health Report for the lifecycle 'lcq_00105'. Include detailed performance metrics derived from recent ticket activities for the management's review. Set it-management-dl@company.com as the default email for notifications if no other default is specified."
            "Provide comprehensive performance metrics based on recent ticket activity for management review. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00105", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 30, "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ExportRecentTickets", kwargs={"days": 30}),
            Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00105", "event": "MONTHLY_REPORT_GENERATED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00105", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00105", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
Task(
    annotator="0",
    user_id="it-help-desk-v4-022",
    instruction=("You are onboarding a new 'Support Manager', Skyler Lopez (hr-227), in 'Support' for lifecycle_id 'lcq_00034'. Complete the standard onboarding process to provision their account, role-based access, and hardware."),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Skyler Lopez", "hr_id": "hr-227", "department": "Support", "job_title": "Support Manager"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00034", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_kendallc227"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Support", "job_title": "Support Manager"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_kendallc227", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00034", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_kendallc227"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_kendallc227", "employee_id": "emp_227", "license_id": "lic_m365_e3"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00034", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_kendallc227", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_kendallc227", "employee_id": "emp_227", "license_id": "lic_slack_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00034", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_kendallc227", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_227"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00034", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_227", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_227_ast_0013", "employee_id": "emp_227", "asset_id": "ast_0013", "process": "onboarding"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00034", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_227_ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_kendallc227"],
),
Task(
    annotator="0",
    user_id="it-help-desk-v4-023",
    instruction=("You must offboard the terminated employee Kendall Garcia (employee_id 'emp_0023') for lifecycle_id 'lcq_00035'. Your goal is to securely deprovision all access and assets, including their account ('acc_696506'), licenses, and assigned hardware ('ast_0041'), ensuring every step is audited."),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0023"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_696506", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00035", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_696506"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_696506", "group_ids": ["grp_it_2990", "grp_it_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00035", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_696506"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0023"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00053"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00035", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00053"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00054"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00035", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00054"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00055"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00035", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00055"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0023"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00035", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0023"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0041", "employee_id": "emp_0023", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0023_ast_0041"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00035", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0023_ast_0041"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_696506"],
),
Task(
    annotator="0",
    user_id="it-help-desk-v4-024",
    instruction=("You are onboarding a new 'Operations Manager', Devin Martinez (hr-228), in 'Operations' for lifecycle_id 'lcq_00036'. The goal is to fully provision the user. You must create the account ('acc_elliotl228'), assign all role-based groups and licenses, and provision a laptop ('ast_0013'). You must ensure every action is audited."),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Devin Martinez", "hr_id": "hr-228", "department": "Operations", "job_title": "Operations Manager"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00036", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_elliotl228"}}),
        Action(name="LookupRoleProfile", kwargs={"department": "Operations", "job_title": "Operations Manager"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_elliotl228", "group_ids": ["grp_operations_9079", "grp_operations_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00036", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_elliotl228"}}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_elliotl228", "employee_id": "emp_228", "license_id": "lic_m365_e3"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00036", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_elliotl228", "license_id": "lic_m365_e3"}}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_elliotl228", "employee_id": "emp_228", "license_id": "lic_slack_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00036", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_elliotl228", "license_id": "lic_slack_ent"}}),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_228"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00036", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_228", "asset_id": "ast_0013"}}),
        Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_228_ast_0013", "employee_id": "emp_228", "asset_id": "ast_0013", "process": "onboarding"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00036", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_228_ast_0013"}}),
    ],
    outputs=["acc_elliotl228"],
),
Task(
    annotator="0",
    user_id="it-help-desk-v4-025",
    instruction=(
        "Because of a compliance audit requirement, you need to handle a comprehensive offboarding for Riley Wang (employee_id 'emp_0011') for lifecycle_id 'lcq_00080'. This involves strict adherence to our data retention policies and complete access deprovisioning to meet regulatory standards."
        "This requires strict adherence to our data retention policies and complete access deprovisioning to meet regulatory standards."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0011"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0011"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00024"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00025"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0011"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}}),
        Action(name="GetUserAsset", kwargs={"employee_id": "emp_0011"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}}),
        Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_return_emp_0011_none", "employee_id": "emp_0011", "asset_id": "none", "process": "device_return"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0011_none", "devices_scheduled": 0}}),
    ],
    outputs=["acc_51e138"],
),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-026",
        instruction=(
            "As an IT manager, your responsibility for lifecycle_id 'lcq_00038' is to coordinate the generation of the standard daily Service Desk Health Report for the past 30 days. You must follow the entire, standard procedure to create the final PDF and CSV reports, save the metrics, and inform the management team."
            "You must follow the complete, standard procedure to produce the final PDF and CSV reports, save the metrics, and notify the management team."
        ),
        actions=[
            Action(name="ExportRecentTickets", kwargs={"days": 30}),
            Action(
                name="CalculateTicketKpis",
                kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"},
            ),
            Action(
                name="GenerateHealthReportPdf",
                kwargs={"kpis": { "total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5 }},
            ),
            Action(
                name="SaveReportToMetricsDb",
                kwargs={"kpis": { "total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5 }},
            ),
            Action(
                name="NotifyTeamOfReport",
                kwargs={
                    "pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf",
                    "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv",
                },
            ),
            Action(
                name="CreateAuditRecord",
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
        annotator="0",
        user_id="it-help-desk-v4-027",
        instruction=(
            "As an IT automation engineer, your responsibility is to re-enable the directory account for the re-hired employee Jordan Kim ('acc_e2a5e9'). Subsequently, ensure they are fully provisioned with the standard groups, license bundle, and a standard laptop for their position as a 'Systems Engineer' in 'IT' for lifecycle_id 'lcq_00039'."
            "You must then fully provision them with the standard groups, license bundle, and a standard laptop for their role as a 'Systems Engineer' in 'IT' for lifecycle_id 'lcq_00039'."
        ),
        actions=[
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_e2a5e9", "status": "enabled"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00039", "event": "ACCOUNT_ENABLED", "details": {"account_id": "acc_e2a5e9"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "IT", "job_title": "Systems Engineer"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_e2a5e9", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00039", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_e2a5e9"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_e2a5e9", "employee_id": "emp_0007", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_e2a5e9", "employee_id": "emp_0007", "license_id": "lic_github_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_e2a5e9", "employee_id": "emp_0007", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00039", "event": "LICENSES_ASSIGNED_COMPLETE", "details": {"account_id": "acc_e2a5e9"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0007"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00039", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_0007", "asset_id": "ast_0013", "process": "onboarding"}),
        ],
        outputs=["acc_e2a5e9"],
    ),

             Task(
        annotator="0",
        user_id="it-help-desk-v4-028",
        instruction=(
            "Your responsibility is to coordinate a complete, compliant offboarding for Sam Tran (employee_id 'emp_0004') for lifecycle_id 'lcq_00040'. You need to follow the policy-driven offboarding process thoroughly, including addressing scenarios where no hardware is assigned."
            "You must follow the complete, policy-driven offboarding sequence, including handling cases where no hardware is assigned."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0004"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_38d007", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00040", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_38d007"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_38d007", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00040", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_38d007"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0004"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00009"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00040", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00009"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00010"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00040", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00010"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00011"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00040", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00011"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0004"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00040", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0004"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0004"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00040", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_38d007"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_38d007"],
    ),
            Task(
        annotator="0",
        user_id="it-help-desk-v4-029",
        instruction=(
            "Handle a role transition for Sam Tran (employee_id 'emp_0004') regarding lifecycle_id 'lcq_00041'. Morgan is transferring from 'Systems Engineer' to 'Identity Engineer' within the 'IT' department. Completely deprovision their previous access and set up all necessary access for the new position, auditing every IAM procedure."
            "They are moving from 'Systems Engineer' to 'Identity Engineer' within the 'IT' department. You must fully deprovision their old access and provision all access for the new role, ensuring every IAM step is audited."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0004"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_38d007", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00041", "event": "OLD_GROUPS_REMOVED", "details": {"account_id": "acc_38d007"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0004"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00009"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00009"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00010"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00010"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00011"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00011"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "IT", "job_title": "Identity Engineer"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_38d007", "group_ids": ["grp_it_b55e", "grp_it_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00041", "event": "NEW_GROUPS_ASSIGNED", "details": {"account_id": "acc_38d007"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_38d007", "employee_id": "emp_0004", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_38d007", "employee_id": "emp_0004", "license_id": "lic_github_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_github_ent"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_38d007", "employee_id": "emp_0004", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00041", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
        ],
        outputs=["acc_38d007"],
    ),

            Task(
    annotator="0",
    user_id="it-help-desk-v4-030",
    instruction=(
        "As an IT manager, for lifecycle 'lcq_00042', coordinate the preparation of the service desk report for the last 90 days. This quarterly evaluation necessitates thorough performance metrics without requiring PDF documentation. Confirm that all data is accurately stored in the metrics database for reports to executives."
        "This quarterly review requires comprehensive performance metrics but no PDF documentation. "
        "Ensure all data is properly archived in the metrics database for executive reporting."
    ),
    actions=[
        Action(name="ExportRecentTickets", kwargs={"days": 90}),
        Action(
            name="CalculateTicketKpis",
            kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"},
        ),
        Action(
            name="SaveReportToMetricsDb",
            kwargs={"kpis": { "total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5 }},
        ),
        Action(
            name="CreateAuditRecord",
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
    annotator="0",
    user_id="it-help-desk-v4-031",
    instruction=(
        "Manage the onboarding of contractor 'Alex Kirby' (hr-901) for the role of 'Systems Engineer' in IT under lifecycle 'lcq_00043'. Execute the entire contractor onboarding procedure, including setting up accounts and assigning groups. Contractors are provided with directory accounts, granting email access but excluding any licensed software or hardware assets."
        "Handle the contractor onboarding process including account provisioning and group assignments. "
        "Contractors receive directory accounts which provide email access, but no licensed software or hardware assets."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Alex Kirby", "hr_id": "hr-901", "department": "IT", "job_title": "Systems Engineer"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00043", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_alexk901"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "IT", "job_title": "Systems Engineer"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_alexk901", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00043", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_alexk901"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_alexk901"],
),
            Task(
        annotator="0",
        user_id="it-help-desk-v4-032",
        instruction=(
            "Coordinate the offboarding process for employee 'emp_0016' (Hayden Brown) associated with lifecycle 'lcq_00044'. You must execute the full and irreversible offboarding protocol: deactivate the account, remove group memberships, revoke all licenses, archive the mailbox, and arrange for asset return, ensuring an audit trail for each action."
            "You must follow the complete and immutable offboarding sequence: disable their account, remove groups, revoke all assigned licenses, "
            "archive their mailbox, and schedule the return of their asset, ensuring every step is audited."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0016"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_0099f1", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00044", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_0099f1"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(
                name="RemoveUserFromGroups",
                kwargs={
                    "account_id": "acc_0099f1",
                    "group_ids": ["grp_marketing_719b", "grp_marketing_all"],
                },
            ),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00044", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_0099f1"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0016"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00036"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00044", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00036"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00037"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00044", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00037"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00038"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00044", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00038"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0016"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00044", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0016"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0016"}),
            Action(
                name="CreateDeviceWorkflow",
                kwargs={
                    "workflow_id": "wf_return_emp_0016_ast_0022",
                    "employee_id": "emp_0016",
                    "asset_id": "ast_0022",
                    "process": "offboarding_return",
                },
            ),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00044", "event": "DEVICE_RETURN_SCHEDULED", "details": {"asset_id": "ast_0022"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_0099f1"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-033",
        instruction=(
            "Coordinate the onboarding of a new VIP, 'Jordan Rivera' (hr-235), who holds the position of 'Executive VP' in the 'Executive' department for lifecycle 'lcq_00045'. Upon noticing that their role profile isn't defined in the system, your responsibility is to establish their user account and subsequently escalate the absence of the profile by initiating a 'missing_role_profile' ticket with a P3 priority level."
            "You discover that their role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket with P3 priority."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Jordan Rivera", "hr_id": "hr-235", "department": "Executive", "job_title": "Executive VP"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00045", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordanr235"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Executive", "job_title": "Executive VP"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00045 - MISSING_ROLE_PROFILE 'Executive VP'", "priority": "P3"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00045", "event": "ONBOARDING_BLOCKED", "details": {"reason": "Missing role profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-034",
        instruction=(
            "Handle a software-only onboarding for the new 'Recruiter', 'Sam Jones' (hr-230), within 'HR' for lifecycle 'lcq_00046'. Your duty is to set up their account and allocate their standard software package, guaranteeing that every IAM step undergoes auditing and complies with requirements."
            "Your task is to create their account and assign their standard software bundle, ensuring each IAM step is audited and compliant."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Sam Jones", "hr_id": "hr-230", "department": "HR", "job_title": "Recruiter"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00046", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_samj230"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "HR", "job_title": "Recruiter"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_samj230", "group_ids": ["grp_hr_92d4", "grp_hr_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00046", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_samj230"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_samj230", "employee_id": "emp_230", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00046", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_samj230", "employee_id": "emp_230", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00046", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_samj230"],
    ),
        Task(
    annotator="0",
    user_id="it-help-desk-v4-035",
    instruction=(
        "Currently, you are investigating a significant issue with the report generation process for lifecycle 'lcq_00047'. Your role involves conducting a thorough incident analysis by contrasting KPIs from the most recent successful report execution with present ticket data. Archive your analysis results in the metrics database and proceed to escalate via a P1 TaskTrack incident ticket."
        "Your task is to perform a comprehensive incident analysis by comparing KPIs from the last successful report run with current ticket data. "
        "You must archive the analysis findings in the metrics database and escalate through a P1 TaskTrack incident ticket."
    ),
    actions=[
        Action(name="GetLastReportRun", kwargs={}),
        Action(name="ExportRecentTickets", kwargs={"days": 30}),
        Action(
            name="CalculateTicketKpis",
            kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"},
        ),
        Action(
            name="CompareTicketKpis",
            kwargs={
                "previous_kpis": {"total_open": 45, "avg_age_open_hours": 22.0, "avg_ttr_mins": 1300, "pct_closed_1d": 65.0, "p1_open_count": 4},
                "current_kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5},
            },
        ),
        Action(
            name="SaveReportToMetricsDb",
            kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}},
        ),
        Action(
            name="CreateAuditRecord",
            kwargs={
                "lifecycle_id": "lcq_00047",
                "event": "INCIDENT_RESPONSE_INITIATED",
                "details": {"incident_type": "report_generation_failure", "analysis_completed": True},
                "timestamp": "2025-08-15T13:00:00Z",
            },
        ),
        Action(
            name="CreateJiraTicket",
            kwargs={
                "issue_type": "Incident",
                "summary": "INCIDENT lcq_00047: REPORTING_FAILURE | ANALYSIS: Open tickets changed by 1. P1 tickets changed by 1.",
                "priority": "P1",
            },
        ),
        Action(
            name="CreateAuditRecord",
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
    annotator="0",
    user_id="it-help-desk-v4-036",
    instruction=(
        "As part of the onboarding process for the intern 'Chris Green' (hr-902) in the 'Marketing' department as a 'Growth Marketer' for lifecycle 'lcq_00048', your assignment is to adhere to the full, standard onboarding protocol: set up their account, allocate groups, provide the necessary M365 E3 license, and issue a standard laptop, ensuring all steps are audited."
        "Your task is to follow the complete, standard onboarding procedure: create their account, assign groups, provision the required M365 E3 license, and assign a standard laptop, auditing all actions."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Chris Green", "hr_id": "hr-902", "department": "Marketing", "job_title": "Growth Marketer"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00048", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_chrisg902"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Marketing", "job_title": "Growth Marketer"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_chrisg902", "group_ids": ["grp_marketing_231e", "grp_marketing_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00048", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_chrisg902"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_chrisg902", "employee_id": "emp_902", "license_id": "lic_m365_e3"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00048", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_902"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00048", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_902_ast_0013", "employee_id": "emp_902", "asset_id": "ast_0013", "process": "onboarding"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00048", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_902_ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_chrisg902"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-037",
        instruction=(
            "Regarding lifecycle 'lcq_00049', handle the offboarding of the terminated employee 'emp_0017' (Dakota Wilson). Your responsibility includes adhering to the complete, policy-driven offboarding procedure by deprovisioning their account, groups, licenses, and mailbox, while auditing every IAM step. This user has no hardware assigned."
            "Your task is to follow the complete, policy-driven offboarding sequence, ensuring you deprovision their account, groups, licenses, and mailbox, auditing every IAM step. This user has no hardware assigned."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0017"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_82aecf", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00049", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_82aecf"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_82aecf", "group_ids": ["grp_finance_c147", "grp_finance_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00049", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_82aecf"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0017"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00039"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00049", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00039"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00040"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00049", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00040"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0017"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00049", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0017"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0017"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00049", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_82aecf"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_82aecf"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-038",
    instruction=(
        "A potential security issue requires your investigation. A manager has requested an audit to ensure the effective offboarding of terminated employee 'emp_0029' (Lane Taylor) under lifecycle 'lcq_00050'. You should inspect their account and fully address any active access found, in line with security policy. Document all findings and remediation actions taken in a formal ticket."
        "You need to investigate their account and fully remediate any active access found according to security policy. "
        "You must document your findings and all remediation actions taken in a formal ticket."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0029"}),
        Action(name="GetUserAsset", kwargs={"employee_id": "emp_0029"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0029"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_48efe8", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00050", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_48efe8"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_48efe8", "group_ids": ["grp_finance_5d50", "grp_finance_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00050", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_48efe8"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00071"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00050", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00071"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00072"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00050", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00072"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0029"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00050", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0029"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_0029", "asset_id": "ast_0039", "process": "offboarding_return", "workflow_id": "wf_return_emp_0029_ast_0039"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00050", "event": "DEVICE_RETURN_SCHEDULED", "details": {"asset_id": "ast_0039"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(
            name="CreateJiraTicket",
            kwargs={
                "issue_type": "Task",
                "summary": "OFFBOARDING_SECURITY_AUDIT: lcq_00050 - emp_0029",
                "priority": "P3",
            },
        ),
        Action(
            name="CreateAuditRecord",
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
        annotator="0",
        user_id="it-help-desk-v4-039",
        instruction=(
            "Regarding lifecycle 'lcq_00051', you are facilitating the onboarding of a new 'Accounting Manager', 'Alex Ray' (hr-231), in 'Finance'. Your responsibility is to set up their account and grant software access. The user has asked for a 'Vertex Vertex Pro 7440', however, you discover there is no stock available. You need to generate a ticket due to the hardware shortage."
            "Your task is to provision their account and software access. The user has requested a 'Vertex Vertex Pro 7440', "
            "but you find that none are in stock. You must create a ticket for the hardware shortage."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Alex Ray", "hr_id": "hr-231", "department": "Finance", "job_title": "Accounting Manager"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00051", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_alexr231"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Finance", "job_title": "Accounting Manager"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_alexr231", "group_ids": ["grp_finance_5d50", "grp_finance_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00051", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_alexr231"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_alexr231", "employee_id": "emp_231", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00051", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_alexr231", "employee_id": "emp_231", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00051", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "Vertex Vertex Pro 7440"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "Hardware Shortage", "summary": "HARDWARE_SHORTAGE: lcq_00051 - Vertex Vertex Pro 7440"}),
        ],
        outputs=["ITSD-1013"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-040",
    instruction=(
        "Concerning lifecycle 'lcq_00052', your duty is to examine a reported decline in service desk performance. Match the current ticket KPIs with the last successful report compilation. Should there be an increase in open P1 tickets, escalate the matter by opening a P1 'Incident' ticket that outlines the change."
        "Compare the current ticket KPIs against the last successful report run. If the number of open P1 tickets has increased, "
        "escalate by creating a P1 'Incident' ticket summarizing the change."
    ),
    actions=[
        Action(name="GetLastReportRun", kwargs={}),
        Action(name="ExportRecentTickets", kwargs={"days": 30}),
        Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(name="CompareTicketKpis", kwargs={
            "previous_kpis": {"total_open": 45, "avg_age_open_hours": 22.0, "avg_ttr_mins": 1300, "pct_closed_1d": 65.0, "p1_open_count": 4},
            "current_kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5},
        }),
        Action(name="CreateJiraTicket", kwargs={
            "issue_type": "Incident",
            "summary": "PERFORMANCE_DEGRADATION: lcq_00052 | P1_TICKET_INCREASE: 1",
            "priority": "P1",
        }),
        Action(name="CreateAuditRecord", kwargs={
            "lifecycle_id": "lcq_00052",
            "event": "INCIDENT_ESCALATED",
            "details": {"issue_type": "Incident", "reason": "P1 ticket count increased", "jira_id": "ITSD-1013"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
    ],
    outputs=["ITSD-1013"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-041",
        instruction=(
            "Manage the promotion of employee 'emp_0022' (Skyler Lopez) from 'Ops Coordinator' to 'Operations Manager' for lifecycle 'lcq_00053'. You are required to update their role-based access by eliminating their previous group memberships, assigning the new ones, and ensuring the provision of the 'M365 E5' license for their updated role."
            "Your task is to update their role-based access. You must remove their old group memberships, assign the new ones, and provision the required 'M365 E5' license for their new role."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0022"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_51ba73", "group_ids": ["grp_operations_772e", "grp_operations_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00053", "event": "PROMOTION_OLD_GROUPS_REMOVED", "details": {"account_id": "acc_51ba73"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Operations", "job_title": "Operations Manager"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_51ba73", "group_ids": ["grp_operations_9079", "grp_operations_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00053", "event": "PROMOTION_NEW_GROUPS_ASSIGNED", "details": {"account_id": "acc_51ba73"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e5"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_51ba73", "employee_id": "emp_0022", "license_id": "lic_m365_e5"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e5", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00053", "event": "PROMOTION_NEW_LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e5"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_51ba73"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-042",
    instruction=(
        "Facilitate the offboarding of employee 'emp_0027' (Jesse Moore) for lifecycle 'lcq_00054' in line with the standard termination policy. The procedure must fully deprovision their account, groups, and any licenses. You notice they lack assigned hardware, which requires auditing to finalize the process."
        "The process must include fully deprovisioning their account, groups, and all licenses. You discover they have no assigned hardware, which must be audited to complete the process."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0027"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_5494f2", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00054", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_5494f2"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_5494f2", "group_ids": ["grp_marketing_231e", "grp_marketing_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00054", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_5494f2"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0027"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00065"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00054", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00065"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00066"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00054", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00066"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00067"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00054", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00067"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0027"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00054", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0027"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserAsset", kwargs={"employee_id": "emp_0027"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00054", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_5494f2"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_5494f2"],
),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-043",
    instruction=(
        "Handle the onboarding of a new 'VP of Product', 'Riley Kim' (hr-236), within the 'Product' department for lifecycle 'lcq_00055'. Upon creating their account, it becomes apparent that their role profile is undefined in the system. It is necessary to escalate this by logging a P2 ticket that includes the lifecycle ID and the specific missing role."
        "You create their account but discover that their role profile is not defined in the system. You must escalate this by creating a P2 ticket that details the lifecycle ID and the specific missing role."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Riley Kim", "hr_id": "hr-236", "department": "Product", "job_title": "VP of Product"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00055", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyk236"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Product", "job_title": "VP of Product"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "MISSING_ROLE_PROFILE: lcq_00055 | department: Product | job_title: VP of Product", "priority": "P2"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00055", "event": "ONBOARDING_BLOCKED", "details": {"reason": "Missing role profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-044",
        instruction=(
            "Coordinate a software-only offboarding for 'emp_0011' (Riley Wang) specific to lifecycle 'lcq_00056', ensuring compliance with the complete and immutable offboarding policy, which includes hardware verification."
            "ensuring the process follows the complete, immutable offboarding policy, including hardware verification."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0011"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00056", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00056", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00024"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00056", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00025"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00056", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00056", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0011"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00056", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_51e138"],
    ),

    Task(
    annotator="0",
    user_id="it-help-desk-v4-045",
    instruction=(
        "The objective is to fully set up a new 'Controller', 'Morgan Kai' (hr-233), in 'Finance' for lifecycle 'lcq_00057'. This includes creating their account, assigning groups, obtaining all necessary licenses, and providing them with a standard laptop following the immutable onboarding policy."
        "This involves creating their account, assigning groups, all required licenses, and a standard laptop according to the immutable onboarding policy."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Morgan Kai", "hr_id": "hr-233", "department": "Finance", "job_title": "Controller"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00057", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_morgank233"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Finance", "job_title": "Controller"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_morgank233", "group_ids": ["grp_finance_c147", "grp_finance_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00057", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_morgank233"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_morgank233", "employee_id": "emp_233", "license_id": "lic_m365_e3"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00057", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_morgank233", "employee_id": "emp_233", "license_id": "lic_slack_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00057", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_233"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00057", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_233"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_morgank233"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-046",
    instruction=(
        "The assignment is to manage a complex re-onboarding for employee 'emp_0007' (Jordan Kim) for lifecycle 'lcq_00058', returning to a new, undefined role as a 'Lead DevOps Engineer' in 'Engineering'. You must re-activate their account and then resolve two separate obstacles: the new role lacks a profile, and the standard temporary license ('lic_m365_e5') is also unavailable. These issues need to be escalated."
        "You must re-activate their account and then address two distinct blockers: the new role is missing a profile, and the standard temporary license ('lic_m365_e5') is also out of stock. You need to escalate both issues."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0007"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_e2a5e9", "status": "enabled"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00058", "event": "ACCOUNT_REACTIVATED", "details": {"account_id": "acc_e2a5e9"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "Lead DevOps Engineer"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "Task", "summary": "PROVISIONING_BLOCKED: lcq_00058 - MISSING_ROLE_PROFILE 'Lead DevOps Engineer'"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00058", "event": "ONBOARDING_BLOCKED", "details": {"reason": "Missing role profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "License Shortage", "summary": "LICENSE_SHORTAGE: lcq_00058 - M365 E5 license unavailable for temporary assignment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00058", "event": "TEMP_LICENSE_PROVISIONING_BLOCKED", "details": {"license_id": "lic_m365_e5", "jira_id": "ITSD-1014"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013", "ITSD-1014"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-047",
        instruction=(
            "Your responsibility is to manage an asset replacement for employee 'emp_0018' under lifecycle 'lcq_00059'. You need to remove the assignment of their old device, 'ast_0004', and set up the specified replacement, 'ast_0013'."
            "You must unassign their old device, 'ast_0004', and provision the designated replacement, 'ast_0013'."
        ),
        actions=[
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0004", "employee_id": None}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0018"}),
            Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_0018", "asset_id": "ast_0013", "process": "onboarding"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00059", "event": "ASSET_SWAP_COMPLETED", "details": {"employee_id": "emp_0018", "old_asset": "ast_0004", "new_asset": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["dwf_00022"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-048",
    instruction=(
        "Regarding lifecycle 'lcq_00060', you need to offboard 'emp_0029' (Lane Taylor). The objective is to ensure secure deprovisioning of all access and assets following standard termination protocols."
        "The goal is to securely deprovision all access and assets according to standard termination procedures."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0029"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_48efe8", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00060", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_48efe8"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_48efe8", "group_ids": ["grp_finance_5d50", "grp_finance_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00060", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_48efe8"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0029"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00071"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00060", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00071"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00072"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00060", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00072"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0029"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00060", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0029"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserAsset", kwargs={"employee_id": "emp_0029"}),
        Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_return_emp_0029_ast_0039", "employee_id": "emp_0029", "asset_id": "ast_0039", "process": "offboarding_return"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00060", "event": "DEVICE_RETURN_SCHEDULED", "details": {"asset_id": "ast_0039"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_48efe8"],
),
            Task(
        annotator="0",
        user_id="it-help-desk-v4-049",
        instruction=(
            "An identity sync process has encountered a failure, likely involving employee 'emp_0030'. For lifecycle 'lcq_00061', your responsibility is to examine the user's assigned groups and resolve their access by removing them. Afterward, disable the account and forward the issue to the relevant teams for further evaluation."
            "For lifecycle 'lcq_00061', your task is to investigate the user's assigned groups and remediate their access by removing them. "
            "You must then disable the account and escalate to the appropriate teams for further analysis."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0030"}),
            Action(name="GetUserGroupMemberships", kwargs={"account_id": "acc_db017d"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_db017d", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00061", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_db017d"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_db017d", "status": "disabled"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00061", "event": "ACCOUNT_ACCESS_SUSPENDED", "details": {"account_id": "acc_db017d"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "Incident", "summary": "INCIDENT: lcq_00061 - Account acc_db017d disabled for sync investigation", "priority": "P2"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "Task", "summary": "TASK: lcq_00061 - Forensic analysis for acc_db017d", "priority": "P1"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00061", "event": "INCIDENT_RESPONSE_INITIATED", "details": {"account_id": "acc_db017d", "jira_ids": ["ITSD-1013", "ITSD-1014"]}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013", "ITSD-1014"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-050",
    instruction=(
        "Handle the onboarding of new Systems Engineer Finley Blue (hr-234) in the IT department for lifecycle 'lcq_00062'. Execute standard onboarding protocols to set up their account, allocate the correct role-based permissions, and prepare necessary equipment."
        "Follow standard onboarding procedures to provision their account, assign appropriate role-based access, and prepare hardware."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Finley Blue", "hr_id": "hr-234", "department": "IT", "job_title": "Systems Engineer"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00062", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_finleyb234"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "IT", "job_title": "Systems Engineer"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_finleyb234", "group_ids": ["grp_it_6b89", "grp_it_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00062", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_finleyb234", "group_ids": ["grp_it_6b89", "grp_it_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_finleyb234", "license_id": "lic_m365_e3"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00062", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_finleyb234", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_finleyb234", "license_id": "lic_github_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00062", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_finleyb234", "license_id": "lic_github_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_finleyb234", "license_id": "lic_slack_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00062", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_finleyb234", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_234"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00062", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_234", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_finleyb234"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-051",
    instruction=(
        "Coordinate the onboarding of a new 'Legal Counsel', 'Kai Chen' (hr-237), following a directive from HR (memo_102). A major component of this task involves creating an entry in the lifecycle queue. Should you discover that their role profile is undefined, your objective is to escalate this issue accordingly."
    ),
    actions=[
        Action(name="AddMemoToLifecycleQueue", kwargs={"memo_id": "memo_102", "hr_id": "hr-237", "event_type": "onboarding"}),
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Kai Chen", "hr_id": "hr-237", "department": "Legal", "job_title": "Legal Counsel"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_kaic237"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Legal", "job_title": "Legal Counsel"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00013 - MISSING_ROLE_PROFILE", "priority": "P2"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
),
        Task(
    annotator="0",
    user_id="it-help-desk-v4-052",
    instruction=(
        "Facilitate a comprehensive, policy-compliant offboarding for employee 'emp_0025' (Elliot Johnson) within the lifecycle context 'lcq_00064'. Your objective is to remove all access for their account ('acc_1e8432'), which entails eliminating group associations, revoking their four assigned licenses (Salesforce, CreativeWorks, TeamChat, M365), archiving their mailbox, and arranging for the laptop return ('ast_0044'). You must ensure that every IAM action is thoroughly audited."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0025"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_1e8432", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00064", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_1e8432"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_1e8432", "group_ids": ["grp_marketing_719b", "grp_marketing_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00064", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_1e8432"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0025"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00059"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00064", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00059"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00060"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_adobe_cc", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00064", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00060"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00061"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00064", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00061"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00062"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00064", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00062"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0025"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00064", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0025"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserAsset", kwargs={"employee_id": "emp_0025"}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0044", "employee_id": "emp_0025", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0025_ast_0044"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00064", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0025_ast_0044"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0025_ast_0044"],
),

Task(
    annotator="0",
    user_id="it-help-desk-v4-053",
    instruction=(
        "As an IT manager, your responsibility is to create the daily Service Desk Health Report for lifecycle 'lcq_00065'. Your objective is to compile the final PDF and CSV reports, preserve the resulting metrics for historical tracking, and inform the management team at 'it-management-dl@company.com'."
        "Your goal is to produce the final PDF and CSV reports, save the resulting metrics for historical tracking, and notify the management team at 'it-management-dl@company.com'."
    ),
    actions=[
        Action(name="ExportRecentTickets", kwargs={"days": 30}),
        Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
        Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
        Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(
            name="CreateAuditRecord",
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
    annotator="0",
    user_id="it-help-desk-v4-054",
    instruction=(
        "Your assignment is to coordinate a full, policy-compliant offboarding for employee 'emp_0020' (River Allen) for lifecycle 'lcq_00066'. You need to disable their account, remove their groups, identify and revoke all of their assigned licenses, and archive their mailbox. You must ensure that all IAM actions are audited."
        "You must disable their account, remove their groups, find and revoke all of their assigned licenses, and archive their mailbox. You must ensure all IAM actions are audited."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0020"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_401a71", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00066", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_401a71"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_401a71", "group_ids": ["grp_hr_92d4", "grp_hr_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00066", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_401a71"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0020"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00046"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00066", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00046"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00047"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00066", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00047"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0020"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00066", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0020"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserAsset", kwargs={"employee_id": "emp_0020"}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0011", "employee_id": "emp_0020", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0020_ast_0011"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00066", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0020_ast_0011"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0020_ast_0011"],
),

    Task(
    annotator="0",
    user_id="it-help-desk-v4-055",
    instruction=(
        "Your responsibility is to handle a comprehensive, policy-compliant onboarding for a new 'IT Support Specialist', 'Morgan Casey' (hr-240), within lifecycle context 'lcq_00067'. Begin by establishing their account, then proceed to allocate role-based groups and the standard licenses appropriate for their role, and make sure to provision a laptop. However, you'll discover that the role profile is absent, so adhere to policy by initiating a TaskTrack ticket for the profile to be defined and halt any further onboarding procedures until this matter is addressed."
        "You must create their account, and then attempt to assign role-based groups and standard licenses for their role, and provision a laptop. "
        "However, you'll find the role profile doesn't exist, so you must follow policy by creating a TaskTrack ticket to have the profile defined and block further onboarding steps until this is resolved."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Morgan Casey", "hr_id": "hr-240", "department": "IT", "job_title": "IT Support Specialist"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00067", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_morganc240"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "IT", "job_title": "IT Support Specialist"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00067 - MISSING_ROLE_PROFILE"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00067", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-056",
    instruction=(
        "Your responsibility is to coordinate a detailed, policy-compliant onboarding for a new 'IT Help Desk Analyst', 'Jamie Bell' (hr-239), within lifecycle context 'lcq_00068'. Start with setting up their account, then try to assign role-based groups and provide the standard licenses associated with their role, and ensure a laptop is provided. However, you'll become aware that the role profile is missing, so follow protocol by generating a TaskTrack ticket to have the profile created and pause further onboarding processes until this issue is resolved."
        "You must create their account, and then attempt to assign role-based groups and standard licenses for their role, and provision a laptop. "
        "However, you'll find the role profile doesn't exist, so you must follow policy by creating a TaskTrack ticket to have the profile defined and block further onboarding steps until this is resolved."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Jamie Bell", "hr_id": "hr-239", "department": "IT", "job_title": "IT Help Desk Analyst"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00068", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jamieb239"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "IT", "job_title": "IT Help Desk Analyst"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00068 - MISSING_ROLE_PROFILE"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00068", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-057",
        instruction=(
            "Handle a comprehensive, policy-compliant software-only offboarding for employee 'Jesse Moore' (emp_0027) concerning lifecycle 'lcq_00072'. Ensure you disable their account, remove their groups, locate and revoke all assigned licenses (Salesforce, TeamChat, M365), and archive their mailbox. The task is finalized after confirming they possess no assigned hardware. Ensure all IAM actions are audited."
            "You must disable their account, remove their groups, find and revoke all of their assigned licenses (Salesforce, TeamChat, M365), and archive their mailbox. "
            "The process is complete after you verify they have no assigned hardware. You must ensure all IAM actions are audited."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0027"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_5494f2", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_5494f2"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_5494f2", "group_ids": ["grp_marketing_231e", "grp_marketing_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_5494f2"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0027"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00065"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00065"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00066"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00066"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00067"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00067"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0027"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0027"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0027"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_5494f2"}}),
        ],
        outputs=["acc_5494f2"],
    ),

Task(
    annotator="0",
    user_id="it-help-desk-v4-058",
    instruction=(
        "Coordinate the offboarding of terminated employee Kendall Garcia (employee_id 'emp_0023') for lifecycle 'lcq_00070'. Adhere to standard termination protocols to securely deprovision access, revoke licenses, and schedule asset return."
        "Follow standard termination protocols to securely deprovision access, revoke licenses, and schedule asset return."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0023"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_696506", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00070", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_696506"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_696506", "group_ids": ["grp_it_2990", "grp_it_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00070", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_696506"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0023"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00053"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00070", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00053"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00054"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00070", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00054"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00055"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00070", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00055"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0023"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00070", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0023"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0041", "employee_id": "emp_0023", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0023_ast_0041"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00070", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0023_ast_0041"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0023_ast_0041"],
),

Task(
    annotator="0",
    user_id="it-help-desk-v4-059",
    instruction=(
        "An employee, 'emp_0026' (Charlie Garcia), has a broken laptop ('ast_0052'). Within lifecycle 'lcq_00071', take charge of executing the asset swap. Your aim is to provide them a functional device, but you discover there are no 'laptop_loaner' devices available. You must escalate the shortage through the creation of a P2 TaskTrack ticket."
        "lifecycle 'lcq_00071', your task is to handle the asset swap. Your goal is to get them a working "
        "device, but you find there are no 'laptop_loaner' devices available. You must escalate the shortage "
        "by creating a P2 TaskTrack ticket."
    ),
    actions=[
        Action(name="GetUserAsset", kwargs={"employee_id": "emp_0026"}),
        Action(name="UnassignAsset", kwargs={"asset_id": "ast_0052"}),
        Action(name="CreateAuditRecord", kwargs={
            "lifecycle_id": "lcq_00071",
            "event": "BROKEN_ASSET_UNASSIGNED",
            "details": {"asset_id": "ast_0052"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop_loaner"}),
        Action(name="CreateJiraTicket", kwargs={
            "issue_type": "Hardware Shortage",
            "priority": "P2"
        }),
        Action(name="CreateAuditRecord", kwargs={
            "lifecycle_id": "lcq_00071",
            "event": "JIRA_TICKET_CREATED",
            "details": {"issue_type": "Hardware Shortage", "jira_id": "ITSD-1013"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
    ],
    outputs=["ITSD-1013"],
),

Task(
    annotator="0",
    user_id="it-help-desk-v4-060",
    instruction=(
        "Coordinate the onboarding of new Senior Software Engineer Avery Morgan (hr-238) in the Engineering department for lifecycle 'lcq_00072'. Adhere to standard onboarding procedures to set up their account, grant appropriate role-based access, and arrange hardware."
        "Follow standard onboarding procedures to provision their account, assign appropriate role-based access, and prepare hardware."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Avery Morgan", "hr_id": "hr-238", "department": "Engineering", "job_title": "Senior Software Engineer"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_averym238"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "Senior Software Engineer"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_averym238", "group_ids": ["grp_engineering_639b", "grp_engineering_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_averym238", "group_ids": ["grp_engineering_639b", "grp_engineering_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_averym238", "license_id": "lic_m365_e3"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averym238", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_averym238", "license_id": "lic_slack_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averym238", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_averym238", "license_id": "lic_github_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_averym238", "license_id": "lic_github_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_238"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00072", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_238", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_averym238"],
),

    Task(
    annotator="0",
    user_id="it-help-desk-v4-061",
    instruction=(
        "Handle a compliance check for Hayden Brown (employee_id=emp_0016). Your task involves verifying that their assigned phone is under MDM, with a creation date of 2025-07-18T11:10:00+00:00. Furthermore, validate their directory account status, group memberships against the RBAC baseline, and active license assignments. Ensure the asset remains correctly assigned and document any issues. Log all steps in the lifecycle audit record."
        "that their assigned phone is under MDM, with a creation date of 2025-07-18T11:10:00+00:00. "
        "Additionally, you must validate their directory account status, group memberships against the RBAC baseline, "
        "and active license assignments. You should confirm the asset remains correctly assigned and log any issues. "
        "Record all steps in the lifecycle audit log."
    ),
    actions=[
        Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0016"}),
        Action(name="GetDirectoryAccount", kwargs={"employee_id": "emp_0016"}),
        Action(name="CreateAuditRecord", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "ACCOUNT_STATUS_VERIFIED",
            "details": {"account_id": "acc_0099f1", "status": "enabled"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="GetUserGroupMemberships", kwargs={"account_id": "acc_0099f1"}),
        Action(name="GetBaselineForRole", kwargs={"department": "Marketing", "job_title": "Content Strategist"}),
        Action(name="CreateAuditRecord", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "GROUPS_ASSIGNED",
            "details": {"actual_groups": ["grp_marketing_719b", "grp_marketing_all"], "baseline": ["grp_marketing_719b", "grp_marketing_all"]},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="GetLicenseAssignments", kwargs={"employee_id": "emp_0016"}),
        Action(name="CreateAuditRecord", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "LICENSE_VERIFICATION_COMPLETE",
            "details": {"assignments": ["lic_salesforce", "lic_slack_ent", "lic_m365_e3"], "expected": ["lic_salesforce", "lic_slack_ent", "lic_m365_e3"]},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="FindAssets", kwargs={
            "assigned_to": "emp_0016",
            "asset_type": "phone",
            "mdm_enrolled": True
        }),
        Action(name="CreateAuditRecord", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "ASSET_VERIFICATION_COMPLETE",
            "details": {"asset_id": "ast_0022", "asset_type": "phone", "mdm_enrolled": True},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="CreateAuditRecord", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "ASSET_VERIFICATION_COMPLETE",
            "details": {"asset_id": "ast_0022", "expected_date": "2025-07-18T11:10:00+00:00", "actual_date": "2022-07-27", "status": "mismatch"},
            "timestamp": "2025-08-15T13:00:00Z"
        }),
        Action(name="RecordLifecycleAudit", kwargs={
            "lifecycle_id": "lcq_compliance_emp_0016",
            "event": "COMPLIANCE_CHECK_COMPLETED",
            "timestamp": "2025-08-15T13:00:00Z",
            "actor": "system"
        }),
    ],
    outputs=["lcq_compliance_emp_0016"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-062",
        instruction=(
            "Coordinate the issuance of a standard company laptop to Skyler Lopez (employee_id=emp_0022) from the available inventory for lifecycle 'lcq_hw_emp_0022'. Company policy necessitates consistent asset allocation using the lowest available asset ID. Confirm the device goes through full MDM enrollment and verify successful assignment and management status. Manage any hardware shortages by creating suitable escalation tickets."
        ),
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0022"}),
            Action(name="GetDirectoryAccount", kwargs={"employee_id": "emp_0022"}),
            Action(name="FindAssets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0022"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_hw_emp_0022", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0022"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_mdm_emp_0022_ast_0013", "employee_id": "emp_0022", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_mdm_emp_0022_ast_0013", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
            Action(name="UpdateAssetStatus", kwargs={"asset_id": "ast_0013", "status": "READY FOR PICKUP", "mdm_enrolled": True}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_hw_emp_0022", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_mdm_emp_0022_ast_0013", "pickup_code": "pc_mdm_emp_0022_ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="EnqueueLifecycleEvent", kwargs={"lifecycle_id": "lcq_hw_emp_0022", "memo_id": "memo_hw_emp_0022", "employee_ref": "emp_0022", "event": "hardware_provision", "status": "completed", "created_at": "2025-08-15T13:00:00Z"}),
            Action(name="FindAssets", kwargs={"asset_type": "laptop", "assigned_to": "emp_0022", "mdm_enrolled": True}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-063",
    instruction=(
        "Handle the return of the phone assigned to Micah White (employee_id=emp_0030). You must arrange the device return and initiate a corresponding MDM wipe exactly on 2025-08-15T13:00:00Z. Ensure that the asset's ownership remains unchanged until the collection process is thoroughly completed."
    ),
    actions=[
        Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0030"}),
        Action(name="FindAssets", kwargs={"asset_type": "phone", "assigned_to": "emp_0030", "mdm_enrolled": True}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0014", "employee_id": "emp_0030", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0030_ast_0014"}),
        Action(name="ScheduleMdmAction", kwargs={"asset_id": "ast_0014", "when": "2025-08-15T13:00:00Z", "action": "wipe", "workflow_id": "wf_return_emp_0030_ast_0014"}),
        Action(name="EnqueueLifecycleEvent", kwargs={"lifecycle_id": "lcq_return_emp_0030", "memo_id": "memo_return_emp_0030", "employee_ref": "emp_0030", "event": "return", "status": "queued", "created_at": "2025-08-15T13:00:00Z"}),
        Action(name="RecordLifecycleAudit", kwargs={"lifecycle_id": "lcq_return_emp_0030", "event": "DEVICE_WORKFLOW_CREATED", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
    ],
    outputs=["wf_return_emp_0030_ast_0014"],
),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-064",
    instruction=(
        "Coordinate the return of two managed phones for Lane Taylor, an Accounting Manager (employee_id=emp_0029). You are responsible for setting up distinct return workflows and arranging MDM wipes for each device at their assigned deterministic due times. Asset 'ast_0039' must be ready by 2025-07-26T17:00:00+00:00, and 'ast_0049' by 2025-07-26T17:30:00+00:00. Do not make changes to ownership records until the collection is verified."
    ),
    actions=[
        Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0029"}),
        Action(name="GetDirectoryAccount", kwargs={"employee_id": "emp_0029"}),
        Action(name="FindAssets", kwargs={"assigned_to": "emp_0029"}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0039", "employee_id": "emp_0029", "due_ts": "2025-07-26T17:00:00+00:00", "workflow_id": "wf_return_emp_0029_ast_0039"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_return_emp_0029", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0029_ast_0039"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ScheduleMdmAction", kwargs={"asset_id": "ast_0039", "when": "2025-07-26T17:00:00+00:00", "action": "wipe", "workflow_id": "wf_return_emp_0029_ast_0039"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_return_emp_0029", "event": "DEVICE_SECURITY_WIPE_SCHEDULED", "details": {"workflow_id": "wf_return_emp_0029_ast_0039"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0049", "employee_id": "emp_0029", "due_ts": "2025-07-26T17:30:00+00:00", "workflow_id": "wf_return_emp_0029_ast_0049"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_return_emp_0029", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0029_ast_0049"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ScheduleMdmAction", kwargs={"asset_id": "ast_0049", "when": "2025-07-26T17:30:00+00:00", "action": "wipe", "workflow_id": "wf_return_emp_0029_ast_0049"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_return_emp_0029", "event": "DEVICE_SECURITY_WIPE_SCHEDULED", "details": {"workflow_id": "wf_return_emp_0029_ast_0049"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0029_ast_0039", "wf_return_emp_0029_ast_0049"],
),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-065",
    instruction=(
        "Handle the provisioning of a managed laptop for Support Manager Sasha Phillips (employee_id=emp_0038) for lifecycle 'lcq_hardware_provision_emp_0038'. Ensure compliance with company policy by consistently allocating assets using the lowest available asset ID and achieving full MDM compliance for any distributed devices."
    ),
    actions=[
        Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0038"}),
        Action(name="GetDirectoryAccount", kwargs={"employee_id": "emp_0038"}),
        Action(name="FindAssets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0038"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0038", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0038"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_mdm_emp_0038_ast_0013", "employee_id": "emp_0038", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0038", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_mdm_emp_0038_ast_0013", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ast_0013"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-066",
        instruction=(
            "Coordinate the issuance of a laptop from company stock to Emerson Davis (employee_id=emp_0014). Company policy insists on maintaining consistent asset allocation with the lowest available asset ID and demands all devices be fully enrolled in MDM with complete lifecycle tracking. Confirm that the final provisioning adheres to all management and assignment criteria."
        ),
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0014"}),
            Action(name="GetDirectoryAccount", kwargs={"employee_id": "emp_0014"}),
            Action(name="FindAssets", kwargs={"asset_type": "laptop", "status": "in_stock"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0014"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0014", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0014"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_mdm_emp_0014_ast_0013", "employee_id": "emp_0014", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
            Action(name="EnqueueLifecycleEvent", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0014", "memo_id": "memo_hardware_provision_emp_0014", "employee_ref": "emp_0014", "event": "hardware_provision", "status": "queued", "created_at": "2025-08-15T13:00:00Z"}),
            Action(name="UpdateLifecycleStatus", kwargs={"lifecycle_id": "lcq_hardware_provision_emp_0014", "status": "completed", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
            Action(name="FindAssets", kwargs={"assigned_to": "emp_0014"}),
            Action(name="FindAssets", kwargs={"asset_type": "laptop", "assigned_to": "emp_0014", "mdm_enrolled": True}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-067",
        instruction=(
            "Initiate the onboarding process for new Senior Marketing Analyst River Chen (hr-240) in the Marketing department for lifecycle 'lcq_ob_emp_0040'. Upon discovering that their role profile is undefined in the system, your task is to create their user account and escalate the issue by filing a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "River Chen", "hr_id": "hr-240", "department": "Marketing", "job_title": "Senior Marketing Analyst"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_riverc240"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Marketing", "job_title": "Senior Marketing Analyst"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_ob_emp_0040 - MISSING_ROLE_PROFILE"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "AUDIT_BLOCKED", "details": {"reason": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013"],
    ),
            Task(
        annotator="0",
        user_id="it-help-desk-v4-068",
        instruction=(
            "Securely offboard terminated employee Evan Roberts (employee_id 'emp_0041') for lifecycle 'lcq_off_emp_0041'. Company policy requires complete revocation of access, reclamation of licenses, and recovery of assets. Ensure a comprehensive audit trail is in place and manage any deprovisioning exceptions through appropriate escalation."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0041"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_6f9008", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_6f9008"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_6f9008", "group_ids": ["grp_marketing_719b", "grp_marketing_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_6f9008"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0041"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00101"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00101"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00102"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00102"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00103"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00103"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0041"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0041"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0041"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"employee_id": "emp_0041", "assets_found": 0}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_6f9008"}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_return_emp_0041_none", "employee_id": "emp_0041", "asset_id": "none", "process": "device_return"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_off_emp_0041", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0041_none", "devices_scheduled": 0}, "actor": "SYSTEM", "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_6f9008"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-069",
    instruction=(
        "Coordinate an internal role transfer for Harper Hernandez (employee_id 'emp_0042') transitioning from 'Operations Manager' in Operations to 'Business Intelligence Manager' in Operations under lifecycle 'lcq_role_emp_0042'. Company policy necessitates complete access transition with continuous audit compliance and accurate license management."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0042"}),
        Action(name="GetUserGroupMemberships", kwargs={"account_id": "acc_43980f"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_43980f", "group_ids": ["grp_operations_9079", "grp_operations_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "PROMOTION_OLD_GROUPS_REMOVED", "details": {"account_id": "acc_43980f"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0042"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00048"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00048"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00049"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00049"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00050"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00050"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Operations", "job_title": "Business Intelligence Manager"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ROLE_TRANSFER_BLOCKED: lcq_role_emp_0042 - MISSING_ROLE_PROFILE", "priority": "P2"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_role_emp_0042", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-070",
        instruction=(
            "Organize the provisioning of a laptop for DevOps Engineer Zion Mitchell (employee_id=emp_0036) regarding lifecycle 'lcq_spec_emp_emp_0036'. The role requires CodeHub Enterprise, TechSoft 365 E3, and TeamChat Enterprise licenses. Company policy demands consistent allocation procedures with thorough tracking and escalation for any resource constraints."
        ),
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0036"}),
            Action(name="GetDirectoryAccount", kwargs={"employee_id": "emp_0036"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "DevOps Engineer"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_f9a6bc", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_f9a6bc", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_github_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_github_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_f9a6bc", "employee_id": "emp_0036", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0036"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0036"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_mdm_emp_0036_ast_0013", "employee_id": "emp_0036", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
            Action(name="UpdateAssetStatus", kwargs={"asset_id": "ast_0013", "status": "READY FOR PICKUP", "mdm_enrolled": True}),
            Action(name="EnqueueLifecycleEvent", kwargs={"lifecycle_id": "lcq_spec_emp_emp_0036", "memo_id": "memo_spec_emp_emp_0036", "employee_ref": "emp_0036", "event": "hardware_provision", "status": "completed", "created_at": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-071",
        instruction=(
            "Coordinate a critical asset replacement for Sasha Phillips (employee_id=emp_0038) whose laptop 'ast_0002' has failed for lifecycle 'lcq_replace_emp_0038'. Company policy mandates immediate replacement with correct asset lifecycle management. Address any inventory shortages through emergency procurement escalation."
        ),
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0038"}),
            Action(name="GetDirectoryAccount", kwargs={"employee_id": "emp_0038"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "ASSET_FAILURE_REPORTED", "details": {"asset_id": "ast_0002", "employee_id": "emp_0038", "failure_type": "hardware_malfunction"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0038"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"asset_id": "ast_0002", "current_status": "assigned"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="UnassignAsset", kwargs={"asset_id": "ast_0002"}),
            Action(name="UpdateAssetStatus", kwargs={"asset_id": "ast_0002", "status": "broken"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "BROKEN_ASSET_UNASSIGNED", "details": {"asset_id": "ast_0002", "unassignment_reason": "hardware_failure"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "REPLACEMENT_ASSET_LOCATED", "details": {"replacement_asset_id": "ast_0013", "asset_type": "laptop"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0038"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "REPLACEMENT_ASSET_ASSIGNED", "details": {"asset_id": "ast_0013", "employee_id": "emp_0038"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_mdm_emp_0038_ast_0013", "employee_id": "emp_0038", "asset_id": "ast_0013", "process": "mdm", "status": "completed", "pickup_code": "pc_dwf_replace_emp_0038_ast_0013", "created_at": "2025-08-15T13:00:00Z", "completed_at": "2025-08-15T13:00:00Z"}),
            Action(name="UpdateAssetStatus", kwargs={"asset_id": "ast_0013", "status": "READY FOR PICKUP", "mdm_enrolled": True}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "event": "REPLACEMENT_DEVICE_READY", "details": {"asset_id": "ast_0013", "mdm_status": "enrolled"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="EnqueueLifecycleEvent", kwargs={"lifecycle_id": "lcq_replace_emp_0038", "memo_id": "memo_replace_emp_0038", "employee_ref": "emp_0038", "event": "hardware_provision", "status": "completed", "created_at": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ast_0013"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-072",
        instruction=(
            "Carry out a compliance audit verification for Logan Park (employee_id=emp_0045) for lifecycle 'lcq_audit_emp_0045'. Company policy requires the validation of directory account status, group memberships against RBAC baseline, active license assignments, and asset management compliance. Document all findings with comprehensive audit trails."
        ),
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0045"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "AUDIT_INITIATED", "details": {"employee_id": "emp_0045", "audit_type": "compliance_verification"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetDirectoryAccount", kwargs={"employee_id": "emp_0045"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "ACCOUNT_STATUS_VERIFIED", "details": {"employee_id": "emp_0045", "account_status": "not_found"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "identity_not_found", "summary": "AUDIT_BLOCKED: lcq_audit_emp_0045 - EMPLOYEE_NOT_FOUND"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "identity_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "AUDIT_BLOCKED", "details": {"employee_id": "emp_0045", "reason": "employee_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RecordLifecycleAudit", kwargs={"lifecycle_id": "lcq_audit_emp_0045", "event": "COMPLIANCE_AUDIT_FAILED", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
        ],
        outputs=["lcq_audit_emp_0045"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-073",
        instruction=(
            "Handle a contractor conversion for Alex Reed (hr-0046) moving from contractor to full-time 'Security Analyst' in IT for lifecycle 'lcq_convert_emp_0046'. The employee record is not located in the directory. Company policy mandates identity verification before advancing with any provisioning."
        ),
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0046"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_INITIATED", "details": {"employee_id": "emp_0046", "legal_name": "Alex Reed"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "identity_not_found", "summary": "CONTRACTOR_CONVERSION_BLOCKED: lcq_convert_emp_0046 - EMPLOYEE_NOT_FOUND"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "identity_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_FAILED", "details": {"reason": "employee_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RecordLifecycleAudit", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_FAILED", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
        ],
        outputs=["ITSD-1013"],
    ),
            Task(
        annotator="0",
        user_id="it-help-desk-v4-074",
        instruction=(
            "Coordinate the onboarding of a new Marketing Specialist, Riley Walker (hr-245), in the Marketing department for lifecycle_id 'lcq_00079'. You find that their role profile is not set up in the system. Your responsibility is to create their user account and then report the missing profile by generating a 'missing_role_profile' ticket."
            "You discover that their role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Riley Walker", "hr_id": "hr-245", "department": "Marketing", "job_title": "Marketing Specialist"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00079", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyw245"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Marketing", "job_title": "Marketing Specialist"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00079 - MISSING_ROLE_PROFILE"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00079", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-075",
        instruction=(
            "Your task is to coordinate a complete, compliant offboarding for terminated employee Riley Wang (employee_id 'emp_0011') for lifecycle_id 'lcq_00080'. Follow all standard security protocols to safely deprovision user access and manage their assets according to policy."
            "You must follow all standard security protocols to securely deprovision user access and handle their assets according to policy."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0011"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00024"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00025"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0011"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_return_emp_0011_none", "employee_id": "emp_0011", "asset_id": "none", "process": "device_return"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00080", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0011_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_51e138"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-076",
        instruction=(
            "You are assigned an onboarding for Blake Thompson (hr-246) in the 'Operations' department as a 'Operations Coordinator' for lifecycle_id 'lcq_00081'. You find that this role profile is undefined in the system. Your responsibility is to create their user account and then escalate the missing profile by submitting a 'missing_role_profile' ticket."
            "You discover this role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Blake Thompson", "hr_id": "hr-246", "department": "Operations", "job_title": "Operations Coordinator"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00081", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_blaket246"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Operations", "job_title": "Operations Coordinator"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00081 - MISSING_ROLE_PROFILE"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00081", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}}),
        ],
        outputs=["ITSD-1013"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-077",
        instruction=(
            "Handle the offboarding process for terminated employee Peyton Shah (employee_id 'emp_0015') associated with lifecycle_id 'lcq_00082'. The employee has no hardware assigned. Adhere to the standard termination policy applicable to software-only users."
            "Employee has no assigned hardware. You should follow standard termination policy for software-only user."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0015"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_3818d8", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00082", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_3818d8", "group_ids": ["grp_operations_dcb3", "grp_operations_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00082", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0015"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00034"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00082", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00034"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00035"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00082", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00035"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0015"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00082", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0015"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0015"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00082", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"assets_found": 0}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_return_emp_0015_none", "employee_id": "emp_0015", "asset_id": "none", "process": "device_return"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00082", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0015_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_3818d8"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-078",
        instruction=(
            "Coordinate the offboarding procedure for terminated employee Alex Park (employee_id 'emp_0006') for lifecycle_id 'lcq_00083'. Execute the standard termination policy to securely deprovision access, revoke licenses, and coordinate asset return."
            "Follow standard termination policy to securely deprovision access, revoke licenses, and handle asset return."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0006"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_e7e9ee", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00083", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_e7e9ee"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_e7e9ee", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00083", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_e7e9ee"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0006"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00014"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00083", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00014"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00015"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00083", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00015"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00016"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00083", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00016"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0006"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00083", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0006"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0006"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00083", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_e7e9ee"}}),
        ],
        outputs=["acc_e7e9ee"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-079",
        instruction=(
            "Ensure you conduct a full, compliant offboarding for the terminated employee Riley Wang (employee_id 'emp_0011') associated with lifecycle_id 'lcq_00084'. Adhere to all standard security measures to safely deprovision user access and manage their assets according to policy."
            "for lifecycle_id 'lcq_00084'. You must follow all standard security protocols to securely deprovision user access "
            "and handle their assets according to policy."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0011"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00084", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00084", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00024"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00084", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00025"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00084", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00084", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0011"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00084", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"assets_found": 0}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_return_emp_0011_none", "employee_id": "emp_0011", "asset_id": "none", "process": "device_return"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00084", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0011_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_51e138"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-080",
        instruction=(
            "It is necessary to offboard the terminated employee Peyton Shah (employee_id 'emp_0015') linked to lifecycle_id 'lcq_00085'. The employee is not assigned any hardware. You are required to follow the standard termination protocol for a software-only user."
            "Employee has no assigned hardware. You should follow standard termination policy for software-only user."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0015"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_3818d8", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00085", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_3818d8", "group_ids": ["grp_operations_dcb3", "grp_operations_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00085", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_3818d8"}}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0015"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00034"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00085", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00034"}}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00035"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00085", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00035"}}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0015"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00085", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0015"}}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0015"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00085", "event": "ASSET_VERIFICATION_COMPLETE", "details": {"assets_found": 0}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_return_emp_0015_none", "employee_id": "emp_0015", "asset_id": "none", "process": "device_return"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00085", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0015_none", "devices_scheduled": 0}}),
        ],
        outputs=["acc_3818d8"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-081",
        instruction=(
            "Handle the onboarding process for new Financial Analyst Jordan Kim (hr-220) in Finance for lifecycle_id 'lcq_00086'. The role requires an M365 E5 license in addition to the standard bundle. If there is a license shortage, initiate a ticket for it."
            "Role requires M365 E5 license in addition to standard bundle. Create ticket for license shortage if needed."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Jordan Kim", "hr_id": "hr-220", "department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00086", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_parkerd220"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_parkerd220", "group_ids": ["grp_finance_7304", "grp_finance_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00086", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_parkerd220"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00086", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_m365_e3"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00086", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_slack_ent"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e5"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_parkerd220", "employee_id": "emp_220", "license_id": "lic_m365_e5"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e5", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00086", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_parkerd220", "license_id": "lic_m365_e5"}}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_220"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00086", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_220", "asset_id": "ast_0013"}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_220_ast_0013", "employee_id": "emp_220", "asset_id": "ast_0013", "process": "onboarding", "status": "pending"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00086", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_220_ast_0013", "pickup_code": "PU0013"}}),
        ],
        outputs=["acc_parkerd220"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-082",
        instruction=(
            "Coordinate the standard onboarding for the new Account Executive, Casey Liu (hr-216), in the Sales department for lifecycle_id 'lcq_00087'. Ensure you adhere to the full, policy-compliant procedure to set up their account, groups, all necessary licenses, and a standard laptop."
            "You must follow the complete, policy-compliant procedure to provision their account, groups, all required licenses, and a standard laptop."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Casey Liu", "hr_id": "hr-216", "department": "Sales", "job_title": "Account Executive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00087", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordang216"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Sales", "job_title": "Account Executive"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_jordang216", "group_ids": ["grp_sales_6744", "grp_sales_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00087", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_jordang216"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00087", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_m365_e3"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_salesforce"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_salesforce"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00087", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_salesforce"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_jordang216", "employee_id": "emp_216", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00087", "event": "LICENSE_ASSIGNED", "details": {"license_id": "lic_slack_ent"}}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_216"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00087", "event": "ASSET_ASSIGNED", "details": {"asset_id": "ast_0013"}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_216_ast_0013", "employee_id": "emp_216", "asset_id": "ast_0013", "process": "onboarding", "status": "pending_pickup"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00087", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_216_ast_0013"}}),
        ],
        outputs=["acc_jordang216"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-083",
    instruction=(
        "Manage the onboarding of Blake Thompson (hr-246) as an Operations Coordinator within the Operations department for lifecycle 'lcq_00088'. Navigate through the standard onboarding process and resolve any obstacles that emerge in line with established policies."
        "Handle the standard onboarding process and any blockers that arise according to established policies."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Blake Thompson", "hr_id": "hr-246", "department": "Operations", "job_title": "Operations Coordinator"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00088", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_blaket246"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Operations", "job_title": "Operations Coordinator"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00088 - MISSING_ROLE_PROFILE"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00088", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-084",
        instruction=(
            "Coordinate the onboarding of new Software Engineer Maya Patel (hr-301) into Engineering for lifecycle_id 'lcq_00089'. Execute the standard onboarding process to set up accounts, groups, licenses, and hardware."
            "Follow standard onboarding procedure to provision account, groups, licenses, and hardware."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Maya Patel", "hr_id": "hr-301", "department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00089", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_mayap301"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_mayap301", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00089", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_mayap301"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_mayap301", "employee_id": "emp_301", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00089", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_mayap301", "license_id": "lic_m365_e3"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_mayap301", "employee_id": "emp_301", "license_id": "lic_github_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00089", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_mayap301", "license_id": "lic_github_ent"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_mayap301", "employee_id": "emp_301", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00089", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_mayap301", "license_id": "lic_slack_ent"}}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_301"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00089", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_301", "asset_id": "ast_0013"}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_301_ast_0013", "employee_id": "emp_301", "asset_id": "ast_0013", "process": "onboarding", "status": "pending"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00089", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_301_ast_0013", "pickup_code": "PU0013"}}),
        ],
        outputs=["acc_mayap301"],
    ),
    Task(
    annotator="0",
    user_id="it-help-desk-v4-085",
    instruction=(
        "You are assigned to manage the onboarding process for Sam Chen (hr-302) in the 'HR' department as a 'HR Specialist' under lifecycle_id 'lcq_00090'. Adhere to the standard onboarding procedure to set up the account and verify resource availability. If the role profile is absent, escalate this matter as needed."
        "Follow the standard onboarding process to provision account and check resource availability. "
        "During the process, you discover the role profile is not defined and must escalate appropriately."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Sam Chen", "hr_id": "hr-302", "department": "HR", "job_title": "HR Specialist"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00090", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_samc302"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "HR", "job_title": "HR Specialist"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00090 - MISSING_ROLE_PROFILE"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00090", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-086",
        instruction=(
            "Ensure the onboarding of new Support Manager Alex Rodriguez (hr-303) in Support for lifecycle_id 'lcq_00091'. Carry out the standard onboarding steps, providing the necessary role-based access and hardware."
            "Complete standard onboarding with appropriate role-based access and hardware provisioning."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Alex Rodriguez", "hr_id": "hr-303", "department": "Support", "job_title": "Support Manager"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00091", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_alexr303"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Support", "job_title": "Support Manager"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_alexr303", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00091", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_alexr303"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_alexr303", "employee_id": "emp_303", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00091", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexr303", "license_id": "lic_m365_e3"}}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_alexr303", "employee_id": "emp_303", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00091", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexr303", "license_id": "lic_slack_ent"}}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_303"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00091", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_303", "asset_id": "ast_0013"}}),
            Action(name="CreateDeviceWorkflow", kwargs={"workflow_id": "wf_onboard_emp_303_ast_0013", "employee_id": "emp_303", "asset_id": "ast_0013", "process": "onboarding", "status": "pending"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00091", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_onboard_emp_303_ast_0013", "pickup_code": "PU0013"}}),
        ],
        outputs=["acc_alexr303"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-087",
        instruction=(
            "Handle the creation of the weekly Service Desk Health Report for lifecycle 'lcq_00092'. Deliver thorough performance metrics based on recent ticket activity for management review. In the absence of a specified default email id, set it-management-dl@company.com as the default for notifications."
            "Provide comprehensive performance metrics based on recent ticket activity for management review. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00092", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 7, "report_type": "weekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ExportRecentTickets", kwargs={"days": 7}),
            Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00092", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "weekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00092", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "weekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-088",
        instruction=(
            "Coordinate the creation of the monthly Service Desk Health Report for lifecycle 'lcq_00093'. Evaluate ticket data from the past 30 days and present comprehensive metrics to management."
            "Analyze ticket data from the last 30 days and provide comprehensive metrics to management."
        ),
        actions=[
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00093", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 30, "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ExportRecentTickets", kwargs={"days": 30}),
            Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00093", "event": "MONTHLY_REPORT_GENERATED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-089",
        instruction=(
            "Handle the creation of the bi-weekly Service Desk Health Report for lifecycle 'lcq_00094'. Export ticket data from the last 14 days, compute performance metrics, and send the report to stakeholders."
            "Export last 14 days of ticket data, calculate performance metrics, and distribute to stakeholders."
        ),
        actions=[
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00094", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 14, "report_type": "biweekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ExportRecentTickets", kwargs={"days": 14}),
            Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15","timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00094", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "biweekly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-090",
        instruction=(
            "Coordinate the onboarding of new Software Engineer Alex Kim (hr-225) in the Engineering department for lifecycle 'lcq_00095'. Proceed with the standard onboarding procedures to set up their account, allocate the correct role-based access, and arrange the hardware. If a default email id is not provided, then it-management-dl@company.com should be used as the default id for notifications."
            "Follow standard onboarding procedures to provision their account, assign appropriate role-based access, and prepare hardware. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Alex Kim", "hr_id": "hr-225", "department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00095", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_alexk225", "default_email": "it-management-dl@company.com"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Engineering", "job_title": "Software Engineer"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_alexk225", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00095", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_alexk225", "group_ids": ["grp_engineering_cbaf", "grp_engineering_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_alexk225", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00095", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexk225", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_github_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_alexk225", "license_id": "lic_github_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00095", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexk225", "license_id": "lic_github_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_alexk225", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00095", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_alexk225", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_225"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00095", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_225", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_alexk225"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-091",
        instruction=(
            "Handle the offboarding of terminated employee Taylor Singh (employee_id 'emp_0009') for lifecycle 'lcq_00096'. Adhere to standard termination protocols to securely remove user access and carry out the termination procedure."
            "Follow standard termination procedures to securely deprovision user access and handle the termination process."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0009"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_9e0388", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00096", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_9e0388"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_9e0388", "group_ids": ["grp_engineering_4162", "grp_engineering_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00096", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_9e0388"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0009"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00019"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00096", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00019"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00020"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_github_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00096", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00020"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00021"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00096", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00021"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0009"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00096", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0009"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0009"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00096", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_9e0388"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_9e0388"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-092",
        instruction=(
            "Coordinate the onboarding for Riley Chen (hr-226) in the 'Legal' department as a 'Legal Analyst' for lifecycle 'lcq_00097'. Manage the creation of their account and escalate any issues with missing role profiles through appropriate channels."
            "Process their account creation and escalate any missing role profile issues through proper channels."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Riley Chen", "hr_id": "hr-226", "department": "Legal", "job_title": "Legal Analyst"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00097", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyc226"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Legal", "job_title": "Legal Analyst"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00097 - MISSING_ROLE_PROFILE"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00097", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["ITSD-1013"],
    ),
        Task(
        annotator="0",
        user_id="it-help-desk-v4-093",
        instruction=(
            "Handle the offboarding of the terminated employee Alex Park (employee_id 'emp_0006') for the lifecycle 'lcq_00098'. Adhere to standard termination protocols to ensure secure access deprovisioning, license revocation, and scheduling of asset returns."
            "Follow standard termination protocols to securely deprovision access, revoke licenses, and schedule asset return."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0006"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_e7e9ee", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00098", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_e7e9ee"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_e7e9ee", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00098", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_e7e9ee"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0006"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00014"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00098", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00014"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00015"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00098", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00015"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00016"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00098", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00016"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0006"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00098", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0006"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0006"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00098", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_e7e9ee"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_e7e9ee"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-094",
        instruction=(
            "Coordinate the generation of the quarterly Service Desk Health Report for the lifecycle 'lcq_00099'. Deliver a comprehensive performance analysis based on the last 90 days of ticket activity for executive review. If no default email id is provided, set it-management-dl@company.com as the default id for notifications."
            "Provide comprehensive performance analysis based on last 90 days of ticket activity for executive review. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00099", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 90, "report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ExportRecentTickets", kwargs={"days": 90}),
            Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00099", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00099", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),
    Task(
        annotator="0",
        user_id="it-help-desk-v4-095",
        instruction=(
            "Handle the onboarding process for new Account Executive Morgan Taylor (hr-227) within the Sales department for lifecycle 'lcq_00100'. Adhere to the standard onboarding procedures to set up their account, allocate suitable role-based permissions, and arrange hardware setup. If there is no specified default email id, utilize it-management-dl@company.com as the default id for any notifications."
            "Follow standard onboarding procedures to provision their account, assign appropriate role-based access, and prepare hardware. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Morgan Taylor", "hr_id": "hr-227", "department": "Sales", "job_title": "Account Executive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00100", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_morgant227", "default_email": "it-management-dl@company.com"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Sales", "job_title": "Account Executive"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_morgant227", "group_ids": ["grp_sales_6744", "grp_sales_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00100", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_morgant227", "group_ids": ["grp_sales_6744", "grp_sales_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_morgant227", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00100", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_morgant227", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_salesforce"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_morgant227", "license_id": "lic_salesforce"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00100", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_morgant227", "license_id": "lic_salesforce"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_morgant227", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00100", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_morgant227", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_227", "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00100", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_227", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_morgant227"],
    ),

    Task(
        annotator="0",
        user_id="it-help-desk-v4-096",
        instruction=(
            "Manage the offboarding of the terminated employee Cameron Patel (employee_id 'emp_0013') for lifecycle 'lcq_00101'. Adhere to standard termination protocols to ensure secure deprovisioning of access, license revocation, and the scheduling of asset return."
            "Follow standard termination protocols to securely deprovision access, revoke licenses, and schedule asset return."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0013"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_78fb5c", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00101", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_78fb5c"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_78fb5c", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00101", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_78fb5c"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0013"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00029"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00101", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00029"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00030"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00101", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00030"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00031"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00101", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00031"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0013"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00101", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0013"}),
            Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0033", "employee_id": "emp_0013", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0013_ast_0033"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00101", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0013_ast_0033"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["wf_return_emp_0013_ast_0033"],
    ),

    Task(
        annotator="0",
        user_id="it-help-desk-v4-097",
        instruction=(
            "Handle the onboarding process for the new Financial Analyst, Jordan Lee (hr-228), within the Finance department for lifecycle 'lcq_00102'. Coordinate standard onboarding steps and address any license shortages by utilizing appropriate escalation protocols."
            "Follow standard onboarding procedures and handle any license shortage issues through proper escalation channels."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Jordan Lee", "hr_id": "hr-228", "department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00102", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordanl228"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Finance", "job_title": "Financial Analyst"}),
            Action(name="AddUserToGroups", kwargs={"account_id": "acc_jordanl228", "group_ids": ["grp_finance_7304", "grp_finance_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00102", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_jordanl228", "group_ids": ["grp_finance_7304", "grp_finance_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_jordanl228", "license_id": "lic_m365_e3"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00102", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_jordanl228", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
            Action(name="AssignLicense", kwargs={"account_id": "acc_jordanl228", "license_id": "lic_slack_ent"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00102", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_jordanl228", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_228"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00102", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_228", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_jordanl228"],
    ),

    Task(
        annotator="0",
        user_id="it-help-desk-v4-098",
        instruction=(
            "Coordinate the offboarding of terminated employee Riley Wang (employee_id 'emp_0011') for lifecycle 'lcq_00103'. Adhere to standard termination procedures to securely remove user access and manage the termination process."
            "Follow standard termination procedures to securely deprovision user access and handle the termination process."
        ),
        actions=[
            Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0011"}),
            Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_51e138", "status": "inactive"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00103", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_51e138", "group_ids": ["grp_support_ada3", "grp_support_all"]}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00103", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0011"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00024"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00103", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00024"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00025"}),
            Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00103", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00025"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0011"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00103", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0011"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="GetUserAsset", kwargs={"employee_id": "emp_0011"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00103", "event": "OFFBOARDING_NO_ASSETS", "details": {"account_id": "acc_51e138"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["acc_51e138"],
    ),

    Task(
        annotator="0",
        user_id="it-help-desk-v4-099",
        instruction=(
            "Generate the monthly Service Desk Health Report for lifecycle 'lcq_00104'. Deliver comprehensive performance metrics focusing on recent ticket activity for management's review. In the absence of a default email ID, assign it-management-dl@company.com as the default for notifications."
            "Provide comprehensive performance metrics based on recent ticket activity for management review. "
            "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
        ),
        actions=[
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00104", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 30, "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="ExportRecentTickets", kwargs={"days": 30}),
            Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00104", "event": "MONTHLY_REPORT_GENERATED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
            Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00104", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00104", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "monthly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=["run_20250815"],
    ),

    Task(
    annotator="0",
    user_id="it-help-desk-v4-100",
    instruction=(
        "Handle the onboarding for VP of Operations Casey Morgan (hr-229) within the Operations department for lifecycle 'lcq_00105'. Manage their account creation and escalate any issues with missing role profiles through the appropriate channels. If no default email ID is supplied, it-management-dl@company.com should be set as the default for notifications."
        "Process their account creation and escalate any missing role profile issues through proper channels. "
        "If no default email id is given then it-management-dl@company.com should be set as the default id for notifications."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Casey Morgan", "hr_id": "hr-229", "department": "Operations", "job_title": "VP of Operations", "default_email": "it-management-dl@company.com"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00105", "event": "EXECUTIVE_ACCOUNT_CREATED", "details": {"account_id": "acc_caseym229", "default_email": "it-management-dl@company.com"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Operations", "job_title": "VP of Operations"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00105 - MISSING_ROLE_PROFILE"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00105", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["ITSD-1013"],
    ),

Task(
    annotator="0",
    user_id="it-help-desk-v4-101",
    instruction=(
        "In your role as the IT director, you are required to compile the executive quarterly Service Desk Health Report regarding lifecycle 'lcq_00106'. The board necessitates a detailed examination of all operational metrics from the last 90 days, along with clear visual representations of performance trends. Ensure to use the standard distribution list for executive communications if a specific recipient is not indicated."
        "The board requires a comprehensive analysis of all operational metrics from the past 90 days with clear visualization of performance trends. "
        "Remember to use the standard distribution list for executive communications if no specific recipient is provided."
    ),
    actions=[
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00106", "event": "TICKET_EXPORT_INITIATED", "details": {"period_days": 90, "report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ExportRecentTickets", kwargs={"days": 90}),
        Action(name="CalculateTicketKpis", kwargs={"export_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(name="GenerateHealthReportPdf", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}}),
        Action(name="SaveReportToMetricsDb", kwargs={"kpis": {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}, "report_date": "2025-08-15"}),
        Action(name="NotifyTeamOfReport", kwargs={"pdf_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\ServiceDesk_Health_Report.pdf", "csv_path": "\\\\IT\\Reports\\DailyReports\\2025-08-15\\Tickets_Export.csv"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00106", "event": "MANAGEMENT_NOTIFICATION_SENT", "details": {"report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00106", "event": "KPI_CALCULATION_COMPLETED", "details": {"run_id": "run_20250815", "report_type": "quarterly"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["run_20250815"],
),

Task(
    annotator="0",
    user_id="it-help-desk-v4-102",
    instruction=(
        "There is an urgent task to incorporate Taylor Reed (hr-229), a new senior Account Executive within the Sales department for lifecycle 'lcq_00107'. The VP of Sales has highlighted this as critical with a requirement for same-day finalization to uphold client commitments. Make sure all standard protocols are observed, paying close attention to license provisioning and immediate assignment of hardware."
        "The VP of Sales has flagged this as urgent with a same-day completion requirement to meet client commitments. "
        "Ensure all standard procedures are followed with particular attention to license provisioning and immediate hardware assignment."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Taylor Reed", "hr_id": "hr-229", "department": "Sales", "job_title": "Account Executive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00107", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_taylorr229", "default_email": "it-management-dl@company.com"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Sales", "job_title": "Account Executive"}),
        Action(name="AddUserToGroups", kwargs={"account_id": "acc_taylorr229", "group_ids": ["grp_sales_6744", "grp_sales_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00107", "event": "GROUPS_ASSIGNED", "details": {"account_id": "acc_taylorr229", "group_ids": ["grp_sales_6744", "grp_sales_all"]}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_m365_e3"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_taylorr229", "license_id": "lic_m365_e3"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00107", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_taylorr229", "license_id": "lic_m365_e3"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_salesforce"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_taylorr229", "license_id": "lic_salesforce"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00107", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_taylorr229", "license_id": "lic_salesforce"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CheckLicenseAvailability", kwargs={"license_id": "lic_slack_ent"}),
        Action(name="AssignLicense", kwargs={"account_id": "acc_taylorr229", "license_id": "lic_slack_ent"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "increment"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00107", "event": "LICENSE_ASSIGNED", "details": {"account_id": "acc_taylorr229", "license_id": "lic_slack_ent"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="FindAvailableAsset", kwargs={"asset_type": "laptop"}),
        Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_229", "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00107", "event": "ASSET_ASSIGNED", "details": {"employee_id": "emp_229", "asset_id": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["acc_taylorr229"],
),

Task(
    annotator="0",
    user_id="it-help-desk-v4-103",
    instruction=(
        "Due to a security compliance requirement, you need to promptly handle a SOC2-compliant offboarding for Cameron Patel (employee_id 'emp_0013') for lifecycle 'lcq_00108'. This must adhere to our enhanced security protocol with thorough audit trail documentation. The security team requires confirmation of all access removal and asset recovery within the same business day."
        "This must follow our enhanced security protocol with complete audit trail documentation. The security team requires verification of all access removal and asset recovery within the same business day."
    ),
    actions=[
        Action(name="GetUserByUpnOrHrId", kwargs={"user_lookup": "emp_0013"}),
        Action(name="SetDirectoryAccountStatus", kwargs={"account_id": "acc_78fb5c", "status": "inactive"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00108", "event": "ACCOUNT_DISABLED", "details": {"account_id": "acc_78fb5c"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RemoveUserFromGroups", kwargs={"account_id": "acc_78fb5c", "group_ids": ["grp_sales_4bcb", "grp_sales_all"]}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00108", "event": "GROUPS_REMOVED", "details": {"account_id": "acc_78fb5c"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserLicenseAssignments", kwargs={"employee_id": "emp_0013"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00029"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_salesforce", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00108", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00029"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00030"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_slack_ent", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00108", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00030"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="RevokeLicense", kwargs={"assignment_id": "lca_00031"}),
        Action(name="UpdateLicenseInventory", kwargs={"license_id": "lic_m365_e3", "operation": "decrement"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00108", "event": "LICENSE_REVOKED", "details": {"assignment_id": "lca_00031"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="ArchiveMailbox", kwargs={"employee_id": "emp_0013"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00108", "event": "MAILBOX_ARCHIVED", "details": {"employee_id": "emp_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="GetUserAsset", kwargs={"employee_id": "emp_0013"}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0033", "employee_id": "emp_0013", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0013_ast_0033"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00108", "event": "DEVICE_WORKFLOW_CREATED", "details": {"workflow_id": "wf_return_emp_0013_ast_0033"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=["wf_return_emp_0013_ast_0033"],
    ),
]
