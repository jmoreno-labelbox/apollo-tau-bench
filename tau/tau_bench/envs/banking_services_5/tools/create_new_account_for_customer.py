# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewAccountForCustomer(Tool):
    """Creates a new account for a customer using account type and returns the full account object."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        account_type = kwargs.get("account_type", "").strip()
        account_type_code = kwargs.get("account_type_code", "").strip()

        currency = kwargs.get("currency", "USD")

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
