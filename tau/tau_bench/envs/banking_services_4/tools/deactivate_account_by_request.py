from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
def _convert_db_to_list(db_data: Any) -> List[Dict]:
    """Convert database data to list of dicts"""
    if isinstance(db_data, list):
        return db_data
    elif isinstance(db_data, dict):
        return [db_data]
    else:
        return []

class DeactivateAccountByRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        accounts = _convert_db_to_list(accounts)
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
                'name': 'deactivateAccountByRequest',
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