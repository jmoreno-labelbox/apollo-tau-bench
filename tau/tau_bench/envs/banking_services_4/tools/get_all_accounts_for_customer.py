# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllAccountsForCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        if not customer_id:
            return json.dumps({"error": "customer_id is required"})

        accounts = load_json("accounts.json")
        customer_accounts = [
            account for account in accounts if account.get("customer_id") == customer_id
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
                'name': 'get_all_accounts_for_customer',
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
