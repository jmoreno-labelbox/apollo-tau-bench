from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class CloseActiveAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        updated = False
        for a in accounts:
            if a['account_id'] == account_id and a.get('status') == 'Active':
                if 'status' not in a:
                    return json.dumps({'error': 'Account closure not supported: no status field in data.'})
                a['status'] = 'Inactive'
                updated = True
        if not updated:
            return json.dumps({'error': 'Account not found or not eligible for closure.'})
        return json.dumps({'success': True, 'account_id': account_id})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'closeActiveAccount',
                'description': 'Sets an active account status to inactive (only if status field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }
