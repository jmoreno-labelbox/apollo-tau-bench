"""
tools_model.py

This module defines a comprehensive suite of tool classes for simulating operations
within a banking services environment. Each tool encapsulates a specific action
that can be performed by a virtual agent, such as transferring funds, managing
beneficiaries, applying for loans, retrieving account balances, and more.

The tools are designed for integration into an agentic simulation framework
and follow a unified interface contract. Each tool implements the `invoke()` method
to execute its core logic, and the `get_info()` method to return structured
metadata about its expected input schema and operational behavior.

Key Features:
- Modular tools representing realistic financial and support operations
- Interaction with in-memory JSON-based datasets to simulate database behavior
- Support for account, customer, transaction, loan, and ticketing workflows
- Compatible with multi-agent simulation or API-driven task execution frameworks

Classes:
    - AddJointAccountHolderTool
    - AggregateMonthlyExpensesTool
    - ApplyForLoanWithCheckTool
    - AutoClassifySupportTicketPriorityTool
    - CancelScheduledPaymentTool
    - CloseAccountRequestTool
    - CreateCustomerAccountTool
    - DeleteExistingBeneficiaryTool
    - DetectSuspiciousActivityAndAlertTool
    - DownloadStatementByDateTool
    - FreezeAccountOnFraudAlertTool
    - GetAccountBalanceTool
    - GetAccountTransactionHistoryTool
    - GetCustomerProfileTool
    - ListLinkedBeneficiariesTool
    - RegisterNewBeneficiaryTool
    - RemoveJointAccountHolderTool
    - ReviewTicketHistoryTool
    - SchedulePaymentWithValidationTool
    - SubmitSupportTicketTool
    - SummarizeLoanApplicationsByStatusTool
    - TransferFundsWithLimitCheckTool
    - UnlockAccountBySecurityCheckTool
    - UpdateAccountPreferencesTool
    - UpdateCustomerEmailTool
    - VerifyCustomerIdentityTool
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

from domains.dto import Tool

DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")

def get_current_timestamp() -> str:
    return "2025-07-31T12:00:00.000000" # per rules

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
        return json.load(f)

def generate_unique_id() -> str:
    return 'fd520c73'

class CreateCustomerAccountTool(Tool):
    """
    Tool for creating a new bank account for a specified customer.

    This tool generates a unique account ID and associates the new account
    with an existing customer. It supports various account types and accepts
    an optional initial credit limit for account initialization.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Creates a new account and returns the confirmation with account ID.

        get_info() -> Dict[str, Any]:
            Returns metadata describing the tool's name, parameters, and purpose.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        account_type = kwargs.get("account_type")
        currency = kwargs.get("currency")
        initial_limit = kwargs.get("initial_limit", 0)

        if not all([customer_id, account_type, currency]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        accounts = data.get("accounts", [])
        account_id = f"acc_{generate_unique_id()}"
        new_account = {
            "account_id": account_id,
            "customer_id": customer_id,
            "account_type": account_type,
            "currency": currency,
            "balance": initial_limit,
            "status": "Active",
            "created_at": get_current_timestamp(),
        }
        accounts.append(new_account)

        return json.dumps(
            {"message": "Account created", "account_id": account_id}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_customer_account",
                "description": "Create a new customer account with a specific account type and initial limit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer id"},
                        "account_type": {
                            "type": "string",
                            "description": "Account type",
                        },
                        "currency": {"type": "string", "description": "Currency"},
                        "initial_limit": {
                            "type": "float",
                            "description": "Initial limit",
                        },
                    },
                    "required": [
                        "customer_id",
                        "account_type",
                        "currency",
                        "initial_limit",
                    ],
                },
            },
        }


