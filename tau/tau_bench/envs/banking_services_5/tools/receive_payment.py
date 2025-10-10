# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReceivePayment(Tool):
    """Credits a specified amount into the given account for a customer."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        account_id = kwargs.get("account_id")
        amount = kwargs.get("amount")
        currency = kwargs.get("currency")

        if not all([customer_id, account_id, amount, currency]):
            return json.dumps(
                {"error": "customer_id, account_id, amount, and currency are required."},
                indent=2
            )

        # Find account and verify ownership
        account = next(
            (a for a in list(data.get("accounts", {}).values())
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
                "name": "receive_payment",
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
