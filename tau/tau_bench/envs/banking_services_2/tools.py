from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

def get_current_timestamp() -> str:
    return "2025-07-31T12:00:00.000000" + "Z" # per rules

def generate_unique_id() -> str:
    return 'fd520c73'

class FindCustomerByNameTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str = '', last_name: str = '') -> str:
        first_name = first_name.lower()
        last_name = last_name.lower()
        customers = data.get('customers', [])

        matches = []
        for customer in customers:
            if (customer['personal_info']['first_name'].lower() == first_name and
                customer['personal_info']['last_name'].lower() == last_name):
                matches.append({
                    'customer_id': customer['customer_id'],
                    'full_name': f"{customer['personal_info']['first_name']} {customer['personal_info']['last_name']}",
                    'email': customer['contact_info']['email_address']
                })

        return json.dumps(matches, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCustomerByName",
                "description": "Find customer records by first and last name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string", "description": "Customer's first name"},
                        "last_name": {"type": "string", "description": "Customer's last name"}
                    },
                    "required": ["first_name", "last_name"]
                }
            }
        }

class GetCustomerAccountsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        accounts = data.get('accounts', [])

        customer_accounts = []
        for account in accounts:
            if account['customer_id'] == customer_id:
                customer_accounts.append({
                    'account_id': account['account_id'],
                    'account_type': account['account_type'],
                    'balance': account['balance'],
                    'status': account['status'],
                    'last_4': account['account_number_last_4']
                })

        return json.dumps(customer_accounts, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerAccounts",
                "description": "Get all accounts for a specific customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }

class GetAccountTransactionsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, limit: int = 10) -> str:
        transactions = data.get('transactions', [])

        account_transactions = []
        for transaction in transactions:
            if transaction['account_id'] == account_id:
                account_transactions.append({
                    'transaction_id': transaction['transaction_id'],
                    'date': transaction['transaction_date'],
                    'amount': transaction['amount'],
                    'description': transaction['description'],
                    'status': transaction['status']
                })

        account_transactions.sort(key=lambda x: x['date'], reverse=True)
        return json.dumps(account_transactions[:limit], indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountTransactions",
                "description": "Get recent transactions for a specific account",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "limit": {"type": "integer", "description": "Maximum number of transactions to return", "default": 10}
                    },
                    "required": ["account_id"]
                }
            }
        }

class TransferFundsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], from_account_id: str, to_account_id: str, amount: float, description: str = 'Internal transfer') -> str:
        accounts = data.get('accounts', [])
        transactions = data.get('transactions', [])

        from_account = None
        to_account = None

        for account in accounts:
            if account['account_id'] == from_account_id:
                from_account = account
            elif account['account_id'] == to_account_id:
                to_account = account

        if not from_account or not to_account:
            return json.dumps({"error": "Account not found"}, indent=2)

        if from_account['balance'] < amount:
            return json.dumps({"error": "Insufficient funds"}, indent=2)

        from_account['balance'] -= amount
        to_account['balance'] += amount

        debit_transaction = {
            "transaction_id": f"txn_{generate_unique_id()}",
            "account_id": from_account_id,
            "transaction_date": get_current_timestamp(),
            "amount": -amount,
            "currency": "USD",
            "transaction_type": "Transfer",
            "description": f"Transfer to {to_account_id}: {description}",
            "status": "Completed",
            "channel": "Online"
        }

        credit_transaction = {
            "transaction_id": f"txn_{generate_unique_id()}",
            "account_id": to_account_id,
            "transaction_date": get_current_timestamp(),
            "amount": amount,
            "currency": "USD",
            "transaction_type": "Transfer",
            "description": f"Transfer from {from_account_id}: {description}",
            "status": "Completed",
            "channel": "Online"
        }

        transactions.append(debit_transaction)
        transactions.append(credit_transaction)

        return json.dumps({
            "success": True,
            "transfer_amount": amount,
            "from_account_new_balance": from_account['balance'],
            "to_account_new_balance": to_account['balance'],
            "debit_transaction_id": debit_transaction['transaction_id'],
            "credit_transaction_id": credit_transaction['transaction_id']
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferFunds",
                "description": "Transfer funds between two accounts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account_id": {"type": "string", "description": "Source account ID"},
                        "to_account_id": {"type": "string", "description": "Destination account ID"},
                        "amount": {"type": "number", "description": "Amount to transfer"},
                        "description": {"type": "string", "description": "Transfer description"}
                    },
                    "required": ["from_account_id", "to_account_id", "amount"]
                }
            }
        }

class CalculateAccountBalanceTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        accounts = data.get('accounts', [])

        for account in accounts:
            if account['account_id'] == account_id:
                return json.dumps({
                    "account_id": account_id,
                    "current_balance": account['balance'],
                    "account_type": account['account_type'],
                    "currency": account['currency']
                }, indent=2)

        return json.dumps({"error": f"Account {account_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAccountBalance",
                "description": "Get current balance for a specific account",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"}
                    },
                    "required": ["account_id"]
                }
            }
        }


class CreateSupportTicketTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, subject: str, description: str, priority: str = 'Medium') -> str:
        support_tickets = data.get('support_tickets', [])

        ticket_id = f"ticket_{generate_unique_id()}"
        new_ticket = {
            "ticket_id": ticket_id,
            "customer_id": customer_id,
            "subject": subject,
            "description": description,
            "priority": priority,
            "status": "Open",
            "created_date": get_current_timestamp(),
            "assigned_agent": None,
            "resolution": None
        }

        support_tickets.append(new_ticket)

        return json.dumps({
            "ticket_id": ticket_id,
            "status": "Created",
            "priority": priority,
            "created_date": new_ticket["created_date"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSupportTicket",
                "description": "Create a new customer support ticket",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "subject": {"type": "string", "description": "Ticket subject"},
                        "description": {"type": "string", "description": "Detailed issue description"},
                        "priority": {"type": "string", "description": "Priority level", "enum": ["Low", "Medium", "High", "Urgent"]}
                    },
                    "required": ["customer_id", "subject", "description"]
                }
            }
        }

class SearchTransactionsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, 
               end_date: str = None, min_amount: float = None, max_amount: float = None, description_keywords: str = None, 
               transaction_type: str = None) -> str:
        transactions = data.get('transactions', [])
        filtered_transactions = []

        for transaction in transactions:
            if transaction['account_id'] != account_id:
                continue

            if start_date and transaction['transaction_date'] < start_date:
                continue
            if end_date and transaction['transaction_date'] > end_date:
                continue
            if min_amount is not None and abs(transaction['amount']) < min_amount:
                continue
            if max_amount is not None and abs(transaction['amount']) > max_amount:
                continue
            if transaction_type and transaction['transaction_type'] != transaction_type:
                continue

            filtered_transactions.append({
                'transaction_id': transaction['transaction_id'],
                'date': transaction['transaction_date'],
                'amount': transaction['amount'],
                'type': transaction['transaction_type'],
                'description': transaction['description'],
                'merchant': transaction.get('merchant_name', 'N/A')
            })

        return json.dumps(filtered_transactions, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchTransactions",
                "description": "Search transactions with filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"},
                        "min_amount": {"type": "number", "description": "Minimum transaction amount"},
                        "max_amount": {"type": "number", "description": "Maximum transaction amount"},
                        "transaction_type": {"type": "string", "description": "Transaction type filter"}
                    },
                    "required": ["account_id"]
                }
            }
        }

class ApplyForLoanTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, loan_type: str = None, 
               requested_amount: float = None, purpose: str = None, 
               annual_income: float = None) -> str:
        loan_applications = data.get('loan_applications', [])

        application_id = f"loan_app_{generate_unique_id()}"

        credit_score = 720
        if annual_income > 80000:
            credit_score = 750
        elif annual_income < 40000:
            credit_score = 650

        status = "Under Review"
        if requested_amount > annual_income * 5:
            status = "Requires Additional Documentation"

        new_application = {
            "application_id": application_id,
            "customer_id": customer_id,
            "loan_type": loan_type,
            "requested_amount": requested_amount,
            "purpose": purpose,
            "annual_income": annual_income,
            "credit_score": credit_score,
            "status": status,
            "application_date": get_current_timestamp(),
            "decision": None,
            "approved_amount": None
        }

        loan_applications.append(new_application)

        return json.dumps({
            "application_id": application_id,
            "status": status,
            "credit_score": credit_score,
            "application_date": new_application["application_date"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyForLoan",
                "description": "Submit a loan application",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "loan_type": {"type": "string", "description": "Type of loan", "enum": ["Personal", "Auto", "Mortgage", "Business"]},
                        "requested_amount": {"type": "number", "description": "Requested loan amount"},
                        "purpose": {"type": "string", "description": "Purpose of the loan"},
                        "annual_income": {"type": "number", "description": "Applicant's annual income"}
                    },
                    "required": ["customer_id", "loan_type", "requested_amount", "purpose", "annual_income"]
                }
            }
        }

class AddBeneficiaryTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_name: str = None, 
               account_number: str = None, routing_number: str = None, bank_name: str = None, iban: str = None) -> str:
        beneficiaries = data.get('beneficiaries', [])

        beneficiary_id = f"ben_{generate_unique_id()}"

        new_beneficiary = {
            "beneficiary_id": beneficiary_id,
            "customer_id": customer_id,
            "beneficiary_name": beneficiary_name,
            "account_number": account_number,
            "routing_number": routing_number,
            "bank_name": bank_name,
            "status": "Active",
            "date_added": get_current_timestamp()
        }
        
        if iban:
            new_beneficiary["iban"] = iban

        beneficiaries.append(new_beneficiary)

        return json.dumps({
            "beneficiary_id": beneficiary_id,
            "beneficiary_name": beneficiary_name,
            "status": "Active",
            "date_added": new_beneficiary["date_added"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddBeneficiary",
                "description": "Add a new payment beneficiary",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "beneficiary_name": {"type": "string", "description": "Name of beneficiary"},
                        "account_number": {"type": "string", "description": "Beneficiary account number"},
                        "routing_number": {"type": "string", "description": "Bank routing number"},
                        "iban": {"type": "string", "description": "Iban routing number"},
                        "bank_name": {"type": "string", "description": "Bank name"},
                        "sort_code": {"type": "string", "description": "Sort_code routing number"}
                    },
                    "required": ["customer_id", "beneficiary_name", "bank_name"]
                }
            }
        }

class CalculateMonthlySpendingTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, month: int = None, year: int = None) -> str:
        transactions = data.get('transactions', [])

        total_spending = 0
        spending_by_category = {}
        transaction_count = 0

        for transaction in transactions:
            if transaction['account_id'] != account_id:
                continue
            if transaction['amount'] >= 0:
                continue

            trans_date = transaction['transaction_date']
            if f"{year}-{month:02d}" not in trans_date:
                continue

            amount = abs(transaction['amount'])
            total_spending += amount
            transaction_count += 1

            merchant = transaction.get('merchant_name', 'Other')
            if merchant not in spending_by_category:
                spending_by_category[merchant] = 0
            spending_by_category[merchant] += amount

        return json.dumps({
            "account_id": account_id,
            "month": f"{year}-{month:02d}",
            "total_spending": total_spending,
            "transaction_count": transaction_count,
            "spending_by_merchant": spending_by_category,
            "average_transaction": round(total_spending / max(1, transaction_count), 2)
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateMonthlySpending",
                "description": "Calculate spending summary for a specific month",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "month": {"type": "integer", "description": "Month (1-12)"},
                        "year": {"type": "integer", "description": "Year"}
                    },
                    "required": ["account_id", "month", "year"]
                }
            }
        }

class GetCustomerLoansTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        loans = data.get('loans', [])

        customer_loans = []
        for loan in loans:
            if loan['customer_id'] == customer_id:
                customer_loans.append({
                    'loan_id': loan['loan_id'],
                    'loan_type': loan['loan_type'],
                    'original_amount': loan['principal_amount'],
                    'current_balance': loan['current_balance'],
                    'interest_rate': loan['interest_rate'],
                    'monthly_payment': loan['monthly_payment'],
                    'status': loan['status']
                })

        return json.dumps(customer_loans, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerLoans",
                "description": "Get all loans for a specific customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }

class SetupScheduledPaymentTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, from_account_id: str = None, 
               beneficiary_id: str = None, amount: float = None, frequency: str = None, 
               start_date: str = None) -> str:
        scheduled_payments = data.get('scheduled_payments', [])

        payment_id = f"sched_{generate_unique_id()}"

        new_payment = {
            "payment_id": payment_id,
            "customer_id": customer_id,
            "from_account_id": from_account_id,
            "beneficiary_id": beneficiary_id,
            "amount": amount,
            "frequency": frequency,
            "start_date": start_date,
            "status": "Active",
            "created_date": get_current_timestamp(),
            "next_payment_date": start_date
        }

        scheduled_payments.append(new_payment)

        return json.dumps({
            "payment_id": payment_id,
            "status": "Active",
            "next_payment_date": start_date,
            "amount": amount,
            "frequency": frequency
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetupScheduledPayment",
                "description": "Setup a recurring scheduled payment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "from_account_id": {"type": "string", "description": "Source account"},
                        "beneficiary_id": {"type": "string", "description": "Beneficiary identifier"},
                        "amount": {"type": "number", "description": "Payment amount"},
                        "frequency": {"type": "string", "description": "Payment frequency", "enum": ["Weekly", "Monthly", "Quarterly"]},
                        "start_date": {"type": "string", "description": "First payment date (YYYY-MM-DD)"}
                    },
                    "required": ["customer_id", "from_account_id", "beneficiary_id", "amount", "frequency", "start_date"]
                }
            }
        }

class UpdateCustomerContactTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, email: str = None, phone: str = None) -> str:
        customers = data.get('customers', [])

        for customer in customers:
            if customer['customer_id'] == customer_id:
                if email:
                    customer['contact_info']['email_address'] = email
                if phone:
                    for phone_entry in customer['contact_info']['phone_numbers']:
                        if phone_entry['is_primary']:
                            phone_entry['number'] = phone
                            break

                return json.dumps({
                    "customer_id": customer_id,
                    "updated_email": email,
                    "updated_phone": phone,
                    "status": "Updated"
                }, indent=2)

        return json.dumps({"error": f"Customer {customer_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerContact",
                "description": "Update customer contact information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "email": {"type": "string", "description": "New email address"},
                        "phone": {"type": "string", "description": "New phone number"}
                    },
                    "required": ["customer_id"]
                }
            }
        }

class FreezeAccountTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, reason: str = 'Customer request') -> str:
        accounts = data.get('accounts', [])

        for account in accounts:
            if account['account_id'] == account_id:
                old_status = account['status']
                account['status'] = 'Frozen'
                account['freeze_reason'] = reason
                account['freeze_date'] = get_current_timestamp()

                return json.dumps({
                    "account_id": account_id,
                    "old_status": old_status,
                    "new_status": "Frozen",
                    "reason": reason,
                    "freeze_date": account['freeze_date']
                }, indent=2)

        return json.dumps({"error": f"Account {account_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FreezeAccount",
                "description": "Freeze an account to prevent transactions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "reason": {"type": "string", "description": "Reason for freezing"}
                    },
                    "required": ["account_id"]
                }
            }
        }

class GetCustomerBeneficiariesTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        beneficiaries = data.get('beneficiaries', [])

        customer_beneficiaries = []
        for beneficiary in beneficiaries:
            if beneficiary['customer_id'] == customer_id:
                bank_name = beneficiary.get('bank_name')
                if not bank_name and 'account_details' in beneficiary:
                    bank_name = beneficiary['account_details'].get('bank_name', 'N/A')

                customer_beneficiaries.append({
                    'beneficiary_id': beneficiary['beneficiary_id'],
                    'beneficiary_name': beneficiary['beneficiary_name'],
                    'bank_name': bank_name or 'N/A',
                    'status': beneficiary.get('status', 'Active'),
                    'date_added': beneficiary.get('date_added', 'N/A')
                })

        return json.dumps(customer_beneficiaries, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerBeneficiaries",
                "description": "Get all beneficiaries for a customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }

class ProcessLoanPaymentTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, payment_amount: float = None, from_account_id: str = None) -> str:
        loans = data.get('loans', [])
        accounts = data.get('accounts', [])
        transactions = data.get('transactions', [])

        loan = None
        for l in loans:
            if l['loan_id'] == loan_id:
                loan = l
                break

        if not loan:
            return json.dumps({"error": f"Loan {loan_id} not found"}, indent=2)

        account = None
        for a in accounts:
            if a['account_id'] == from_account_id:
                account = a
                break

        if not account or account['balance'] < payment_amount:
            return json.dumps({"error": "Insufficient funds"}, indent=2)

        account['balance'] -= payment_amount
        loan['current_balance'] -= payment_amount

        transaction = {
            "transaction_id": f"txn_{generate_unique_id()}",
            "account_id": from_account_id,
            "transaction_date": get_current_timestamp(),
            "amount": -payment_amount,
            "currency": "USD",
            "transaction_type": "Loan Payment",
            "description": f"Loan payment for {loan_id}",
            "status": "Completed",
            "channel": "Online"
        }

        transactions.append(transaction)

        return json.dumps({
            "loan_id": loan_id,
            "payment_amount": payment_amount,
            "new_loan_balance": loan['current_balance'],
            "new_account_balance": account['balance'],
            "transaction_id": transaction['transaction_id']
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessLoanPayment",
                "description": "Make a payment towards a loan",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_id": {"type": "string", "description": "Loan identifier"},
                        "payment_amount": {"type": "number", "description": "Payment amount"},
                        "from_account_id": {"type": "string", "description": "Source account for payment"}
                    },
                    "required": ["loan_id", "payment_amount", "from_account_id"]
                }
            }
        }

class ValidateRoutingNumberTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], routing_number: str = None) -> str:
        valid_routing_numbers = {
            "021000021": "Chase Bank",
            "011401533": "Wells Fargo",
            "121042882": "Wells Fargo CA",
            "111000025": "Bank of America",
            "026009593": "Bank of America",
            "031201360": "Citibank",
            "221172186": "TD Bank"
        }

        is_valid = routing_number in valid_routing_numbers
        bank_name = valid_routing_numbers.get(routing_number, "Unknown")

        return json.dumps({
            "routing_number": routing_number,
            "is_valid": is_valid,
            "bank_name": bank_name if is_valid else "Invalid routing number"
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateRoutingNumber",
                "description": "Validate a bank routing number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "routing_number": {"type": "string", "description": "9-digit routing number"}
                    },
                    "required": ["routing_number"]
                }
            }
        }

class GetTransactionDetailsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str = None) -> str:
        transactions = data.get('transactions', [])

        for transaction in transactions:
            if transaction['transaction_id'] == transaction_id:
                return json.dumps({
                    'transaction_id': transaction['transaction_id'],
                    'account_id': transaction['account_id'],
                    'date': transaction['transaction_date'],
                    'amount': transaction['amount'],
                    'type': transaction['transaction_type'],
                    'description': transaction['description'],
                    'merchant': transaction.get('merchant_name', 'N/A'),
                    'channel': transaction['channel'],
                    'status': transaction['status']
                }, indent=2)

        return json.dumps({"error": f"Transaction {transaction_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTransactionDetails",
                "description": "Get detailed information about a specific transaction",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {"type": "string", "description": "Transaction identifier"}
                    },
                    "required": ["transaction_id"]
                }
            }
        }

class CalculateCreditUtilizationTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        accounts = data.get('accounts', [])

        credit_accounts = []
        total_balance = 0
        total_limit = 0

        for account in accounts:
            if (account['customer_id'] == customer_id and
                account['account_type'] == 'Credit Card'):
                credit_limit = account.get('credit_limit', 5000)
                current_balance = abs(account['balance'])

                utilization = (current_balance / credit_limit) * 100 if credit_limit > 0 else 0

                credit_accounts.append({
                    'account_id': account['account_id'],
                    'balance': current_balance,
                    'credit_limit': credit_limit,
                    'utilization_percent': round(utilization, 2)
                })

                total_balance += current_balance
                total_limit += credit_limit

        overall_utilization = (total_balance / total_limit) * 100 if total_limit > 0 else 0

        return json.dumps({
            "customer_id": customer_id,
            "credit_accounts": credit_accounts,
            "total_balance": total_balance,
            "total_limit": total_limit,
            "overall_utilization_percent": round(overall_utilization, 2)
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateCreditUtilization",
                "description": "Calculate credit utilization for all customer credit cards",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }

class ResolveTicketTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_id: str, resolution: str, agent_id: str = 'SYSTEM') -> str:
        support_tickets = data.get('support_tickets', [])

        for ticket in support_tickets:
            if ticket['ticket_id'] == ticket_id:
                ticket['status'] = 'Resolved'
                ticket['resolution'] = resolution
                ticket['assigned_agent'] = agent_id
                ticket['resolved_date'] = get_current_timestamp()

                return json.dumps({
                    "ticket_id": ticket_id,
                    "status": "Resolved",
                    "resolution": resolution,
                    "resolved_by": agent_id,
                    "resolved_date": ticket['resolved_date']
                }, indent=2)

        return json.dumps({"error": f"Ticket {ticket_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolveTicket",
                "description": "Resolve a customer support ticket",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "Ticket identifier"},
                        "resolution": {"type": "string", "description": "Resolution description"},
                        "agent_id": {"type": "string", "description": "Agent resolving the ticket"}
                    },
                    "required": ["ticket_id", "resolution"]
                }
            }
        }

class CalculateInterestEarnedTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, days: int = 30) -> str:
        accounts = data.get('accounts', [])

        for account in accounts:
            if account['account_id'] == account_id:
                if account['account_type'] != 'Savings':
                    return json.dumps({"error": "Interest calculation only available for savings accounts"}, indent=2)

                balance = account['balance']
                annual_rate = account.get('interest_rate', 0.02)
                daily_rate = annual_rate / 365

                interest_earned = balance * daily_rate * days

                return json.dumps({
                    "account_id": account_id,
                    "current_balance": balance,
                    "annual_interest_rate": annual_rate,
                    "days_calculated": days,
                    "interest_earned": round(interest_earned, 2),
                    "projected_balance": round(balance + interest_earned, 2)
                }, indent=2)

        return json.dumps({"error": f"Account {account_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateInterestEarned",
                "description": "Calculate interest earned for a savings account",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Savings account identifier"},
                        "days": {"type": "integer", "description": "Number of days to calculate", "default": 30}
                    },
                    "required": ["account_id"]
                }
            }
        }

class UpdateLoanApplicationStatusTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], application_id: str, status: str, approved_amount: float = None, notes: str = '') -> str:
        loan_applications = data.get('loan_applications', [])

        for application in loan_applications:
            if application['application_id'] == application_id:
                application['status'] = status
                application['decision'] = status
                application['decision_date'] = get_current_timestamp()
                application['notes'] = notes

                if approved_amount:
                    application['approved_amount'] = approved_amount

                return json.dumps({
                    "application_id": application_id,
                    "new_status": status,
                    "approved_amount": approved_amount,
                    "decision_date": application['decision_date'],
                    "notes": notes
                }, indent=2)

        return json.dumps({"error": f"Application {application_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateLoanApplicationStatus",
                "description": "Update the status of a loan application",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {"type": "string", "description": "Loan application identifier"},
                        "status": {"type": "string", "description": "New status", "enum": ["Approved", "Denied", "Under Review"]},
                        "approved_amount": {"type": "number", "description": "Approved loan amount"},
                        "notes": {"type": "string", "description": "Decision notes"}
                    },
                    "required": ["application_id", "status"]
                }
            }
        }

class GenerateAccountStatementTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        accounts = data.get('accounts', [])
        transactions = data.get('transactions', [])

        account = None
        for a in accounts:
            if a['account_id'] == account_id:
                account = a
                break

        if not account:
            return json.dumps({"error": f"Account {account_id} not found"}, indent=2)

        statement_transactions = []
        total_credits = 0
        total_debits = 0

        for transaction in transactions:
            if (transaction['account_id'] == account_id and
                start_date <= transaction['transaction_date'] <= end_date):

                statement_transactions.append({
                    'date': transaction['transaction_date'],
                    'description': transaction['description'],
                    'amount': transaction['amount'],
                    'type': transaction['transaction_type']
                })

                if transaction['amount'] > 0:
                    total_credits += transaction['amount']
                else:
                    total_debits += abs(transaction['amount'])

        return json.dumps({
            "account_id": account_id,
            "account_type": account['account_type'],
            "statement_period": f"{start_date} to {end_date}",
            "opening_balance": account['balance'] + total_debits - total_credits,
            "closing_balance": account['balance'],
            "total_credits": total_credits,
            "total_debits": total_debits,
            "transaction_count": len(statement_transactions),
            "transactions": statement_transactions
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateAccountStatement",
                "description": "Generate account statement for a date range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Statement start date (ISO format)"},
                        "end_date": {"type": "string", "description": "Statement end date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

class CancelScheduledPaymentTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str, reason: str = 'Customer request') -> str:
        scheduled_payments = data.get('scheduled_payments', [])

        for payment in scheduled_payments:
            if payment['payment_id'] == payment_id:
                old_status = payment['status']
                payment['status'] = 'Cancelled'
                payment['cancellation_reason'] = reason
                payment['cancelled_date'] = get_current_timestamp()

                return json.dumps({
                    "payment_id": payment_id,
                    "old_status": old_status,
                    "new_status": "Cancelled",
                    "reason": reason,
                    "cancelled_date": payment['cancelled_date']
                }, indent=2)

        return json.dumps({"error": f"Scheduled payment {payment_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelScheduledPayment",
                "description": "Cancel a scheduled payment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "payment_id": {"type": "string", "description": "Scheduled payment identifier"},
                        "reason": {"type": "string", "description": "Cancellation reason"}
                    },
                    "required": ["payment_id"]
                }
            }
        }

class SearchCustomersByEmailTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], email_domain: str = '', partial_email: str = '') -> str:
        customers = data.get('customers', [])
        matches = []

        for customer in customers:
            email = customer['contact_info']['email_address']

            if email_domain and email.endswith(f"@{email_domain}"):
                matches.append({
                    'customer_id': customer['customer_id'],
                    'name': f"{customer['personal_info']['first_name']} {customer['personal_info']['last_name']}",
                    'email': email
                })
            elif partial_email and partial_email.lower() in email.lower():
                matches.append({
                    'customer_id': customer['customer_id'],
                    'name': f"{customer['personal_info']['first_name']} {customer['personal_info']['last_name']}",
                    'email': email
                })

        return json.dumps(matches, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCustomersByEmail",
                "description": "Search customers by email domain or partial email",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_domain": {"type": "string", "description": "Email domain to search for"},
                        "partial_email": {"type": "string", "description": "Partial email address to match"}
                    }
                }
            }
        }

class GetCustomerSupportTicketsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, status: str = None) -> str:
        support_tickets = data.get('support_tickets', [])
        customer_tickets = []

        for ticket in support_tickets:
            if ticket['customer_id'] == customer_id:
                if not status or ticket['status'] == status:
                    subject = ticket.get('subject', ticket.get('category', 'N/A'))

                    customer_tickets.append({
                        'ticket_id': ticket['ticket_id'],
                        'subject': subject,
                        'priority': ticket['priority'],
                        'status': ticket['status'],
                        'created_date': ticket.get('created_date', 'N/A'),
                        'assigned_agent': ticket.get('assigned_agent', 'Unassigned')
                    })

        return json.dumps(customer_tickets, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerSupportTickets",
                "description": "Get support tickets for a customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "status": {"type": "string", "description": "Filter by status", "enum": ["Open", "Resolved", "In Progress"]}
                    },
                    "required": ["customer_id"]
                }
            }
        }

class GenerateDetailedMonthlySummaryTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, month: str = None) -> str:
        transactions = data.get('transactions', [])
        scheduled_payments = data.get('scheduled_payments', [])
        support_tickets = data.get('support_tickets', [])

        start_date = f"{month}-01T00:00:00Z"
        end_date = f"{month}-31T23:59:59Z"

        purchases = []
        deposits = []
        total_purchases = 0
        total_deposits = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            if txn.get('transaction_date', '') < start_date or txn.get('transaction_date', '') > end_date:
                continue
            if txn.get('transaction_type') == 'Purchase':
                purchases.append(txn)
                total_purchases += abs(txn.get('amount', 0))
            if txn.get('transaction_type') == 'Deposit':
                deposits.append(txn)
                total_deposits += txn.get('amount', 0)

        scheduled = []
        recurring = []
        for payment in scheduled_payments:
            if payment.get('from_account_id', None) == account_id and payment.get('next_payment_date', '')[:7] == month:
                scheduled.append(payment)
                if payment.get('frequency') in ['Monthly', 'Weekly']:
                    recurring.append(payment)

        tickets = []
        for ticket in support_tickets:
            if ticket.get('account_id', '') == account_id and ticket.get('created_date', '')[:7] == month:
                tickets.append(ticket)

        summary = {
            "account_id": account_id,
            "month": month,
            "total_purchases": total_purchases,
            "total_deposits": total_deposits,
            "scheduled_payments": scheduled,
            "recurring_payments": recurring,
            "support_tickets": tickets
        }
        return json.dumps(summary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateDetailedMonthlySummary",
                "description": "Generate a detailed monthly summary for an account including purchases, deposits, scheduled payments, and support tickets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"}
                    },
                    "required": ["account_id", "month"]
                }
            }
        }

class RetrieveScheduledPaymentsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, source_account_id: str = None, month: str = None, frequency: Any = None, source_account_ids: list = None) -> str:
        # Support source_account_ids parameter
        if source_account_ids and not source_account_id:
            source_account_id = source_account_ids[0] if source_account_ids else None
        scheduled_payments = data.get('scheduled_payments', [])
        results = []

        for payment in scheduled_payments:
            if payment.get('customer_id') != customer_id:
                continue
            if payment.get('from_account_id', None) != source_account_id:
                continue
            next_payment_date = payment.get('next_payment_date', '')
            if not next_payment_date.startswith(month):
                continue
            if frequency and payment.get('frequency') not in frequency:
                continue
            results.append({
                "payment_id": payment.get("payment_id"),
                "amount": payment.get("amount"),
                "frequency": payment.get("frequency"),
                "next_payment_date": payment.get("next_payment_date"),
                "status": payment.get("status"),
                "beneficiary_id": payment.get("beneficiary_id"),
                "from_account_id": payment.get("from_account_id", "N/A"),
            })

        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrieveScheduledPayments",
                "description": "Retrieve scheduled payments for a customer and account, with optional month and frequency filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "source_account_id": {"type": "string", "description": "Source account identifier"},
                        "month": {"type": "string", "description": "Filter payments scheduled for this month (YYYY-MM)"},
                        "frequency": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by frequency (e.g. Monthly, Weekly)"
                        }
                    },
                    "required": ["customer_id", "source_account_id", "month"]
                }
            }
        }

class CalculateTotalExpenditureTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, start_date: str = None, end_date: str = None, transaction_type: str = 'Purchase') -> str:
        transactions = data.get('transactions', [])
        total = 0
        matching = []

        for transaction in transactions:
            if transaction.get('account_id') != account_id:
                continue
            if transaction.get('transaction_type') != transaction_type:
                continue
            if start_date and transaction.get('transaction_date', '') < start_date:
                continue
            if end_date and transaction.get('transaction_date', '') > end_date:
                continue
            total += abs(transaction.get('amount', 0))
            matching.append(transaction)

        return json.dumps({
            "account_id": account_id,
            "transaction_type": transaction_type,
            "start_date": start_date,
            "end_date": end_date,
            "total_expenditure": total,
            "transaction_count": len(matching)
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalExpenditure",
                "description": "Calculate total expenditure for purchases or other transaction types in a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"},
                        "transaction_type": {"type": "string", "description": "Type of transaction (e.g. Purchase, Withdrawal)"}
                    },
                    "required": ["account_id", "start_date", "end_date", "transaction_type"]
                }
            }
        }

class CalculateTotalWithdrawalTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transaction_type = 'Withdrawal'

        transactions = data.get('transactions', [])
        total = 0
        matching = []

        for transaction in transactions:
            if transaction.get('account_id') != account_id:
                continue
            if transaction.get('transaction_type') != transaction_type:
                continue
            if start_date and transaction.get('transaction_date', '') < start_date:
                continue
            if end_date and transaction.get('transaction_date', '') > end_date:
                continue
            total += abs(transaction.get('amount', 0))
            matching.append(transaction)

        return json.dumps({
            "account_id": account_id,
            "transaction_type": transaction_type,
            "start_date": start_date,
            "end_date": end_date,
            "total_withdrawal": total,
            "transaction_count": len(matching)
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalWithdrawal",
                "description": "Calculate total withdrawals for an account in a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

class CalculateTotalDepositsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transaction_type = 'Deposit'

        transactions = data.get('transactions', [])
        total = 0
        matching = []

        for transaction in transactions:
            if transaction.get('account_id') != account_id:
                continue
            if transaction.get('transaction_type') != transaction_type:
                continue
            if start_date and transaction.get('transaction_date', '') < start_date:
                continue
            if end_date and transaction.get('transaction_date', '') > end_date:
                continue
            total += transaction.get('amount', 0)
            matching.append(transaction)

        return json.dumps({
            "account_id": account_id,
            "transaction_type": transaction_type,
            "start_date": start_date,
            "end_date": end_date,
            "total_deposits": total,
            "transaction_count": len(matching)
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalDeposits",
                "description": "Calculate total deposits for an account in a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

class GetSupportTicketsForAccountTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, fields: list = None, start_date: str = None, end_date: str = None, customer_id: str = None) -> str:
        # Support both account_id and customer_id
        if not account_id and customer_id:
            # Find account for this customer
            accounts = data.get('accounts', [])
            for acc in accounts:
                if acc.get('customer_id') == customer_id:
                    account_id = acc.get('account_id')
                    break
        support_tickets = data.get('support_tickets', [])
        results = []

        for ticket in support_tickets:
            ticket_account_id = ticket.get('account_id', None)
            if ticket_account_id != account_id:
                continue
            if fields:
                subject = ticket.get('subject', '').lower()
                description = ticket.get('description', '').lower()
                category = ticket.get('category', '').lower()
                if not any(field.lower() in subject or field.lower() in description or field.lower() in category for field in fields):
                    continue
            created_date = ticket.get('created_date', '')
            resolved_date = ticket.get('resolved_date', '')
            in_range = False
            if start_date and end_date:
                if (created_date and start_date <= created_date <= end_date) or (resolved_date and start_date <= resolved_date <= end_date):
                    in_range = True
            else:
                in_range = True

            if not in_range:
                continue

            results.append({
                "ticket_id": ticket.get("ticket_id"),
                "subject": ticket.get("subject", ""),
                "description": ticket.get("description", ""),
                "category": ticket.get("category", ""),
                "priority": ticket.get("priority", ""),
                "status": ticket.get("status", ""),
                "created_date": created_date,
                "resolved_date": resolved_date,
                "assigned_agent": ticket.get("assigned_agent", "")
            })

        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupportTicketsForAccount",
                "description": "Get support tickets for a specific account, filtered by keywords and date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "fields": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of keywords to filter tickets (e.g. payment issues, account inquiries)"
                        },
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id"]
                }
            }
        }

class GetSupportTicketsForAccountsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_ids: list = None, fields: list = None, start_date: str = None, end_date: str = None, account_id: str = None, customer_id: str = None) -> str:
        # Support single account_id or customer_id parameters
        if account_id and not account_ids:
            account_ids = [account_id]
        elif customer_id and not account_ids:
            # Find accounts for this customer
            accounts = data.get('accounts', [])
            account_ids = [acc.get('account_id') for acc in accounts if acc.get('customer_id') == customer_id]
        account_ids = account_ids or []
        support_tickets = data.get('support_tickets', [])
        results = []

        for ticket in support_tickets:
            ticket_account_id = ticket.get('account_id', None)
            if ticket_account_id not in account_ids:
                continue
            if fields:
                subject = ticket.get('subject', '').lower()
                description = ticket.get('description', '').lower()
                category = ticket.get('category', '').lower()
                if not any(field.lower() in subject or field.lower() in description or field.lower() in category for field in fields):
                    continue
            created_date = ticket.get('created_date', '')
            resolved_date = ticket.get('resolved_date', '')
            in_range = False
            if start_date and end_date:
                if (created_date and start_date <= created_date <= end_date) or (resolved_date and start_date <= resolved_date <= end_date):
                    in_range = True
            else:
                in_range = True
            if not in_range:
                continue
            results.append({
                "ticket_id": ticket.get("ticket_id"),
                "account_id": ticket_account_id,
                "subject": ticket.get("subject", ""),
                "description": ticket.get("description", ""),
                "category": ticket.get("category", ""),
                "priority": ticket.get("priority", ""),
                "status": ticket.get("status", ""),
                "created_date": created_date,
                "resolved_date": resolved_date,
                "assigned_agent": ticket.get("assigned_agent", "")
            })

        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupportTicketsForAccounts",
                "description": "Get support tickets for multiple accounts, filtered by keywords and date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of account identifiers"
                        },
                        "fields": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of keywords to filter tickets"
                        },
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_ids"]
                }
            }
        }

class GetLoanApplicationsForCustomerTool(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        customer_id: str = None,
        application_id: str = None,
        loan_type: str = None,
        requested_amount: float = None,
        purpose: str = None,
        annual_income: float = None,
        credit_score: int = None,
        status: str = None,
        application_date: str = None,
        decision: str = None,
        approved_amount: float = None,
        notes: str = None,
        before_date: str = None
    ) -> str:
        loan_applications = data.get('loan_applications', [])
        result = []

        for application in loan_applications:
            if application.get('customer_id') == customer_id:
                result.append({
                    "application_id": application.get("application_id"),
                    "loan_type": application.get("loan_type"),
                    "requested_amount": application.get("requested_amount"),
                    "purpose": application.get("purpose"),
                    "annual_income": application.get("annual_income"),
                    "credit_score": application.get("credit_score"),
                    "status": application.get("status"),
                    "application_date": application.get("application_date"),
                    "decision": application.get("decision"),
                    "approved_amount": application.get("approved_amount"),
                    "notes": application.get("notes"),
                })

        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLoanApplicationsForCustomer",
                "description": "Get all loan applications for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }

class GenerateDetailedMonthlyReportTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, month: str = None) -> str:
        transactions = data.get('transactions', [])
        scheduled_payments = data.get('scheduled_payments', [])
        support_tickets = data.get('support_tickets', [])

        start_date = f"{month}-01T00:00:00Z"
        end_date = f"{month}-31T23:59:59Z"

        purchases = []
        deposits = []
        withdrawals = []
        total_purchases = 0
        total_deposits = 0
        total_withdrawals = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            if txn.get('transaction_date', '') < start_date or txn.get('transaction_date', '') > end_date:
                continue
            if txn.get('transaction_type') == 'Purchase':
                purchases.append(txn)
                total_purchases += abs(txn.get('amount', 0))
            if txn.get('transaction_type') == 'Deposit':
                deposits.append(txn)
                total_deposits += txn.get('amount', 0)
            if txn.get('transaction_type') == 'Withdrawal':
                withdrawals.append(txn)
                total_withdrawals += abs(txn.get('amount', 0))

        scheduled = []
        recurring = []
        for payment in scheduled_payments:
            if payment.get('from_account_id', None) == account_id and payment.get('next_payment_date', '')[:7] == month:
                scheduled.append(payment)
                if payment.get('frequency') in ['Monthly', 'Weekly']:
                    recurring.append(payment)

        tickets = []
        for ticket in support_tickets:
            if ticket.get('account_id', '') == account_id and ticket.get('created_date', '')[:7] == month:
                tickets.append(ticket)

        report = {
            "account_id": account_id,
            "month": month,
            "total_purchases": total_purchases,
            "total_deposits": total_deposits,
            "total_withdrawals": total_withdrawals,
            "scheduled_payments": scheduled,
            "recurring_payments": recurring,
            "support_tickets": tickets
        }
        return json.dumps(report, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateDetailedMonthlyReport",
                "description": "Generate a comprehensive monthly report for an account including purchases, deposits, withdrawals, scheduled payments, and support tickets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"}
                    },
                    "required": ["account_id", "month"]
                }
            }
        }

class GenerateMonthlyAccountSummaryTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, month: str = None) -> str:
        transactions = data.get('transactions', [])
        scheduled_payments = data.get('scheduled_payments', [])
        support_tickets = data.get('support_tickets', [])

        start_date = f"{month}-01T00:00:00Z"
        end_date = f"{month}-31T23:59:59Z"

        total_deposits = 0
        total_withdrawals = 0
        total_purchases = 0
        transaction_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if txn_date < start_date or txn_date > end_date:
                continue
            transaction_count += 1
            if txn.get('transaction_type') == 'Deposit':
                total_deposits += txn.get('amount', 0)
            if txn.get('transaction_type') == 'Withdrawal':
                total_withdrawals += abs(txn.get('amount', 0))
            if txn.get('transaction_type') == 'Purchase':
                total_purchases += abs(txn.get('amount', 0))

        scheduled_count = sum(
            1 for payment in scheduled_payments
            if payment.get('from_account_id', None) == account_id and payment.get('next_payment_date', '')[:7] == month
        )

        support_ticket_count = sum(
            1 for ticket in support_tickets
            if ticket.get('account_id', '') == account_id and ticket.get('created_date', '')[:7] == month
        )

        summary = {
            "account_id": account_id,
            "month": month,
            "total_deposits": total_deposits,
            "total_withdrawals": total_withdrawals,
            "total_purchases": total_purchases,
            "transaction_count": transaction_count,
            "scheduled_payment_count": scheduled_count,
            "support_ticket_count": support_ticket_count
        }
        return json.dumps(summary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateMonthlyAccountSummary",
                "description": "Generate a summary for an account for a given month, including totals for deposits, withdrawals, purchases, transaction count, scheduled payments, and support tickets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"}
                    },
                    "required": ["account_id", "month"]
                }
            }
        }

class CalculateTotalEventAndPurchaseSpendingTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transactions = data.get('transactions', [])
        total_spending = 0
        event_spending = 0
        purchase_spending = 0
        event_count = 0
        purchase_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            txn_type = txn.get('transaction_type', '')
            amount = abs(txn.get('amount', 0))
            if txn_type == 'Event':
                event_spending += amount
                total_spending += amount
                event_count += 1
            elif txn_type == 'Purchase':
                purchase_spending += amount
                total_spending += amount
                purchase_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_event_spending": event_spending,
            "total_purchase_spending": purchase_spending,
            "total_combined_spending": total_spending,
            "event_transaction_count": event_count,
            "purchase_transaction_count": purchase_count
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalEventAndPurchaseSpending",
                "description": "Calculate total spending for 'Event' and 'Purchase' transactions for an account in a given date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

class GetAccountChangesFromTicketsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        support_tickets = data.get('support_tickets', [])
        changes = []

        for ticket in support_tickets:
            if ticket.get('account_id') != account_id:
                continue
            change_types = []
            subject = ticket.get('subject', '').lower()
            description = ticket.get('description', '').lower()
            category = ticket.get('category', '').lower()

            keywords = ["update", "change", "modify", "freeze", "close", "re-open", "unlock", "limit", "restriction", "address", "contact", "status", "name"]
            if any(kw in subject or kw in description or kw in category for kw in keywords):
                change_types.append("change_detected")

            changes.append({
                "ticket_id": ticket.get("ticket_id"),
                "subject": ticket.get("subject", ""),
                "description": ticket.get("description", ""),
                "category": ticket.get("category", ""),
                "status": ticket.get("status", ""),
                "created_date": ticket.get("created_date", ""),
                "change_types": change_types,
                "raw_ticket": ticket
            })

        return json.dumps(changes, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountChangesFromTickets",
                "description": "Extract tickets that indicate account changes (update, freeze, contact change, etc) for a specific account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"}
                    },
                    "required": ["account_id"]
                }
            }
        }

class CalculateTotalBillPaymentsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transactions = data.get('transactions', [])
        total_bill_payments = 0
        bill_payment_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            if txn.get('transaction_type', '').lower() == 'bill payment':
                total_bill_payments += abs(txn.get('amount', 0))
                bill_payment_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_bill_payments": total_bill_payments,
            "bill_payment_count": bill_payment_count
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalBillPayments",
                "description": "Calculate total bill payments for an account in a given date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

class CalculateTotalPaymentsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None, transaction_type: str = None) -> str:
        transactions = data.get('transactions', [])
        total_payments = 0
        payment_count = 0
        
        # Use transaction_type parameter if provided, otherwise default to 'payment'
        filter_type = transaction_type.lower() if transaction_type else 'payment'

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            if txn.get('transaction_type', '').lower() == filter_type:
                total_payments += abs(txn.get('amount', 0))
                payment_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_payments": total_payments,
            "payment_count": payment_count
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalPayments",
                "description": "Calculate total payments for an account in a given date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

class CalculateTotalDepositsAndPurchasesTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transactions = data.get('transactions', [])
        total_deposits = 0
        total_purchases = 0
        deposit_count = 0
        purchase_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            txn_type = txn.get('transaction_type', '')
            amount = txn.get('amount', 0)
            if txn_type == 'Deposit':
                total_deposits += amount
                deposit_count += 1
            elif txn_type == 'Purchase':
                total_purchases += abs(amount)
                purchase_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_deposits": total_deposits,
            "total_purchases": total_purchases,
            "deposit_count": deposit_count,
            "purchase_count": purchase_count
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalDepositsAndPurchases",
                "description": "Calculate total deposits and purchases for an account in a given date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

class CalculateTotalATMWithdrawalsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transactions = data.get('transactions', [])
        total_atm_withdrawals = 0
        withdrawal_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            if txn.get('transaction_type', '').lower() == 'atm withdrawal':
                total_atm_withdrawals += abs(txn.get('amount', 0))
                withdrawal_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_atm_withdrawals": total_atm_withdrawals,
            "atm_withdrawal_count": withdrawal_count
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalAtmWithdrawals",
                "description": "Calculate total ATM withdrawals for an account in a given date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

class GenerateFinancialReportTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transactions = data.get('transactions', [])
        scheduled_payments = data.get('scheduled_payments', [])
        support_tickets = data.get('support_tickets', [])
        loans = data.get('loans', [])

        total_deposits = 0
        total_withdrawals = 0
        total_purchases = 0
        total_payments = 0
        total_bill_payments = 0
        total_atm_withdrawals = 0
        deposit_count = 0
        withdrawal_count = 0
        purchase_count = 0
        payment_count = 0
        bill_payment_count = 0
        atm_withdrawal_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')

            if start_date and txn_date and txn_date < start_date:
                continue
            if end_date and txn_date and txn_date > end_date:
                continue

            txn_type = txn.get('transaction_type', '').lower()
            amount = txn.get('amount', 0)

            if txn_type == 'deposit':
                total_deposits += amount
                deposit_count += 1
            elif txn_type == 'withdrawal':
                total_withdrawals += abs(amount)
                withdrawal_count += 1
            elif txn_type == 'purchase':
                total_purchases += abs(amount)
                purchase_count += 1
            elif txn_type == 'payment':
                total_payments += abs(amount)
                payment_count += 1
            elif txn_type == 'bill payment':
                total_bill_payments += abs(amount)
                bill_payment_count += 1
            elif txn_type == 'atm withdrawal':
                total_atm_withdrawals += abs(amount)
                atm_withdrawal_count += 1

        scheduled_count = 0
        for payment in scheduled_payments:
            if payment.get('from_account_id', None) != account_id:
                continue
            payment_date = payment.get('next_payment_date', '')

            if start_date and payment_date and payment_date < start_date:
                continue
            if end_date and payment_date and payment_date > end_date:
                continue
            scheduled_count += 1

        support_ticket_count = 0
        for ticket in support_tickets:
            if ticket.get('account_id', '') != account_id:
                continue
            ticket_date = ticket.get('created_date', '')

            if start_date and ticket_date and ticket_date < start_date:
                continue
            if end_date and ticket_date and ticket_date > end_date:
                continue
            support_ticket_count += 1

        loans_for_account = []
        for loan in loans:
            if loan.get('account_id', '') != account_id:
                continue
            loan_date = loan.get('issue_date', '')

            if start_date and loan_date and loan_date < start_date:
                continue
            if end_date and loan_date and loan_date > end_date:
                continue
            loans_for_account.append(loan)

        report = {
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "totals": {
                "deposits": total_deposits,
                "withdrawals": total_withdrawals,
                "purchases": total_purchases,
                "payments": total_payments,
                "bill_payments": total_bill_payments,
                "atm_withdrawals": total_atm_withdrawals
            },
            "counts": {
                "deposits": deposit_count,
                "withdrawals": withdrawal_count,
                "purchases": purchase_count,
                "payments": payment_count,
                "bill_payments": bill_payment_count,
                "atm_withdrawals": atm_withdrawal_count,
                "scheduled_payments": scheduled_count,
                "support_tickets": support_ticket_count,
                "loans": len(loans_for_account)
            },
            "loans": loans_for_account
        }
        return json.dumps(report, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateFinancialReport",
                "description": "Generate a comprehensive financial report for an account, including totals and counts for deposits, withdrawals, purchases, payments, bill payments, ATM withdrawals, scheduled payments, support tickets, and loans over a given period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }

TOOLS = [
    FindCustomerByNameTool(),
    GetCustomerAccountsTool(),
    GetAccountTransactionsTool(),
    TransferFundsTool(),
    CalculateAccountBalanceTool(),
    CreateSupportTicketTool(),
    SearchTransactionsTool(),
    ApplyForLoanTool(),
    AddBeneficiaryTool(),
    CalculateMonthlySpendingTool(),
    GetCustomerLoansTool(),
    SetupScheduledPaymentTool(),
    UpdateCustomerContactTool(),
    FreezeAccountTool(),
    GetCustomerBeneficiariesTool(),
    ProcessLoanPaymentTool(),
    ValidateRoutingNumberTool(),
    GetTransactionDetailsTool(),
    CalculateCreditUtilizationTool(),
    ResolveTicketTool(),
    CalculateInterestEarnedTool(),
    UpdateLoanApplicationStatusTool(),
    GenerateAccountStatementTool(),
    CancelScheduledPaymentTool(),
    SearchCustomersByEmailTool(),
    GetCustomerSupportTicketsTool(),
    CalculateTotalExpenditureTool(),
    CalculateTotalWithdrawalTool(),
    CalculateTotalDepositsTool(),
    GenerateDetailedMonthlySummaryTool(),
    RetrieveScheduledPaymentsTool(),
    GetSupportTicketsForAccountsTool(),
    GetSupportTicketsForAccountTool(),
    GetLoanApplicationsForCustomerTool(),
    GenerateDetailedMonthlyReportTool(),
    GenerateMonthlyAccountSummaryTool(),
    CalculateTotalEventAndPurchaseSpendingTool(),
    GetAccountChangesFromTicketsTool(),
    CalculateTotalBillPaymentsTool(),
    CalculateTotalPaymentsTool(),
    CalculateTotalDepositsAndPurchasesTool(),
    CalculateTotalATMWithdrawalsTool(),
    GenerateFinancialReportTool()
]