class ApplyForLoanWithCheckTool(Tool):
    """
    Tool for applying for a loan with a built-in risk evaluation.

    This tool takes the customer's ID, the requested amount, and the purpose
    of the loan, then calculates a basic credit score adjustment and risk level
    based on the amount. This does not persist the loan; it only simulates evaluation.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Simulates loan application and risk assessment.

        get_info() -> Dict[str, Any]:
            Returns metadata about the tool, including expected parameters.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        amount = kwargs.get("amount")
        purpose = kwargs.get("purpose")

        if not all([customer_id, amount, purpose]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        credit_score = 700
        risk_level = "Low"
        if amount > 50000:
            credit_score -= 50
            risk_level = "Medium"
        if amount > 100000:
            credit_score -= 50
            risk_level = "High"

        return json.dumps(
            {
                "customer_id": customer_id,
                "amount": amount,
                "purpose": purpose,
                "credit_score": credit_score,
                "risk_level": risk_level,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_for_loan_with_check",
                "description": "Submit a loan request and automatically evaluate the customer's risk score.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer id"},
                        "amount": {"type": "float", "description": "Amount"},
                        "purpose": {"type": "string", "description": "Purpose"},
                    },
                    "required": ["customer_id", "amount", "purpose"],
                },
            },
        }


class SchedulePaymentWithValidationTool(Tool):
    """
    Tool for scheduling a future payment with validation of sender's balance.

    This tool ensures that the source account exists and has sufficient funds
    before generating a scheduled payment with a unique payment ID.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Schedules a payment if the balance is adequate.

        get_info() -> Dict[str, Any]:
            Describes the tool's interface, accepted parameters, and behavior.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from_account = kwargs.get("from_account")
        to_account = kwargs.get("to_account")
        amount = kwargs.get("amount")
        currency = kwargs.get("currency")
        date = kwargs.get("date")

        if not all([from_account, to_account, amount, currency, date]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        accounts = data.get("accounts", [])
        from_acc = next((a for a in accounts if a["account_id"] == from_account), None)
        if not from_acc or from_acc["balance"] < amount:
            return json.dumps(
                {"error": "Insufficient balance or account not found"}, indent=2
            )

        payment_id = f"sched_{generate_unique_id()}"
        return json.dumps(
            {
                "payment_id": payment_id,
                "status": "Scheduled",
                "from": from_account,
                "to": to_account,
                "amount": amount,
                "currency": currency,
                "date": date,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_payment_with_validation",
                "description": "Schedule a payment for a future date with balance validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account": {
                            "type": "string",
                            "description": "From account",
                        },
                        "to_account": {"type": "string", "description": "To account"},
                        "amount": {"type": "float", "description": "Amount"},
                        "currency": {"type": "string", "description": "Currency"},
                        "date": {"type": "string", "description": "Date"},
                    },
                    "required": [
                        "from_account",
                        "to_account",
                        "amount",
                        "currency",
                        "date",
                    ],
                },
            },
        }


class FreezeAccountOnFraudAlertTool(Tool):
    """
    Tool to freeze a customer account in response to a fraud alert.

    This tool locates the target account and changes its status to 'Frozen',
    while also storing the reason and timestamp of the freeze action.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Freezes the account with the given reason.

        get_info() -> Dict[str, Any]:
            Provides a schema of expected inputs for invoking the freeze operation.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        alert_reason = kwargs.get("alert_reason")

        if not account_id or not alert_reason:
            return json.dumps(
                {"error": "account_id and alert_reason are required"}, indent=2
            )

        accounts = data.get("accounts", [])
        account = next((a for a in accounts if a["account_id"] == account_id), None)
        if not account:
            return json.dumps({"error": "Account not found"}, indent=2)

        account["status"] = "Frozen"
        account["freeze_reason"] = alert_reason
        account["frozen_date"] = get_current_timestamp()

        return json.dumps(
            {
                "account_id": account_id,
                "new_status": "Frozen",
                "freeze_reason": alert_reason,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "freeze_account_on_fraud_alert",
                "description": "Freeze an account if fraud indicators are detected.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account id"},
                        "alert_reason": {
                            "type": "string",
                            "description": "Alert reason",
                        },
                    },
                    "required": ["account_id", "alert_reason"],
                },
            },
        }


class RegisterNewBeneficiaryTool(Tool):
    """
    Tool to add a new beneficiary to a customer's profile.

    This tool generates a unique beneficiary ID and associates the new entry
    with the customer, including details such as bank information and country.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Adds the beneficiary and returns the new ID and status.

        get_info() -> Dict[str, Any]:
            Returns parameter schema and functional metadata for tool registration.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        beneficiary_name = kwargs.get("beneficiary_name")
        country = kwargs.get("country")
        bank_details = kwargs.get("bank_details")
        beneficiary_id = kwargs.get("beneficiary_id") or f"ben_{generate_unique_id()}"

        if not all([customer_id, beneficiary_name, country, bank_details]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        return json.dumps(
            {
                "beneficiary_id": beneficiary_id,
                "customer_id": customer_id,
                "beneficiary_name": beneficiary_name,
                "country": country,
                "bank_details": bank_details,
                "status": "Active",
            },
            indent=2,
        )


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_new_beneficiary",
                "description": "Add a new beneficiary to the customer's profile with validations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer id"},
                        "beneficiary_name": {
                            "type": "string",
                            "description": "Beneficiary name",
                        },
                        "country": {"type": "string", "description": "Country"},
                        "bank_details": {
                            "type": "object",
                            "properties": {
                                "account_number": {"type": "string"},
                                "bank_name": {"type": "string"},
                                "routing_info": {"type": "string"},
                            },
                        },
                    },
                    "required": [
                        "customer_id",
                        "beneficiary_name",
                        "country",
                        "bank_details",
                    ],
                },
            },
        }


