# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductByItemId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_id) -> str:

        if not item_id:
            return json.dumps({'error': 'item_id is required'})

        products = data['products']

        # Scan all products to identify the one that includes this item_id.
        for product in products:
            if item_id in product['variants']:
                variant_info = product['variants'][item_id]
                return json.dumps({
                    'product_id': product['product_id'],
                    'product_name': product['name'],
                    'supplier_id': product['supplier_id'],
                    'item_id': item_id
                }, indent=2)

        return json.dumps({'error': f'Item ID {item_id} not found in any product'})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_product_by_item_id',
                'description': 'Find the product ID and details given a specific item ID (variant ID).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'item_id': {'type': 'string', 'description': 'Item ID (variant ID) to search for'}
                    },
                    'required': ['item_id']
                }
            }
        }
