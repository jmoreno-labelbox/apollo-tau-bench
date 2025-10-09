import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
from tau_bench.envs.tool import Tool
import random

random.seed(42)

def get_next_customer_id() -> str:
    return f"cust_1"

def get_next_account_id() -> str:
    return f"acc_1"

def get_next_beneficiary_id() -> str:
    return f"bene_1"

def get_next_loan_application_id() -> str:
    return f"app_1"

def get_next_loan_id() -> str:
    return f"loan_1"

def get_next_loanacc_id() -> str:
    return f"loanacc_1"

def get_next_payment_id() -> str:
    return f"sp_1"

def get_next_support_ticket_id() -> str:
    return f"tkt_1"

def get_next_transaction_id() -> str:
    return f"txn_1"

def get_current_timestamp() -> str:
    return "2025-07-31T12:00:00Z" # per rules

def add_months(orig_date: datetime, months: int) -> datetime:
    """Return a new datetime that is `months` after `orig_date`, capping the day to month's length."""
    month = orig_date.month - 1 + months
    year = orig_date.year + month // 12
    month = month % 12 + 1
    day = min(orig_date.day, calendar.monthrange(year, month)[1])
    return orig_date.replace(year=year, month=month, day=day)

class AddNewCustomer(Tool):

    def invoke(
        data: Dict[str, Any],
        first_name: str,
        annual_income: float = None,
        city: str = None,
        country: str = None,
        date_of_birth: str = None,
        email_address: str = None,
        last_name: str = None,
        phone_number: str = None,
        postal_code: str = None,
        state: str = None,
        street_address: str = None
    ) -> str:
        # Required inputs
        required = [
            "first_name", "last_name", "date_of_birth", "email_address",
            "phone_number", "street_address", "city", "state", "postal_code", "country", "annual_income"
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        # Build minimal customer record
        customer_id = get_next_customer_id()
        date_joined = get_current_timestamp()

        personal_info = {
            "first_name":    first_name,
            "last_name":     last_name,
            "date_of_birth": date_of_birth,
            "annual_income": annual_income
        }
        contact_info = {
            "email_address": email_address,
            "phone_numbers": [{"type": "Mobile", "number": phone_number, "is_primary": True}],
            "mailing_address": {
                "street_address": street_address,
                "city":           city,
                "state":          state,
                "postal_code":    postal_code,
                "country":        country
            },
            "residential_address": {}
        }

        new_customer = {
            "customer_id":       customer_id,
            "personal_info":     personal_info,
            "contact_info":      contact_info,
            "account_ids":       [],
            "bank_relationship": {"date_joined": date_joined, "customer_segment": "Retail"},
            "financial_profile": {"annual_income": annual_income}
        }

        data.setdefault("customers", []).append(new_customer)
        return json.dumps(new_customer, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addNewCustomer",
                "description": "Creates a new customer with only essential profile fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name":       {"type": "string"},
                        "last_name":        {"type": "string"},
                        "date_of_birth":    {"type": "string"},
                        "email_address":    {"type": "string"},
                        "phone_number":     {"type": "string"},
                        "street_address":   {"type": "string"},
                        "state":            {"type": "string"},
                        "city":             {"type": "string"},
                        "postal_code":      {"type": "string"},
                        "country":          {"type": "string"},
                        "annual_income":    {"type": "integer"}
                    },
                    "required": [
                        "first_name", "last_name", "date_of_birth", "email_address",
                        "phone_number", "street_address", "city", "state", "postal_code", "country", "annual_income"
                    ]
                }
            }
        }



class AddNewBeneficiaryForCustomer(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        beneficiary_name: str,
        beneficiary_type: str,
        customer_id: str,
        relationship: str,
        account_number: str = None,
        bank_code: str = None,
        bank_name: str = None,
        bic_swift: str = None,
        branch_code: str = None,
        date_added: str = None,
        iban: str = None,
        ifsc_code: str = None,
        routing_number: str = None,
        sort_code: str = None
    ) -> str:
        for field in (
            "customer_id",
            "beneficiary_name",
            "beneficiary_type",
            "relationship",
            "bank_name",
        ):
            if not locals().get(field):
                return json.dumps({"error": f"{field} is required."}, indent=2)

        beneficiary_id = get_next_beneficiary_id()

        if date_added is None:
            date_added = get_current_timestamp()

        account_details = {
            k: v
            for k, v in {
                "bank_name": bank_name,
                "account_number": account_number,
                "routing_number": routing_number,
                "ifsc_code": ifsc_code,
                "iban": iban,
                "bic_swift": bic_swift,
                "sort_code": sort_code,
                "bank_code": bank_code,
                "branch_code": branch_code,
            }.items()
            if v is not None
        }

        new_beneficiary = {
            "beneficiary_id": beneficiary_id,
            "customer_id": customer_id,
            "beneficiary_name": beneficiary_name,
            "beneficiary_type": beneficiary_type,
            "relationship": relationship,
            "account_details": account_details,
            "date_added": date_added,
        }

        data.setdefault("beneficiaries", []).append(new_beneficiary)
        return json.dumps(new_beneficiary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddNewBeneficiaryForCustomer",
                "description": (
                    "Adds a new beneficiary for a customer and returns the full beneficiary record. "
                    "Supports various global bank account formats."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string"},
                        "beneficiary_name": {"type": "string"},
                        "beneficiary_type": {"type": "string"},
                        "relationship": {"type": "string"},
                        "bank_name": {"type": "string"},
                        "account_number": {"type": "string"},
                        "routing_number": {"type": "string"},
                        "ifsc_code": {"type": "string"},
                        "iban": {"type": "string"},
                        "bic_swift": {"type": "string"},
                        "sort_code": {"type": "string"},
                        "bank_code": {"type": "string"},
                        "branch_code": {"type": "string"},
                        "date_added":  {"type": "string"},
                    },
                    "required": [
                        "customer_id",
                        "beneficiary_name",
                        "beneficiary_type",
                        "relationship",
                        "bank_name",
                        "date_added"
                    ],
                },
            },
        }


class CreateNewAccountForCustomer(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        customer_id: str,
        account_type: str = "",
        account_type_code: str = "",
        currency: str = "USD"
    ) -> str:
        account_type = account_type.strip()
        account_type_code = account_type_code.strip()

        if not customer_id or not account_type or not account_type_code or not currency:
            return json.dumps({
                "error": "customer_id, account_type, and currency are required."
            }, indent=2)

        account_id = get_next_account_id()
        account_number_last_4 = str(random.randint(1000, 9999))
        date_opened = get_current_timestamp()

        new_account = {
            "account_id": account_id,
            "customer_id": customer_id,
            "account_type": account_type,
            "account_number_last_4": account_number_last_4,
            "balance": 0.0,
            "currency": currency,
            "date_opened": date_opened,
            "status": "Active"
        }

        # Optional fields
        if account_type == "Checking":
            new_account["overdraft_limit"] = 500.0
        elif account_type == "Savings":
            new_account["interest_rate"] = 0.02
        elif account_type == "Credit Card":
            new_account["credit_limit"] = 10000.0
            new_account["rewards_points"] = 0

        # Add to DB
        data.setdefault("accounts", []).append(new_account)

        # add to customer's account_ids
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                ids = customer.setdefault("account_ids", [])
                if account_id not in ids:
                    ids.append(account_id)
                break

        return json.dumps(new_account, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewAccountForCustomer",
                "description": (
                    "Creates a new account for a customer using account type (not code) "
                    "and returns the full account record. Acceptable values: "
                    "'Checking', 'Savings', 'Credit Card', 'Loan', 'Investment'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique customer ID to link the account to"
                        },
                        "account_type": {
                            "type": "string",
                            "description":  "Account type to create. Acceptable values: 'Checking', 'Savings', 'Credit Card', 'Loan', 'Investment'."
                        },
                        "account_type_code": {
                            "type": "string",
                            "description": "3-letter code for the account type. Acceptable values: 'chk', 'sav', 'crd', 'loan', 'inv'."
                        },
                        "currency": {
                            "type": "string",
                            "description": "Currency for the account (e.g., 'USD')"
                        }
                    },
                    "required": ["customer_id", "account_type", "account_type_code", "currency"]
                }
            }
        }