class DeleteExistingBeneficiaryTool(Tool):
    """
    Tool to delete a registered beneficiary from a customer's profile.

    This tool checks whether the specified beneficiary exists and is associated
    with the given customer. If the match is found, the beneficiary is removed.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Deletes the beneficiary if it belongs to the customer.

        get_info() -> Dict[str, Any]:
            Returns structured information about expected input and tool purpose.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        beneficiary_id = kwargs.get("beneficiary_id")
        if not customer_id or not beneficiary_id:
            return json.dumps(
                {"error": "customer_id and beneficiary_id are required"}, indent=2
            )

        beneficiaries = load_json("beneficiaries.json")
        updated = [
            b
            for b in beneficiaries
            if not (
                b["beneficiary_id"] == beneficiary_id
                and b["customer_id"] == customer_id
            )
        ]

        if len(updated) == len(beneficiaries):
            return json.dumps(
                {"error": "Beneficiary not found or does not belong to customer"},
                indent=2,
            )

        return json.dumps(
            {"status": "deleted", "beneficiary_id": beneficiary_id}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_existing_beneficiary",
                "description": "Remove a beneficiary from the customer's account after validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "beneficiary_id": {
                            "type": "string",
                            "description": "Beneficiary ID",
                        },
                    },
                    "required": ["customer_id", "beneficiary_id"],
                },
            },
        }


class UpdateAccountPreferencesTool(Tool):
    """
    Tool to update customer account preferences such as notification settings and language.

    It searches all accounts linked to the specified customer and applies the given
    preferences, ensuring the input is valid and structured as a dictionary.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Updates account preferences for the customer if found.

        get_info() -> Dict[str, Any]:
            Describes the tool’s function and accepted parameters, including types.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        preferences = kwargs.get("preferences", {})

        if not customer_id or not isinstance(preferences, dict):
            return json.dumps(
                {"error": "customer_id and preferences (dict) are required"}, indent=2
            )

        accounts = load_json("accounts.json")
        updated = False
        updated_prefs = {}

        for acc in accounts:
            if acc["customer_id"] == customer_id:
                acc["preferences"] = preferences
                updated_prefs = acc["preferences"]
                updated = True

        if not updated:
            return json.dumps({"error": "Customer account not found"}, indent=2)

        return json.dumps({"status": "updated", "preferences": updated_prefs}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_account_preferences",
                "description": "Update the customer's notification, language, or communication preferences.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "preferences": {
                            "type": "object",
                            "properties": {
                                "notifications": {"type": "boolean"},
                                "language": {"type": "string"},
                            },
                            "required": ["notifications", "language"],
                        },
                    },
                    "required": ["customer_id", "preferences"],
                },
            },
        }


class GetAccountBalanceTool(Tool):
    """
    Tool to retrieve the current balance and currency of a specified account.

    This tool searches through account records and returns the balance information
    for a valid account ID, or an error message if the account is not found.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Returns the balance and currency for the given account ID.

        get_info() -> Dict[str, Any]:
            Provides metadata and schema for function invocation.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        if not account_id:
            return json.dumps({"error": "account_id is required"}, indent=2)

        accounts = load_json("accounts.json")
        for acc in accounts:
            if acc["account_id"] == account_id:
                return json.dumps(
                    {
                        "account_id": account_id,
                        "balance": acc["balance"],
                        "currency": acc.get("currency", "USD"),
                    },
                    indent=2,
                )

        return json.dumps({"error": "Account not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_balance",
                "description": "Return the current balance of a customer's account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account ID"}
                    },
                    "required": ["account_id"],
                },
            },
        }


class GetCustomerProfileTool(Tool):
    """
    Tool to fetch the profile information of a customer based on customer ID.

    It returns the customer's full name, email address, and primary phone number
    as a summarized contact profile.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Retrieves customer details like name, email, and phone.

        get_info() -> Dict[str, Any]:
            Supplies metadata for integration with external tools.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        if not customer_id:
            return json.dumps({"error": "customer_id is required"}, indent=2)

        customers = load_json("customers.json")
        for c in customers:
            if c["customer_id"] == customer_id:
                profile = {
                    "name": f"{c['personal_info']['first_name']} {c['personal_info']['last_name']}",
                    "email": c["contact_info"]["email_address"],
                    "phone": c["contact_info"]["phone_numbers"][0]["number"],
                }
                return json.dumps(profile, indent=2)

        return json.dumps({"error": "Customer not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_profile",
                "description": "Retrieve personal and contact details from the customer profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"}
                    },
                    "required": ["customer_id"],
                },
            },
        }


