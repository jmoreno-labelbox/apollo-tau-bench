from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

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
