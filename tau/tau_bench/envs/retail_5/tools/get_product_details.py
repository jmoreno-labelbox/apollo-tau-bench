# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], product_id) -> str:

        if not product_id:
            return json.dumps({'error': 'product_id is required'})

        products = data['products']
        product = next((p for p in products if p['product_id'] == product_id), None)

        if not product:
            return json.dumps({'error': f'Product {product_id} not found'})

        return json.dumps(product, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_product_details',
                'description': 'Get detailed information about a specific product including all variants.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'product_id': {'type': 'string', 'description': 'Product ID to get details for'}
                    },
                    'required': ['product_id']
                }
            }
        }
