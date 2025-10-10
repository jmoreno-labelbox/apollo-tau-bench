# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        address = kwargs.get('address')
        if not user_id or not address:
            return json.dumps({'error': 'user_id and address are required'})

        user = next((u for u in data['users'] if u['user_id'] == user_id), None)
        if not user:
            return json.dumps({'error': 'User not found'})

        user['address'] = address
        return json.dumps({'success': True, 'user_id': user_id, 'message': 'Address updated.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_user_address',
                'description': "Update a user's primary shipping address.",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'user_id': {'type': 'string', 'description': 'The ID of the user to update.'},
                        'address': {'type': 'object', 'description': 'A complete address object.'}
                    },
                    'required': ['user_id', 'address']
                }
            }
        }
