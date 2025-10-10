# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserOrders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        status_filter = kwargs.get('status')
        limit = kwargs.get('limit', 10)

        if not user_id:
            return json.dumps({'error': 'user_id is required'})

        orders = data['orders']
        user_orders = []

        for order in orders:
            if order['user_id'] == user_id:
                if status_filter and order['status'] != status_filter:
                    continue
                user_orders.append({
                    'order_id': order['order_id'],
                    'status': order['status'],
                    'items': order['items'],
                    'total_amount': sum(item['price'] for item in order['items'])
                })

        user_orders.sort(key=lambda x: x['order_id'], reverse=True)
        return json.dumps(user_orders[:limit], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_user_orders',
                'description': 'Get all orders for a specific user with optional status filtering.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'user_id': {'type': 'string', 'description': 'User ID to get orders for'},
                        'status': {'type': 'string', 'description': 'Filter by order status'},
                        'limit': {'type': 'integer', 'description': 'Maximum number of orders to return', 'default': 10}
                    },
                    'required': ['user_id']
                }
            }
        }