class CreateNewLoanApplication(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, loan_type: str = None, 
               requested_amount: float = None, requested_term_months: int = None, 
               purpose: str = None) -> str:
        if not all([customer_id, loan_type, requested_amount, requested_term_months, purpose]):
            return json.dumps({"error": "All loan-related fields and customer_id are required."}, indent=2)

        # Look up customer in the database
        customers = data.get("customers", [])
        customer = next((c for c in customers if c.get("customer_id") == customer_id), None)

        if not customer:
            return json.dumps({"error": f"Customer with ID '{customer_id}' not found."}, indent=2)

        # Extract data from customer profile
        personal_info = customer.get("personal_info", {})
        contact_info = customer.get("contact_info", {})
        financial_profile = customer.get("financial_profile", {})

        first_name = personal_info.get("first_name")
        last_name = personal_info.get("last_name")
        date_of_birth = personal_info.get("date_of_birth")
        email_address = contact_info.get("email_address")
        phone_number = next((p.get("number") for p in contact_info.get("phone_numbers", []) if p.get("is_primary")), None)
        address = contact_info.get("mailing_address") or {}

        employment_status = personal_info.get("occupation", "Employed")  # Default assumption
        employer_name = personal_info.get("employer")
        annual_income = financial_profile.get("annual_income", 0)
        monthly_debt_payments = 0  # Not present in customer DB, default to 0

        # Construct application entry
        application_id = get_next_loan_application_id()
        submission_date = get_current_timestamp()

        new_application = {
            "application_id": application_id,
            "customer_id": customer_id,
            "existing_customer": True,
            "submission_date": submission_date,
            "application_status": "Submitted",

            "applicant_info": {
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "email_address": email_address,
                "phone_number": phone_number,
                "address": address
            },

            "loan_details": {
                "loan_type": loan_type,
                "requested_amount": requested_amount,
                "requested_term_months": requested_term_months,
                "purpose": purpose

            },

            "financial_snapshot": {
                "employment_status": employment_status,
                "employer_name": employer_name,
                "annual_income": annual_income,
                "monthly_debt_payments": monthly_debt_payments
            },

            "decision": "Pending"
        }

        data.setdefault("loan_applications", []).append(new_application)

        return json.dumps({
            "application_id": application_id,
            "application_status": "Submitted"
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewLoanApplication",
                "description": (
                    "Submits a new loan application using the customer's existing record. "
                    "Only customer_id and loan details are required as input."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Existing customer ID"},
                        "loan_type": {"type": "string", "description": "Type of loan"},
                        "requested_amount": {"type": "number", "description": "Requested loan amount"},
                        "requested_term_months": {"type": "integer", "description": "Requested loan term in months"},
                        "purpose": {"type": "string", "description": "Purpose of the loan"}
                    },
                    "required": ["customer_id", "loan_type", "requested_amount", "requested_term_months", "purpose"]
                }
            }
        }


class CreateNewSchedulePayment(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        amount: float = None,
        beneficiary_id: str = None,
        currency: str = "",
        customer_id: str = None,
        end_date_str: str = None,
        frequency: str = "One-Time",
        source_account_id: str = None,
        start_date: Any = None,
        start_date_str: str = None
    ) -> str:
        frequency = frequency.capitalize()

        # required fields
        if not all([customer_id, source_account_id, beneficiary_id, amount, currency, frequency, start_date_str]):
            return json.dumps({"error": "All required fields must be provided."}, indent=2)

        # parse dates
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        except ValueError:
            return json.dumps({"error": "start_date must be YYYY-MM-DD."}, indent=2)
        end_date = None
        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            except ValueError:
                return json.dumps({"error": "end_date must be YYYY-MM-DD."}, indent=2)

        # validate source account and balance
        account = next((a for a in data.get("accounts", []) if a["account_id"] == source_account_id), None)
        if not account:
            return json.dumps({"error": "Source account not found."}, indent=2)
        if account.get("currency") != currency:
            return json.dumps({"error": "Currency mismatch with source account."}, indent=2)

        if account.get("balance", 0.0) < amount:
            status = "Paused"
        else:
            # deduct immediately
            account["balance"] -= amount
            status = "One-Time" if frequency == "One-Time" else "Active"

        # compute next_payment_date
        if frequency == "One-Time":
            next_payment_date = start_date
        elif frequency == "Weekly":
            next_payment_date = start_date + timedelta(weeks=1)
        elif frequency == "Monthly":
            next_payment_date = add_months(start_date, 1)
        elif frequency == "Quarterly":
            next_payment_date = add_months(start_date, 3)
        elif frequency == "Yearly":
            next_payment_date = add_months(start_date, 12)
        else:
            return json.dumps({"error": f"Unsupported frequency '{frequency}'."}, indent=2)

        # check end_date
        if end_date and next_payment_date.date() > end_date.date():
            status = "Completed"

        payment_id = get_next_payment_id()
        new_payment = {
            "payment_id": payment_id,
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "beneficiary_id": beneficiary_id,
            "amount": amount,
            "currency": currency,
            "frequency": frequency,
            "start_date": start_date_str,
            "next_payment_date": next_payment_date.strftime("%Y-%m-%d"),
            "end_date": end_date_str,
            "status": status
        }

        data.setdefault("scheduled_payments", []).append(new_payment)

        return json.dumps({
            "message": "Scheduled payment created successfully.",
            "payment_id": payment_id,
            "status": status,
            "next_payment_date": new_payment["next_payment_date"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewSchedulePayment",
                "description": (
                    "Schedules a new payment with logic for frequency, start/end dates, balance check, "
                    "and updates account balances accordingly."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string"},
                        "source_account_id": {"type": "string"},
                        "beneficiary_id": {"type": "string"},
                        "amount": {"type": "number"},
                        "currency": {"type": "string"},
                        "frequency": {
                            "type": "string",
                            "enum": ["One-Time", "Weekly", "Monthly", "Quarterly", "Yearly"]
                        },
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"}
                    },
                    "required": ["customer_id", "source_account_id", "beneficiary_id", "amount", "currency", "frequency", "start_date"]
                }
            }
        }

