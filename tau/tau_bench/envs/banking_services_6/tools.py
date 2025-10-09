import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

from tau_bench.envs.tool import Tool

NOW: datetime = datetime(2025, 7, 22, 16, 35, 15, tzinfo=timezone.utc)

DT_STR_FORMAT = "%Y-%m-%dT%H:%M:%SZ"




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _get_next_id(prefix: str, existing_ids: List[str]) -> str:
    if not existing_ids:
        return f"{prefix}_1"

    return f"{prefix}_generated_{len(existing_ids) + 1}"


def _get_next_transaction_id(data: Dict[str, Any]) -> str:
    transaction_ids = [t['transaction_id'] for t in data.get("transactions", {}).values()]
    return _get_next_id('txn', transaction_ids)


def _get_next_customer_id(data: Dict[str, Any]) -> str:
    customer_ids = [c['customer_id'] for c in data.get("customers", {}).values()]
    return _get_next_id('customer', customer_ids)


def _get_next_loan_application_id(data: Dict[str, Any]) -> str:
    app_ids = [app['application_id'] for app in data.get("loan_applications", {}).values()]
    return _get_next_id('app', app_ids)


def _get_next_beneficiary_id(data: Dict[str, Any]) -> str:
    bene_ids = [b['beneficiary_id'] for b in data.get("beneficiaries", {}).values()]
    return _get_next_id('bene', bene_ids)


def _get_next_scheduled_payment_id(data: Dict[str, Any]) -> str:
    payment_ids = [p['payment_id'] for p in data.get("scheduled_payments", {}).values()]
    return _get_next_id('sp', payment_ids)


def _get_next_support_ticket_id(data: Dict[str, Any]) -> str:
    ticket_ids = [t['ticket_id'] for t in data.get("support_tickets", {}).values()]
    return _get_next_id('tkt', ticket_ids)


def _get_next_account_id(data: Dict[str, Any]) -> str:
    account_ids = [a['account_id'] for a in data.get("accounts", {}).values()]
    return _get_next_id('acc', account_ids)


class SearchCustomerByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str = None, last_name: str = None) -> str:
        customers = data.get("customers", {}).values()
        results = []
        for customer in customers.values():
            pi = customer.get("personal_info", {}).values()
            if pi.get("first_name", "").lower().strip() == first_name.lower().strip() and \
                    pi.get("last_name", "").lower().strip() == last_name.lower().strip():
                results.append(customer)
        return json.dumps(results)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "SearchCustomerByName",
                        "description": "Searches for a customer by their first and last name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "first_name": {"type": "string", "description": "The customer's first name."},
                                        "last_name": {"type": "string", "description": "The customer's last name."}
                                },
                                "required": ["first_name", "last_name"],
                        },
                },
        }


class GetCustomerAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        accounts = data.get("accounts", {}).values()
        customer_accounts = [acc for acc in accounts.values() if acc.get("customer_id") == customer_id]
        return json.dumps(customer_accounts)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetCustomerAccounts",
                        "description": "Retrieves all accounts associated with a given customer ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique identifier for the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }


class GetAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        accounts = data.get("accounts", {}).values()
        for account in accounts.values():
            if account.get("account_id") == account_id:
                return json.dumps({"account_id": account_id, "balance": account.get("balance"), "currency": account.get("currency")})
        return json.dumps({"error": "Account not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetAccountBalance",
                        "description": "Gets the current balance for a specific account.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "account_id": {"type": "string", "description": "The unique identifier for the account."}
                                },
                                "required": ["account_id"],
                        },
                },
        }


class CalculateSum(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], values: list = None) -> str:
        total = 0
        if values:
            total = sum([float(v) for v in values])

        return json.dumps({"total": f"{total}"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CalculateSum",
                        "description": "Calculate the total sum for a list of numerical values.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "values": {"type": "array", "items": {"type": "string"}, "description": "The values to sum up."}
                                },
                                "required": ["values"],
                        },
                },
        }


class UpdateCustomerAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, street_address: str = None, city: str = None, state: str = None, postal_code: str = None, country: str = None) -> str:
        for customer in data.get("customers", {}).values():
            if customer.get("customer_id") == customer_id:
                new_address = {
                    "street_address": street_address,
                    "city": city,
                    "state": state,
                    "postal_code": postal_code,
                    "country": country
                }
                customer["contact_info"]["mailing_address"] = new_address
                customer["contact_info"]["residential_address"] = new_address
                return json.dumps(customer)
        return json.dumps({"error": "Customer not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateCustomerAddress",
                        "description": "Updates the mailing and residential address for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The customer's unique ID."},
                                        "street_address": {"type": "string", "description": "The new street address."},
                                        "city": {"type": "string", "description": "The new city."},
                                        "state": {"type": "string", "description": "The new state or province."},
                                        "postal_code": {"type": "string", "description": "The new postal code."},
                                        "country": {"type": "string", "description": "The new country."}
                                },
                                "required": ["customer_id", "street_address", "city", "state", "postal_code", "country"],
                        },
                },
        }


