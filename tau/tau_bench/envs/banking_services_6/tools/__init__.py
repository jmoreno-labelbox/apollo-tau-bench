# Copyright owned by Sierra.

from .search_customer_by_name import SearchCustomerByName
from .get_customer_accounts import GetCustomerAccounts
from .get_account_balance import GetAccountBalance
from .calculate_sum import CalculateSum
from .update_customer_address import UpdateCustomerAddress
from .update_customer_phone import UpdateCustomerPhone
from .create_transaction import CreateTransaction
from .update_account_status import UpdateAccountStatus
from .create_customer import CreateCustomer
from .create_loan_application import CreateLoanApplication
from .add_beneficiary import AddBeneficiary
from .create_scheduled_payment import CreateScheduledPayment
from .get_transaction_details import GetTransactionDetails
from .create_support_ticket import CreateSupportTicket
from .get_beneficiary_by_name import GetBeneficiaryByName
from .get_beneficiary_details import GetBeneficiaryDetails
from .get_customer_financial_profile import GetCustomerFinancialProfile
from .get_account_details import GetAccountDetails
from .get_loan_details import GetLoanDetails
from .calculate_new_loan_payment import CalculateNewLoanPayment
from .list_account_types_by_currency import ListAccountTypesByCurrency
from .get_loan_application_details import GetLoanApplicationDetails
from .update_loan_balance import UpdateLoanBalance
from .create_account import CreateAccount
from .remove_beneficiary import RemoveBeneficiary
from .update_customer_personal_info import UpdateCustomerPersonalInfo
from .list_beneficiaries import ListBeneficiaries
from .update_customer_preferences import UpdateCustomerPreferences
from .update_customer_security_question import UpdateCustomerSecurityQuestion
from .create_deposit import CreateDeposit
from .get_account_transactions import GetAccountTransactions
from .update_scheduled_payment_status import UpdateScheduledPaymentStatus
from .get_scheduled_payment_details import GetScheduledPaymentDetails
from .get_scheduled_payments import GetScheduledPayments
from .get_customer_details import GetCustomerDetails
from .update_loan_status import UpdateLoanStatus
from .get_customer_loan_applications import GetCustomerLoanApplications
from .get_customer_loans import GetCustomerLoans
from .get_support_ticket_details import GetSupportTicketDetails
from .update_loan_application_status import UpdateLoanApplicationStatus
from .add_customer_phone_number import AddCustomerPhoneNumber
from .create_scheduled_internal_transfer import CreateScheduledInternalTransfer
from .get_total_accounts_count import GetTotalAccountsCount
from .get_total_beneficiaries_count import GetTotalBeneficiariesCount
from .get_total_customers_count import GetTotalCustomersCount
from .get_total_loan_applications_count import GetTotalLoanApplicationsCount
from .get_total_loans_count import GetTotalLoansCount
from .get_total_scheduled_payments_count import GetTotalScheduledPaymentsCount
from .get_total_support_tickets_count import GetTotalSupportTicketsCount
from .get_total_transactions_count import GetTotalTransactionsCount

ALL_TOOLS = [
    SearchCustomerByName,
    GetCustomerAccounts,
    GetAccountBalance,
    CalculateSum,
    UpdateCustomerAddress,
    UpdateCustomerPhone,
    CreateTransaction,
    UpdateAccountStatus,
    CreateCustomer,
    CreateLoanApplication,
    AddBeneficiary,
    CreateScheduledPayment,
    GetTransactionDetails,
    CreateSupportTicket,
    GetBeneficiaryByName,
    GetBeneficiaryDetails,
    GetCustomerFinancialProfile,
    GetAccountDetails,
    GetLoanDetails,
    CalculateNewLoanPayment,
    ListAccountTypesByCurrency,
    GetLoanApplicationDetails,
    UpdateLoanBalance,
    CreateAccount,
    RemoveBeneficiary,
    UpdateCustomerPersonalInfo,
    ListBeneficiaries,
    UpdateCustomerPreferences,
    UpdateCustomerSecurityQuestion,
    CreateDeposit,
    GetAccountTransactions,
    UpdateScheduledPaymentStatus,
    GetScheduledPaymentDetails,
    GetScheduledPayments,
    GetCustomerDetails,
    UpdateLoanStatus,
    GetCustomerLoanApplications,
    GetCustomerLoans,
    GetSupportTicketDetails,
    UpdateLoanApplicationStatus,
    AddCustomerPhoneNumber,
    CreateScheduledInternalTransfer,
    GetTotalAccountsCount,
    GetTotalBeneficiariesCount,
    GetTotalCustomersCount,
    GetTotalLoanApplicationsCount,
    GetTotalLoansCount,
    GetTotalScheduledPaymentsCount,
    GetTotalSupportTicketsCount,
    GetTotalTransactionsCount,
]
