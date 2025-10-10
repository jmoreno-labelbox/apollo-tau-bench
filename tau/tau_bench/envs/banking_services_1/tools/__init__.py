# Copyright owned by Sierra

from .create_customer_account_tool import CreateCustomerAccountTool
from .apply_for_loan_with_check_tool import ApplyForLoanWithCheckTool
from .schedule_payment_with_validation_tool import SchedulePaymentWithValidationTool
from .freeze_account_on_fraud_alert_tool import FreezeAccountOnFraudAlertTool
from .register_new_beneficiary_tool import RegisterNewBeneficiaryTool
from .delete_existing_beneficiary_tool import DeleteExistingBeneficiaryTool
from .update_account_preferences_tool import UpdateAccountPreferencesTool
from .get_account_balance_tool import GetAccountBalanceTool
from .get_customer_profile_tool import GetCustomerProfileTool
from .update_customer_email_tool import UpdateCustomerEmailTool
from .close_account_request_tool import CloseAccountRequestTool
from .submit_support_ticket_tool import SubmitSupportTicketTool
from .review_ticket_history_tool import ReviewTicketHistoryTool
from .unlock_account_by_security_check_tool import UnlockAccountBySecurityCheckTool
from .add_joint_account_holder_tool import AddJointAccountHolderTool
from .remove_joint_account_holder_tool import RemoveJointAccountHolderTool
from .verify_customer_identity_tool import VerifyCustomerIdentityTool
from .download_statement_by_date_tool import DownloadStatementByDateTool
from .list_linked_beneficiaries_tool import ListLinkedBeneficiariesTool
from .cancel_scheduled_payment_tool import CancelScheduledPaymentTool
from .aggregate_monthly_expenses_tool import AggregateMonthlyExpensesTool
from .auto_classify_support_ticket_priority_tool import AutoClassifySupportTicketPriorityTool
from .detect_suspicious_activity_and_alert_tool import DetectSuspiciousActivityAndAlertTool
from .get_account_transaction_history_tool import GetAccountTransactionHistoryTool
from .summarize_loan_applications_by_status_tool import SummarizeLoanApplicationsByStatusTool
from .transfer_funds_with_limit_check_tool import TransferFundsWithLimitCheckTool

ALL_TOOLS = [
    CreateCustomerAccountTool,
    ApplyForLoanWithCheckTool,
    SchedulePaymentWithValidationTool,
    FreezeAccountOnFraudAlertTool,
    RegisterNewBeneficiaryTool,
    DeleteExistingBeneficiaryTool,
    UpdateAccountPreferencesTool,
    GetAccountBalanceTool,
    GetCustomerProfileTool,
    UpdateCustomerEmailTool,
    CloseAccountRequestTool,
    SubmitSupportTicketTool,
    ReviewTicketHistoryTool,
    UnlockAccountBySecurityCheckTool,
    AddJointAccountHolderTool,
    RemoveJointAccountHolderTool,
    VerifyCustomerIdentityTool,
    DownloadStatementByDateTool,
    ListLinkedBeneficiariesTool,
    CancelScheduledPaymentTool,
    AggregateMonthlyExpensesTool,
    AutoClassifySupportTicketPriorityTool,
    DetectSuspiciousActivityAndAlertTool,
    GetAccountTransactionHistoryTool,
    SummarizeLoanApplicationsByStatusTool,
    TransferFundsWithLimitCheckTool,
]
