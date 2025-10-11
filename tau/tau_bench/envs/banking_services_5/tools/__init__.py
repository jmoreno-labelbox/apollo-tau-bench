# Copyright Sierra

from .add_new_customer import AddNewCustomer
from .add_new_beneficiary_for_customer import AddNewBeneficiaryForCustomer
from .create_new_account_for_customer import CreateNewAccountForCustomer
from .create_new_loan_application import CreateNewLoanApplication
from .create_new_schedule_payment import CreateNewSchedulePayment
from .add_new_loan_for_customer import AddNewLoanForCustomer
from .add_support_ticket_for_customer_id import AddSupportTicketForCustomerId
from .create_new_transaction import CreateNewTransaction
from .block_account_for_customer_id import BlockAccountForCustomerId
from .get_customer_details_by_name import GetCustomerDetailsByName
from .get_all_accounts_of_customer_by_customer_id import GetAllAccountsOfCustomerByCustomerId
from .update_address_for_customer_id import UpdateAddressForCustomerId
from .get_customer_account_details_by_customer_id_and_account_type import GetCustomerAccountDetailsByCustomerIdAndAccountType
from .update_email_for_of_customer_id import UpdateEmailForOfCustomerId
from .update_contact_number_of_customer_id import UpdateContactNumberOfCustomerId
from .get_account_type_and_account_type_code import GetAccountTypeAndAccountTypeCode
from .pay_to_beneficiary import PayToBeneficiary
from .calculate_total_balance import CalculateTotalBalance
from .get_customer_account_details_by_customer_id import GetCustomerAccountDetailsByCustomerId
from .get_contact_details_of_customer import GetContactDetailsOfCustomer
from .get_all_beneficiaries_for_customer_id import GetAllBeneficiariesForCustomerId
from .get_beneficiary_details_for_customer_id_and_beneficiary_name import GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName
from .remove_beneficiary_by_beneficiary_id import RemoveBeneficiaryByBeneficiaryId
from .get_loan_application_status_by_customer_id_and_type import GetLoanApplicationStatusByCustomerIdAndType
from .process_loan_application_id import ProcessLoanApplicationId
from .get_loan_information_by_loan_id import GetLoanInformationByLoanId
from .get_loan_details_by_customer_id_and_type import GetLoanDetailsByCustomerIdAndType
from .get_scheduled_payment_details_by_customer_id_and_beneficiary_id import GetScheduledPaymentDetailsByCustomerIdAndBeneficiaryId
from .cancel_payment_by_scheduled_payment_id import CancelPaymentByScheduledPaymentId
from .get_transaction_details_by_account_id_for_time_duration import GetTransactionDetailsByAccountIdForTimeDuration
from .get_transaction_details_by_account_id_and_merchant_name import GetTransactionDetailsByAccountIdAndMerchantName
from .get_support_ticket_information_by_customer_id import GetSupportTicketInformationByCustomerId
from .transfer_money_same_currency import TransferMoneySameCurrency
from .transfer_money_with_conversion import TransferMoneyWithConversion
from .get_currency_conversion_amount import GetCurrencyConversionAmount
from .change_support_ticket_status import ChangeSupportTicketStatus
from .pay_to_beneficiary_same_currency import PayToBeneficiarySameCurrency
from .pay_to_beneficiary_with_conversion import PayToBeneficiaryWithConversion
from .check_account_balance import CheckAccountBalance
from .receive_payment import ReceivePayment
from .get_customer_details_by_customer_id import GetCustomerDetailsByCustomerId
from .get_account_details_by_customer_id_and_account_id import GetAccountDetailsByCustomerIdAndAccountId

def get_next_account_id(data, account_type='checking'):
    """Generate next account ID."""
    accounts = data.get('accounts', {})
    max_id = 0
    for acc_id in accounts.keys():
        if account_type in acc_id:
            try:
                num = int(acc_id.split('_')[-1])
                max_id = max(max_id, num)
            except (ValueError, IndexError):
                pass
    return f"acc_{account_type}_{max_id + 1}"


ALL_TOOLS = [
    AddNewCustomer,
    AddNewBeneficiaryForCustomer,
    CreateNewAccountForCustomer,
    CreateNewLoanApplication,
    CreateNewSchedulePayment,
    AddNewLoanForCustomer,
    AddSupportTicketForCustomerId,
    CreateNewTransaction,
    BlockAccountForCustomerId,
    GetCustomerDetailsByName,
    GetAllAccountsOfCustomerByCustomerId,
    UpdateAddressForCustomerId,
    GetCustomerAccountDetailsByCustomerIdAndAccountType,
    UpdateEmailForOfCustomerId,
    UpdateContactNumberOfCustomerId,
    GetAccountTypeAndAccountTypeCode,
    PayToBeneficiary,
    CalculateTotalBalance,
    GetCustomerAccountDetailsByCustomerId,
    GetContactDetailsOfCustomer,
    GetAllBeneficiariesForCustomerId,
    GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName,
    RemoveBeneficiaryByBeneficiaryId,
    GetLoanApplicationStatusByCustomerIdAndType,
    ProcessLoanApplicationId,
    GetLoanInformationByLoanId,
    GetLoanDetailsByCustomerIdAndType,
    GetScheduledPaymentDetailsByCustomerIdAndBeneficiaryId,
    CancelPaymentByScheduledPaymentId,
    GetTransactionDetailsByAccountIdForTimeDuration,
    GetTransactionDetailsByAccountIdAndMerchantName,
    GetSupportTicketInformationByCustomerId,
    TransferMoneySameCurrency,
    TransferMoneyWithConversion,
    GetCurrencyConversionAmount,
    ChangeSupportTicketStatus,
    PayToBeneficiarySameCurrency,
    PayToBeneficiaryWithConversion,
    CheckAccountBalance,
    ReceivePayment,
    GetCustomerDetailsByCustomerId,
    GetAccountDetailsByCustomerIdAndAccountId,
]
