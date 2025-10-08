from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

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
