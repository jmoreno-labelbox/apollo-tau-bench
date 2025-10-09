from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
            (a for a in data.get("accounts", {}).values()
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
