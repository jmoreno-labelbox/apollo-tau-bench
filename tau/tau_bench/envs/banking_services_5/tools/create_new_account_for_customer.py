# Copyright Sierra

import calendar
from datetime import datetime
import random
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool

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



class CreateNewAccountForCustomer(Tool):
    """Creates a new account for a customer using account type and returns the full account object."""

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, account_type = "", account_type_code = "", currency = "USD") -> str:
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

        # Fields that are not mandatory
        if account_type == "Checking":
            new_account["overdraft_limit"] = 500.0
        elif account_type == "Savings":
            new_account["interest_rate"] = 0.02
        elif account_type == "Credit Card":
            new_account["credit_limit"] = 10000.0
            new_account["rewards_points"] = 0

        # Insert into database
        data.setdefault("accounts", []).append(new_account)

        # append to the customer's account_ids
        customers = list(data.get("customers", {}).values())
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
                "name": "create_new_account_for_customer",
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
