# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReviewOverdraftActivityAndAdjustLimit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get('account_id')
        new_limit = kwargs.get('new_limit')
        if not account_id or new_limit is None:
            return json.dumps({'error': 'account_id and new_limit are required'})
        accounts = load_json('accounts.json')
        account = next((a for a in accounts if a['account_id'] == account_id and a['account_type'] == 'Checking'), None)
        if not account or 'overdraft_limit' not in account:
            return json.dumps({'error': 'Account not found or overdraft_limit field missing.'})
        account['overdraft_limit'] = new_limit
        return json.dumps({'success': True, 'account_id': account_id, 'new_overdraft_limit': new_limit})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'review_overdraft_activity_and_adjust_limit',
                'description': 'Adjusts overdraft limit based on recent usage and account behavior (only if overdraft_limit field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Checking Account ID'},
                        'new_limit': {'type': 'number', 'description': 'New overdraft limit'}
                    },
                    'required': ['account_id', 'new_limit']
                }
            }
        }
