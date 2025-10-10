# Copyright Sierra

from .find_customer_by_name_tool import FindCustomerByNameTool
from .get_customer_accounts_tool import GetCustomerAccountsTool
from .get_account_transactions_tool import GetAccountTransactionsTool
from .transfer_funds_tool import TransferFundsTool
from .calculate_account_balance_tool import CalculateAccountBalanceTool
from .create_support_ticket_tool import CreateSupportTicketTool
from .search_transactions_tool import SearchTransactionsTool
from .apply_for_loan_tool import ApplyForLoanTool
from .add_beneficiary_tool import AddBeneficiaryTool
from .calculate_monthly_spending_tool import CalculateMonthlySpendingTool
from .get_customer_loans_tool import GetCustomerLoansTool
from .setup_scheduled_payment_tool import SetupScheduledPaymentTool
from .update_customer_contact_tool import UpdateCustomerContactTool
from .freeze_account_tool import FreezeAccountTool
from .get_customer_beneficiaries_tool import GetCustomerBeneficiariesTool
from .process_loan_payment_tool import ProcessLoanPaymentTool
from .validate_routing_number_tool import ValidateRoutingNumberTool
from .get_transaction_details_tool import GetTransactionDetailsTool
from .calculate_credit_utilization_tool import CalculateCreditUtilizationTool
from .resolve_ticket_tool import ResolveTicketTool
from .calculate_interest_earned_tool import CalculateInterestEarnedTool
from .update_loan_application_status_tool import UpdateLoanApplicationStatusTool
from .generate_account_statement_tool import GenerateAccountStatementTool
from .cancel_scheduled_payment_tool import CancelScheduledPaymentTool
from .search_customers_by_email_tool import SearchCustomersByEmailTool
from .get_customer_support_tickets_tool import GetCustomerSupportTicketsTool
from .generate_detailed_monthly_summary_tool import GenerateDetailedMonthlySummaryTool
from .retrieve_scheduled_payments_tool import RetrieveScheduledPaymentsTool
from .calculate_total_expenditure_tool import CalculateTotalExpenditureTool
from .calculate_total_withdrawal_tool import CalculateTotalWithdrawalTool
from .calculate_total_deposits_tool import CalculateTotalDepositsTool
from .get_support_tickets_for_account_tool import GetSupportTicketsForAccountTool
from .get_support_tickets_for_accounts_tool import GetSupportTicketsForAccountsTool
from .get_loan_applications_for_customer_tool import GetLoanApplicationsForCustomerTool
from .generate_detailed_monthly_report_tool import GenerateDetailedMonthlyReportTool
from .generate_monthly_account_summary_tool import GenerateMonthlyAccountSummaryTool
from .calculate_total_event_and_purchase_spending_tool import CalculateTotalEventAndPurchaseSpendingTool
from .get_account_changes_from_tickets_tool import GetAccountChangesFromTicketsTool
from .calculate_total_bill_payments_tool import CalculateTotalBillPaymentsTool
from .calculate_total_payments_tool import CalculateTotalPaymentsTool
from .calculate_total_deposits_and_purchases_tool import CalculateTotalDepositsAndPurchasesTool
from .calculate_total_atm_withdrawals_tool import CalculateTotalATMWithdrawalsTool
from .generate_financial_report_tool import GenerateFinancialReportTool

ALL_TOOLS = [
    FindCustomerByNameTool,
    GetCustomerAccountsTool,
    GetAccountTransactionsTool,
    TransferFundsTool,
    CalculateAccountBalanceTool,
    CreateSupportTicketTool,
    SearchTransactionsTool,
    ApplyForLoanTool,
    AddBeneficiaryTool,
    CalculateMonthlySpendingTool,
    GetCustomerLoansTool,
    SetupScheduledPaymentTool,
    UpdateCustomerContactTool,
    FreezeAccountTool,
    GetCustomerBeneficiariesTool,
    ProcessLoanPaymentTool,
    ValidateRoutingNumberTool,
    GetTransactionDetailsTool,
    CalculateCreditUtilizationTool,
    ResolveTicketTool,
    CalculateInterestEarnedTool,
    UpdateLoanApplicationStatusTool,
    GenerateAccountStatementTool,
    CancelScheduledPaymentTool,
    SearchCustomersByEmailTool,
    GetCustomerSupportTicketsTool,
    GenerateDetailedMonthlySummaryTool,
    RetrieveScheduledPaymentsTool,
    CalculateTotalExpenditureTool,
    CalculateTotalWithdrawalTool,
    CalculateTotalDepositsTool,
    GetSupportTicketsForAccountTool,
    GetSupportTicketsForAccountsTool,
    GetLoanApplicationsForCustomerTool,
    GenerateDetailedMonthlyReportTool,
    GenerateMonthlyAccountSummaryTool,
    CalculateTotalEventAndPurchaseSpendingTool,
    GetAccountChangesFromTicketsTool,
    CalculateTotalBillPaymentsTool,
    CalculateTotalPaymentsTool,
    CalculateTotalDepositsAndPurchasesTool,
    CalculateTotalATMWithdrawalsTool,
    GenerateFinancialReportTool,
]
