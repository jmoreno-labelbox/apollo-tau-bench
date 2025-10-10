from datetime import datetime
# Copyright Sierra


def _fixed_now_iso():
    """Return current time in ISO format."""
    return datetime.now().isoformat()


from .get_consultant_profile import GetConsultantProfile
from .update_consultant_contact import UpdateConsultantContact
from .get_publisher_info import GetPublisherInfo
from .create_publisher import CreatePublisher
from .update_publisher_contact import UpdatePublisherContact
from .fetch_projects import FetchProjects
from .get_project_details import GetProjectDetails
from .create_project import CreateProject
from .fetch_time_entries import FetchTimeEntries
from .validate_time_entries import ValidateTimeEntries
from .group_hours_by_isbn import GroupHoursByISBN
from .resolve_hourly_rates import ResolveHourlyRates
from .calculate_invoice_totals import CalculateInvoiceTotals
from .insert_invoice import InsertInvoice
from .get_invoice_details import GetInvoiceDetails
from .insert_invoice_lines import InsertInvoiceLines
from .list_invoice_lines import ListInvoiceLines
from .record_invoice_audit import RecordInvoiceAudit
from .list_invoice_audit import ListInvoiceAudit
from .send_invoice_email import SendInvoiceEmail
from .fetch_invoices import FetchInvoices
from .compute_days_outstanding import ComputeDaysOutstanding
from .categorize_aging import CategorizeAging
from .summarize_ar_by_client import SummarizeARByClient
from .compute_collection_kp_is import ComputeCollectionKPIs
from .export_ar_aging_report import ExportARAgingReport
from .insert_dashboard_snapshot import InsertDashboardSnapshot
from .get_dashboard_snapshot_details import GetDashboardSnapshotDetails
from .insert_project_revenue_rows import InsertProjectRevenueRows
from .insert_monthly_revenue_rows import InsertMonthlyRevenueRows

ALL_TOOLS = [
    GetConsultantProfile,
    UpdateConsultantContact,
    GetPublisherInfo,
    CreatePublisher,
    UpdatePublisherContact,
    FetchProjects,
    GetProjectDetails,
    CreateProject,
    FetchTimeEntries,
    ValidateTimeEntries,
    GroupHoursByISBN,
    ResolveHourlyRates,
    CalculateInvoiceTotals,
    InsertInvoice,
    GetInvoiceDetails,
    InsertInvoiceLines,
    ListInvoiceLines,
    RecordInvoiceAudit,
    ListInvoiceAudit,
    SendInvoiceEmail,
    FetchInvoices,
    ComputeDaysOutstanding,
    CategorizeAging,
    SummarizeARByClient,
    ComputeCollectionKPIs,
    ExportARAgingReport,
    InsertDashboardSnapshot,
    GetDashboardSnapshotDetails,
    InsertProjectRevenueRows,
    InsertMonthlyRevenueRows,
]
