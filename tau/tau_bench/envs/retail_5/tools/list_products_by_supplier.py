# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListProductsBySupplier(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id) -> str:

        if not supplier_id:
            return json.dumps({'error': 'supplier_id is required'})

        products = data['products']
        supplier_products = [p for p in products if p['supplier_id'] == supplier_id]

        return json.dumps(supplier_products, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'list_products_by_supplier',
                'description': 'Get all products supplied by a specific supplier.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supplier_id': {'type': 'string', 'description': 'Supplier ID to get products for'}
                    },
                    'required': ['supplier_id']
                }
            }
        }
