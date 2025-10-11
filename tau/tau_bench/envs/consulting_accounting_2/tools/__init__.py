# Copyright Sierra

from .ca_v2_get_consultant_profile import CaV2GetConsultantProfile
from .ca_v2_find_publisher_by_name import CaV2FindPublisherByName
from .ca_v2_find_project_by_isbn import CaV2FindProjectByIsbn
from .ca_v2_get_project_by_id import CaV2GetProjectById
from .ca_v2_get_project_by_id import CaV2GetProjectById
from .ca_v2_get_project_by_id import CaV2GetProjectById
from .ca_v2_get_projects_by_publisher import CaV2GetProjectsByPublisher
from .ca_v2_get_time_entries_for_period import CaV2GetTimeEntriesForPeriod
from .ca_v2_get_unpaid_invoices import CaV2GetUnpaidInvoices
from .ca_v2_get_invoice_by_id import CaV2GetInvoiceById
from .ca_v2_get_invoice_lines_for_invoice import CaV2GetInvoiceLinesForInvoice
from .ca_v2_get_expenses_by_category import CaV2GetExpensesByCategory
from .ca_v2_get_expense_categories import CaV2GetExpenseCategories
from .ca_v2_get_payment_behavior_by_publisher import CaV2GetPaymentBehaviorByPublisher
from .ca_v2_get_bank_accounts import CaV2GetBankAccounts
from .ca_v2_get_pipeline_opportunities import CaV2GetPipelineOpportunities
from .ca_v2_get_recurring_schedules import CaV2GetRecurringSchedules
from .ca_v2_calculate_invoice_aging import CaV2CalculateInvoiceAging
from .ca_v2_calculate_ytd_revenue import CaV2CalculateYtdRevenue
from .ca_v2_calculate_project_profitability import CaV2CalculateProjectProfitability
from .ca_v2_calculate_expense_summary import CaV2CalculateExpenseSummary
from .ca_v2_create_invoice import CaV2CreateInvoice
from .ca_v2_create_invoice_line import CaV2CreateInvoiceLine
from .ca_v2_update_invoice_payment import CaV2UpdateInvoicePayment
from .ca_v2_create_invoice_audit_entry import CaV2CreateInvoiceAuditEntry
from .ca_v2_create_expense import CaV2CreateExpense
from .ca_v2_forecast_cash_flow import CaV2ForecastCashFlow
from .ca_v2_create_dashboard_snapshot import CaV2CreateDashboardSnapshot
from .ca_v2_get_tax_rate_by_year import CaV2GetTaxRateByYear
from .ca_v2_create_project_revenue import CaV2CreateProjectRevenue
from .ca_v2_create_monthly_revenue import CaV2CreateMonthlyRevenue
from .ca_v2_create_scheduler_run import CaV2CreateSchedulerRun
from .ca_v2_generate_invoice_number import CaV2GenerateInvoiceNumber
from .ca_v2_calculate_hours_worked_in_period import CaV2CalculateHoursWorkedInPeriod
from .ca_v2_approve_time_entry import CaV2ApproveTimeEntry
from .ca_v2_calculate_bank_total import CaV2CalculateBankTotal

ALL_TOOLS = [
    CaV2GetConsultantProfile,
    CaV2FindPublisherByName,
    CaV2FindProjectByIsbn,
    CaV2GetProjectById,
    CaV2GetProjectById,
    CaV2GetProjectById,
    CaV2GetProjectsByPublisher,
    CaV2GetTimeEntriesForPeriod,
    CaV2GetUnpaidInvoices,
    CaV2GetInvoiceById,
    CaV2GetInvoiceLinesForInvoice,
    CaV2GetExpensesByCategory,
    CaV2GetExpenseCategories,
    CaV2GetPaymentBehaviorByPublisher,
    CaV2GetBankAccounts,
    CaV2GetPipelineOpportunities,
    CaV2GetRecurringSchedules,
    CaV2CalculateInvoiceAging,
    CaV2CalculateYtdRevenue,
    CaV2CalculateProjectProfitability,
    CaV2CalculateExpenseSummary,
    CaV2CreateInvoice,
    CaV2CreateInvoiceLine,
    CaV2UpdateInvoicePayment,
    CaV2CreateInvoiceAuditEntry,
    CaV2CreateExpense,
    CaV2ForecastCashFlow,
    CaV2CreateDashboardSnapshot,
    CaV2GetTaxRateByYear,
    CaV2CreateProjectRevenue,
    CaV2CreateMonthlyRevenue,
    CaV2CreateSchedulerRun,
    CaV2GenerateInvoiceNumber,
    CaV2CalculateHoursWorkedInPeriod,
    CaV2ApproveTimeEntry,
    CaV2CalculateBankTotal,
]
