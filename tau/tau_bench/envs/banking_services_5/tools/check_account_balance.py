# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckAccountBalance(Tool):
    """Returns the current balance for a customer’s account, and optionally validates against a requested amount."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id     = kwargs.get("customer_id")
        account_id      = kwargs.get("account_id")
        requested_amount = kwargs.get("requested_amount", 0.0)

        if not customer_id or not account_id:
            return json.dumps(
                {"error": "customer_id and account_id are required."},
                indent=2
            )

        # find the account and verify ownership
        acct = next(
            (a for a in list(data.get("accounts", {}).values())
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
                "name": "check_account_balance",
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
