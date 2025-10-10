# Copyright owned by Sierra


def _find_all(items, **filters):
    """Find all items matching filters."""
    if not filters:
        return items
    
    results = []
    for item in items:
        match = True
        for key, value in filters.items():
            if item.get(key) != value:
                match = False
                break
        if match:
            results.append(item)
    return results



def _find_one(items, key, value):
    """Find one item in a list where item[key] == value."""
    for item in items:
        if item.get(key) == value:
            return item
    return None


from .get_employee_by_id import GetEmployeeById
from .find_employees import FindEmployees
from .get_directory_account import GetDirectoryAccount
from .create_directory_account import CreateDirectoryAccount
from .update_directory_account_status import UpdateDirectoryAccountStatus
from .set_account_groups import SetAccountGroups
from .add_account_groups import AddAccountGroups
from .remove_account_groups import RemoveAccountGroups
from .get_baseline_for_role import GetBaselineForRole
from .create_mailbox import CreateMailbox
from .update_mailbox_status import UpdateMailboxStatus
from .archive_mailbox import ArchiveMailbox
from .get_mailbox import GetMailbox
from .get_license_inventory import GetLicenseInventory
from .assign_license import AssignLicense
from .revoke_license import RevokeLicense
from .reserve_license import ReserveLicense
from .release_license_reservation import ReleaseLicenseReservation
from .ensure_license_capacity_or_open_jira import EnsureLicenseCapacityOrOpenJira
from .get_license_assignments import GetLicenseAssignments
from .find_assets import FindAssets
from .assign_asset import AssignAsset
from .update_asset_status import UpdateAssetStatus
from .create_device_workflow import CreateDeviceWorkflow
from .schedule_mdm_action import ScheduleMdmAction
from .request_asset_return import RequestAssetReturn
from .create_ticket import CreateTicket
from .update_ticket_status import UpdateTicketStatus
from .find_tickets import FindTickets
from .take_backlog_snapshot import TakeBacklogSnapshot
from .recompute_daily_metrics import RecomputeDailyMetrics
from .create_jira_ticket import CreateJiraTicket
from .update_jira_status import UpdateJiraStatus
from .find_jira_tickets import FindJiraTickets
from .ingest_hr_memo import IngestHrMemo
from .enqueue_lifecycle_event import EnqueueLifecycleEvent
from .update_lifecycle_status import UpdateLifecycleStatus
from .record_lifecycle_audit import RecordLifecycleAudit
from .get_app_accounts import GetAppAccounts
from .upsert_app_account import UpsertAppAccount
from .disable_app_account import DisableAppAccount
from .generate_service_desk_health_report import GenerateServiceDeskHealthReport
from .record_validation_issue import RecordValidationIssue

ALL_TOOLS = [
    GetEmployeeById,
    FindEmployees,
    GetDirectoryAccount,
    CreateDirectoryAccount,
    UpdateDirectoryAccountStatus,
    SetAccountGroups,
    AddAccountGroups,
    RemoveAccountGroups,
    GetBaselineForRole,
    CreateMailbox,
    UpdateMailboxStatus,
    ArchiveMailbox,
    GetMailbox,
    GetLicenseInventory,
    AssignLicense,
    RevokeLicense,
    ReserveLicense,
    ReleaseLicenseReservation,
    EnsureLicenseCapacityOrOpenJira,
    GetLicenseAssignments,
    FindAssets,
    AssignAsset,
    UpdateAssetStatus,
    CreateDeviceWorkflow,
    ScheduleMdmAction,
    RequestAssetReturn,
    CreateTicket,
    UpdateTicketStatus,
    FindTickets,
    TakeBacklogSnapshot,
    RecomputeDailyMetrics,
    CreateJiraTicket,
    UpdateJiraStatus,
    FindJiraTickets,
    IngestHrMemo,
    EnqueueLifecycleEvent,
    UpdateLifecycleStatus,
    RecordLifecycleAudit,
    GetAppAccounts,
    UpsertAppAccount,
    DisableAppAccount,
    GenerateServiceDeskHealthReport,
    RecordValidationIssue,
]