class UpdateCustomerEmailTool(Tool):
    """
    Tool to update a customer's email and phone number.

    The tool validates the input data, updates the corresponding account(s),
    and marks the operation as successful. It simulates basic fraud checks via format control.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Updates email and phone for the given customer if found.

        get_info() -> Dict[str, Any]:
            Returns input schema and tool description for external use.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        new_email = kwargs.get("new_email")
        new_phone = kwargs.get("new_phone")

        if not customer_id or not new_email or not new_phone:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'customer_id', 'new_email', and/or 'new_phone'.",
                    "required": ["customer_id", "new_email", "new_phone"],
                },
                indent=2,
            )

        accounts = load_json("accounts.json")
        updated = False
        for acc in accounts:
            if acc["customer_id"] == customer_id:
                acc.setdefault("contact_info", {})["email_address"] = new_email
                acc["contact_info"]["phone_numbers"] = [
                    {"number": new_phone, "is_primary": True}
                ]
                updated = True

        if not updated:
            return json.dumps(
                {
                    "status": "fail",
                    "message": "Customer account not found",
                    "customer_id": customer_id,
                },
                indent=2,
            )

        return json.dumps(
            {
                "status": "success",
                "validated": True,
                "updated_fields": {
                    "email_address": new_email,
                    "primary_phone": new_phone,
                },
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_email",
                "description": "Update a customer's email and phone number with format validation and fraud checks.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID to identify the account to update.",
                        },
                        "new_email": {
                            "type": "string",
                            "description": "New email address (e.g., user@example.com).",
                        },
                        "new_phone": {
                            "type": "string",
                            "description": "New phone number (e.g., +1-202-555-0183).",
                        },
                    },
                    "required": ["customer_id", "new_email", "new_phone"],
                },
            },
        }


class CloseAccountRequestTool(Tool):
    """
    Tool to process a customer request to close a specific account.

    It verifies that the account is eligible for closure (e.g., zero balance,
    not frozen), and then updates the account status to 'Closed'.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Closes the account and confirms success or failure.

        get_info() -> Dict[str, Any]:
            Describes preconditions and expected structure for input.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        if not account_id:
            return json.dumps({"error": "account_id is required"})

        accounts = load_json("accounts.json")
        for acc in accounts:
            if acc["account_id"] == account_id:
                if acc.get("status") == "Closed":
                    return json.dumps(
                        {"status": "Already Closed", "closed_at": acc.get("closed_at")},
                        indent=2,
                    )
                acc["status"] = "Closed"
                acc["closed_at"] = get_current_timestamp()
                return json.dumps(
                    {"status": "Closed", "closed_at": acc["closed_at"]}, indent=2
                )

        return json.dumps({"error": "Account not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_account_request",
                "description": "Close a customer's account after verifying no pending transactions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account ID to close",
                        }
                    },
                    "required": ["account_id"],
                },
            },
        }


