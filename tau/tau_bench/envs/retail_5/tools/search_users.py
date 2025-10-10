# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchUsers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], email, name, user_id) -> str:

        if not any([email, name, user_id]):
            return json.dumps({'error': 'email, name, or user_id is required'})

        users = data['users']

        if user_id:
            user = next((u for u in users if u['user_id'] == user_id), None)
            if not user:
                return json.dumps({'error': 'User not found'})
            return json.dumps(user, indent=2)

        matching_users = []
        for user in users:
            if email and email.lower() in user['email'].lower():
                matching_users.append(user)
            elif name:
                full_name = f"{user['name']['first_name']} {user['name']['last_name']}".lower()
                if name.lower() in full_name:
                    matching_users.append(user)

        return json.dumps(matching_users, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'search_users',
                'description': 'Search for users by email, name, or user ID.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'email': {'type': 'string', 'description': 'Email address to search for'},
                        'name': {'type': 'string', 'description': 'Name to search for (partial match)'},
                        'user_id': {'type': 'string', 'description': 'Specific user ID to look up'}
                    }
                }
            }
        }
