# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRecommendations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], preferred_category, user_id, max_price = 1000) -> str:

        if not user_id:
            return json.dumps({'error': 'user_id is required'})

        products = data['products']
        recommendations = []

        for product in products:
            if not preferred_category or preferred_category.lower() in product['name'].lower():
                for variant_id, variant in product['variants'].items():
                    if variant['available'] and variant['price'] <= max_price:
                        recommendations.append({
                            'product_id': product['product_id'],
                            'name': product['name'],
                            'item_id': variant['item_id'],
                            'price': variant['price'],
                            'options': variant['options']
                        })

        recommendations.sort(key=lambda x: x['price'])

        return json.dumps({
            'user_id': user_id,
            'recommendations': recommendations[:5],
            'based_on_category': preferred_category
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'create_recommendations',
                'description': 'Create product recommendations for a user based on their preferences.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'user_id': {'type': 'string', 'description': 'User ID to create recommendations for'},
                        'preferred_category': {'type': 'string', 'description': 'Preferred product category'},
                        'max_price': {'type': 'number', 'description': 'Maximum price for recommendations', 'default': 1000}
                    },
                    'required': ['user_id']
                }
            }
        }
