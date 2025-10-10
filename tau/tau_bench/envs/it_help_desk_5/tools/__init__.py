# Copyright Sierra Corporation

from .get_employee_id import GetEmployeeId
from .employee_account_exists import EmployeeAccountExists
from .get_employee_info import GetEmployeeInfo
from .mailbox_exists import MailboxExists
from .get_employee_licenses import GetEmployeeLicenses
from .filter_employees import FilterEmployees
from .get_license_availability import GetLicenseAvailability
from .assign_licenses import AssignLicenses
from .get_license_info import GetLicenseInfo
from .get_job_licenses import GetJobLicenses
from .create_jira_ticket import CreateJiraTicket
from .filter_hr_memos import FilterHRMemos
from .device_assignment import DeviceAssignment
from .license_requires_renewal import LicenseRequiresRenewal
from .get_employee_by_license import GetEmployeeByLicense
from .filter_licenses import FilterLicenses
from .export_underutilized_licenses import ExportUnderutilizedLicenses
from .update_license_audit import UpdateLicenseAudit
from .archive_mailbox import ArchiveMailbox
from .log_lifecycle import LogLifecycle
from .missing_licenses import MissingLicenses
from .generate_reviewand_log import GenerateReviewandLog
from .get_ticket_info import GetTicketInfo
from .get_tickets_backlog import GetTicketsBacklog
from .filter_tickets import FilterTickets
from .save_report import SaveReport
from .assign_app_account import AssignAppAccount
from .assign_rbac_license import AssignRBACLicense
from .report_run import ReportRun
from .update_directory_account import UpdateDirectoryAccount
from .unassign_licenses import UnassignLicenses
from .notify import Notify
from .ticket_statistics import TicketStatistics
from .assign_device import AssignDevice

ALL_TOOLS = [
    GetEmployeeId,
    EmployeeAccountExists,
    GetEmployeeInfo,
    MailboxExists,
    GetEmployeeLicenses,
    FilterEmployees,
    GetLicenseAvailability,
    AssignLicenses,
    GetLicenseInfo,
    GetJobLicenses,
    CreateJiraTicket,
    FilterHRMemos,
    DeviceAssignment,
    LicenseRequiresRenewal,
    GetEmployeeByLicense,
    FilterLicenses,
    ExportUnderutilizedLicenses,
    UpdateLicenseAudit,
    ArchiveMailbox,
    LogLifecycle,
    MissingLicenses,
    GenerateReviewandLog,
    GetTicketInfo,
    GetTicketsBacklog,
    FilterTickets,
    SaveReport,
    AssignAppAccount,
    AssignRBACLicense,
    ReportRun,
    UpdateDirectoryAccount,
    UnassignLicenses,
    Notify,
    TicketStatistics,
    AssignDevice,
]
