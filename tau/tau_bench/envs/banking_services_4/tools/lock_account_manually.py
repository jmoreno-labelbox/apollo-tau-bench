from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class LockAccountManually(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        account = next((a for a in accounts.values() if a['account_id'] == account_id), None)
        if not account or 'status' not in account:
            return json.dumps({'error': 'Account not found or missing status field.'})
        if account['status'] == 'Locked':
            return json.dumps({'success': False, 'account_id': account_id, 'locked': True, 'note': 'Account is already locked.'})
        account['status'] = 'Locked'
        return json.dumps({'success': True, 'account_id': account_id, 'locked': True})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'lockAccountManually',
                'description': 'Manually locks an account by setting its status to "Locked".',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }
