# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProductPrice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_id, new_price, product_id) -> str:

        if not product_id or not item_id or new_price is None:
            return json.dumps({'error': 'product_id, item_id, and new_price are required'})

        products = data['products']
        product = next((p for p in products if p['product_id'] == product_id), None)

        if not product:
            return json.dumps({'error': f'Product {product_id} not found'})

        if item_id not in product['variants']:
            return json.dumps({'error': f'Item {item_id} not found in product {product_id}'})

        old_price = product['variants'][item_id]['price']
        product['variants'][item_id]['price'] = new_price

        return json.dumps({
            'success': True,
            'product_id': product_id,
            'item_id': item_id,
            'old_price': old_price,
            'new_price': new_price,
            'updated_at': get_current_timestamp()
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_product_price',
                'description': 'Update the price of a specific product variant.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'product_id': {'type': 'string', 'description': 'Product ID'},
                        'item_id': {'type': 'string', 'description': 'Variant ID to update price for'},
                        'new_price': {'type': 'number', 'description': 'New price for the variant'}
                    },
                    'required': ['product_id', 'item_id', 'new_price']
                }
            }
        }