class UpdateCustomerPhone(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, new_phone_number: str = None) -> str:
        for customer in data.get("customers", {}).values():
            if customer.get("customer_id") == customer_id:
                for phone in customer.get("contact_info", {}).values().get("phone_numbers", []):
                    if phone.get("is_primary"):
                        phone["number"] = new_phone_number
                        return json.dumps(customer)
                customer["contact_info"]["phone_numbers"].append({"type": "Mobile", "number": new_phone_number, "is_primary": True})
                return json.dumps(customer)
        return json.dumps({"error": "Customer not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateCustomerPhone",
                        "description": "Updates the primary phone number for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The customer's unique ID."},
                                        "new_phone_number": {"type": "string", "description": "The new primary phone number."}
                                },
                                "required": ["customer_id", "new_phone_number"],
                        },
                },
        }


class CreateTransaction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_account_id: str = None, destination_account_id: str = None, amount: float = 0.0, description: str = "") -> str:
        transaction_id = _get_next_transaction_id(data)

        source_account = next((acc for acc in data["accounts"].values() if acc["account_id"] == source_account_id), None)
        if not source_account:
            return json.dumps({"error": "Source account not found."})

        source_account["balance"] -= amount

        if destination_account_id:
            dest_account = next((acc for acc in data["accounts"].values() if acc["account_id"] == destination_account_id), None)
            if dest_account:
                dest_account["balance"] += amount

        new_transaction = {
                "transaction_id": transaction_id,
                "account_id": source_account_id,
                "transaction_date": NOW.strftime(DT_STR_FORMAT),
                "amount": -amount,
                "currency": source_account['currency'],
                "transaction_type": "Transfer" if destination_account_id else "Payment",
                "description": description,
                "status": "Completed",
                "channel": "Online"
        }
        data["transactions"][transaction_id] = new_transaction

        return json.dumps(new_transaction)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateTransaction",
                        "description": "Creates a new transaction between accounts.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "source_account_id": {"type": "string", "description": "The ID of the account to transfer from."},
                                        "destination_account_id": {"type": "string", "description": "The ID of the account to transfer to (optional for external)."},
                                        "amount": {"type": "number", "description": "The amount to transfer."},
                                        "description": {"type": "string", "description": "A description for the transaction."}
                                },
                                "required": ["source_account_id", "amount", "description"],
                        },
                },
        }


class UpdateAccountStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, new_status: str = None) -> str:
        account = next((acc for acc in data["accounts"].values() if acc["account_id"] == account_id), None)
        if not account:
            return json.dumps({"error": "Account not found."})

        if new_status.lower() == "closed" and account["balance"] < 0:
            return json.dumps({"error": "Account has a negative balance and cannot be closed."})

        account["status"] = new_status
        return json.dumps(account)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateAccountStatus",
                        "description": "Updates the status of an account (e.g., Active, Frozen, Closed).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "account_id": {"type": "string", "description": "The unique identifier for the account."},
                                        "new_status": {"type": "string", "description": "The new status for the account."},
                                        "reason": {"type": "string", "description": "Optional reason for the status change."}
                                },
                                "required": ["account_id", "new_status"],
                        },
                },
        }


class CreateCustomer(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        first_name: str = None,
        last_name: str = None,
        dob: str = None,
        email: str = None,
        phone: str = None,
        street: str = None,
        city: str = None,
        postal_code: str = None,
        country: str = None,
        annual_income: float = None
    ) -> str:
        customer_id = _get_next_customer_id(data)
        new_customer = {
            "customer_id": customer_id,
            "personal_info": {"first_name": first_name, "last_name": last_name, "date_of_birth": dob},
            "contact_info": {
                "email_address": email,
                "phone_numbers": [{"type": "Mobile", "number": phone, "is_primary": True}],
                "mailing_address": {"street_address": street, "city": city, "postal_code": postal_code, "country": country},
                "residential_address": {"street_address": street, "city": city, "postal_code": postal_code, "country": country}
            },
            "account_ids": [],
            "financial_profile": {"annual_income": annual_income},
            "bank_relationship": {"date_joined": NOW.strftime('%Y-%m-%d')},
            "compliance": {"kyc_status": "Verified", "aml_risk_level": "Low"}
        }
        data['customers'].append(new_customer)
        return json.dumps(new_customer)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateCustomer",
                        "description": "Creates a new customer profile.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "first_name": {"type": "string"}, "last_name": {"type": "string"}, "dob": {"type": "string"},
                                        "email": {"type": "string"}, "phone": {"type": "string"}, "street": {"type": "string"}, "city": {"type": "string"},
                                        "postal_code": {"type": "string"}, "country": {"type": "string"}, "annual_income": {"type": "integer"}
                                },
                                "required": ["first_name", "last_name", "dob", "email", "phone", "street", "city", "postal_code", "country", "annual_income"]
                        }
                }
        }


