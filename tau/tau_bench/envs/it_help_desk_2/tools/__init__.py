# Copyright Sierra

from .ingest_hr_memo import IngestHrMemo
from .find_employees import FindEmployees
from .add_user_to_groups import AddUserToGroups
from .check_license_availability import CheckLicenseAvailability
from .assign_license import AssignLicense
from .update_license_inventory import UpdateLicenseInventory
from .find_available_asset import FindAvailableAsset
from .assign_asset import AssignAsset
from .create_device_workflow import CreateDeviceWorkflow
from .create_jira_ticket import CreateJiraTicket
from .create_audit_record import CreateAuditRecord
from .get_user_license_assignments import GetUserLicenseAssignments
from .get_license_assignment_by_type import GetLicenseAssignmentByType
from .revoke_license import RevokeLicense
from .remove_user_from_groups import RemoveUserFromGroups
from .archive_mailbox import ArchiveMailbox
from .get_user_asset import GetUserAsset
from .export_service_desk_tickets import ExportServiceDeskTickets
from .normalize_ticket_timestamps import NormalizeTicketTimestamps
from .calculate_service_desk_kp_is import CalculateServiceDeskKPIs
from .generate_report_pdf import GenerateReportPDF
from .save_metrics_to_database import SaveMetricsToDatabase
from .notify_management_team import NotifyManagementTeam
from .export_recent_tickets import ExportRecentTickets
from .calculate_ticket_kp_is import CalculateTicketKPIs
from .generate_health_report_pdf import GenerateHealthReportPDF
from .save_report_to_metrics_db import SaveReportToMetricsDB
from .notify_team_of_report import NotifyTeamOfReport
from .schedule_device_return import ScheduleDeviceReturn
from .read_onboarding_memo import ReadOnboardingMemo
from .validate_memo_fields import ValidateMemoFields
from .create_mailbox import CreateMailbox
from .enroll_device_in_mdm import EnrollDeviceInMDM
from .send_new_hire_welcome_email import SendNewHireWelcomeEmail
from .notify_manager import NotifyManager
from .add_memo_to_lifecycle_queue import AddMemoToLifecycleQueue
from .calculate_ticket_metrics import CalculateTicketMetrics
from .aggregate_ticket_kp_is import AggregateTicketKPIs
from .get_user_group_memberships import GetUserGroupMemberships
from .schedule_device_mdm_removal import ScheduleDeviceMDMRemoval
from .archive_user_app_accounts import ArchiveUserAppAccounts
from .update_lifecycle_queue_status import UpdateLifecycleQueueStatus
from .read_offboarding_memo import ReadOffboardingMemo
from .create_data_archive_entry import CreateDataArchiveEntry
from .filter_open_tickets import FilterOpenTickets
from .build_open_tickets_csv import BuildOpenTicketsCSV
from .unassign_asset import UnassignAsset
from .get_last_report_run import GetLastReportRun
from .compare_ticket_kp_is import CompareTicketKPIs
from .get_employee_by_id import GetEmployeeById
from .get_directory_account import GetDirectoryAccount
from .find_assets import FindAssets
from .get_license_assignments import GetLicenseAssignments
from .get_mailbox import GetMailbox
from .request_asset_return import RequestAssetReturn
from .update_asset_status import UpdateAssetStatus
from .get_baseline_for_role import GetBaselineForRole
from .schedule_mdm_action import ScheduleMdmAction
from .enqueue_lifecycle_event import EnqueueLifecycleEvent
from .record_lifecycle_audit import RecordLifecycleAudit
from .set_account_groups import SetAccountGroups
from .ensure_license_capacity_or_open_jira import EnsureLicenseCapacityOrOpenJira
from .update_lifecycle_status import UpdateLifecycleStatus
from .upsert_app_account import UpsertAppAccount
from .lookup_role_profile import LookupRoleProfile
from .set_directory_account_status import SetDirectoryAccountStatus
from .create_directory_account import CreateDirectoryAccount
from .get_user_by_upn_or_hr_id import GetUserByUpnOrHrId

ALL_TOOLS = [
    IngestHrMemo,
    FindEmployees,
    AddUserToGroups,
    CheckLicenseAvailability,
    AssignLicense,
    UpdateLicenseInventory,
    FindAvailableAsset,
    AssignAsset,
    CreateDeviceWorkflow,
    CreateJiraTicket,
    CreateAuditRecord,
    GetUserLicenseAssignments,
    GetLicenseAssignmentByType,
    RevokeLicense,
    RemoveUserFromGroups,
    ArchiveMailbox,
    GetUserAsset,
    ExportServiceDeskTickets,
    NormalizeTicketTimestamps,
    CalculateServiceDeskKPIs,
    GenerateReportPDF,
    SaveMetricsToDatabase,
    NotifyManagementTeam,
    ExportRecentTickets,
    CalculateTicketKPIs,
    GenerateHealthReportPDF,
    SaveReportToMetricsDB,
    NotifyTeamOfReport,
    ScheduleDeviceReturn,
    ReadOnboardingMemo,
    ValidateMemoFields,
    CreateMailbox,
    EnrollDeviceInMDM,
    SendNewHireWelcomeEmail,
    NotifyManager,
    AddMemoToLifecycleQueue,
    CalculateTicketMetrics,
    AggregateTicketKPIs,
    GetUserGroupMemberships,
    ScheduleDeviceMDMRemoval,
    ArchiveUserAppAccounts,
    UpdateLifecycleQueueStatus,
    ReadOffboardingMemo,
    CreateDataArchiveEntry,
    FilterOpenTickets,
    BuildOpenTicketsCSV,
    UnassignAsset,
    GetLastReportRun,
    CompareTicketKPIs,
    GetEmployeeById,
    GetDirectoryAccount,
    FindAssets,
    GetLicenseAssignments,
    GetMailbox,
    RequestAssetReturn,
    UpdateAssetStatus,
    GetBaselineForRole,
    ScheduleMdmAction,
    EnqueueLifecycleEvent,
    RecordLifecycleAudit,
    SetAccountGroups,
    EnsureLicenseCapacityOrOpenJira,
    UpdateLifecycleStatus,
    UpsertAppAccount,
    LookupRoleProfile,
    SetDirectoryAccountStatus,
    CreateDirectoryAccount,
    GetUserByUpnOrHrId,
]