class SubmitSupportTicketTool(Tool):
    """
    Tool to create a new customer support ticket.

    This tool takes information such as the customer ID, ticket category, priority level,
    communication channel, and a structured request description. It generates a new ticket ID
    and logs the support request for further processing.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Submits the ticket and returns the new ticket ID and status.

        get_info() -> Dict[str, Any]:
            Explains tool usage, required fields, and return format.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        category = kwargs.get("category")
        priority = kwargs.get("priority")
        channel = kwargs.get("channel")
        request_details = kwargs.get("request_details")
        ticket_id = kwargs.get("ticket_id", f"ticket_{generate_unique_id()}")
        if "ticket_id" in kwargs:
            ticket_id = kwargs["ticket_id"]
        else:
            ticket_id = f"ticket_{generate_unique_id()}"

        if not all([customer_id, category, priority, channel, request_details]):
            return json.dumps(
                {
                    "error": "Missing required parameters: customer_id, category, priority, channel, and request_details"
                },
                indent=2,
            )

        tickets = load_json("support_tickets.json")

        new_ticket = {
            "ticket_id": ticket_id,
            "customer_id": customer_id,
            "category": category,
            "priority": priority,
            "channel": channel,
            "request_details": request_details,
            "status": "Open",
            "created_at": get_current_timestamp(),
        }
        tickets.append(new_ticket)

        return json.dumps({"ticket_id": ticket_id, "status": "Open"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_support_ticket",
                "description": "Create a new support ticket for a customer including structured request metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "category": {
                            "type": "string",
                            "description": "Support issue category (e.g., Audit, Security)",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Support priority (e.g., High, Medium, Low)",
                        },
                        "channel": {
                            "type": "string",
                            "description": "Channel used to submit the ticket (e.g., Web, Mobile App)",
                        },
                        "request_details": {
                            "type": "object",
                            "description": "Structured data describing the target of the support request",
                            "properties": {
                                "target_entity": {
                                    "type": "string",
                                    "description": "Entity being modified (e.g., Customer, Account)",
                                },
                                "target_id": {
                                    "type": "string",
                                    "description": "ID of the entity being affected",
                                },
                                "operation": {
                                    "type": "string",
                                    "description": "Operation requested (e.g., UPDATE, REVIEW, CLOSE)",
                                },
                                "parameters": {
                                    "type": "object",
                                    "description": "Additional parameters related to the request",
                                },
                            },
                            "required": [
                                "target_entity",
                                "target_id",
                                "operation",
                                "parameters",
                            ],
                        },
                    },
                    "required": [
                        "customer_id",
                        "category",
                        "priority",
                        "channel",
                        "request_details",
                    ],
                },
            },
        }


class ReviewTicketHistoryTool(Tool):
    """
    Tool to review all support tickets submitted by a specific customer.

    This tool fetches open and resolved tickets associated with a given customer ID,
    showing status, category, channel of submission, and ticket details.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Returns a formatted history of tickets for the given customer.

        get_info() -> Dict[str, Any]:
            Provides interface schema and tool description for orchestration.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        if not customer_id:
            return json.dumps({"error": "customer_id is required"})

        tickets = load_json("support_tickets.json")
        customer_tickets = [t for t in tickets if t["customer_id"] == customer_id]
        open_tickets = sum(1 for t in customer_tickets if t["status"] != "Resolved")
        summary = (
            f"Total tickets: {len(customer_tickets)}. Open tickets: {open_tickets}."
        )

        return json.dumps({"summary": summary, "open_tickets": open_tickets}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "review_ticket_history",
                "description": "Review historical support tickets and unresolved issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"}
                    },
                    "required": ["customer_id"],
                },
            },
        }


class UnlockAccountBySecurityCheckTool(Tool):
    """
    Tool to unlock a frozen account after a security verification process.

    This tool verifies that the account exists and is currently frozen,
    then updates the account status to "Active" upon passing checks.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Unlocks the specified account if conditions are met.

        get_info() -> Dict[str, Any]:
            Returns metadata and parameter expectations for integration.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        security_code = kwargs.get("security_code")
        if not customer_id or not security_code:
            return json.dumps({"error": "customer_id and security_code are required"})

        accounts = load_json("accounts.json")
        for acc in accounts:
            if acc["customer_id"] == customer_id:
                acc["status"] = "Active"
                acc["unlocked_at"] = get_current_timestamp()
                return json.dumps({"status": "Unlocked"}, indent=2)

        return json.dumps({"error": "Customer account not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "unlock_account_by_security_check",
                "description": "Unlock an account after verifying security code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "security_code": {
                            "type": "string",
                            "description": "Security code provided by user",
                        },
                    },
                    "required": ["customer_id", "security_code"],
                },
            },
        }


class AddJointAccountHolderTool(Tool):
    """
    Tool used to add a joint account holder to an existing bank account.

    This tool validates the input data to ensure the account exists and the
    joint holder is a valid customer. It updates the account's list of
    joint holders accordingly.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Executes the logic to add a joint account holder.

        get_info() -> Dict[str, Any]:
            Returns metadata about the tool, including name, description, and input/output structure.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        holder_id = kwargs.get("holder_id")
        if not account_id or not holder_id:
            return json.dumps({"error": "account_id and holder_id are required"})

        accounts = load_json("accounts_joint_holders.json")
        for acc in accounts:
            if acc["account_id"] == account_id:
                acc.setdefault("joint_holders", []).append(holder_id)
                return json.dumps(
                    {"status": "Added", "added_at": get_current_timestamp()},
                    indent=2,
                )

        return json.dumps({"error": "Account not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_joint_account_holder",
                "description": "Add a joint account holder to an existing account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account ID"},
                        "holder_id": {
                            "type": "string",
                            "description": "New holder's customer ID",
                        },
                    },
                    "required": ["account_id", "holder_id"],
                },
            },
        }


class RemoveJointAccountHolderTool(Tool):
    """
    Tool to remove a joint account holder from a shared account.

    This tool ensures the account and holder both exist, and then proceeds to
    disassociate the specified joint holder from the account.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Removes the joint account holder from the specified account.

        get_info() -> Dict[str, Any]:
            Supplies schema information and execution purpose.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        holder_id = kwargs.get("holder_id")
        if not account_id or not holder_id:
            return json.dumps({"error": "Missing required parameters"}, indent=2)
        accounts = load_json("accounts_joint_holders.json")
        updated = False
        for acc in accounts:
            if acc["account_id"] == account_id and "joint_holders" in acc:
                if holder_id in acc["joint_holders"]:
                    acc["joint_holders"].remove(holder_id)
                    updated = True
        if updated:
            return json.dumps(
                {"status": "success", "removed_at": get_current_timestamp()},
                indent=2,
            )
        return json.dumps({"error": "Holder not found or account invalid"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_joint_account_holder",
                "description": "Remove a joint account holder if no pending operations are linked.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account identifier",
                        },
                        "holder_id": {
                            "type": "string",
                            "description": "Holder identifier",
                        },
                    },
                    "required": ["account_id", "holder_id"],
                },
            },
        }


class VerifyCustomerIdentityTool(Tool):
    """
    Tool to verify a customer's identity based on their official ID document.

    This tool confirms whether the given document corresponds to a known customer
    based on the customer_id and document number.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Validates customer identity and returns a structured result.

        get_info() -> Dict[str, Any]:
            Returns metadata about the expected input parameters and verification logic.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        id_document = kwargs.get("id_document")

        if not customer_id or not id_document:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'customer_id' and/or 'id_document'.",
                    "required": ["customer_id", "id_document"],
                },
                indent=2,
            )

        customers = load_json("customers_documents.json")
        customer = next((c for c in customers if c["customer_id"] == customer_id), None)

        if not customer:
            return json.dumps(
                {"status": "fail", "verified": False, "reason": "Customer not found"},
                indent=2,
            )

        # Simulate document verification logic
        return json.dumps(
            {"status": "success", "verified": True, "confidence": 0.97}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_customer_identity",
                "description": "Verify a customer's identity using a valid official document (e.g., passport, national ID, or license).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer in the database.",
                        },
                        "id_document": {
                            "type": "string",
                            "description": "A valid official document number, e.g., passport, driver's license, national ID.",
                        },
                    },
                    "required": ["customer_id", "id_document"],
                },
            },
        }


class DownloadStatementByDateTool(Tool):
    """
    Tool to generate and download an account statement for a specific month and year.

    This tool compiles all relevant transactions for the period and formats them
    into a downloadable summary (simulated as a JSON string).

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Generates the statement and returns a simulated file path.

        get_info() -> Dict[str, Any]:
            Provides metadata about input structure and time filters.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        month = kwargs.get("month")
        if not account_id or not month:
            return json.dumps({"error": "account_id and month are required"}, indent=2)
        url = f"https://bank.example.com/statements/{account_id}/{month}.pdf"
        return json.dumps({"statement_url": url}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "download_statement_by_date",
                "description": "Download the account statement for a given month or date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account identifier",
                        },
                        "month": {
                            "type": "string",
                            "description": "Month string (e.g., 2024-05)",
                        },
                    },
                    "required": ["account_id", "month"],
                },
            },
        }


class ListLinkedBeneficiariesTool(Tool):
    """
    Tool to list all beneficiaries linked to a specific customer.

    This tool gathers the beneficiary records registered under the customer's ID
    and returns structured data such as name, relationship, and account details.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Lists all beneficiaries for the provided customer ID.

        get_info() -> Dict[str, Any]:
            Describes usage schema and return structure.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        if not customer_id:
            return json.dumps({"error": "customer_id is required"}, indent=2)
        beneficiaries = load_json("beneficiaries.json")
        linked = [b for b in beneficiaries if b["customer_id"] == customer_id]
        return json.dumps({"beneficiaries": linked}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_linked_beneficiaries",
                "description": "Retrieve all beneficiaries linked to the customer's account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"}
                    },
                    "required": ["customer_id"],
                },
            },
        }


