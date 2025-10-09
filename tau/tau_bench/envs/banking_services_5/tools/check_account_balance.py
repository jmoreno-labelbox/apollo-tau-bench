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
        return list(db.values())
    return db

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
