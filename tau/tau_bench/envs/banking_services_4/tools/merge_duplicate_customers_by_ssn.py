from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
from . import load_json

class MergeDuplicateCustomersBySSN(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ssn_last_4: str = None) -> str:
        if not ssn_last_4:
            return json.dumps({'error': 'ssn_last_4 is required'})
        customers = load_json('customers.json')
        matches = [c for c in customers.values() if c.get('personal_info', {}).values().get('ssn_last_4') == ssn_last_4]
        if len(matches) < 2:
            return json.dumps({'error': 'Less than two customers with this SSN'})
        # Merge only if all fields required for merging are present.
        for c in matches:
            if 'account_ids' not in c:
                return json.dumps({'error': 'Customer merge not supported: account_ids field missing in one or more records.'})
        canonical = matches[0]
        merged_ids = [c['customer_id'] for c in matches[1:]]
        for c in matches[1:]:
            canonical['account_ids'] = list(set(canonical.get('account_ids', []) + c.get('account_ids', [])))
            customers.remove(c)
        return json.dumps({'success': True, 'canonical_customer_id': canonical['customer_id'], 'merged_customer_ids': merged_ids})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'mergeDuplicateCustomersBySsn',
                'description': 'Merges two customer records with same SSN into a single canonical one (only if account_ids field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'ssn_last_4': {'type': 'string', 'description': 'Last 4 digits of SSN'}
                    },
                    'required': ['ssn_last_4']
                }
            }
        }
