# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewTransaction(Tool):
    """Adds a new transaction to the transactions database and updates the account balance if sufficient funds are available."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id", "").strip()
        transaction_date = date.today()
        amount = kwargs.get("amount")
        currency =  kwargs.get("currency")
        purchase_type = kwargs.get("purchase_type", "").strip()
        description = kwargs.get("description", "").strip()
        merchant_name = kwargs.get("merchant_name", "").strip()
        channel = kwargs.get("channel", "").strip()

        if not all([account_id, transaction_date, amount, currency, purchase_type, description, merchant_name, channel]):
            return json.dumps({"error": "All fields are required."}, indent=2)

        accounts = list(data.get("accounts", {}).values())
        account = next((acc for acc in accounts if acc.get("account_id") == account_id), None)

        if not account:
            return json.dumps({"error": "Account not found."}, indent=2)

        currency = kwargs.get("currency", "").strip()
        transaction_status = "Completed" if account["balance"] >= amount else "Pending"

        # Subtract the amount from the account if there are enough funds.
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
                "name": "create_new_transaction",
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
