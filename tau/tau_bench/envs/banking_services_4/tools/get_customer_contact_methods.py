from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class GetCustomerContactMethods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})
        customers = load_json('customers.json')
        customer = next((c for c in customers.values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({'error': 'Customer not found'})
        contact_info = customer.get('contact_info', {}).values()
        preferences = customer.get('preferences', {}).values()
        result = {
            'email_address': contact_info.get('email_address'),
            'phone_numbers': contact_info.get('phone_numbers'),
            'communication_channel': preferences.get('communication_channel')
        }
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getCustomerContactMethods',
                'description': 'Returns current contact preferences and phone/email on file.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'}
                    },
                    'required': ['customer_id']
                }
            }
        }
