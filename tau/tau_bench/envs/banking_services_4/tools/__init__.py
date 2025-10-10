import json
# Copyright Sierra


def load_json(file_path):
    """Load JSON from file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {}


from .get_customer_accounts_by_type import GetCustomerAccountsByType
from .list_recent_transactions_by_category import ListRecentTransactionsByCategory
from .get_scheduled_payments_due_in_range import GetScheduledPaymentsDueInRange
from .get_customer_risk_profile_summary import GetCustomerRiskProfileSummary
from .get_customer_contact_methods import GetCustomerContactMethods
from .list_active_loans_with_balances import ListActiveLoansWithBalances
from .fetch_beneficiaries_by_relationship import FetchBeneficiariesByRelationship
from .get_payment_schedule_for_account import GetPaymentScheduleForAccount
from .find_recent_support_tickets_by_category import FindRecentSupportTicketsByCategory
from .get_total_deposits_over_period import GetTotalDepositsOverPeriod
from .verify_beneficiary_exists import VerifyBeneficiaryExists
from .reassign_relationship_manager import ReassignRelationshipManager
from .deactivate_account_by_request import DeactivateAccountByRequest
from .create_support_ticket_for_transaction import CreateSupportTicketForTransaction
from .update_scheduled_payment_amount import UpdateScheduledPaymentAmount
from .merge_duplicate_customers_by_ssn import MergeDuplicateCustomersBySSN
from .add_employer_to_customer_profile import AddEmployerToCustomerProfile
from .get_account_overdraft_limit import GetAccountOverdraftLimit
from .close_active_account import CloseActiveAccount
from .check_funds_for_next_scheduled_payment import CheckFundsForNextScheduledPayment
from .initiate_fund_transfer_to_beneficiary import InitiateFundTransferToBeneficiary
from .make_loan_overpayment import MakeLoanOverpayment
from .adjust_loan_payment_due_date import AdjustLoanPaymentDueDate
from .apply_partial_refund_to_transaction import ApplyPartialRefundToTransaction
from .split_transaction_between_accounts import SplitTransactionBetweenAccounts
from .get_customer_total_balance import GetCustomerTotalBalance
from .enforce_kyc_refresh_for_customer import EnforceKYCRefreshForCustomer
from .lock_account_manually import LockAccountManually
from .review_overdraft_activity_and_adjust_limit import ReviewOverdraftActivityAndAdjustLimit
from .update_customer_communication_preference import UpdateCustomerCommunicationPreference
from .close_active_account import CloseActiveAccount
from .get_all_accounts_for_customer import GetAllAccountsForCustomer
from .create_support_ticket_for_account import CreateSupportTicketForAccount
from .get_account_balance import GetAccountBalance
from .get_loan_details import GetLoanDetails
from .apply_transaction_adjustment import ApplyTransactionAdjustment
from .transfer_funds_between_accounts import TransferFundsBetweenAccounts

ALL_TOOLS = [
    GetCustomerAccountsByType,
    ListRecentTransactionsByCategory,
    GetScheduledPaymentsDueInRange,
    GetCustomerRiskProfileSummary,
    GetCustomerContactMethods,
    ListActiveLoansWithBalances,
    FetchBeneficiariesByRelationship,
    GetPaymentScheduleForAccount,
    FindRecentSupportTicketsByCategory,
    GetTotalDepositsOverPeriod,
    VerifyBeneficiaryExists,
    ReassignRelationshipManager,
    DeactivateAccountByRequest,
    CreateSupportTicketForTransaction,
    UpdateScheduledPaymentAmount,
    MergeDuplicateCustomersBySSN,
    AddEmployerToCustomerProfile,
    GetAccountOverdraftLimit,
    CloseActiveAccount,
    CheckFundsForNextScheduledPayment,
    InitiateFundTransferToBeneficiary,
    MakeLoanOverpayment,
    AdjustLoanPaymentDueDate,
    ApplyPartialRefundToTransaction,
    SplitTransactionBetweenAccounts,
    GetCustomerTotalBalance,
    EnforceKYCRefreshForCustomer,
    LockAccountManually,
    ReviewOverdraftActivityAndAdjustLimit,
    UpdateCustomerCommunicationPreference,
    CloseActiveAccount,
    GetAllAccountsForCustomer,
    CreateSupportTicketForAccount,
    GetAccountBalance,
    GetLoanDetails,
    ApplyTransactionAdjustment,
    TransferFundsBetweenAccounts,
]