class CreateLoanApplication(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, loan_type: str = None, amount: float = None, 
               term: int = None, purpose: str = None, annual_income: float = None) -> str:
        application_id = _get_next_loan_application_id(data)
        customer = next((c for c in data['customers'].values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        new_application = {
                "application_id": application_id,
                "customer_id": customer_id,
                "existing_customer": True,
                "applicant_info": {
                        "first_name": customer['personal_info']['first_name'],
                        "last_name": customer['personal_info']['last_name'],
                },
                "loan_details": {
                        "loan_type": loan_type,
                        "requested_amount": amount,
                        "requested_term_months": term,
                        "purpose": purpose
                },
                "financial_snapshot": {"annual_income": annual_income},
                "application_status": "Submitted",
                "submission_date": NOW.strftime(DT_STR_FORMAT)
        }
        data['loan_applications'].append(new_application)
        return json.dumps(new_application)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateLoanApplication",
                        "description": "Creates a new loan application for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "loan_type": {"type": "string"}, "amount": {"type": "number"},
                                        "term": {"type": "integer"}, "purpose": {"type": "string"}, "annual_income": {"type": "integer"}
                                },
                                "required": ["customer_id", "loan_type", "amount", "term", "purpose", "annual_income"]
                        }
                }
        }


class AddBeneficiary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, name: str = None, relationship: str = None, iban: str = None, account_number: str = None, sort_code: str = None, routing_number: str = None, bank_name: str = None, country: str = None) -> str:
        beneficiary_id = _get_next_beneficiary_id(data)
        new_beneficiary = {
                "beneficiary_id": beneficiary_id,
                "customer_id": customer_id,
                "beneficiary_name": name,
                "relationship": relationship,
                "account_details": {
                        "iban": iban,
                        "account_number": account_number,
                        "sort_code": sort_code,
                        "routing_number": routing_number,
                        "bank_name": bank_name,
                        "country": country
                },
                "date_added": NOW.strftime(DT_STR_FORMAT)
        }
        data['beneficiaries'].append(new_beneficiary)
        return json.dumps(new_beneficiary)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "AddBeneficiary",
                        "description": "Adds a new beneficiary to a customer's profile.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "name": {"type": "string"}, "relationship": {"type": "string"},
                                        "iban": {"type": "string"},
                                        "account_number": {"type": "string"},
                                        "sort_code": {"type": "string"},
                                        "routing_number": {"type": "string"},
                                        "bank_name": {"type": "string"}, "country": {"type": "string"}
                                },
                                "required": ["customer_id", "name", "relationship", "iban", "bank_name", "country"]
                        }
                }
        }


class CreateScheduledPayment(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], 
        customer_id: str = None, 
        source_account_id: str = None, 
        beneficiary_id: str = None, 
        amount: float = None, 
        frequency: str = None, 
        start_date: str = None
    ) -> str:
        payment_id = _get_next_scheduled_payment_id(data)
        new_payment = {
                "payment_id": payment_id,
                "customer_id": customer_id,
                "source_account_id": source_account_id,
                "beneficiary_id": beneficiary_id,
                "amount": amount,
                "currency": next((a['currency'] for a in data['accounts'].values() if a['account_id'] == source_account_id), "EUR"),
                "frequency": frequency,
                "start_date": start_date,
                "next_payment_date": start_date,
                "status": "Active"
        }
        data['scheduled_payments'].append(new_payment)
        return json.dumps(new_payment)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateScheduledPayment",
                        "description": "Schedules a new recurring payment.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "source_account_id": {"type": "string"},
                                        "beneficiary_id": {"type": "string"}, "amount": {"type": "number"}, "frequency": {"type": "string"}, "start_date": {"type": "string"}
                                },
                                "required": ["customer_id", "source_account_id", "beneficiary_id", "amount", "frequency", "start_date"]
                        }
                }
        }


