# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergeDuplicateCustomersBySSN(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ssn_last_4 = kwargs.get('ssn_last_4')
        if not ssn_last_4:
            return json.dumps({'error': 'ssn_last_4 is required'})
        customers = load_json('customers.json')
        matches = [c for c in customers if c.get('personal_info', {}).get('ssn_last_4') == ssn_last_4]
        if len(matches) < 2:
            return json.dumps({'error': 'Less than two customers with this SSN'})
        # Only merge if all fields to be merged exist
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
                'name': 'merge_duplicate_customers_by_ssn',
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