class AddNewLoanForCustomer(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        application_id: str = None,
        collateral_info: str = None,
        collateral_type: str = None,
        currency: str = "USD",
        customer_id: str = None
    ) -> str:
        loan_application_id = application_id

        if not all([customer_id, loan_application_id, collateral_type, collateral_info]):
            return json.dumps({
                "error": "customer_id, application_id, collateral_type, and collateral_info are required."
            }, indent=2)

        customers = data.get("customers", [])
        loan_applications = data.get("loan_applications", [])

        # Get customer object
        customer = next((c for c in customers if c["customer_id"] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found."}, indent=2)

        # Get loan application
        application = next((a for a in loan_applications if a["application_id"] == loan_application_id), None)
        if not application:
            return json.dumps({"error": "Loan application not found."}, indent=2)

        loan_details = application.get("loan_details", {})
        decision = application.get("decision", {})
        loan_type = loan_details.get("loan_type")

        # Generate IDs
        loan_id = get_next_loan_id()
        loan_account_id = get_next_loanacc_id()

        # Create loan account
        new_account = {
            "account_id": loan_account_id,
            "customer_id": customer_id,
            "account_type": "Loan",
            "account_number_last_4": str(random.randint(1000, 9999)),
            "balance": 0.0,
            "currency": currency,
            "date_opened": datetime.utcnow().strftime("%Y-%m-%d"),
            "status": "Active"
        }

        data.setdefault("accounts", []).append(new_account)
        customer.setdefault("account_ids", []).append(loan_account_id)

        # Loan fields based on DB structure
        principal_amount = decision.get("approved_amount")
        interest_rate = decision.get("interest_rate")
        term_months = loan_details.get("requested_term_months")
        origination_date = datetime.utcnow().strftime("%Y-%m-%d")
        maturity_date = (datetime.utcnow().replace(year=datetime.utcnow().year + (term_months // 12))).strftime("%Y-%m-%d")

        # Calculate monthly payment using simple amortization formula
        r = interest_rate / 100 / 12
        n = term_months
        if r > 0:
            monthly_payment = (principal_amount * r * (1 + r)**n) / ((1 + r)**n - 1)
        else:
            monthly_payment = principal_amount / n

        # Add loan to database
        new_loan = {
            "loan_id": loan_id,
            "customer_id": customer_id,
            "account_id": loan_account_id,
            "loan_type": loan_type,
            "principal_amount": principal_amount,
            "current_balance": principal_amount,  # Assuming full disbursement
            "interest_rate": interest_rate,
            "term_months": term_months,
            "origination_date": origination_date,
            "maturity_date": maturity_date,
            "monthly_payment": round(monthly_payment, 2),
            "status": "Active",
            "collateral": {
                "type": collateral_type,
                "address": collateral_info
            },
            "purpose": loan_details.get("purpose")
        }

        data.setdefault("loans", []).append(new_loan)

        return json.dumps({
            "status": "Loan successfully added.",
            "loan_id": loan_id,
            "loan_account_id": loan_account_id,
            "loan_type": loan_type
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddNewLoanForCustomer",
                "description": (
                    "Creates a new loan entry based on a customer's loan application and collateral details. "
                    "Generates new loan and account IDs and links them to the customer."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "ID of the customer taking the loan"},
                        "application_id": {"type": "string", "description": "ID of the related loan application"},
                        "collateral_type": {"type": "string", "description": "Type of collateral (e.g., 'Car', 'Property')"},
                        "collateral_info": {"type": "string", "description": "Detailed information about the collateral"},
                        "currency": {
                            "type": "string",
                            "description": "Currency for the account (e.g., 'USD')"
                        }
                    },
                    "required": ["customer_id", "application_id", "collateral_type", "collateral_info", "currency"]
                }
            }
        }


class AddSupportTicketForCustomerId(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        category: str = None,
        channel: str = None,
        customer_id: str = None,
        operation: str = None,
        parameters: Dict[str, Any] = {},
        priority: str = "Medium",
        target_entity: str = None,
        target_id: str = None
    ) -> str:
        required_fields = [
            "customer_id", "channel", "priority",
            "category", "target_id", "target_entity",
            "operation"
        ]
        missing = [f for f in required_fields if not locals().get(f)]
        if missing:
            return json.dumps(
                {"error": f"Missing required fields: {', '.join(missing)}"},
                indent=2
            )

        priority = priority.capitalize()
        ticket_id = get_next_support_ticket_id()
        now = get_current_timestamp()

        new_ticket = {
            "ticket_id": ticket_id,
            "customer_id": customer_id,
            "priority": priority,
            "channel": channel,
            "category": category,
            "target_id": target_id,
            "target_entity": target_entity,
            "operation": operation,
            "parameters": parameters,
            "status": "Open",
            "created_at": now,
            "last_updated": now
        }

        data.setdefault("support_tickets", []).append(new_ticket)
        return json.dumps(new_ticket, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSupportTicketForCustomerId",
                "description": "Adds a new support ticket for the given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer creating the support ticket"
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority of the ticket (e.g., Low, Medium, High); defaults to Medium"
                        },
                        "channel": {
                            "type": "string",
                            "description": "Channel via which the ticket was created (e.g., Phone, Email, Web Portal)"
                        },
                        "category": {
                            "type": "string",
                            "description": "Category of the support issue (e.g., Transaction, Loan, Account, Security)"
                        },
                        "target_id": {
                            "type": "string",
                            "description": "ID of the entity being affected (e.g., transaction ID, loan ID)"
                        },
                        "target_entity": {
                            "type": "string",
                            "description": "Type of entity affected (e.g., Transaction, Account, Loan)"
                        },
                        "operation": {
                            "type": "string",
                            "description": "Requested operation (e.g., Update, Cancel, Refund)"
                        },
                        "parameters": {
                            "type": "object",
                            "description": "Additional parameters for the operation (e.g., fields to update, new values)"
                        }
                    },
                    "required": [
                        "customer_id", "channel", "category", "priority",
                        "target_id", "target_entity", "operation"
                    ]
                }
            }
        }


class CreateNewTransaction(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        account_id: str = "",
        amount: float = None,
        currency: str = "",
        purchase_type: str = "",
        description: str = "",
        merchant_name: str = "",
        channel: str = ""
    ) -> str:
        account_id = account_id.strip()
        transaction_date = date.today()
        purchase_type = purchase_type.strip()
        description = description.strip()
        merchant_name = merchant_name.strip()
        channel = channel.strip()

        if not all([account_id, transaction_date, amount, currency, purchase_type, description, merchant_name, channel]):
            return json.dumps({"error": "All fields are required."}, indent=2)

        accounts = data.get("accounts", [])
        account = next((acc for acc in accounts if acc.get("account_id") == account_id), None)

        if not account:
            return json.dumps({"error": "Account not found."}, indent=2)

        currency = currency.strip()
        transaction_status = "Completed" if account["balance"] >= amount else "Pending"

        # Deduct amount from account if balance is sufficient
        if transaction_status == "Completed":
            account["balance"] -= amount

        transaction_id = get_next_transaction_id()

        new_transaction = {
            "transaction_id": transaction_id,
            "account_id": account_id,
            "transaction_date": transaction_date,
            "amount": amount,
            "currency": currency,
            "purchase_type": purchase_type,
            "description": description,
            "merchant_name": merchant_name,
            "channel": channel,
            "status": transaction_status
        }

        data.setdefault("transactions", []).append(new_transaction)

        return json.dumps({
            "transaction_id": transaction_id,
            "status": transaction_status,
            "message": "Transaction added successfully."
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createNewTransaction",
                "description": (
                    "Creates a new transaction entry. If the account has sufficient balance, "
                    "the status is 'Completed' and balance is deducted. Otherwise, status is 'Pending'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "The account from which the transaction is initiated"
                        },
                        "amount": {
                            "type": "number",
                            "description": "The amount of the transaction"
                        },
                        "currency": {
                            "type": "string",
                            "description": "The currency of the transaction"
                        },
                        "purchase_type": {
                            "type": "string",
                            "description": "Type of purchase (e.g., 'Online', 'In-store')"
                        },
                        "description": {
                            "type": "string",
                            "description": "Short description of the transaction"
                        },
                        "merchant_name": {
                            "type": "string",
                            "description": "Name of the merchant"
                        },
                        "channel": {
                            "type": "string",
                            "description": "Channel through which the transaction was made (e.g., Mobile, Web)"
                        }
                    },
                    "required": [
                        "account_id", "amount", "purchase_type", "description", "merchant_name", "channel"
                    ]
                }
            }
        }


class BlockAccountForCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_id: str = None) -> str:
        if not customer_id or not account_id:
            return json.dumps(
                {"error": "Both customer_id and account_id are required."},
                indent=2
            )

        # Find the account and verify ownership
        accounts = data.get("accounts", [])
        account = next((a for a in accounts
                        if a["account_id"] == account_id
                        and a["customer_id"] == customer_id), None)
        if not account:
            return json.dumps(
                {"error": "Account not found or does not belong to the customer."},
                indent=2
            )

        # Block it
        account["status"] = "Blocked"
        return json.dumps(account, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BlockAccountForCustomerId",
                "description": "Sets the status of a given customer’s account to 'Blocked'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the account"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "ID of the account to block"
                        }
                    },
                    "required": ["customer_id", "account_id"]
                }
            }
        }



class GetCustomerDetailsByName(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str = "", last_name: str = "") -> str:
        first_name = first_name.strip().lower()
        last_name = last_name.strip().lower()

        if not first_name or not last_name:
            return json.dumps({
                "error": "first_name and last_name are required."
            }, indent=2)

        customers = data.get("customers", [])
        for customer in customers:
            pi = customer.get("personal_info", {})
            if (
                pi.get("first_name", "").strip().lower() == first_name and
                pi.get("last_name", "").strip().lower() == last_name
            ):
                return json.dumps(customer, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerDetailsByName",
                "description": "Returns the full customer object based on first name and last name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "Customer's first name"
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Customer's last name"
                        }
                    },
                    "required": ["first_name", "last_name"]
                }
            }
        }


class GetAllAccountsOfCustomerByCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                return json.dumps({
                    "account_ids": customer.get("account_ids", [])
                }, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "description": "Returns all account IDs associated with a given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }


class UpdateAddressForCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, mailing_address: str = None, residential_address: str = None, set_as_primary: bool = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        if not mailing_address and not residential_address:
            return json.dumps({
                "error": "At least one of mailing_address or residential_address must be provided."
            }, indent=2)

        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.setdefault("contact_info", {})
                if mailing_address:
                    contact_info["mailing_address"] = mailing_address
                if residential_address:
                    contact_info["residential_address"] = residential_address
                return json.dumps({"status": "Address updated successfully."}, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAddressForCustomerId",
                "description": "Updates mailing and/or residential address for a given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        },
                        "mailing_address": {
                            "type": "object",
                            "description": "New mailing address object"
                        },
                        "residential_address": {
                            "type": "object",
                            "description": "New residential address object"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }


class GetCustomerAccountDetailsByCustomerIdAndAccountType(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_type: str = None) -> str:
        account_type = account_type.strip().lower() if account_type else ""

        if not customer_id or not account_type:
            return json.dumps({
                "error": "customer_id and account_type are required."
            }, indent=2)

        accounts = data.get("accounts", [])
        for account in accounts:
            if (account.get("customer_id") == customer_id and
                account.get("account_type", "").strip().lower() == account_type):
                return json.dumps(account, indent=2)

        return json.dumps({"error": "Account not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "description": (
                    "Returns full account details of a customer using customer_id and account_type "
                    "(e.g., 'Checking', 'Savings', 'Credit Card', etc.)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique ID of the customer"
                        },
                        "account_type": {
                            "type": "string",
                            "description": (
                                "Type of account to search for. Acceptable values: "
                                "'Checking', 'Savings', 'Credit Card', 'Loan', 'Investment'."
                            )
                        }
                    },
                    "required": ["customer_id", "account_type"]
                }
            }
        }


class UpdateEmailForOfCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, new_email: str = None) -> str:
        if not customer_id or not new_email:
            return json.dumps({
                "error": "Both customer_id and new_email are required."
            }, indent=2)

        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.setdefault("contact_info", {})
                contact_info["email_address"] = new_email
                return json.dumps({"status": "Email updated successfully."}, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmailForOfCustomerId",
                "description": "Updates the email address for the specified customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        },
                        "new_email": {
                            "type": "string",
                            "description": "New email address to set for the customer"
                        }
                    },
                    "required": ["customer_id", "new_email"]
                }
            }
        }


class UpdateContactNumberOfCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, new_phone_number: str = None, set_as_primary: bool = False) -> str:
        if not customer_id or not new_phone_number:
            return json.dumps({
                "error": "Both customer_id and new_phone_number are required."
            }, indent=2)

        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.setdefault("contact_info", {})
                phone_numbers = contact_info.setdefault("phone_numbers", [])

                if set_as_primary:
                    for phone in phone_numbers:
                        phone["is_primary"] = False

                phone_entry = {
                    "type": "Mobile",
                    "number": new_phone_number,
                    "is_primary": set_as_primary
                }
                phone_numbers.append(phone_entry)

                return json.dumps({"status": "Phone number updated successfully."}, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateContactNumberOfCustomerId",
                "description": "Adds a new phone number for a customer and sets it as primary if specified.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        },
                        "new_phone_number": {
                            "type": "string",
                            "description": "New phone number to be added"
                        },
                        "set_as_primary": {
                            "type": "boolean",
                            "description": "Flag to mark the new number as the primary number"
                        }
                    },
                    "required": ["customer_id", "new_phone_number"]
                }
            }
        }


class GetAccountTypeAndAccountTypeCode(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], account_type: str = "") -> str:
        account_type_input = account_type.strip().lower()

        if not account_type_input:
            return json.dumps({"error": "account_type is required."}, indent=2)

        type_map = {
            "checking": "chk",
            "savings": "sav",
            "credit card": "crd",
            "loan": "loan",
            "investment": "inv"
        }

        account_code = type_map.get(account_type_input)
        if account_code:
            standardized_type = account_type_input.title()  # e.g., "savings" → "Savings"
            return json.dumps({
                "account_type": standardized_type,
                "account_code": account_code
            }, indent=2)
        else:
            return json.dumps({
                "error": f"Unknown account type: {account_type_input}"
            }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountTypeAndAccountTypeCode",
                "description": (
                    "Returns both the standardized account type and its 3-letter account code. "
                    "Acceptable input values: 'Checking', 'Savings', 'Credit Card', 'Loan', 'Investment'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_type": {
                            "type": "string",
                            "description": (
                                "Human-readable account type. Acceptable values: "
                                "'Checking', 'Savings', 'Credit Card', 'Loan', 'Investment'."
                            )
                        }
                    },
                    "required": ["account_type"]
                }
            }
        }


class PayToBeneficiary(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id: str = None, source_account_id: str = None, amount: float = None, currency: str = None) -> str:
        # validate inputs
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        missing = [p for p in ("beneficiary_id", "source_account_id", "amount", "currency")
                   if params_dict.get(p) is None]
        if missing:
            return json.dumps(
                {"error": f"Missing required fields: {', '.join(missing)}"},
                indent=2
            )

        # find beneficiary
        bene = next((b for b in data.get("beneficiaries", [])
                     if b["beneficiary_id"] == beneficiary_id), None)
        if not bene:
            return json.dumps(
                {"error": f"Beneficiary '{beneficiary_id}' not found."},
                indent=2
            )

        # find source account
        acct = next((a for a in data.get("accounts", [])
                     if a["account_id"] == source_account_id), None)
        if not acct:
            return json.dumps(
                {"error": f"Source account '{source_account_id}' not found."},
                indent=2
            )

        # balance check
        if acct.get("balance", 0.0) < amount:
            return json.dumps(
                {"error": "Insufficient balance in source account."},
                indent=2
            )

        # perform debit
        acct["balance"] -= amount
        target_acc_num = bene["account_details"].get("account_number")

        return json.dumps({
            "message": f"Paid {amount:.2f} {currency} to beneficiary '{bene['beneficiary_name']}' "
                       f"(account {target_acc_num}).",
            "source_account_id": source_account_id,
            "beneficiary_account_number": target_acc_num,
            "amount": amount,
            "currency": currency,
            "new_source_balance": acct["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "payToBeneficiary",
                "description": (
                    "Debits the specified amount and currency from a source account and pays it "
                    "to the external account number stored for the given beneficiary."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "beneficiary_id": {
                            "type": "string",
                            "description": "Identifier of the beneficiary to pay"
                        },
                        "source_account_id": {
                            "type": "string",
                            "description": "Account ID from which funds will be debited"
                        },
                        "amount": {
                            "type": "number",
                            "description": "Amount to debit and pay"
                        },
                        "currency": {
                            "type": "string",
                            "description": "Currency of the payment (must match the source account)"
                        }
                    },
                    "required": [
                        "beneficiary_id",
                        "source_account_id",
                        "amount",
                    ]
                }
            }
        }


class CalculateTotalBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_ids: list = None) -> str:
        if account_ids is None:
            account_ids = []
        if not customer_id or not isinstance(account_ids, list) or not account_ids:
            return json.dumps(
                {"error": "customer_id and a non-empty list of account_ids are required."},
                indent=2
            )

        customers = data.get("customers", [])
        if not any(c.get("customer_id") == customer_id for c in customers):
            return json.dumps({"error": "Customer not found."}, indent=2)

        accounts = data.get("accounts", [])
        total = 0.0
        for acc in accounts:
            if acc.get("account_id") in account_ids and acc.get("customer_id") == customer_id:
                total += acc.get("balance", 0.0)

        return json.dumps({"total_balance": total}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalBalance",
                "description": "Calculates the sum of balances for the specified accounts of a given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer whose accounts are to be summed"
                        },
                        "account_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of account IDs to include in the total"
                        }
                    },
                    "required": ["customer_id", "account_ids"]
                }
            }
        }


class GetCustomerAccountDetailsByCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({
                "error": "customer_id is required."
            }, indent=2)

        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("customer_id") == customer_id:
                return json.dumps(account, indent=2)

        return json.dumps({"error": "Account not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCustomerAccountDetailsByCustomerId",
                "description": (
                    "Returns the full account record for a customer using their customer_id "
                    "and the last 4 digits of their account number."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique ID of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }




class GetContactDetailsOfCustomer(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.get("contact_info", {})
                email = contact_info.get("email_address")
                phone_list = contact_info.get("phone_numbers", [])
                primary_phone = next((p["number"] for p in phone_list if p.get("is_primary")), None)

                return json.dumps({
                    "email": email,
                    "primary_phone_number": primary_phone
                }, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getContactDetailsOfCustomer",
                "description": "Returns the email and primary phone number of a customer given their customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique ID of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }




class GetAllBeneficiariesForCustomerId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        all_benes = [
            bene for bene in data.get("beneficiaries", [])
            if bene.get("customer_id") == customer_id
        ]

        return json.dumps(all_benes, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllBeneficiariesForCustomerId",
                "description": "Returns a list of all beneficiary records for a given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer whose beneficiaries you want to retrieve"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }


class GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_name: str = None) -> str:
        beneficiary_name = beneficiary_name.strip().lower() if beneficiary_name else ""

        if not customer_id or not beneficiary_name:
            return json.dumps({
                "error": "Both customer_id and beneficiary_name are required."
            }, indent=2)

        beneficiaries = data.get("beneficiaries", [])
        for beneficiary in beneficiaries:
            if (beneficiary.get("customer_id") == customer_id and
                beneficiary.get("beneficiary_name", "").strip().lower() == beneficiary_name):
                return json.dumps(beneficiary, indent=2)

        return json.dumps({"error": "Beneficiary not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "description": "Fetches the full details of a beneficiary using customer ID and beneficiary name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the beneficiary"
                        },
                        "beneficiary_name": {
                            "type": "string",
                            "description": "Full name of the beneficiary to match (case-insensitive)"
                        }
                    },
                    "required": ["customer_id", "beneficiary_name"]
                }
            }
        }


class RemoveBeneficiaryByBeneficiaryId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_id: str = None) -> str:
        if not customer_id or not beneficiary_id:
            return json.dumps({"error": "customer_id and beneficiary_id are required."}, indent=2)

        beneficiaries = data.get("beneficiaries", [])
        for i, beneficiary in enumerate(beneficiaries):
            if (beneficiary.get("beneficiary_id") == beneficiary_id
                    and beneficiary.get("customer_id") == customer_id):
                del beneficiaries[i]
                return json.dumps({
                    "status": "Beneficiary removed successfully."
                }, indent=2)

        return json.dumps({"error": "Beneficiary not found for this customer."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveBeneficiaryByBeneficiaryId",
                "description": "Removes a beneficiary from the database using the beneficiary ID and customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the beneficiary"
                        },
                        "beneficiary_id": {
                            "type": "string",
                            "description": "Unique ID of the beneficiary to be removed"
                        }
                    },
                    "required": ["customer_id", "beneficiary_id"]
                }
            }
        }





class GetLoanApplicationStatusByCustomerIdAndType(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", loan_type: str = "") -> str:
        customer_id = customer_id.strip()
        loan_type = loan_type.strip().lower()

        if not customer_id or not loan_type:
            return json.dumps({"error": "customer_id and loan_type are required."}, indent=2)

        for app in data.get("loan_applications", []):
            if (app.get("customer_id") == customer_id and
                app.get("loan_details", {}).get("loan_type", "").strip().lower() == loan_type):

                status = app.get("application_status", "")
                # return json.dumps(status, indent=2)
                response = {
                    "application_id":     app.get("application_id"),
                    "application_status": status,
                    "submission_date":    app.get("submission_date")
                }

                # decision = app.get("decision") or {}

                # if status.lower() == "approved":
                #     response.update({
                #         "decision_date":   decision.get("decision_date"),
                #         "approved_amount": decision.get("approved_amount"),
                #         "interest_rate":   decision.get("interest_rate")
                #     })

                # elif status.lower() == "rejected":
                #     response["rejection_reason"] = decision.get("rejection_reason", "Not specified")

                # else:
                #     # Submitted, Under-Review, or other in-progress states
                # response["note"] = status

                return json.dumps(response, indent=2)

        return json.dumps({"message": "No matching loan application found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "description": (
                    "Returns loan application status for a specific customer and loan type. "
                    "If approved, includes decision date, approved amount, and interest rate. "
                    "If rejected, includes rejection reason."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID"
                        },
                        "loan_type": {
                            "type": "string",
                            "description": (
                                "Loan type to search for (e.g., Personal, Auto, Mortgage, Business)"
                            )
                        }
                    },
                    "required": ["customer_id", "loan_type"]
                }
            }
        }


class ProcessLoanApplicationId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", application_id: str = "") -> str:
        customer_id = customer_id.strip()
        application_id = application_id.strip()
        if not customer_id or not application_id:
            return json.dumps({"error": "customer_id and application_id are required."}, indent=2)

        loan_applications = data.get("loan_applications", [])
        customers = data.get("customers", [])

        # verify customer exists
        if not any(c.get("customer_id") == customer_id for c in customers):
            return json.dumps({"error": "Customer not found."}, indent=2)

        # Find loan application
        loan_application = next(
            (l for l in loan_applications
             if l.get("application_id") == application_id
             and l.get("customer_id") == customer_id),
            None
        )
        if not loan_application:
            return json.dumps({"error": "Loan application not found for this customer."}, indent=2)

        # Extract loan and customer financial info
        loan_details = loan_application.get("loan_details", {})
        financials = loan_application.get("financial_snapshot", {})
        annual_income = financials.get("annual_income", 0)
        monthly_debt = financials.get("monthly_debt_payments", 0)
        employment_status = financials.get("employment_status", "").strip().lower()
        requested_amount = loan_details.get("requested_amount", 0)
        loan_type = loan_details.get("loan_type", "Others")

        # Derived metrics
        dti = monthly_debt / (annual_income / 12) if annual_income else 1.0
        now = datetime.utcnow().isoformat() + "Z"

        decision = {"decision_date": now}
        approved = True
        rejection_reason = None

        # Loan approval logic
        if annual_income < 15000:
            approved = False
            rejection_reason = "Insufficient income"
        elif dti >= 0.50:
            approved = False
            rejection_reason = "High debt-to-income ratio"
        elif employment_status == "unemployed":
            approved = False
            rejection_reason = "Unstable employment"
        elif requested_amount > (annual_income * 5):
            approved = False
            rejection_reason = "Requested amount disproportionate to income"

        interest_rate = 0.0
        if loan_type == "Auto":
            interest_rate = 0.10
        elif loan_type == "Home":
            interest_rate = 0.12
        elif loan_type == "Student":
            interest_rate = 0.08
        elif loan_type == "Business":
            interest_rate = 0.09
        elif loan_type == "Personal":
            interest_rate = 0.15
        else:
            interest_rate = 0.18

        if approved:
            loan_application["application_status"] = "Approved"
            decision.update({
                "approved_amount": requested_amount,
                "interest_rate": interest_rate
            })
        else:
            loan_application["application_status"] = "Rejected"
            decision["reason"] = rejection_reason

        # Save decision
        loan_application["decision"] = decision

        return json.dumps({
            "customer_id": customer_id,
            "application_id": application_id,
            "application_status": loan_application["application_status"],
            "decision": decision
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessLoanApplicationId",
                "description": (
                    "Evaluates a loan application and determines whether it should be approved or rejected "
                    "based on standard lending criteria like income, DTI, and employment."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer whose application is being processed"
                        },
                        "application_id": {
                            "type": "string",
                            "description": "Loan application ID to evaluate and process"
                        }
                    },
                    "required": ["customer_id", "application_id"]
                }
            }
        }




class GetLoanInformationByLoanId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", loan_id: str = "") -> str:
        customer_id = customer_id.strip()
        loan_id = loan_id.strip()

        if not customer_id or not loan_id:
            return json.dumps({"error": "customer_id and loan_id are required."}, indent=2)

        # Verify and fetch the loan
        loans = data.get("loans", [])
        loan = next(
            (ln for ln in loans
             if ln.get("loan_id") == loan_id and ln.get("customer_id") == customer_id),
            None
        )
        if not loan:
            return json.dumps({"error": "Loan not found for this customer."}, indent=2)

        return json.dumps(loan, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLoanInformationByLoanId",
                "description": "Returns loan details for the given loan_id after verifying customer ownership.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the loan"
                        },
                        "loan_id": {
                            "type": "string",
                            "description": "Loan ID to retrieve the loan information for"
                        }
                    },
                    "required": ["customer_id", "loan_id"]
                }
            }
        }

