from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class AddEmployerToCustomerProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, employer: str = None) -> str:
        if not customer_id or not employer:
            return json.dumps({'error': 'customer_id and employer are required'})
        customers = load_json('customers.json')
        updated = False
        for c in customers:
            if c['customer_id'] == customer_id:
                if 'personal_info' not in c or 'employer' not in c['personal_info']:
                    return json.dumps({'error': 'Employer update not supported: employer field missing in data.'})
                c['personal_info']['employer'] = employer
                updated = True
        if not updated:
            return json.dumps({'error': 'Customer not found or employer update not supported.'})
        return json.dumps({'success': True, 'customer_id': customer_id, 'employer': employer})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'addEmployerToCustomerProfile',
                'description': 'Updates the employer field for an existing customer (only if employer field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'employer': {'type': 'string', 'description': 'Employer name'}
                    },
                    'required': ['customer_id', 'employer']
                }
            }
        }
