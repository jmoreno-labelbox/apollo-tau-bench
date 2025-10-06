from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

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
    def invoke(
        data: Dict[str, Any],
        account_type: str = None,
        currency: str = None,
        customer_id: str = None,
        initial_limit: int = 0
    ) -> str:
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
                "name": "CreateCustomerAccount",
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
                            "type": "number",
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
