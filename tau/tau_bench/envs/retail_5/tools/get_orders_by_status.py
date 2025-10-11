# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrdersByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], end_date, start_date, status, limit = 20) -> str:

        if not status:
            return json.dumps({'error': 'status is required'})

        orders = data['orders']
        filtered_orders = []

        for order in orders:
            if order['status'] != status:
                continue

            # Date filtering is intricate without appropriate datetime objects, deferring for the moment as in the original.

            order_summary = {
                'order_id': order['order_id'],
                'user_id': order['user_id'],
                'status': order['status'],
                'item_count': len(order['items']),
                'total_amount': sum(item['price'] for item in order['items']),
                'tracking_ids': [f['tracking_id'][0] for f in order.get('fulfillments', []) if f.get('tracking_id')]
            }
            filtered_orders.append(order_summary)

        filtered_orders.sort(key=lambda x: x['order_id'], reverse=True)
        return json.dumps(filtered_orders[:limit], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_orders_by_status',
                'description': 'Get all orders with a specific status.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'status': {'type': 'string', 'description': 'Order status to filter by'},
                        'limit': {'type': 'integer', 'description': 'Maximum number of orders to return', 'default': 20},
                        'start_date': {'type': 'string', 'description': 'Start date for filtering (ISO format, not fully implemented)'},
                        'end_date': {'type': 'string', 'description': 'End date for filtering (ISO format, not fully implemented)'}
                    },
                    'required': ['status']
                }
            }
        }
