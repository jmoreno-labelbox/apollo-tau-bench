# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountOverdraftLimit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get('account_id')
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        account = next((a for a in accounts if a['account_id'] == account_id), None)
        if not account:
            return json.dumps({'error': 'Account not found.'})
        if account.get('account_type') != 'Checking':
            return json.dumps({'error': 'Overdraft limit is only applicable to Checking accounts.'})

        limit = account.get('overdraft_limit')
        if limit is None:
            return json.dumps({'error': 'Overdraft limit field not found for this account.'})

        return json.dumps({'account_id': account_id, 'overdraft_limit': limit}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_account_overdraft_limit',
                'description': 'Retrieves the current overdraft limit for a specified checking account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'The ID of the checking account.'}
                    },
                    'required': ['account_id']
                }
            }
        }
