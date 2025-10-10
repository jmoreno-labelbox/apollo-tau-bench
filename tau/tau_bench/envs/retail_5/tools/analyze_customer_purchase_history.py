# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnalyzeCustomerPurchaseHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')

        if not user_id:
            return json.dumps({'error': 'user_id is required'})

        orders = data['orders']
        user_orders = [o for o in orders if o['user_id'] == user_id]
        # and o['status'] in ['delivered', 'completed', 'processed']

        total_spent = 0.0
        categories = {}
        most_expensive_item = None
        max_price = 0.0

        for order in user_orders:
            for item in order['items']:
                total_spent += item['price']
                category = item['name']
                categories[category] = categories.get(category, 0) + 1

                if item['price'] > max_price:
                    max_price = item['price']
                    most_expensive_item = item

        preferred_category = max(categories, key=categories.get) if categories else None

        return json.dumps({
            'user_id': user_id,
            'total_orders': len(user_orders),
            'total_spent': total_spent,
            'average_order_value': total_spent / max(len(user_orders), 1),
            'preferred_category': preferred_category,
            'most_expensive_item': most_expensive_item,
            'category_breakdown': categories
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'analyze_customer_purchase_history',
                'description': 'Analyze a customer\'s purchase history to understand buying patterns and preferences.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'user_id': {'type': 'string', 'description': 'User ID to analyze'}
                    },
                    'required': ['user_id']
                }
            }
        }