class GetLoanDetailsByCustomerIdAndType(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", loan_type: str = "") -> str:
        customer_id = customer_id.strip()
        loan_type = loan_type.strip().lower()

        if not customer_id or not loan_type:
            return json.dumps({
                "error": "Both customer_id and loan_type are required."
            }, indent=2)

        loans = data.get("loans", [])
        matched_loan = next(
            (loan for loan in loans
             if loan.get("customer_id") == customer_id and
                loan.get("loan_type", "").strip().lower() == loan_type),
            None
        )

        if not matched_loan:
            return json.dumps({
                "message": "No matching loan found for the customer and loan type."
            }, indent=2)

        return json.dumps(matched_loan, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLoanDetailsByCustomerIdAndType",
                "description": (
                    "Returns a customer's loan details for a specific loan type. "
                    "Loan type values can include: 'Mortgage', 'Auto', 'Personal', 'Business', etc."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the loan"
                        },
                        "loan_type": {
                            "type": "string",
                            "description": (
                                "Type of loan to search for. "
                                "Acceptable values: 'Mortgage', 'Auto', 'Personal', 'Business', etc."
                            )
                        }
                    },
                    "required": ["customer_id", "loan_type"]
                }
            }
        }





class GetScheduledPaymentDetailsByCustomerIdAndBeneficiaryId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", beneficiary_id: str = "") -> str:
        customer_id = customer_id.strip()
        beneficiary_id = beneficiary_id.strip()

        if not customer_id or not beneficiary_id:
            return json.dumps({
                "error": "customer_id and beneficiary_id are required."
            }, indent=2)

        scheduled_payments = data.get("scheduled_payments", [])
        for payment in scheduled_payments:
            if payment.get("customer_id") == customer_id and payment.get("beneficiary_id") == beneficiary_id:
                return json.dumps(payment, indent=2)

        return json.dumps({
            "error": "No scheduled payment found for the given customer and beneficiary."
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "description": "Returns a scheduled payment using customer ID and beneficiary ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer"
                        },
                        "beneficiary_id": {
                            "type": "string",
                            "description": "ID of the beneficiary"
                        }
                    },
                    "required": ["customer_id", "beneficiary_id"]
                }
            }
        }


class CancelPaymentByScheduledPaymentId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", scheduled_payment_id: str = "") -> str:
        customer_id = customer_id.strip()
        scheduled_payment_id = scheduled_payment_id.strip()

        # Validate inputs
        missing = []
        if not customer_id:
            missing.append("customer_id")
        if not scheduled_payment_id:
            missing.append("scheduled_payment_id")
        if missing:
            return json.dumps(
                {"error": f"Missing required fields: {', '.join(missing)}"},
                indent=2
            )

        # Find and cancel the payment
        scheduled_payments = data.get("scheduled_payments", [])
        for payment in scheduled_payments:
            if (payment.get("payment_id") == scheduled_payment_id and
                    payment.get("customer_id") == customer_id):
                payment["status"] = "Cancelled"
                return json.dumps({
                    "message": "Scheduled payment cancelled successfully.",
                    "customer_id": customer_id,
                    "payment_id": scheduled_payment_id,
                    "status": "Cancelled"
                }, indent=2)

        return json.dumps({
            "error": "Scheduled payment not found for the given ID and customer."
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelPaymentByScheduledPaymentId",
                "description": "Cancels a scheduled payment by setting its status to 'Cancelled', verifying customer ownership.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the scheduled payment"
                        },
                        "scheduled_payment_id": {
                            "type": "string",
                            "description": "ID of the scheduled payment to cancel"
                        }
                    },
                    "required": ["customer_id", "scheduled_payment_id"]
                }
            }
        }


class GetTransactionDetailsByAccountIdForTimeDuration(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = "", start_date: str = "", end_date: str = "", customer_id: str = "") -> str:
        account_id = account_id.strip()
        start_date_str = start_date.strip()
        end_date_str = end_date.strip()
        customer_id = customer_id.strip()
        if not account_id or not start_date_str or not end_date_str:
            return json.dumps({
                "error": "account_id, start_date, and end_date are required."
            }, indent=2)

        try:
            start_date = datetime.fromisoformat(start_date_str)
            end_date = datetime.fromisoformat(end_date_str)
        except ValueError:
            return json.dumps({
                "error": "Invalid date format. Use ISO format (YYYY-MM-DD)."
            }, indent=2)

        transactions = data.get("transactions", [])
        filtered_transactions = [
            txn for txn in transactions
            if txn.get("account_id") == account_id and
               start_date <= datetime.fromisoformat(txn.get("transaction_date", "")) <= end_date
        ]

        return json.dumps(filtered_transactions, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTransactionDetailsByAccountIdForTimeDuration",
                "description": (
                    "Returns all transactions for a specific account ID between the provided start and end dates."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account ID for which to fetch transactions"
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in ISO format (YYYY-MM-DD)"
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in ISO format (YYYY-MM-DD)"
                        }
                    },
                    "required": ["customer_id", "account_id", "start_date", "end_date"]
                }
            }
        }





class GetTransactionDetailsByAccountIdAndMerchantName(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, merchant_name: str = None) -> str:
        account_id = (account_id or "").strip()
        merchant_name = (merchant_name or "").strip().lower()

        if not account_id or not merchant_name:
            return json.dumps(
                {"error": "account_id and merchant_name are required."},
                indent=2
            )

        transactions = data.get("transactions", [])
        matched = [
            txn for txn in transactions
            if txn.get("account_id") == account_id
            and (txn.get("merchant_name") or "").strip().lower() == merchant_name
        ]

        if not matched:
            return json.dumps({"message": "No matching transactions found."}, indent=2)

        return json.dumps({"transactions": matched}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTransactionDetailsByAccountIdAndMerchantName",
                "description": (
                    "Fetches transaction records using the account ID and merchant name."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account ID used for the transactions"
                        },
                        "merchant_name": {
                            "type": "string",
                            "description": "Merchant name to filter transactions (case-insensitive)"
                        }
                    },
                    "required": ["account_id", "merchant_name"]
                }
            }
        }


class GetSupportTicketInformationByCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "") -> str:
        customer_id = customer_id.strip()

        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        support_tickets = data.get("support_tickets", [])
        matched_tickets = [
            ticket for ticket in support_tickets
            if ticket.get("customer_id") == customer_id
        ]

        if not matched_tickets:
            return json.dumps({"message": "No support tickets found for this customer."}, indent=2)

        return json.dumps({"tickets": matched_tickets}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSupportTicketInformationByCustomerId",
                "description": "Fetches all support tickets associated with the given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique ID of the customer whose support tickets are to be fetched"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }





class TransferMoneySameCurrency(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, source_account_id: str = None, 
               target_account_id: str = None, currency: str = None, amount: float = None) -> str:
        if not all([customer_id, source_account_id, target_account_id, currency, amount]):
            return json.dumps(
                {"error": "customer_id, source_account_id, target_account_id, currency, and amount are required."},
                indent=2
            )

        accounts = data.get("accounts", [])
        src = next((a for a in accounts if a["account_id"] == source_account_id and a.get("customer_id") == customer_id), None)
        tgt = next((a for a in accounts if a["account_id"] == target_account_id), None)

        if not src:
            return json.dumps({"error": f"Source account '{source_account_id}' not found for customer '{customer_id}'."}, indent=2)
        if not tgt:
            return json.dumps({"error": f"Target account '{target_account_id}' not found for customer '{customer_id}'."}, indent=2)

        if src.get("currency") != currency or tgt.get("currency") != currency:
            return json.dumps({"error": "Currency mismatch for same‑currency transfer."}, indent=2)

        if src.get("balance", 0.0) < amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        src["balance"] -= amount
        tgt["balance"] += amount

        return json.dumps({
            "message": "Transfer successful (same currency).",
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "target_account_id": target_account_id,
            "amount_transferred": amount,
            "currency": currency,
            "source_balance": src["balance"],
            "target_balance": tgt["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferMoneySameCurrency",
                "description": "Transfers funds between two accounts of the same customer in the same currency.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "ID of the customer performing the transfer"},
                        "source_account_id": {"type": "string", "description": "Account ID to debit"},
                        "target_account_id": {"type": "string", "description": "Account ID to credit"},
                        "currency": {"type": "string", "description": "Currency of the transfer"},
                        "amount": {"type": "number", "description": "Amount to transfer"}
                    },
                    "required": ["customer_id", "source_account_id", "target_account_id", "currency", "amount"]
                }
            }
        }



