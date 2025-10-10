# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckProductAvailability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get('item_id')
        product_id = kwargs.get('product_id')

        if not item_id and not product_id:
            return json.dumps({'error': 'Either item_id or product_id is required'})

        products = data['products']

        if item_id:
            for product in products:
                for variant_id, variant in product['variants'].items():
                    if variant['item_id'] == item_id:
                        return json.dumps({
                            'item_id': item_id,
                            'product_name': product['name'],
                            'available': variant['available'],
                            'price': variant['price'],
                            'options': variant['options']
                        }, indent=2)
            return json.dumps({'error': 'Item not found'})

        if product_id:
            product = next((p for p in products if p['product_id'] == product_id), None)
            if not product:
                return json.dumps({'error': 'Product not found'})

            available_variants = []
            for variant_id, variant in product['variants'].items():
                if variant['available']:
                    available_variants.append({
                        'item_id': variant['item_id'],
                        'price': variant['price'],
                        'options': variant['options']
                    })

            return json.dumps({
                'product_id': product_id,
                'product_name': product['name'],
                'available_variants': available_variants
            }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'check_product_availability',
                'description': 'Check availability of a specific product variant or all variants of a product.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'item_id': {'type': 'string', 'description': 'Specific item ID to check'},
                        'product_id': {'type': 'string', 'description': 'Product ID to check all variants'}
                    }
                }
            }
        }