class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str = None) -> str:
        transaction = next((t for t in data.get("transactions", {}).values() if t['transaction_id'] == transaction_id), None)
        if transaction:
            return json.dumps(transaction)
        return json.dumps({"error": "Transaction not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetTransactionDetails",
                        "description": "Retrieves the full details of a single transaction.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "transaction_id": {"type": "string", "description": "The unique ID of the transaction."}
                                },
                                "required": ["transaction_id"]
                        }
                }
        }


class CreateSupportTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, priority: str = None, category: str = None, details: str = None, target_entity: str = None, target_id: str = None) -> str:
        ticket_id = _get_next_support_ticket_id(data)
        new_ticket = {
                "ticket_id": ticket_id,
                "customer_id": customer_id,
                "status": "Open",
                "priority": priority,
                "category": category,
                "request_details": {
                        "details": details,
                        "target_entity": target_entity,
                        "target_id": target_id,
                }
        }
        data['support_tickets'].append(new_ticket)
        return json.dumps(new_ticket)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateSupportTicket",
                        "description": "Creates a new support ticket for a customer issue.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "category": {"type": "string"}, "priority": {"type": "string"},
                                        "details": {"type": "string"}, "target_entity": {"type": "string"}, "target_id": {"type": "string"}
                                },
                                "required": ["customer_id", "category", "priority", "details", "target_entity", "target_id"]
                        }
                }
        }


class GetBeneficiaryByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_name: str = None) -> str:
        beneficiary = next((b for b in data['beneficiaries'].values() if b['customer_id'] == customer_id and b['beneficiary_name'].lower().strip() == beneficiary_name.lower().strip()),
                           None)
        if beneficiary:
            return json.dumps(beneficiary)
        return json.dumps({"error": "Beneficiary not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetBeneficiaryByName",
                        "description": "Finds a beneficiary for a customer by their name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "beneficiary_name": {"type": "string"}
                                },
                                "required": ["customer_id", "beneficiary_name"]
                        }
                }
        }

class GetBeneficiaryDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id: str = None) -> str:
        beneficiary = next((b for b in data.get("beneficiaries", {}).values() if b.get('beneficiary_id') == beneficiary_id), None)

        if beneficiary:
            return json.dumps(beneficiary)
        return json.dumps({"error": "Beneficiary not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetBeneficiaryDetails",
                        "description": "Looks up a beneficiary by their unique beneficiary ID and displays the details.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "beneficiary_id": {"type": "string", "description": "The unique ID of the beneficiary."}
                                },
                                "required": ["beneficiary_id"]
                        }
                }
        }

class GetCustomerFinancialProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        customer = next((c for c in data['customers'].values() if c['customer_id'] == customer_id), None)
        if customer and "financial_profile" in customer:
            return json.dumps(customer['financial_profile'])
        return json.dumps({"error": "Customer or financial profile not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetCustomerFinancialProfile",
                        "description": "Retrieves the financial profile of a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {"customer_id": {"type": "string"}},
                                "required": ["customer_id"]
                        }
                }
        }


class GetAccountDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        account = next((a for a in data['accounts'].values() if a['account_id'] == account_id), None)
        if account:
            return json.dumps(account)
        return json.dumps({"error": "Account not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetAccountDetails",
                        "description": "Retrieves full details for a specific account.",
                        "parameters": {
                                "type": "object",
                                "properties": {"account_id": {"type": "string"}},
                                "required": ["account_id"]
                        }
                }
        }


class GetLoanDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None) -> str:
        loan = next((l for l in data['loans'].values() if l['loan_id'] == loan_id), None)
        if loan:
            return json.dumps(loan)
        return json.dumps({"error": "Loan not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetLoanDetails",
                        "description": "Retrieves full details for a specific loan.",
                        "parameters": {
                                "type": "object",
                                "properties": {"loan_id": {"type": "string"}},
                                "required": ["loan_id"]
                        }
                }
        }


class CalculateNewLoanPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], current_balance: float, new_interest_rate: float, remaining_term_months: int) -> str:
        monthly_rate = (new_interest_rate / 100) / 12
        if monthly_rate == 0:
            payment = current_balance / remaining_term_months
        else:
            payment = current_balance * (monthly_rate * (1 + monthly_rate) ** remaining_term_months) / ((1 + monthly_rate) ** remaining_term_months - 1)
        return json.dumps({"new_monthly_payment": round(payment, 2)})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CalculateNewLoanPayment",
                        "description": "Calculates a new monthly loan payment based on new terms.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "current_balance": {"type": "number"},
                                        "new_interest_rate": {"type": "number"},
                                        "remaining_term_months": {"type": "integer"}
                                },
                                "required": ["current_balance", "new_interest_rate", "remaining_term_months"]
                        }
                }
        }