class TransferMoneyWithConversion(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        customer_id: str = None,
        source_account_id: str = None,
        target_account_id: str = None,
        source_amount: float = None,
        target_amount: float = None,
        source_currency: str = None,
        target_currency: str = None
    ) -> str:
        if not all([customer_id, source_account_id, target_account_id, source_amount, target_amount, source_currency, target_currency]):
            return json.dumps(
                {"error": "customer_id, source_account_id, target_account_id, source_amount, target_amount, source_currency, and target_currency are required."},
                indent=2
            )

        accounts = data.get("accounts", [])
        src = next(
            (a for a in accounts if a.get("account_id") == source_account_id and a.get("customer_id") == customer_id),
            None
        )
        tgt = next(
            (a for a in accounts if a.get("account_id") == target_account_id),
            None
        )

        if not src:
            return json.dumps({"error": f"Source account '{source_account_id}' not found for customer '{customer_id}'."}, indent=2)
        if not tgt:
            return json.dumps({"error": f"Target account '{target_account_id}' not found for customer '{customer_id}'."}, indent=2)

        if src.get("currency") != source_currency or tgt.get("currency") != target_currency:
            return json.dumps({"error": "Currency mismatch for one or both accounts."}, indent=2)

        if src.get("balance", 0.0) < source_amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        # perform the transfer
        src["balance"] -= source_amount
        tgt["balance"] = tgt.get("balance", 0.0) + target_amount

        return json.dumps({
            "message": "Cross‑currency transfer successful.",
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "target_account_id": target_account_id,
            "source_amount": source_amount,
            "target_amount": target_amount,
            "source_balance": src["balance"],
            "target_balance": tgt["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transferMoneyWithConversion",
                "description": (
                    "Transfers funds between two accounts of the same customer in different currencies when the source and target amounts are pre‑computed."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id":     {"type": "string", "description": "ID of the customer performing the transfer"},
                        "source_account_id": {"type": "string", "description": "Account ID to debit"},
                        "target_account_id": {"type": "string", "description": "Account ID to credit"},
                        "source_amount":     {"type": "number", "description": "Amount in source currency to debit"},
                        "target_amount":     {"type": "number", "description": "Amount in target currency to credit"},
                        "source_currency":   {"type": "string", "description": "Currency code of the source amount"},
                        "target_currency":   {"type": "string", "description": "Currency code of the target amount"}
                    },
                    "required": [
                        "customer_id",
                        "source_account_id",
                        "target_account_id",
                        "source_amount",
                        "target_amount",
                        "source_currency",
                        "target_currency"
                    ]
                }
            }
        }


class GetCurrencyConversionAmount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_currency: str = None, target_currency: str = None, source_amount: float = None) -> str:
        source = source_currency
        target = target_currency
        amount = source_amount

        if not all([source, target, amount]):
            return json.dumps(
                {"error": "source_currency, source_amount, and target_currency are required."},
                indent=2
            )

        rates = {
            "USD_EUR": 0.85,
            "EUR_USD": 1.18,
            "USD_GBP": 0.75,
            "GBP_USD": 1.33,
            "USD_CAD": 1.25,
            "CAD_USD": 0.80,
            # add more as needed
        }

        key = f"{source.upper()}_{target.upper()}"
        rate = rates.get(key)
        if rate is None:
            return json.dumps(
                {"error": f"No conversion rate available for {source} to {target}."},
                indent=2
            )

        target_amount = amount * rate

        return json.dumps(
            {
                "source_currency": source.upper(),
                "source_amount": amount,
                "target_currency": target.upper(),
                "target_amount": round(target_amount, 2)
            },
            indent=2
        )
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrencyConversionAmount",
                "description": (
                    "Converts a specified amount from one currency to another "
                    "using a static rate table, returning both source and target amounts."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_currency": {
                            "type": "string",
                            "description": "Currency code to convert from (e.g., 'USD')"
                        },
                        "source_amount": {
                            "type": "number",
                            "description": "Amount in the source currency"
                        },
                        "target_currency": {
                            "type": "string",
                            "description": "Currency code to convert to (e.g., 'EUR')"
                        }
                    },
                    "required": ["source_currency", "source_amount", "target_currency"]
                }
            }
        }

class ChangeSupportTicketStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, ticket_id: str = None, new_status: str = "") -> str:
        new_status = new_status.strip()
        if not all([customer_id, ticket_id, new_status]):
            return json.dumps({"error": "customer_id, ticket_id and new_status are required."}, indent=2)

        tickets = data.get("support_tickets", [])
        for ticket in tickets:
            if (ticket.get("ticket_id") == ticket_id and
                ticket.get("customer_id") == customer_id):
                ticket["status"] = new_status
                return json.dumps(ticket, indent=2)

        return json.dumps({"error": "Support ticket not found for this customer."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ChangeSupportTicketStatus",
                "description": "Updates the status of a support ticket given its ID and customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the ticket"
                        },
                        "ticket_id": {
                            "type": "string",
                            "description": "Identifier of the support ticket to update"
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status value (e.g., 'Resolved' or 'Open')"
                        }
                    },
                    "required": ["customer_id", "ticket_id", "new_status"]
                }
            }
        }

class PayToBeneficiarySameCurrency(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_id: str = None, 
               source_account_id: str = None, amount: float = None, currency: str = None) -> str:
        if not all([customer_id, beneficiary_id, source_account_id, amount, currency]):
            return json.dumps(
                {"error": "customer_id, beneficiary_id, source_account_id, amount, and currency are required."},
                indent=2
            )

        # Lookup beneficiary and verify ownership
        ben = next(
            (b for b in data.get("beneficiaries", [])
             if b.get("beneficiary_id") == beneficiary_id and b.get("customer_id") == customer_id),
            None
        )
        if not ben:
            return json.dumps({"error": f"Beneficiary '{beneficiary_id}' not found for customer '{customer_id}'."}, indent=2)

        # Lookup source account and verify ownership
        acct = next(
            (a for a in data.get("accounts", [])
             if a.get("account_id") == source_account_id and a.get("customer_id") == customer_id),
            None
        )
        if not acct:
            return json.dumps({"error": f"Source account '{source_account_id}' not found for customer '{customer_id}'."}, indent=2)

        # Currency check
        if acct.get("currency") != currency:
            return json.dumps(
                {"error": "Currency mismatch for same‑currency payment."},
                indent=2
            )

        # Balance check
        if acct.get("balance", 0.0) < amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        # Perform debit
        acct["balance"] -= amount
        target_acc_num = ben["account_details"].get("account_number")

        return json.dumps({
            "message": f"Paid {amount:.2f} {currency} to beneficiary '{ben['beneficiary_name']}' (acct {target_acc_num}).",
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "beneficiary_account_number": target_acc_num,
            "amount": amount,
            "currency": currency,
            "new_source_balance": acct["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PayToBeneficiarySameCurrency",
                "description": "Pays a beneficiary in the same currency by debiting the source account for the given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer performing the payment"
                        },
                        "beneficiary_id": {
                            "type": "string",
                            "description": "ID of the beneficiary to pay"
                        },
                        "source_account_id": {
                            "type": "string",
                            "description": "Account ID to debit"
                        },
                        "amount": {
                            "type": "number",
                            "description": "Amount to pay"
                        },
                        "currency": {
                            "type": "string",
                            "description": "Currency code (must match source account)"
                        }
                    },
                    "required": ["customer_id", "beneficiary_id", "source_account_id", "amount", "currency"]
                }
            }
        }


