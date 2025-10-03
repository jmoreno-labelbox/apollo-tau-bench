from tau_bench.types import Action, Task
TASKS = [
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_001",
        instruction=(
            "Handle a full, compliant offboarding process for Sam Tran (employee_id 'emp_0004') related to lifecycle_id 'lcq_00040'. Ensure adherence to the entire policy-driven offboarding sequence, including situations where no hardware is allocated."
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
        outputs=[]
    ),
        Task(
annotator="v2",
user_id="It_Help_Desk_V2_002",
instruction="You must offboard terminated employee Alex Park (employee_id 'emp_0006') for lifecycle_id 'lcq_00019'. Follow standard termination policy to securely deprovision access, revoke licenses, and schedule asset return.",
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
outputs=[]
),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_003",
instruction="You must offboard Riley Wang (employee_id 'emp_0011') for lifecycle_id 'lcq_00023'. Employee has no assigned hardware. You should follow standard termination policy for software-only user.",
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
outputs=[]
),
        
Task(
annotator="v2",
user_id="It_Help_Desk_V2_004",
instruction="You must process the onboarding for the new IT Manager, Drew Kumar (hr-217), for lifecycle_id 'lcq_00016'. Follow standard onboarding procedures to provision software access, but report any hardware shortages encountered during the process.",
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
outputs=[]
),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_005",
        instruction=(
            "Handle the creation of the monthly Service Desk Health Report for lifecycle 'lcq_00090'. Examine ticket data from the past 30 days and deliver detailed metrics to the management."
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
        outputs=[]
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_006",
instruction="You are to perform a full, compliant onboarding for the new DevOps Engineer, Robin Jones (hr-219), in Engineering for lifecycle_id 'lcq_00018'. Follow standard policy to fully provision the user with appropriate access, groups, licenses, and hardware.",
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
outputs=[]
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_007",
        instruction=(
            "Handle the standard onboarding for the new Account Executive, Casey Liu (hr-216), in the Sales department with lifecycle_id 'lcq_00014'. Ensure adherence to the entire, policy-compliant procedure to provision their account, groups, all necessary licenses, and a standard laptop."
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
        outputs=[]
    ),

Task(
annotator="v2",
user_id="It_Help_Desk_V2_008",
instruction="You must onboard new Financial Analyst Jordan Kim (hr-220) in Finance for lifecycle_id 'lcq_00020'. Role requires M365 E5 license in addition to standard bundle. Create ticket for license shortage if needed.",
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
outputs=[]
),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_009",
        instruction=(
            "Handle an offboarding exception for Taylor Singh (employee_id 'emp_0009') associated with lifecycle_id 'lcq_00021'. Your responsibility is to make sure the account is inactive and then carry out the standard termination workflow. As there is no hardware assigned, conclude the process after completing the software deprovisioning steps."
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
        outputs=[]
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_010",
instruction="You must onboard new Sales Ops Analyst Avery Zhang (hr-221) in Sales for lifecycle_id 'lcq_00022'. You should follow standard policy for sales role provisioning including optional CreativeWorks Creative Cloud license.",
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
outputs=[]
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_011",
        instruction=(
            "Coordinate a comprehensive and compliant offboarding process for the terminated employee, Jordan Kim (employee_id 'emp_0007'), under lifecycle_id 'lcq_00015'. Ensure adherence to all standard security protocols to securely deprovision user access and manage their assets as per company policy."
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
        outputs=[]
    ),

    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_012",
        instruction=(
            "Undertake the onboarding of the new HRBP, Quinn Miller (hr-222), in the HR department for lifecycle_id 'lcq_00024'. Discover that their necessary hardware, a '16-inch OrionBook Pro', is currently unavailable. Execute provisioning of all required software access and then escalate the hardware shortage by submitting a TaskTrack ticket."
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
        outputs=[]
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_013",
instruction="You must handle the offboarding exception for Cameron Patel (employee_id 'emp_0013') for lifecycle_id 'lcq_00025'. Initial employee ID lookup may fail. You should use UPN fallback to complete standard termination process.",
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
outputs=[]
),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_014",
instruction="You must onboard new Content Strategist Emerson Davis (hr-223) in Marketing for lifecycle_id 'lcq_00026'. Role requires CreativeWorks Creative Cloud license. You should create ticket for license shortage if needed.",
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
outputs=[]
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_015",
        instruction=(
            "You are required to handle the offboarding of former employee Peyton Shah (employee_id 'emp_0015') pertaining to lifecycle_id 'lcq_00027'. Adhere to the standard termination policy to ensure access is securely deprovisioned. As there is no hardware assigned, finalize your process after verifying this detail."
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
        outputs=[]
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_016",
instruction="You must onboard new Senior Software Engineer Hayden Brown (hr-224) in Engineering for lifecycle_id 'lcq_00028'. You should follow standard policy to fully provision the user with appropriate access, groups, licenses, and hardware.",
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
outputs=[]
),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_017",
        instruction=(
            "You need to manage an offboarding exception for an employee with lifecycle_id 'lcq_00029'. The provided employee ID is 'emp_0999' and UPN 'blake.martin@company.com', however, neither can be found in the directory. Your responsibility is to verify both lookups are unsuccessful and then escalate by generating an 'identity_not_found' TaskTrack ticket."
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
        outputs=[]
    ),
Task(
annotator="v2",
user_id="It_Help_Desk_V2_018",
instruction="You are onboarding a new 'QA Engineer', Blake Anderson (hr-225), in 'Engineering' for lifecycle_id 'lcq_00030'. The goal is to fully provision the user. You must create the account ('acc_sawyert225'), assign all role-based groups and licenses, and provision a laptop ('ast_0013'). You must ensure every action is audited.",
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
outputs=[]
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_019",
    instruction=(
        "Attend to the lifecycle 'lcq_00052' by examining a reported slowdown in service desk performance. Assess the current ticket KPIs in comparison to the most recent successful report. Should an increase in open P1 tickets be noted, promptly escalate by generating a P1 'Incident' ticket that encapsulates the change."
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
    outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_020",
    instruction=(
        "Coordinate the onboarding of the new 'Support Specialist', Remy Clark (hr-226), for the 'Support' department under lifecycle_id 'lcq_00032'. Ensure you carry out the complete, standard procedure for setting up their account, role-based groups, licenses, and a laptop, while guaranteeing all IAM actions are audited."
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
    outputs=[]
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_021",
        instruction=(
            "Generate the monthly Service Desk Health Report for lifecycle 'lcq_00105'. Include comprehensive performance metrics from recent ticket activity for management evaluation. In the absence of a default email id, set it-management-dl@company.com as the default for notifications."
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
        outputs=[]
    ),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_022",
    instruction="You are onboarding a new 'Support Manager', Skyler Lopez (hr-227), in 'Support' for lifecycle_id 'lcq_00034'. Complete the standard onboarding process to provision their account, role-based access, and hardware.",
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
    outputs=[]
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_023",
    instruction="You must offboard the terminated employee Kendall Garcia (employee_id 'emp_0023') for lifecycle_id 'lcq_00035'. Your goal is to securely deprovision all access and assets, including their account ('acc_696506'), licenses, and assigned hardware ('ast_0041'), ensuring every step is audited.",
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
    outputs=[]
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_024",
    instruction="You are onboarding a new 'Operations Manager', Devin Martinez (hr-228), in 'Operations' for lifecycle_id 'lcq_00036'. The goal is to fully provision the user. You must create the account ('acc_elliotl228'), assign all role-based groups and licenses, and provision a laptop ('ast_0013'). You must ensure every action is audited.",
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
    outputs=[]
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_025",
    instruction=(
        "Owing to a compliance audit requirement, you are required to handle a comprehensive offboarding for Riley Wang (employee_id 'emp_0011') for lifecycle_id 'lcq_00080'. This involves strict adherence to our data retention policies and ensuring total access deprovisioning to satisfy regulatory standards."
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
    outputs=[]
),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_026",
        instruction=(
            "As an IT manager, for lifecycle_id 'lcq_00038', your responsibility is to coordinate the creation of the standard daily Service Desk Health Report for the past 30 days. You must follow the full, standard procedure to compile the final PDF and CSV reports, save the metrics, and inform the management team."
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
        outputs=[]
    ),
                    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_027",
        instruction=(
            "You are an IT automation engineer. Your assignment is to reactivate the directory account for re-hired employee Jordan Kim ('acc_e2a5e9'). Afterward, fully equip them with the standard groups, license bundle, and provide a standard laptop for their position as a 'Systems Engineer' in 'IT' for lifecycle_id 'lcq_00039'."
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
        outputs=[]
    ),
    Task(
annotator="v2",
user_id="It_Help_Desk_V2_028",
instruction="You are onboarding a new Software Engineer, Jamie Chen (hr-215), in the Engineering department for lifecycle_id 'lcq_00013'. Follow the standard onboarding process: create their directory account, assign appropriate role-based groups and licenses, provision a laptop, and ensure all major events are properly audited throughout the process.",
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
outputs=[]
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_029",
        instruction=(
            "Handle a role transition for Sam Tran (employee_id 'emp_0004') associated with lifecycle_id 'lcq_00041'. Morgan is shifting from 'Systems Engineer' to 'Identity Engineer' within the 'IT' department. Ensure complete deprovisioning of previous access and provisioning of all necessary access for the new role, with all IAM steps being audited."
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
        outputs=[]
    ),

            Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_030",
    instruction=(
        "As an IT manager, coordinate the generation of the quarterly service desk report for lifecycle 'lcq_00042', covering the last 90 days. This quarterly evaluation requires detailed performance metrics but excludes any PDF documentation. Ensure all information is accurately archived in the metrics database for executive reporting."
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
    outputs=[]
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_031",
    instruction=(
        "Manage the onboarding of contractor 'Alex Kirby' (hr-901), appointed as a 'Systems Engineer' in IT for lifecycle 'lcq_00043'. Oversee the onboarding activities including account creation and group assignments. Ensure contractors are provided with directory accounts granting email access, but without any licensed software or hardware assets."
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
    outputs=[]
),
            Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_032",
        instruction=(
            "You are responsible for offboarding the employee 'emp_0016' (Hayden Brown) under lifecycle 'lcq_00044'. Adhere to the complete and fixed offboarding procedure: deactivate their account, eliminate group memberships, revoke all licenses, preserve their mailbox, and plan for the asset return, confirming that each step undergoes auditing."
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
        outputs=[]
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_033",
        instruction=(
            "You are bringing on board a new VIP, 'Jordan Rivera' (hr-235), who serves as an 'Executive VP' within the 'Executive' department for lifecycle 'lcq_00045'. You find that their role profile is not configured in the system. Your responsibility is to set up their user account and then escalate the issue of the missing profile by submitting a 'missing_role_profile' ticket with P3 priority."
            "You discover that their role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket with P3 priority."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Jordan Rivera", "hr_id": "hr-235", "department": "Executive", "job_title": "Executive VP"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00045", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_jordanr235"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Executive", "job_title": "Executive VP"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00045 - MISSING_ROLE_PROFILE 'Executive VP'", "priority": "P3"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00045", "event": "ONBOARDING_BLOCKED", "details": {"reason": "Missing role profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=[]
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_034",
        instruction=(
            "You are coordinating a software-only onboarding for a new 'Recruiter', 'Sam Jones' (hr-230), within 'HR' for lifecycle 'lcq_00046'. Your responsibility is to create their account and assign their standard software bundle, ensuring every IAM step is audited and meets compliance."
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
        outputs=[]
    ),
        Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_035",
    instruction=(
        "You are assessing a crucial failure in the report generation process for lifecycle 'lcq_00047'. Your task is to conduct a comprehensive incident analysis by comparing KPIs from the last successful report with current ticket information. Archive the analysis results in the metrics database and escalate using a P1 TaskTrack incident ticket."
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
    outputs=[]
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_036",
    instruction=(
        "As the IT director, you are required to compile the executive quarterly Service Desk Health Report for lifecycle 'lcq_00106'. The board demands a thorough examination of all operational metrics from the past 90 days with clear visualization of performance trends. Ensure to use the standard distribution list for executive communications if no specific recipient is specified."
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
    outputs=[]
),
    
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_037",
        instruction=(
            "For lifecycle 'lcq_00049', ensure the offboarding of the terminated employee 'emp_0017' (Dakota Wilson) is completed. Handle the comprehensive, policy-guided offboarding procedure by deprovisioning their account, groups, licenses, and mailbox, thoroughly auditing each IAM action. Note that this user has no assigned hardware."
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
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_038",
    instruction=(
        "A potential security concern requires your attention. A manager has initiated an audit to validate the successful offboarding of terminated employee 'emp_0029' (Lane Taylor) for lifecycle 'lcq_00050'. Conduct an investigation of their account and completely resolve any active access encountered, following security policy. Ensure to document your discoveries and every remediation action taken in a formal ticket."
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
    outputs=[]
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_039",
        instruction=(
            "For lifecycle 'lcq_00051', your responsibility is to welcome a new 'Accounting Manager', 'Alex Ray' (hr-231), into 'Finance'. The task involves setting up their account and granting necessary software access. Although the user has requested a 'Vertex Vertex Pro 7440', it's unavailable in stock. You should open a ticket to address the hardware shortage."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_040",
        instruction=(
            "You are assigned to coordinate a complete, compliant offboarding for Sawyer Harris (employee_id 'emp_0019') for lifecycle_id 'lcq_00031'. The objective is to thoroughly deprovision all access and assets in line with the standard offboarding guidelines. Identify the user's account ('acc_1d0980'), deactivate it, remove group memberships, locate and cancel their license assignments, archive their mailbox, and plan the return of their asset ('ast_0031'). Ensure that every IAM procedure is audited."
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
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_041",
    instruction=(
        "Handle a high-priority request concerning the onboarding of Taylor Reed (hr-229), a new Senior Account Executive for the Sales department under lifecycle 'lcq_00107'. The VP of Sales has marked this as urgent, requiring completion within the same day to fulfill client commitments. Ensure that all standard procedures are adhered to, focusing especially on license provisioning and prompt hardware allocation."
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
    outputs=[]
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_042",
    instruction=(
        "You need to coordinate the offboarding for employee 'emp_0027' (Jesse Moore) associated with lifecycle 'lcq_00054' in line with the standard termination policy. The process should involve completely deprovisioning their account, groups, and all licenses. It has been noted that they have no assigned hardware, which needs auditing to finalize the procedure."
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
    outputs=[]
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_043",
    instruction=(
        "Handle the onboarding of a new 'VP of Product', 'Riley Kim' (hr-236), into the 'Product' department for lifecycle 'lcq_00055'. After setting up their account, you notice their role profile is undefined in the system. You need to escalate this issue by creating a P2 ticket that includes the lifecycle ID and highlights the missing role."
        "You create their account but discover that their role profile is not defined in the system. You must escalate this by creating a P2 ticket that details the lifecycle ID and the specific missing role."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Riley Kim", "hr_id": "hr-236", "department": "Product", "job_title": "VP of Product"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00055", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyk236"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Product", "job_title": "VP of Product"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "MISSING_ROLE_PROFILE: lcq_00055 | department: Product | job_title: VP of Product", "priority": "P2"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00055", "event": "ONBOARDING_BLOCKED", "details": {"reason": "Missing role profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_044",
        instruction=(
            "Coordinate a software-only offboarding for 'emp_0011' (Riley Wang) related to lifecycle 'lcq_00056', ensuring adherence to the comprehensive and immutable offboarding policy, including the verification of hardware."
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
        outputs=[]
    ),

    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_045",
    instruction=(
        "Ensure the complete provisioning of a new 'Controller', 'Morgan Kai' (hr-233), within 'Finance' for lifecycle 'lcq_00057'. This includes setting up their account, assigning groups, all necessary licenses, and a standard laptop following the unchangeable onboarding policy."
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
    outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_046",
    instruction=(
        "Coordinate a detailed re-onboarding for employee 'emp_0007' (Jordan Kim) for lifecycle 'lcq_00058', who is taking on a new, unspecified position as a 'Lead DevOps Engineer' in 'Engineering'. You must re-enable their account and then handle two specific issues: the new position lacks a profile, and the standard temporary license ('lic_m365_e5') is currently unavailable. Both problems need to be escalated."
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
    outputs=[]
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_047",
        instruction=(
            "Your responsibility is to coordinate an asset replacement for employee 'emp_0018' for lifecycle 'lcq_00059'. You should unassign their old device, 'ast_0004', and set up the designated replacement, 'ast_0013'."
            "You must unassign their old device, 'ast_0004', and provision the designated replacement, 'ast_0013'."
        ),
        actions=[
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0004", "employee_id": None}),
            Action(name="AssignAsset", kwargs={"asset_id": "ast_0013", "employee_id": "emp_0018"}),
            Action(name="CreateDeviceWorkflow", kwargs={"employee_id": "emp_0018", "asset_id": "ast_0013", "process": "onboarding"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00059", "event": "ASSET_SWAP_COMPLETED", "details": {"employee_id": "emp_0018", "old_asset": "ast_0004", "new_asset": "ast_0013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_048",
    instruction=(
        "For lifecycle 'lcq_00060', you are tasked with offboarding 'emp_0029' (Lane Taylor). The objective is to securely remove all access and assets following the standard termination procedures."
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
    outputs=[]
),
            Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_049",
        instruction=(
            "An identity sync procedure has encountered a failure, potentially linked to the employee 'emp_0030'. With regard to lifecycle 'lcq_00061', your responsibility is to inspect the groups assigned to the user and address their access by removing them. Subsequently, you should disable the account and escalate to the relevant teams for further evaluation."
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
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_050",
    instruction=(
        "Handle the onboarding of new Systems Engineer Finley Blue (hr-234) within the IT department for lifecycle 'lcq_00062'. Adhere to standard onboarding protocols to set up their account, allocate suitable role-based access, and arrange hardware."
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
    outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_051",
    instruction=(
        "Your responsibility is to manage the onboarding of a new 'Legal Counsel', 'Kai Chen' (hr-237), following a request from HR (memo_102). An essential component of the procedure is to generate an entry in the lifecycle queue. If you discover that their role profile is undefined, you should escalate this issue appropriately."
    ),
    actions=[
        Action(name="AddMemoToLifecycleQueue", kwargs={"memo_id": "memo_102", "hr_id": "hr-237", "event_type": "onboarding"}),
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Kai Chen", "hr_id": "hr-237", "department": "Legal", "job_title": "Legal Counsel"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_kaic237"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Legal", "job_title": "Legal Counsel"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00013 - MISSING_ROLE_PROFILE", "priority": "P2"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00013", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=[]
),
        Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_052",
    instruction=(
        "You are required to coordinate a complete, policy-compliant offboarding for employee 'emp_0025' (Elliot Johnson) within the lifecycle context 'lcq_00064'. Your objective is to remove all access for their account ('acc_1e8432'), which involves taking them out of groups, revoking their four assigned licenses (Salesforce, CreativeWorks, TeamChat, M365), archiving their mailbox, and organizing the retrieval of their laptop ('ast_0044'). It's crucial to ensure that every IAM action is logged."
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
    outputs=[]
),

Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_053",
    instruction=(
        "As an IT manager, your responsibility is to compile the daily Service Desk Health Report for lifecycle 'lcq_00065'. Your objective is to create the final PDF and CSV reports, preserve the resulting metrics for historical documentation, and inform the management team at 'it-management-dl@company.com'."
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
    outputs=[]
),

Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_054",
    instruction=(
        "You are to execute a full, policy-compliant offboarding for employee 'emp_0020' (River Allen) for lifecycle 'lcq_00066'. It's necessary to disable their account, remove them from all groups, identify and revoke each of their assigned licenses, and archive their mailbox. Ensure that all IAM actions undergo auditing."
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
    outputs=[]
),

    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_055",
    instruction=(
        "Handle a complete, policy-compliant onboarding for a new 'IT Support Specialist', 'Morgan Casey' (hr-240), within lifecycle context 'lcq_00067'. Start by creating their account, then try to assign role-based groups and standard licenses appropriate for their role, and organize a laptop provision. Nonetheless, you'll notice the role profile is missing, so you must adhere to policy by generating a TaskTrack ticket to define the profile and halt further onboarding steps until this issue is sorted."
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
    outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_056",
    instruction=(
        "Coordinate a thorough, policy-compliant onboarding for a new 'IT Help Desk Analyst', 'Jamie Bell' (hr-239), within lifecycle context 'lcq_00068'. Begin by establishing their account, then proceed to assign role-based groups and standard licenses suitable for their position, and arrange for a laptop provision. However, you'll discover the role profile isn't available, so policy requires you to open a TaskTrack ticket to establish the profile and suspend further onboarding actions until this matter is addressed."
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
    outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_057",
    instruction=(
        "Handle the onboarding for VP of Operations Casey Morgan (hr-229) within the Operations department for lifecycle 'lcq_00105'. Coordinate their account setup and escalate any issues with missing role profiles through the proper channels. If a default email id is not provided, set it-management-dl@company.com as the default id for notifications."
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
    outputs=[]
    ),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_058",
    instruction=(
        "Manage the offboarding of the terminated employee Kendall Garcia (employee_id 'emp_0023') for lifecycle 'lcq_00070'. Adhere to standard termination protocols to safely deprovision access, withdraw licenses, and arrange the return of assets."
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
    outputs=[]
),

Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_059",
    instruction=(
        "An employee, 'emp_0026' (Charlie Garcia), has a broken laptop ('ast_0052'). As part of lifecycle 'lcq_00071', your responsibility is to manage the asset exchange. Your objective is to provide them with a functional device; however, you find there are no 'laptop_loaner' devices on hand. It is necessary to escalate the shortage by creating a P2 TaskTrack ticket."
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
    outputs=[]
),
Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_060",
    instruction=(
        "You are required to oversee an internal role transfer for Harper Hernandez (employee_id 'emp_0042') moving from 'Operations Manager' in Operations to 'Business Intelligence Manager' in Operations for lifecycle 'lcq_role_emp_0042'. Company policy mandates a complete access transition with ongoing audit compliance and correct license management."
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
    outputs=[]
),


    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_061",
    instruction=(
        "Handle a compliance verification for Hayden Brown (employee_id=emp_0016). Your responsibility is to ensure their assigned phone is under MDM, with a creation date of 2025-07-18T11:10:00+00:00. In addition, validate their directory account status, group memberships against the RBAC baseline, and active license assignments. Confirm that the asset is still correctly assigned and document any issues found. Log all actions in the lifecycle audit record."
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
    outputs=[]
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_062",
        instruction=(
            "Coordinate the issuance of a standard company laptop to Skyler Lopez (employee_id=emp_0022) from the available inventory for lifecycle 'lcq_hw_emp_0022'. Company policy mandates consistent asset allocation using the lowest available asset ID. Make sure the device is fully enrolled in MDM and verify successful assignment and management status. Manage any hardware shortages by creating the necessary escalation tickets."
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
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_063",
    instruction=(
        "Manage the return process for the phone allocated to Micah White (employee_id=emp_0030). You must arrange the device return and schedule a corresponding MDM wipe exactly on 2025-08-15T13:00:00Z. Ensure the asset's ownership remains unchanged until the collection is thoroughly completed."
    ),
    actions=[
        Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0030"}),
        Action(name="FindAssets", kwargs={"asset_type": "phone", "assigned_to": "emp_0030", "mdm_enrolled": True}),
        Action(name="RequestAssetReturn", kwargs={"asset_id": "ast_0014", "employee_id": "emp_0030", "due_ts": "2025-08-15T13:00:00Z", "workflow_id": "wf_return_emp_0030_ast_0014"}),
        Action(name="ScheduleMdmAction", kwargs={"asset_id": "ast_0014", "when": "2025-08-15T13:00:00Z", "action": "wipe", "workflow_id": "wf_return_emp_0030_ast_0014"}),
        Action(name="EnqueueLifecycleEvent", kwargs={"lifecycle_id": "lcq_return_emp_0030", "memo_id": "memo_return_emp_0030", "employee_ref": "emp_0030", "event": "return", "status": "queued", "created_at": "2025-08-15T13:00:00Z"}),
        Action(name="RecordLifecycleAudit", kwargs={"lifecycle_id": "lcq_return_emp_0030", "event": "DEVICE_WORKFLOW_CREATED", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
    ],
    outputs=[]
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_064",
    instruction=(
        "Coordinate the return of two managed phones belonging to Lane Taylor, an Accounting Manager (employee_id=emp_0029). Your responsibility is to set up separate return processes and organize MDM wipes for each device at their designated due times. Asset 'ast_0039' is scheduled for 2025-07-26T17:00:00+00:00, and 'ast_0049' is scheduled for 2025-07-26T17:30:00+00:00. Avoid changing ownership records until the pickup is verified."
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
    outputs=[]
),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_065",
    instruction=(
        "Handle the provisioning of a managed laptop for Support Manager Sasha Phillips (employee_id=emp_0038) for lifecycle 'lcq_hardware_provision_emp_0038'. Company policy demands consistent asset allocation using the lowest available asset ID and ensures full MDM compliance for every issued device."
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
    outputs=[]
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_066",
        instruction=(
            "Coordinate the issuance of a laptop from company stock to Emerson Davis (employee_id=emp_0014). Company policy requires consistent asset allocation utilizing the lowest available asset ID and mandates full enrollment in MDM for all devices with comprehensive lifecycle tracking. Confirm that the final provisioning aligns with all management and assignment requirements."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_067",
        instruction=(
            "Commence the onboarding process for new Senior Marketing Analyst River Chen (hr-240) within the Marketing department for lifecycle 'lcq_ob_emp_0040'. Upon discovering their role profile is not available in the system, your responsibility is to create their user account and subsequently escalate the absence of a profile by submitting a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "River Chen", "hr_id": "hr-240", "department": "Marketing", "job_title": "Senior Marketing Analyst"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_riverc240"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Marketing", "job_title": "Senior Marketing Analyst"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_ob_emp_0040 - MISSING_ROLE_PROFILE"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_ob_emp_0040", "event": "AUDIT_BLOCKED", "details": {"reason": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=[]
    ),
            Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_068",
        instruction=(
            "Securely manage the offboarding of terminated employee Evan Roberts (employee_id 'emp_0041') for lifecycle 'lcq_off_emp_0041'. According to company policy, it is essential to completely revoke access, reclaim licenses, and recover assets. Ensure that a thorough audit trail is maintained and properly escalate any deprovisioning exceptions that arise."
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
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_069",
    instruction=(
        "Handle the onboarding of Senior Software Engineer Avery Morgan (hr-238) within the Engineering department related to lifecycle 'lcq_00072'. Adhere to the usual onboarding protocols for account setup, assign suitable role-based access, and arrange necessary hardware."
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
    outputs=[]
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_070",
        instruction=(
            "Coordinate the provisioning of a laptop for DevOps Engineer Zion Mitchell (employee_id=emp_0036) concerning lifecycle 'lcq_spec_emp_emp_0036'. The role necessitates licenses for CodeHub Enterprise, TechSoft 365 E3, and TeamChat Enterprise. Follow company policy for consistent allocation steps, ensuring thorough tracking and prompt action on resource constraints."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_071",
        instruction=(
            "Handle the replacement of a critical asset for Sasha Phillips (employee_id=emp_0038), whose laptop 'ast_0002' is outdated for lifecycle 'lcq_replace_emp_0038'. Company policy mandates immediate replacement following asset lifecycle management guidelines. Address any inventory shortages by escalating to emergency procurement."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_072",
        instruction=(
            "Coordinate a compliance audit verification for Logan Park (employee_id=emp_0045) associated with lifecycle 'lcq_audit_emp_0045'. Company policy mandates confirming directory account status, group memberships against RBAC baseline, making sure active license assignments are correct, and that asset management is compliant. Record all outcomes with detailed audit trails."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_073",
        instruction=(
            "Handle a contractor conversion for Alex Reed (hr-0046), changing status from contractor to full-time 'Security Analyst' in IT concerning lifecycle 'lcq_convert_emp_0046'. Note that the employee record is missing in the directory. It is mandatory according to company policy to verify identity before proceeding with any provisioning."
        ),
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "emp_0046"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_INITIATED", "details": {"employee_id": "emp_0046", "legal_name": "Alex Reed"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "identity_not_found", "summary": "CONTRACTOR_CONVERSION_BLOCKED: lcq_convert_emp_0046 - EMPLOYEE_NOT_FOUND"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "identity_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_FAILED", "details": {"reason": "employee_not_found", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="RecordLifecycleAudit", kwargs={"lifecycle_id": "lcq_convert_emp_0046", "event": "CONTRACTOR_CONVERSION_FAILED", "timestamp": "2025-08-15T13:00:00Z", "actor": "service_desk"}),
        ],
        outputs=[]
    ),
            Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_074",
        instruction=(
            "Coordinate the onboarding of a new Marketing Specialist, Riley Walker (hr-245), within the Marketing department for lifecycle_id 'lcq_00079'. Realize that their role profile isn't set up in the system. Your duty is to establish their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket."
            "You discover that their role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Riley Walker", "hr_id": "hr-245", "department": "Marketing", "job_title": "Marketing Specialist"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00079", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyw245"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Marketing", "job_title": "Marketing Specialist"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00079 - MISSING_ROLE_PROFILE"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00079", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_075",
        instruction=(
            "Handle a full, compliant offboarding process for the terminated employee Riley Wang (employee_id 'emp_0011') with lifecycle_id 'lcq_00080'. Ensure all standard security protocols are adhered to for securely deprovisioning user access and managing their assets according to company policy."
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
        outputs=[]
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_076",
        instruction=(
            "Manage the onboarding process for Blake Thompson (hr-246) in the 'Operations' department, starting as an 'Operations Coordinator' under lifecycle_id 'lcq_00081'. Upon discovering that this role profile is not available in the system, your task is to set up their user account and then escalate the issue by creating a 'missing_role_profile' ticket."
            "You discover this role profile is not defined in the system. Your task is to create their user account and then escalate the missing profile by creating a 'missing_role_profile' ticket."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Blake Thompson", "hr_id": "hr-246", "department": "Operations", "job_title": "Operations Coordinator"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00081", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_blaket246"}}),
            Action(name="LookupRoleProfile", kwargs={"department": "Operations", "job_title": "Operations Coordinator"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00081 - MISSING_ROLE_PROFILE"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00081", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_077",
        instruction=(
            "Handle the creation of the monthly Service Desk Health Report for lifecycle 'lcq_00104'. Deliver detailed performance metrics based on the recent ticket activity for management assessment. In the absence of a specified default email id, use it-management-dl@company.com as the standard id for notifications."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_078",
        instruction=(
            "Coordinate the offboarding process for the terminated employee Alex Park (employee_id 'emp_0006') for lifecycle_id 'lcq_00083'. Adhere to the standard termination policy to ensure secure deprovisioning of access, revocation of licenses, and asset return management."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_079",
        instruction=(
            "Handle the comprehensive, compliant offboarding process for terminated employee Riley Wang (employee_id 'emp_0011') associated with lifecycle_id 'lcq_00084'. Adhere to all established security protocols to securely deprovision user access and manage their assets as per policy."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_080",
        instruction=(
            "Coordinate the offboarding of terminated employee Peyton Shah (employee_id 'emp_0015') for lifecycle_id 'lcq_00085'. The employee has no hardware assigned. Adhere to the standard termination policy applicable for software-only users."
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
        outputs=[]
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_081",
        instruction=(
            "Ensure the onboarding of new Financial Analyst Jordan Kim (hr-220) in Finance for lifecycle_id 'lcq_00086'. The role necessitates an M365 E5 license in addition to the standard bundle. Initiate a ticket if there is a license shortage."
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
        outputs=[]
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_082",
        instruction=(
            "Coordinate a standard onboarding for the new Account Executive, Casey Liu (hr-216), in the Sales department for lifecycle_id 'lcq_00087'. Adhere to the complete, policy-compliant process for provisioning their account, groups, all necessary licenses, and a standard laptop."
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
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_083",
    instruction=(
        "Coordinate the onboarding of Blake Thompson (hr-246) as an Operations Coordinator within the Operations department for lifecycle 'lcq_00088'. Manage the usual onboarding process and address any obstacles based on established policies."
        "Handle the standard onboarding process and any blockers that arise according to established policies."
    ),
    actions=[
        Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Blake Thompson", "hr_id": "hr-246", "department": "Operations", "job_title": "Operations Coordinator"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00088", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_blaket246"}, "timestamp": "2025-08-15T13:00:00Z"}),
        Action(name="LookupRoleProfile", kwargs={"department": "Operations", "job_title": "Operations Coordinator"}),
        Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00088 - MISSING_ROLE_PROFILE"}),
        Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00088", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
    ],
    outputs=[]
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_084",
        instruction=(
            "Facilitate the onboarding of new Software Engineer Maya Patel (hr-301) in Engineering for lifecycle_id 'lcq_00089'. Adhere to the standard onboarding procedure to set up account, groups, licenses, and hardware."
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
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_085",
    instruction=(
        "Handle the onboarding for Sam Chen (hr-302) in the 'HR' department as a 'HR Specialist' for lifecycle_id 'lcq_00090'. Adhere to the standard onboarding process to set up the account and verify resource availability. If you find the role profile is not defined, escalate appropriately."
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
    outputs=[]
),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_086",
        instruction=(
            "Coordinate the onboarding of new Support Manager Alex Rodriguez (hr-303) in Support for lifecycle_id 'lcq_00091'. Execute standard onboarding with necessary role-based access and hardware provisioning."
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
        outputs=[]
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_087",
        instruction=(
            "Handle the creation of the weekly Service Desk Health Report for lifecycle 'lcq_00092'. Deliver detailed performance metrics based on recent ticket activity for management evaluation. In case a default email id is not specified, employ it-management-dl@company.com as the default email address for notifications."
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
        outputs=[]
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_088",
        instruction=(
            "Coordinate the assembly of the monthly Service Desk Health Report for lifecycle 'lcq_00093'. Evaluate ticket data from the past 30 days and offer detailed metrics to management."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_089",
        instruction=(
            "Handle the creation of the bi-weekly Service Desk Health Report for lifecycle 'lcq_00094'. Export ticket data from the past 14 days, compute performance metrics, and share the report with stakeholders."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_090",
        instruction=(
            "Coordinate the onboarding of new Software Engineer Alex Kim (hr-225) for the Engineering department associated with lifecycle 'lcq_00095'. Adhere to the standard onboarding protocol to set up their account, allocate the necessary role-based access, and arrange the required hardware. If no default email id is provided, then it-management-dl@company.com should be used as the default id for notifications."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_091",
        instruction=(
            "You must perform the deactivation for terminated employee Taylor Singh (employee_id 'emp_0009') in lifecycle 'lcq_00096'. Apply standard termination protocols to safely revoke user access and manage the termination procedure."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_092",
        instruction=(
            "You must coordinate the onboarding process for Riley Chen (hr-226) who is joining the 'Legal' department as a 'Legal Analyst' for lifecycle 'lcq_00097'. Execute their account setup and escalate any issues with missing role profiles through appropriate channels."
            "Process their account creation and escalate any missing role profile issues through proper channels."
        ),
        actions=[
            Action(name="CreateDirectoryAccount", kwargs={"legal_name": "Riley Chen", "hr_id": "hr-226", "department": "Legal", "job_title": "Legal Analyst"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00097", "event": "ACCOUNT_CREATED", "details": {"account_id": "acc_rileyc226"}, "timestamp": "2025-08-15T13:00:00Z"}),
            Action(name="LookupRoleProfile", kwargs={"department": "Legal", "job_title": "Legal Analyst"}),
            Action(name="CreateJiraTicket", kwargs={"issue_type": "missing_role_profile", "summary": "ONBOARDING_BLOCKED: lcq_00097 - MISSING_ROLE_PROFILE"}),
            Action(name="CreateAuditRecord", kwargs={"lifecycle_id": "lcq_00097", "event": "JIRA_TICKET_CREATED", "details": {"issue_type": "missing_role_profile", "jira_id": "ITSD-1013"}, "timestamp": "2025-08-15T13:00:00Z"}),
        ],
        outputs=[]
    ),
        Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_093",
        instruction=(
            "Handle the offboarding of the terminated employee Alex Park (employee_id 'emp_0006') for lifecycle 'lcq_00098'. Use standard termination protocols to ensure secure deprovisioning of access, revocation of licenses, and scheduling of asset return."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_094",
        instruction=(
            "Coordinate the generation of the quarterly Service Desk Health Report for lifecycle 'lcq_00099'. Deliver a comprehensive performance analysis based on the past 90 days of ticket activity for an executive review. If no default email id is specified, assign it-management-dl@company.com as the default id for notifications."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_095",
        instruction=(
            "Handle the onboarding of new Account Executive Morgan Taylor (hr-227) in the Sales department for lifecycle 'lcq_00100'. Coordinate standard onboarding procedures to set up their account, assign the right role-based access, and prepare hardware. If no default email id is specified, use it-management-dl@company.com as the default id for notifications."
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
        outputs=[]
    ),

    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_096",
        instruction=(
            "Coordinate the offboarding of terminated employee Cameron Patel (employee_id 'emp_0013') for lifecycle 'lcq_00101'. Follow standard termination protocols to securely deprovision access, revoke licenses, and arrange for asset return."
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
        outputs=[]
    ),

    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_097",
        instruction=(
            "Initiate the onboarding of new Financial Analyst Jordan Lee (hr-228) in the Finance department for lifecycle 'lcq_00102'. Adhere to standard onboarding procedures and address any license shortage issues using appropriate escalation channels."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_098",
        instruction=(
            "Begin the offboarding process for terminated employee Riley Wang (employee_id 'emp_0011') for lifecycle 'lcq_00103'. Ensure compliance with standard termination procedures to securely revoke user access and manage the termination process."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_099",
        instruction=(
            "You are required to offboard terminated employee Peyton Shah (employee_id 'emp_0015') for lifecycle_id 'lcq_00082'. The employee has no hardware assigned. Adhere to the standard termination policy for a software-only user."
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
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_100",
        instruction=(
            "Coordinate a comprehensive, policy-compliant software-only offboarding for employee 'Jesse Moore' (emp_0027) regarding lifecycle 'lcq_00072'. You need to disable their account, remove their group memberships, locate and revoke all of their assigned licenses (Salesforce, TeamChat, M365), and archive their mailbox. Finalize the process by verifying they have no assigned hardware. It is crucial to ensure that all IAM actions are audited."
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
        outputs=[]
    ),
    Task(
    annotator="v2",
    user_id="It_Help_Desk_V2_101",
    instruction=(
        "You are tasked with onboarding an intern, 'Chris Green' (hr-902), into the 'Marketing' department as a 'Growth Marketer' for lifecycle 'lcq_00048'. Begin by executing the full, standard onboarding process: create their account, assign groups, provide the necessary M365 E3 license, and allocate a standard laptop, ensuring all actions are audited."
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
    outputs=[]
),
Task(
        annotator="v2",
        user_id="It_Help_Desk_V2_102",
        instruction=(
            "Coordinate the promotion of employee 'emp_0022' (Skyler Lopez) from 'Ops Coordinator' to 'Operations Manager' for lifecycle 'lcq_00053'. Your duties include updating their role-based access. This requires removing previous group memberships, assigning new ones, and provisioning the required 'M365 E5' license for their new position."
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
        outputs=[]
    ),

]