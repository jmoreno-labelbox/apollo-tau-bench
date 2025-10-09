from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class GetAllAccountsForCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required"})

        accounts = load_json("accounts.json")
        customer_accounts = [
            account for account in accounts.values() if account.get("customer_id") == customer_id
        ]

        return json.dumps({
            "customer_id": customer_id,
            "accounts": [
                {
                    "account_id": acct.get("account_id"),
                    "account_type": acct.get("account_type"),
                    "currency": acct.get("currency"),
                    "balance": acct.get("balance")
                }
                for acct in customer_accounts
            ]
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getAllAccountsForCustomer',
                'description': 'Retrieves all accounts (with type, currency, and balance) associated with a given customer ID.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {
                            'type': 'string',
                            'description': 'The ID of the customer whose accounts should be fetched.'
                        }
                    },
                    'required': ['customer_id']
                }
            }
        }
