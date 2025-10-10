# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import get_current_timestamp
from . import generate_unique_id


class TransferFundsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from_account_id = kwargs.get('from_account_id')
        to_account_id = kwargs.get('to_account_id')
        amount = kwargs.get('amount')
        description = kwargs.get('description', 'Internal transfer')

        accounts = list(data.get('accounts', {}).values())
        transactions = list(data.get('transactions', {}).values())

        from_account = None
        to_account = None

        for account in accounts:
            if account['account_id'] == from_account_id:
                from_account = account
            elif account['account_id'] == to_account_id:
                to_account = account

        if not from_account or not to_account:
            return json.dumps({"error": "Account not found"}, indent=2)

        if from_account['balance'] < amount:
            return json.dumps({"error": "Insufficient funds"}, indent=2)

        from_account['balance'] -= amount
        to_account['balance'] += amount

        debit_transaction = {
            "transaction_id": f"txn_{generate_unique_id()}",
            "account_id": from_account_id,
            "transaction_date": get_current_timestamp(),
            "amount": -amount,
            "currency": "USD",
            "transaction_type": "Transfer",
            "description": f"Transfer to {to_account_id}: {description}",
            "status": "Completed",
            "channel": "Online"
        }

        credit_transaction = {
            "transaction_id": f"txn_{generate_unique_id()}",
            "account_id": to_account_id,
            "transaction_date": get_current_timestamp(),
            "amount": amount,
            "currency": "USD",
            "transaction_type": "Transfer",
            "description": f"Transfer from {from_account_id}: {description}",
            "status": "Completed",
            "channel": "Online"
        }

        transactions.append(debit_transaction)
        transactions.append(credit_transaction)

        return json.dumps({
            "success": True,
            "transfer_amount": amount,
            "from_account_new_balance": from_account['balance'],
            "to_account_new_balance": to_account['balance'],
            "debit_transaction_id": debit_transaction['transaction_id'],
            "credit_transaction_id": credit_transaction['transaction_id']
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_funds",
                "description": "Transfer funds between two accounts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account_id": {"type": "string", "description": "Source account ID"},
                        "to_account_id": {"type": "string", "description": "Destination account ID"},
                        "amount": {"type": "number", "description": "Amount to transfer"},
                        "description": {"type": "string", "description": "Transfer description"}
                    },
                    "required": ["from_account_id", "to_account_id", "amount"]
                }
            }
        }