class ListAccountTypesByCurrency(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], currency: str = None) -> str:
        account_types = []
        if currency == "GBP":
            account_types = ["Checking", "Savings", "ISA"]
        elif currency == "USD":
            account_types = ["Checking", "Savings", "Credit Card", "Investment"]
        elif currency == "EUR":
            account_types = ["Current Account", "Savings Account", "Credit"]

        return json.dumps({"currency": currency, "available_account_types": account_types})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "ListAccountTypesByCurrency",
                        "description": "Lists the types of accounts available for a given currency.",
                        "parameters": {
                                "type": "object",
                                "properties": {"currency": {"type": "string", "description": "The three-letter currency code (e.g., GBP)."}},
                                "required": ["currency"]
                        }
                }
        }


class GetLoanApplicationDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], application_id: str = None) -> str:
        application = next((app for app in data.get("loan_applications", {}).values() if app['application_id'] == application_id), None)
        if application:
            return json.dumps(application)
        return json.dumps({"error": "Loan application not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetLoanApplicationDetails",
                        "description": "Retrieves the full details of a single loan application.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "application_id": {"type": "string", "description": "The unique ID of the loan application."}
                                },
                                "required": ["application_id"]
                        }
                }
        }


class UpdateLoanBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, amount: float = None) -> str:
        loan = next((l for l in data.get("loans", {}).values() if l['loan_id'] == loan_id), None)
        if loan:
            loan['current_balance'] += amount
            return json.dumps(loan)
        return json.dumps({"error": "Loan not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateLoanBalance",
                        "description": "Updates the current balance of a loan, typically after a payment.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "loan_id": {"type": "string", "description": "The unique ID of the loan."},
                                        "amount": {"type": "number", "description": "The amount to adjust the balance by. Use a negative value for payments."}
                                },
                                "required": ["loan_id", "amount"]
                        }
                }
        }


class CreateAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_type: str = None, currency: str = None) -> str:
        account_id = _get_next_account_id(data)

        customer = next((c for c in data['customers'].values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        new_account = {
                "account_id": account_id,
                "customer_id": customer_id,
                "account_type": account_type,
                "balance": 0.0,
                "currency": currency,
                "date_opened": NOW.strftime('%Y-%m-%d'),
                "status": "Active",
        }

        if account_type.lower() in ["checking", "current account"]:
            new_account["overdraft_limit"] = 100.00
        elif account_type.lower() == "savings":
            new_account["interest_rate"] = 1.05
        elif account_type.lower() == "credit card":
            new_account["credit_limit"] = 5000.00

        data['accounts'].append(new_account)
        customer['account_ids'].append(account_id)

        return json.dumps(new_account)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateAccount",
                        "description": "Creates a new bank account for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "account_type": {"type": "string"},
                                        "currency": {"type": "string"}
                                },
                                "required": ["customer_id", "account_type", "currency"]
                        }
                }
        }


class RemoveBeneficiary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id: str = None) -> str:
        beneficiaries = data.get("beneficiaries", {}).values()

        initial_len = len(beneficiaries)
        data['beneficiaries'] = [b for b in beneficiaries.values() if b['beneficiary_id'] != beneficiary_id]

        if len(data['beneficiaries']) < initial_len:
            return json.dumps({"status": "Success", "beneficiary_id": beneficiary_id, "action": "removed"})
        return json.dumps({"error": "Beneficiary not found or could not be removed."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "RemoveBeneficiary",
                        "description": "Removes a beneficiary from the database.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "beneficiary_id": {"type": "string", "description": "The unique ID of the beneficiary to remove."}
                                },
                                "required": ["beneficiary_id"]
                        }
                }
        }


class UpdateCustomerPersonalInfo(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        customer_id: str = None,
        field: str = None,
        value: Any = None
    ) -> str:
        customer = next((c for c in data['customers'].values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        if "personal_info" in customer and field in customer["personal_info"]:
            customer["personal_info"][field] = value
            return json.dumps(customer["personal_info"])

        return json.dumps({"error": f"Field {field} not found in personal info."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateCustomerPersonalInfo",
                        "description": "Updates a specific field in a customer's personal information.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "field": {"type": "string", "description": "The field to update (e.g., 'marital_status')."},
                                        "value": {"type": "string", "description": "The new value for the field."}
                                },
                                "required": ["customer_id", "field", "value"]
                        }
                }
        }


