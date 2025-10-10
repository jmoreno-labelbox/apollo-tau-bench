# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeactivateAccountByRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get('account_id')
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        updated = False
        for a in accounts:
            if a['account_id'] == account_id:
                if 'status' not in a:
                    return json.dumps({'error': 'Account deactivation not supported: no status field in data.'})
                a['status'] = 'Inactive'
                updated = True
        if not updated:
            return json.dumps({'error': 'Account not found or deactivation not supported.'})
        return json.dumps({'success': True, 'account_id': account_id, 'new_status': 'Inactive'})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'deactivate_account_by_request',
                'description': 'Sets account status to "Inactive" for the specified account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }
