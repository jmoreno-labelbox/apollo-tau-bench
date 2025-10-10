# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindRecentSupportTicketsByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        category = kwargs.get('category')  # New
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})

        tickets = load_json('support_tickets.json')
        filtered = [t for t in tickets if t['customer_id'] == customer_id]

        if category:
            filtered = [t for t in filtered if t.get('category') == category]

        # Sort by created_at or updated_at if available for "recent"
        filtered.sort(key=lambda x: x.get('created_at', ''), reverse=True)

        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'find_recent_support_tickets_by_category',
                'description': 'Retrieves recent support tickets for a customer optionally filtered by category.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'category': {'type': 'string', 'description': 'Optional category filter'}
                    },
                    'required': ['customer_id']
                }
            }
        }