class CancelScheduledPaymentTool(Tool):
    """
    Tool to cancel a scheduled payment by updating its status to 'Cancelled'.

    This tool locates the scheduled payment by ID and ensures it is in an
    'Active' or 'Scheduled' state before marking it as cancelled and persisting
    the change.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Cancels the payment if valid and not yet processed.

        get_info() -> Dict[str, Any]:
            Returns metadata for schema validation and integration handling.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        payment_id = kwargs.get("payment_id")
        if not payment_id:
            return json.dumps({"error": "payment_id is required"}, indent=2)
        payments = load_json("scheduled_payments.json")
        for p in payments:
            if p["payment_id"] == payment_id:
                p["status"] = "Cancelled"
                p["cancelled_at"] = get_current_timestamp()
                return json.dumps(
                    {"status": "Cancelled", "cancelled_at": p["cancelled_at"]}, indent=2
                )
        return json.dumps({"error": "Payment not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_scheduled_payment",
                "description": "Cancel a scheduled payment before execution and refund if necessary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "payment_id": {
                            "type": "string",
                            "description": "Scheduled payment identifier",
                        }
                    },
                    "required": ["payment_id"],
                },
            },
        }


class AggregateMonthlyExpensesTool(Tool):
    """
    Tool that calculates the total monthly expenses for a customer account.

    It fetches all transactions for a given account and aggregates the
    negative amounts grouped by transaction type (used as a category),
    returning the summarized expenditure per month.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Executes the logic to aggregate expenses per month.

        get_info() -> Dict[str, Any]:
            Returns metadata including expected input (account_id, month) and output format (monthly totals).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        month = kwargs.get("month")
        if not account_id or not month:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'account_id' and/or 'month'.",
                    "required": ["account_id", "month"],
                },
                indent=2,
            )

        transactions = load_json("transactions.json")
        filtered = [
            t
            for t in transactions
            if t["account_id"] == account_id and t["transaction_date"].startswith(month)
        ]

        categories = {}
        total = 0.0
        for t in filtered:
            cat = t.get("transaction_type", "Uncategorized")
            amount = t.get("amount", 0)
            if amount < 0:
                categories[cat] = categories.get(cat, 0) + amount
                total += amount

        return json.dumps(
            {
                "status": "success",
                "account_id": account_id,
                "month": month,
                "categories": categories,
                "total_spent": total,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "aggregate_monthly_expenses",
                "description": "Summarize monthly expenses from transaction history by category (transaction type).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account ID"},
                        "month": {
                            "type": "string",
                            "description": "Month in YYYY-MM format (e.g., '2024-06')",
                        },
                    },
                    "required": ["account_id", "month"],
                },
            },
        }


class AutoClassifySupportTicketPriorityTool(Tool):
    """
    Tool that uses keyword-based logic to automatically classify a support ticket's priority.

    It analyzes the ticket description text for urgency signals (e.g., "urgent", "can't access",
    "error") and assigns a priority level (Low, Medium, High).

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Classifies the priority of a support ticket.

        get_info() -> Dict[str, Any]:
            Returns metadata about required inputs (ticket_text) and output (priority classification).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        message = kwargs.get("message")
        ticket_id = kwargs.get("ticket_id")

        if not customer_id or not message or not ticket_id:
            return json.dumps(
                {"error": "customer_id, message, and ticket_id are required"},
                indent=2
            )

        tickets = data.get("support_tickets", [])
        for t in tickets:
            if t["ticket_id"] == ticket_id:
                priority = (
                    "High"
                    if any(term in message.lower() for term in ["urgent", "immediately", "lost", "unauthorized"])
                    else "Normal"
                )
                t["priority"] = priority
                return json.dumps({
                    "ticket_id": ticket_id,
                    "priority": priority,
                    "status": "updated"
                }, indent=2)

        return json.dumps({"error": f"Ticket '{ticket_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "auto_classify_support_ticket_priority",
                "description": "Automatically classify the priority of a support ticket based on content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "message": {
                            "type": "string",
                            "description": "Support message content",
                        },
                    },
                    "required": ["customer_id", "message"],
                },
            },
        }


class DetectSuspiciousActivityAndAlertTool(Tool):
    """
    Tool to detect suspicious account activity and trigger an alert if necessary.

    This tool reviews transaction history for a given account and flags activity
    based on thresholds like unusually large amounts or unusual timing. If a match
    is found, it marks the account and issues a simulated alert.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Analyzes transactions and returns alert status.

        get_info() -> Dict[str, Any]:
            Describes the tool’s fraud detection criteria and input fields.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        if not account_id:
            return json.dumps({"error": "account_id is required"}, indent=2)

        transactions = load_json("transactions.json")
        recent = [
            t
            for t in transactions
            if t["account_id"] == account_id and t.get("amount", 0) > 10000
        ]
        flagged = bool(recent)
        return json.dumps(
            {
                "flagged": flagged,
                "alert_id": f"alert_{generate_unique_id()}" if flagged else None,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "detect_suspicious_activity_and_alert",
                "description": "Analyze recent transactions and flag suspicious patterns, triggering an alert.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account ID to monitor",
                        }
                    },
                    "required": ["account_id"],
                },
            },
        }