class ListBeneficiaries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        customer_beneficiaries = [b for b in data['beneficiaries'].values() if b['customer_id'] == customer_id]
        return json.dumps(customer_beneficiaries)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "ListBeneficiaries",
                        "description": "Lists all beneficiaries for a given customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {"customer_id": {"type": "string"}},
                                "required": ["customer_id"]
                        }
                }
        }


class UpdateCustomerPreferences(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, paperless_billing: bool = None, communication_channel: str = None) -> str:
        customer = next((c for c in data['customers'].values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        if "preferences" not in customer:
            customer["preferences"] = {}

        if paperless_billing is not None:
            customer["preferences"]["paperless_billing"] = paperless_billing
        if communication_channel is not None:
            customer["preferences"]["communication_channel"] = communication_channel

        return json.dumps(customer["preferences"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateCustomerPreferences",
                        "description": "Updates a customer's communication preferences.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "paperless_billing": {"type": "boolean"},
                                        "communication_channel": {"type": "string"}
                                },
                                "required": ["customer_id"]
                        }
                }
        }


class UpdateCustomerSecurityQuestion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, security_question: str = None) -> str:
        customer = next((c for c in data['customers'].values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        if "security" not in customer:
            customer["security"] = {}

        if security_question is not None:
            customer["security"]["security_question"] = security_question

        return json.dumps(customer["security"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateCustomerSecurityQuestion",
                        "description": "Updates a customer's security question.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "security_question": {"type": "string"}
                                },
                                "required": ["customer_id", "security_question"]
                        }
                }
        }


class CreateDeposit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, amount: float = None, description: str = None) -> str:
        transaction_id = _get_next_transaction_id(data)

        account = next((acc for acc in data["accounts"].values() if acc["account_id"] == account_id), None)
        if not account:
            return json.dumps({"error": "Account not found."})

        account["balance"] += amount

        new_transaction = {
                "transaction_id": transaction_id,
                "account_id": account_id,
                "transaction_date": NOW.strftime(DT_STR_FORMAT),
                "amount": amount,
                "currency": account['currency'],
                "transaction_type": "Deposit",
                "description": description,
                "status": "Completed",
                "channel": "Online"
        }
        data["transactions"][transaction_id] = new_transaction

        return json.dumps(new_transaction)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateDeposit",
                        "description": "Records an external deposit into an account.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "account_id": {"type": "string"},
                                        "amount": {"type": "number"},
                                        "description": {"type": "string"}
                                },
                                "required": ["account_id", "amount", "description"]
                        }
                }
        }


class GetAccountTransactions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, days_history: int = 30, current_date: str = None) -> str:
        current_dt = NOW if not current_date else datetime.combine(date=date.fromisoformat(current_date), time=time(hour=0, minute=0, second=0, tzinfo=timezone.utc))

        transactions = data.get("transactions", {}).values()
        account_transactions = [t for t in transactions.values() if t['account_id'] == account_id]
        cutoff_date = current_dt - timedelta(days=days_history)

        recent_transactions = [
                t for t in account_transactions
                if datetime.fromisoformat(t['transaction_date'].replace('Z', '')).astimezone(timezone.utc) > cutoff_date
        ]

        return json.dumps(recent_transactions)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetAccountTransactions",
                        "description": "Retrieves transaction history for a specific account for a given period.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "account_id": {"type": "string"},
                                        "days_history": {"type": "integer", "description": "Number of past days to fetch transactions for. Defaults to 30."},
                                        "current_date": {"type": "string", "description": "The current date in ISO format. Defaults to today."}
                                },
                                "required": ["account_id"]
                        }
                }
        }


class UpdateScheduledPaymentStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str = None, new_status: str = None) -> str:
        payment = next((p for p in data['scheduled_payments'].values() if p['payment_id'] == payment_id), None)
        if not payment:
            return json.dumps({"error": "Scheduled payment not found."})

        payment['status'] = new_status
        return json.dumps(payment)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateScheduledPaymentStatus",
                        "description": "Updates the status of a scheduled payment (e.g., Active, Paused, Cancelled).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "payment_id": {"type": "string"},
                                        "new_status": {"type": "string"}
                                },
                                "required": ["payment_id", "new_status"]
                        }
                }
        }


class GetScheduledPaymentDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str = None) -> str:
        payment = next((p for p in data['scheduled_payments'].values() if p['payment_id'] == payment_id), None)
        if payment:
            return json.dumps(payment)
        return json.dumps({"error": "Scheduled payment not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetScheduledPaymentDetails",
                        "description": "Retrieves the full details of a single scheduled payment.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "payment_id": {"type": "string"}
                                },
                                "required": ["payment_id"]
                        }
                }
        }


class GetScheduledPayments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        scheduled_payments = data.get("scheduled_payments", {}).values()
        customer_payments = [pay for pay in scheduled_payments.values() if pay.get("customer_id") == customer_id]
        return json.dumps(customer_payments)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetScheduledPayments",
                        "description": "Get all scheduled payments for a given customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique ID of the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }


class GetCustomerDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        customer = next((c for c in data.get("customers", {}).values() if c['customer_id'] == customer_id), None)
        if customer:
            return json.dumps(customer)
        return json.dumps({"error": "Customer not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetCustomerDetails",
                        "description": "Retrieves the full profile details for a single customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique ID of the customer."}
                                },
                                "required": ["customer_id"]
                        }
                }
        }


class UpdateLoanStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, new_status: str = None) -> str:
        loan = next((l for l in data.get("loans", {}).values() if l['loan_id'] == loan_id), None)
        if loan:
            loan['status'] = new_status
            return json.dumps(loan)
        return json.dumps({"error": "Loan not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateLoanStatus",
                        "description": "Updates the status of a loan (e.g., Active, Paid Off).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "loan_id": {"type": "string", "description": "The unique ID of the loan."},
                                        "new_status": {"type": "string", "description": "The new status for the loan."}
                                },
                                "required": ["loan_id", "new_status"]
                        }
                }
        }


class GetCustomerLoanApplications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        applications = data.get("loan_applications", {}).values()
        customer_loans = [app for app in applications.values() if app.get("customer_id") == customer_id]
        return json.dumps(customer_loans)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetCustomerLoanApplications",
                        "description": "Retrieves all loan applications associated with a given customer ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique identifier for the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }


class GetCustomerLoans(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        loans = data.get("loans", {}).values()
        customer_loans = [loan for loan in loans.values() if loan.get("customer_id") == customer_id]
        return json.dumps(customer_loans)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetCustomerLoans",
                        "description": "Retrieves all loans associated with a given customer ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique identifier for the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }


class GetSupportTicketDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_id: str = None) -> str:
        ticket = next((t for t in data.get("support_tickets", {}).values() if t['ticket_id'] == ticket_id), None)
        if ticket:
            return json.dumps(ticket)
        return json.dumps({"error": "Support ticket not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetSupportTicketDetails",
                        "description": "Retrieves the full details of a single support ticket.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "ticket_id": {"type": "string", "description": "The unique ID of the support ticket."}
                                },
                                "required": ["ticket_id"]
                        }
                }
        }


class UpdateLoanApplicationStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], application_id: str = None, new_status: str = None) -> str:
        application = next((app for app in data.get("loan_applications", {}).values() if app['application_id'] == application_id), None)
        if not application:
            return json.dumps({"error": "Loan application not found."})

        application['application_status'] = new_status
        if new_status.lower() == "withdrawn":
            application['decision'] = None

        return json.dumps(application)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateLoanApplicationStatus",
                        "description": "Updates the status of a loan application (e.g., Under Review, Withdrawn).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "application_id": {"type": "string", "description": "The unique ID of the loan application."},
                                        "new_status": {"type": "string", "description": "The new status for the application."}
                                },
                                "required": ["application_id", "new_status"]
                        }
                }
        }


class AddCustomerPhoneNumber(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, phone_type: str, phone_number: str, is_primary: bool = False) -> str:
        customer = next((c for c in data.get("customers", {}).values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found."})

        if "contact_info" not in customer:
            customer["contact_info"] = {}
        if "phone_numbers" not in customer["contact_info"]:
            customer["contact_info"]["phone_numbers"] = []

        if is_primary:
            for phone in customer["contact_info"]["phone_numbers"]:
                phone["is_primary"] = False

        customer["contact_info"]["phone_numbers"].append({
                "type": phone_type,
                "number": phone_number,
                "is_primary": is_primary
        })

        return json.dumps(customer["contact_info"]["phone_numbers"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "AddCustomerPhoneNumber",
                        "description": "Adds a new phone number to a customer's profile.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "phone_type": {"type": "string", "description": "Type of phone number (e.g., 'Work', 'Home')."},
                                        "phone_number": {"type": "string"},
                                        "is_primary": {"type": "boolean", "description": "Set to true if this should be the new primary number."}
                                },
                                "required": ["customer_id", "phone_type", "phone_number"]
                        }
                }
        }


