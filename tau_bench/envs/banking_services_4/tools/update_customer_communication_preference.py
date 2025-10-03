from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class UpdateCustomerCommunicationPreference(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, new_channel: str = None) -> str:
        if not customer_id or not new_channel:
            return json.dumps({'error': 'customer_id and new_channel are required'})

        customers = load_json('customers.json')
        customer = next((c for c in customers if c['customer_id'] == customer_id), None)

        if not customer:
            return json.dumps({'error': 'Customer not found.'})

        preferences = customer.get('preferences', {})
        if 'communication_channel' not in preferences:
            return json.dumps({'error': 'Communication channel preference not found for this customer.'})

        preferences['communication_channel'] = new_channel

        return json.dumps({'success': True, 'customer_id': customer_id, 'new_communication_channel': new_channel})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'updateCustomerCommunicationPreference',
                'description': 'Updates the preferred communication channel for a customer.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'The ID of the customer to update.'},
                        'new_channel': {'type': 'string', 'description': 'The new preferred channel (e.g., Email, Phone, SMS).'}
                    },
                    'required': ['customer_id', 'new_channel']
                }
            }
        }
