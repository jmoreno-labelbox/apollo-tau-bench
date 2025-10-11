# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserRevenueSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:

        if not user_id:
            return json.dumps({'error': 'user_id is required'})

        orders = data['orders']
        revenue_data = {
            'user_id': user_id,
            'total_revenue': 0.0,
            'order_count': 0
        }

        for order in orders:
            if order['user_id'] == user_id and order['status'] in ['delivered', 'completed', 'processed']:
                order_total = sum(item['price'] for item in order['items'])
                revenue_data['total_revenue'] += order_total
                revenue_data['order_count'] += 1

        revenue_data['average_order_value'] = revenue_data['total_revenue'] / max(1, revenue_data['order_count'])

        return json.dumps(revenue_data, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_user_revenue_summary',
                'description': 'Get revenue summary for a specific user including total revenue, order count, and order details.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'user_id': {'type': 'string', 'description': 'User ID to get revenue summary for'}
                    },
                    'required': ['user_id']
                }
            }
        }