class CreateScheduledInternalTransfer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, source_account_id: str = None, 
               destination_account_id: str = None, amount: float = None, frequency: str = None, 
               start_date: str = None) -> str:
        payment_id = _get_next_scheduled_payment_id(data)

        source_account = next((a for a in data['accounts'].values() if a['account_id'] == source_account_id and a['customer_id'] == customer_id), None)
        dest_account = next((a for a in data['accounts'].values() if a['account_id'] == destination_account_id and a['customer_id'] == customer_id), None)

        if not source_account or not dest_account:
            return json.dumps({"error": "One or both accounts not found or do not belong to the customer."})

        new_payment = {
                "payment_id": payment_id,
                "customer_id": customer_id,
                "source_account_id": source_account_id,
                "beneficiary_id": None,
                "internal_destination_account_id": destination_account_id,
                "amount": amount,
                "currency": source_account['currency'],
                "frequency": frequency,
                "start_date": start_date,
                "next_payment_date": start_date,
                "status": "Active"
        }
        data['scheduled_payments'].append(new_payment)
        return json.dumps(new_payment)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateScheduledInternalTransfer",
                        "description": "Schedules a new recurring transfer between a customer's own accounts.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "source_account_id": {"type": "string"},
                                        "destination_account_id": {"type": "string"},
                                        "amount": {"type": "number"},
                                        "frequency": {"type": "string"},
                                        "start_date": {"type": "string"}
                                },
                                "required": ["customer_id", "source_account_id", "destination_account_id", "amount", "frequency", "start_date"]
                        }
                }
        }


class GetTotalAccountsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("accounts", {}))
        return json.dumps({"total_accounts": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalAccountsCount",
                        "description": "Returns the current total number of accounts in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }


class GetTotalBeneficiariesCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("beneficiaries", {}))
        return json.dumps({"total_beneficiaries": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalBeneficiariesCount",
                        "description": "Returns the current total number of beneficiaries in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }


class GetTotalCustomersCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("customers", {}))
        return json.dumps({"total_customers": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalCustomersCount",
                        "description": "Returns the current total number of customers in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }


class GetTotalLoanApplicationsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("loan_applications", {}))
        return json.dumps({"total_loan_applications": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalLoanApplicationsCount",
                        "description": "Returns the current total number of loan applications in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }


class GetTotalLoansCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("loans", {}))
        return json.dumps({"total_loans": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalLoansCount",
                        "description": "Returns the current total number of loans in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }


class GetTotalScheduledPaymentsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("scheduled_payments", {}))
        return json.dumps({"total_scheduled_payments": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalScheduledPaymentsCount",
                        "description": "Returns the current total number of scheduled payments in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }


class GetTotalSupportTicketsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("support_tickets", {}))
        return json.dumps({"total_support_tickets": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalSupportTicketsCount",
                        "description": "Returns the current total number of support tickets in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }


class GetTotalTransactionsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("transactions", {}))
        return json.dumps({"total_transactions": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalTransactionsCount",
                        "description": "Returns the current total number of transactions in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }


TOOLS = [
        AddBeneficiary(),
        AddCustomerPhoneNumber(),
        CalculateNewLoanPayment(),
        CalculateSum(),
        CreateAccount(),
        CreateCustomer(),
        CreateDeposit(),
        CreateLoanApplication(),
        CreateScheduledInternalTransfer(),
        CreateScheduledPayment(),
        CreateSupportTicket(),
        CreateTransaction(),
        GetAccountBalance(),
        GetAccountDetails(),
        GetAccountTransactions(),
        GetBeneficiaryByName(),
        GetBeneficiaryDetails(),
        GetCustomerAccounts(),
        GetCustomerDetails(),
        GetCustomerFinancialProfile(),
        GetCustomerLoanApplications(),
        GetCustomerLoans(),
        GetLoanApplicationDetails(),
        GetLoanDetails(),
        GetScheduledPaymentDetails(),
        GetScheduledPayments(),
        GetSupportTicketDetails(),
        GetTransactionDetails(),
        ListAccountTypesByCurrency(),
        ListBeneficiaries(),
        RemoveBeneficiary(),
        SearchCustomerByName(),
        UpdateAccountStatus(),
        UpdateCustomerAddress(),
        UpdateCustomerPersonalInfo(),
        UpdateCustomerPhone(),
        UpdateCustomerPreferences(),
        UpdateCustomerSecurityQuestion(),
        UpdateLoanApplicationStatus(),
        UpdateLoanBalance(),
        UpdateLoanStatus(),
        UpdateScheduledPaymentStatus(),
        GetTotalAccountsCount(),
        GetTotalBeneficiariesCount(),
        GetTotalCustomersCount(),
        GetTotalLoanApplicationsCount(),
        GetTotalLoansCount(),
        GetTotalScheduledPaymentsCount(),
        GetTotalSupportTicketsCount(),
        GetTotalTransactionsCount(),
]
