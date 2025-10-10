# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductSupplierSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get('product_id')

        if not product_id:
            return json.dumps({'error': 'product_id is required'})

        products = data['products']
        suppliers = data['suppliers']
        supply_orders = data['supply_orders']

        product = next((p for p in products if p['product_id'] == product_id), None)
        if not product:
            return json.dumps({'error': f'Product {product_id} not found'})

        supplier = next((s for s in suppliers if s['supplier_id'] == product['supplier_id']), None)

        # Get supply orders for this product
        product_supply_orders = [o for o in supply_orders if o['product_id'] == product_id]

        # Calculate stock summary
        stock_summary = {}
        if supplier:
            for variant_id in product['variants'].keys():
                stock_level = supplier['item_stock'].get(variant_id, 'unknown')
                stock_summary[variant_id] = stock_level

        return json.dumps({
            'product': product,
            'supplier': supplier,
            'stock_summary': stock_summary,
            'total_supply_orders': len(product_supply_orders),
            'recent_supply_orders': product_supply_orders[-5:]  # Last 5 orders
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_product_supplier_summary',
                'description': 'Get comprehensive information about a product, its supplier, stock levels, and recent supply orders.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'product_id': {'type': 'string', 'description': 'Product ID to get summary for'}
                    },
                    'required': ['product_id']
                }
            }
        }
