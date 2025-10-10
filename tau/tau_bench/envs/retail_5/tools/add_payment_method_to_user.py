# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import generate_unique_id


class AddPaymentMethodToUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        payment_method = kwargs.get('payment_method')
        if not user_id or not payment_method:
            return json.dumps({'error': 'user_id and payment_method are required'})

        user = next((u for u in data['users'] if u['user_id'] == user_id), None)
        if not user:
            return json.dumps({'error': 'User not found'})

        method_id = f"{payment_method.get('source', 'card')}_{generate_unique_id()}"
        payment_method['id'] = method_id
        user['payment_methods'][method_id] = payment_method

        return json.dumps({'success': True, 'payment_method_id': method_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'add_payment_method_to_user',
                'description': "Add a new payment method to a user's profile.",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'user_id': {'type': 'string', 'description': 'The ID of the user.'},
                        'payment_method': {'type': 'object', 'description': 'Object containing payment details like source, brand, last_four.'}
                    },
                    'required': ['user_id', 'payment_method']
                }
            }
        }
