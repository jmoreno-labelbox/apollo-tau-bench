from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
from . import load_json

class GetAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})

        accounts = load_json('accounts.json')
        account = next((a for a in accounts.values() if a['account_id'] == account_id), None)

        if not account or 'balance' not in account or 'currency' not in account:
            return json.dumps({'error': 'Account not found or missing balance/currency field.'})

        return json.dumps({
            'account_id': account_id,
            'balance': account['balance'],
            'currency': account['currency']
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getAccountBalance',
                'description': 'Fetches the current balance and currency of a given account ID.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {
                            'type': 'string',
                            'description': 'The ID of the account whose balance is requested.'
                        }
                    },
                    'required': ['account_id']
                }
            }
        }
