from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
from . import load_json

class ReviewOverdraftActivityAndAdjustLimit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, new_limit: int = None) -> str:
        if not account_id or new_limit is None:
            return json.dumps({'error': 'account_id and new_limit are required'})
        accounts = load_json('accounts.json')
        account = next((a for a in accounts.values() if a['account_id'] == account_id and a['account_type'] == 'Checking'), None)
        if not account or 'overdraft_limit' not in account:
            return json.dumps({'error': 'Account not found or overdraft_limit field missing.'})
        account['overdraft_limit'] = new_limit
        return json.dumps({'success': True, 'account_id': account_id, 'new_overdraft_limit': new_limit})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'reviewOverdraftActivityAndAdjustLimit',
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