class PayToBeneficiaryWithConversion(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any], 
        customer_id: str = None, 
        beneficiary_id: str = None, 
        source_account_id: str = None, 
        source_amount: float = None, 
        source_currency: str = None, 
        target_currency: str = None
    ) -> str:
        if not all([customer_id, beneficiary_id, source_account_id, source_amount, source_currency, target_currency]):
            return json.dumps(
                {"error": "customer_id, beneficiary_id, source_account_id, source_amount, source_currency, and target_currency are required."},
                indent=2
            )

        # lookup beneficiary and verify ownership
        ben = next(
            (b for b in data.get("beneficiaries", [])
             if b.get("beneficiary_id") == beneficiary_id and b.get("customer_id") == customer_id),
            None
        )
        if not ben:
            return json.dumps(
                {"error": f"Beneficiary '{beneficiary_id}' not found for customer '{customer_id}'."},
                indent=2
            )

        # lookup source account and verify ownership
        acct = next(
            (a for a in data.get("accounts", [])
             if a.get("account_id") == source_account_id and a.get("customer_id") == customer_id),
            None
        )
        if not acct:
            return json.dumps(
                {"error": f"Source account '{source_account_id}' not found for customer '{customer_id}'."},
                indent=2
            )

        # currency & balance checks
        if acct.get("currency") != source_currency:
            return json.dumps({"error": "Source currency mismatch."}, indent=2)
        if acct.get("balance", 0.0) < source_amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        # determine conversion rate
        rates = {
            "USD_EUR": 0.85,
            "EUR_USD": 1.18,
            "USD_GBP": 0.75,
            "GBP_USD": 1.33,
            "USD_CAD": 1.25,
            "CAD_USD": 0.80,
        }
        key = f"{source_currency.upper()}_{target_currency.upper()}"
        rate = rates.get(key)
        if rate is None:
            return json.dumps(
                {"error": f"No conversion rate for {source_currency} to {target_currency}."},
                indent=2
            )

        target_amount = round(source_amount * rate, 2)

        # debit and pay
        acct["balance"] -= source_amount
        target_acc_num = ben["account_details"].get("account_number")

        return json.dumps({
            "message": f"Paid {target_amount:.2f} {target_currency} to beneficiary '{ben['beneficiary_name']}'.",
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "beneficiary_account_number": target_acc_num,
            "source_amount": source_amount,
            "source_currency": source_currency,
            "target_amount": target_amount,
            "target_currency": target_currency,
            "new_source_balance": acct["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PayToBeneficiaryWithConversion",
                "description": "Pays a beneficiary in a different currency by debiting the source account for a given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id":       {"type": "string", "description": "ID of the customer performing the payment"},
                        "beneficiary_id":    {"type": "string", "description": "ID of the beneficiary to pay"},
                        "source_account_id": {"type": "string", "description": "Account ID to debit"},
                        "source_amount":     {"type": "number", "description": "Amount in source currency to debit"},
                        "source_currency":   {"type": "string", "description": "Currency code of the source amount"},
                        "target_currency":   {"type": "string", "description": "Currency code to convert to"}
                    },
                    "required": [
                        "customer_id",
                        "beneficiary_id",
                        "source_account_id",
                        "source_amount",
                        "source_currency",
                        "target_currency"
                    ]
                }
            }
        }

class CheckAccountBalance(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_id: str = None, requested_amount: float = 0.0) -> str:
        if not customer_id or not account_id:
            return json.dumps(
                {"error": "customer_id and account_id are required."},
                indent=2
            )

        # find the account and verify ownership
        acct = next(
            (a for a in data.get("accounts", [])
             if a.get("account_id") == account_id
             and a.get("customer_id") == customer_id),
            None
        )
        if not acct:
            return json.dumps(
                {"error": "Account not found or does not belong to customer."},
                indent=2
            )

        balance = acct.get("balance", 0.0)

        if requested_amount:
            if balance < requested_amount:
                return json.dumps(
                    {"error": f"Insufficient funds: available {balance}, requested {requested_amount}."},
                    indent=2
                )

        return json.dumps(
            {"balance": balance},
            indent=2
        )
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckAccountBalance",
                "description": (
                    "Retrieves the balance for the given account and customer. "
                    "If a requested_amount > 0 is provided, returns an error if balance is insufficient."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the account"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "ID of the account to check"
                        },
                        "requested_amount": {
                            "type": "number",
                            "description": "Optional amount to validate against the balance"
                        }
                    },
                    "required": ["customer_id", "account_id"]
                }
            }
        }

class ReceivePayment(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_id: str = None, amount: float = None, currency: str = None, source: str = None) -> str:
        if not all([customer_id, account_id, amount, currency]):
            return json.dumps(
                {"error": "customer_id, account_id, amount, and currency are required."},
                indent=2
            )

        # Find account and verify ownership
        account = next(
            (a for a in data.get("accounts", [])
             if a.get("account_id") == account_id and a.get("customer_id") == customer_id),
            None
        )
        if not account:
            return json.dumps(
                {"error": "Account not found or does not belong to the customer."},
                indent=2
            )

        # Currency check
        if account.get("currency") != currency:
            return json.dumps(
                {"error": "Currency mismatch with account."},
                indent=2
            )

        # Perform credit
        account["balance"] = account.get("balance", 0.0) + amount

        return json.dumps({
            "message": "Payment received successfully.",
            "customer_id": customer_id,
            "account_id": account_id,
            "amount": amount,
            "currency": currency,
            "new_balance": account["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReceivePayment",
                "description": "Credits the specified amount into a customer's account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string"},
                        "account_id": {"type": "string"},
                        "amount": {"type": "number"},
                        "currency": {"type": "string"}
                    },
                    "required": ["customer_id", "account_id", "amount", "currency"]
                }
            }
        }
class GetCustomerDetailsByCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "") -> str:
        customer_id = customer_id.strip()
        if not customer_id:
            return json.dumps(
                {"error": "customer_id is required."},
                indent=2
            )

        customer = next(
            (c for c in data.get("customers", [])
             if c.get("customer_id") == customer_id),
            None
        )
        if not customer:
            return json.dumps(
                {"error": f"Customer '{customer_id}' not found."},
                indent=2
            )

        return json.dumps(customer, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerDetailsByCustomerId",
                "description": "Fetches the complete customer record for the given customer_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }




class GetAccountDetailsByCustomerIdAndAccountId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_id: str = None) -> str:
        if not customer_id or not account_id:
            return json.dumps({
                "error": "customer_id and account_id are both required."
            }, indent=2)

        # Look up the account
        acct = next(
            (a for a in data.get("accounts", [])
             if a.get("customer_id") == customer_id and a.get("account_id") == account_id),
            None
        )

        if not acct:
            return json.dumps({
                "error": f"No account found for customer_id '{customer_id}' with account_id '{account_id}'."
            }, indent=2)

        # Return the account details
        return json.dumps({
            "account_id":            acct["account_id"],
            "customer_id":           acct["customer_id"],
            "account_type":          acct["account_type"],
            "balance":               acct.get("balance"),
            "currency":              acct.get("currency"),
            "status":                acct.get("status"),
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
        "function": {
            "name": "GetAccountDetailsByCustomerIdAndAccountId",
            "description": "Fetches the full details of an account matching the given customer_id and account_id.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "ID of the customer who owns the account."
                    },
                    "account_id": {
                        "type": "string",
                        "description": "ID of the account to retrieve."
                    }
                },
                "required": ["customer_id", "account_id"]
            }
        }
    }



TOOLS = [
    AddNewCustomer(),
    AddNewBeneficiaryForCustomer(),
    CreateNewAccountForCustomer(),
    CreateNewLoanApplication(),
    CreateNewSchedulePayment(),
    AddNewLoanForCustomer(),
    AddSupportTicketForCustomerId(),
    CreateNewTransaction(),

    GetAccountDetailsByCustomerIdAndAccountId(),

    GetCustomerDetailsByCustomerId(),
    CheckAccountBalance(),
    ReceivePayment(),
    GetCustomerDetailsByName(),
    GetAllAccountsOfCustomerByCustomerId(),
    UpdateAddressForCustomerId(),
    GetCustomerAccountDetailsByCustomerIdAndAccountType(),
    UpdateEmailForOfCustomerId(),
    UpdateContactNumberOfCustomerId(),
    GetAccountTypeAndAccountTypeCode(),
    GetCustomerAccountDetailsByCustomerId(),
    GetContactDetailsOfCustomer(),
    BlockAccountForCustomerId(),

    GetAllBeneficiariesForCustomerId(),
    GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName(),
    RemoveBeneficiaryByBeneficiaryId(),
    PayToBeneficiarySameCurrency(),
    PayToBeneficiaryWithConversion(),

    GetLoanApplicationStatusByCustomerIdAndType(),
    ProcessLoanApplicationId(),
    AddNewLoanForCustomer(),
    GetLoanInformationByLoanId(),
    GetLoanDetailsByCustomerIdAndType(),

    CalculateTotalBalance(),

    GetSupportTicketInformationByCustomerId(),
    ChangeSupportTicketStatus(),

    GetScheduledPaymentDetailsByCustomerIdAndBeneficiaryId(),
    CancelPaymentByScheduledPaymentId(),


    GetTransactionDetailsByAccountIdForTimeDuration(),
    GetTransactionDetailsByAccountIdAndMerchantName(),

    GetCurrencyConversionAmount(),
    TransferMoneyWithConversion(),
    TransferMoneySameCurrency()
]
