# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRevenueSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        group_by = kwargs.get('group_by', 'total')

        orders = data['orders']
        revenue_data = {'total_revenue': 0.0, 'order_count': 0}

        if group_by == 'product':
            revenue_data['by_product'] = {}
        elif group_by == 'user':
            revenue_data['by_user'] = {}

        for order in orders:
            if order['status'] in ['delivered', 'completed', 'processed']:
                order_total = sum(item['price'] for item in order['items'])
                revenue_data['total_revenue'] += order_total
                revenue_data['order_count'] += 1

                if group_by == 'product':
                    for item in order['items']:
                        product_name = item['name']
                        if product_name not in revenue_data['by_product']:
                            revenue_data['by_product'][product_name] = 0.0
                        revenue_data['by_product'][product_name] += item['price']

                elif group_by == 'user':
                    user_id = order['user_id']
                    if user_id not in revenue_data['by_user']:
                        revenue_data['by_user'][user_id] = 0.0
                    revenue_data['by_user'][user_id] += order_total

        revenue_data['average_order_value'] = revenue_data['total_revenue'] / max(1, revenue_data['order_count'])

        return json.dumps(revenue_data, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_revenue_summary',
                'description': 'Get revenue summary with optional grouping by product or user.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'group_by': {'type': 'string', 'description': 'Group results by: total, product, or user', 'default': 'total'}
                    }
                }
            }
        }