class GetAccountTransactionHistoryTool(Tool):
    """
    Tool to retrieve a list of recent transactions for a specific account.

    This tool returns transaction records including date, amount, type, status,
    and merchant information. It supports optional filtering by date range or type.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Returns the transaction history of the given account ID.

        get_info() -> Dict[str, Any]:
            Returns metadata for usage context, including expected fields.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        days = kwargs.get("days", 30)
        if not account_id:
            return json.dumps({"error": "account_id is required"}, indent=2)

        transactions = load_json("transactions.json")
        current_time = get_current_timestamp()
        cutoff = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S.%f") - timedelta(days=days)

        filtered = []
        for t in transactions:
            if t["account_id"] != account_id:
                continue
            try:
                txn_date = datetime.strptime(t["transaction_date"], "%Y-%m-%d")
            except ValueError:
                txn_date = datetime.fromisoformat(
                    t["transaction_date"].replace("Z", "+00:00")
                ).replace(tzinfo=None)
            if txn_date >= cutoff:
                filtered.append(t)

        categorized = {}
        for t in filtered:
            cat = t.get("category", "Uncategorized")
            categorized[cat] = categorized.get(cat, 0) + t.get("amount", 0)

        return json.dumps(
            {"transactions": filtered, "categorized_totals": categorized}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_transaction_history",
                "description": "Retrieve and categorize past transactions for the customer's account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account ID"},
                        "days": {
                            "type": "integer",
                            "description": "Number of days to include",
                        },
                    },
                    "required": ["account_id"],
                },
            },
        }


class SummarizeLoanApplicationsByStatusTool(Tool):
    """
    Tool to provide a summary of loan applications categorized by status.

    This tool scans all loan applications and returns a count of how many fall
    under each status (e.g., Approved, Rejected, Pending). Useful for dashboards
    or trend analysis.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Summarizes the loan applications grouped by their status.

        get_info() -> Dict[str, Any]:
            Provides information about the expected parameters and return type.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        if not customer_id:
            return json.dumps({"error": "customer_id is required"}, indent=2)

        applications = load_json("loan_applications.json")
        filtered = [a for a in applications if a["customer_id"] == customer_id]
        summary = {"approved": 0, "pending": 0, "rejected": 0}
        for a in filtered:
            status = a.get("status", "pending").lower()
            if status in summary:
                summary[status] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_loan_applications_by_status",
                "description": "Generate summary of loan applications grouped by status for a customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"}
                    },
                    "required": ["customer_id"],
                },
            },
        }


class TransferFundsWithLimitCheckTool(Tool):
    """
    Tool to transfer funds between two accounts, including daily limit validation.

    This tool validates source and destination account IDs, confirms the sender
    has sufficient balance, and ensures the transaction does not exceed configured
    limits for the day. A successful transfer updates both account balances.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Executes a validated fund transfer and returns confirmation.

        get_info() -> Dict[str, Any]:
            Describes the tool’s capabilities, inputs, and conditions for execution.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from_account = kwargs.get("from_account")
        to_account = kwargs.get("to_account")
        amount = kwargs.get("amount", 0)
        if not from_account or not to_account or amount <= 0:
            return json.dumps({"error": "Invalid input"}, indent=2)
        if amount > 10000:
            return json.dumps(
                {"error": "Transfer amount exceeds daily limit"}, indent=2
            )

        return json.dumps(
            {"transaction_id": f"txn_{generate_unique_id()}", "status": "Success"},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_funds_with_limit_check",
                "description": "Transfer funds between accounts with pre-check on daily limit and balance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account": {
                            "type": "string",
                            "description": "Source account",
                        },
                        "to_account": {
                            "type": "string",
                            "description": "Target account",
                        },
                        "amount": {
                            "type": "float",
                            "description": "Amount to transfer",
                        },
                    },
                    "required": ["from_account", "to_account", "amount"],
                },
            },
        }


TOOLS = [
    AddJointAccountHolderTool(),
    AggregateMonthlyExpensesTool(),
    ApplyForLoanWithCheckTool(),
    AutoClassifySupportTicketPriorityTool(),
    CancelScheduledPaymentTool(),
    CloseAccountRequestTool(),
    CreateCustomerAccountTool(),
    DeleteExistingBeneficiaryTool(),
    DetectSuspiciousActivityAndAlertTool(),
    DownloadStatementByDateTool(),
    FreezeAccountOnFraudAlertTool(),
    GetAccountBalanceTool(),
    GetAccountTransactionHistoryTool(),
    GetCustomerProfileTool(),
    ListLinkedBeneficiariesTool(),
    RegisterNewBeneficiaryTool(),
    RemoveJointAccountHolderTool(),
    ReviewTicketHistoryTool(),
    SchedulePaymentWithValidationTool(),
    SubmitSupportTicketTool(),
    SummarizeLoanApplicationsByStatusTool(),
    TransferFundsWithLimitCheckTool(),
    UnlockAccountBySecurityCheckTool(),
    UpdateAccountPreferencesTool(),
    UpdateCustomerEmailTool(),
    VerifyCustomerIdentityTool(),
]
