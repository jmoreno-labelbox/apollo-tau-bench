# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchProductsByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get('category')
        available_only = kwargs.get('available_only', True)
        max_price = kwargs.get('max_price')
        min_price = kwargs.get('min_price')
        min_stock = kwargs.get('min_stock', 1)
        max_stock = kwargs.get('max_stock')

        if not category:
            return json.dumps({'error': 'category is required'})

        # Check stock range validity.
        if min_stock is not None and max_stock is not None and min_stock > max_stock:
            return json.dumps({'error': 'min_stock cannot be greater than max_stock'})

        products = data['products']
        suppliers = data['suppliers']
        results = []

        # Generate a mapping of item_id to inventory level for efficient retrieval.
        item_stock_map = {}
        for supplier in suppliers:
            for item_id, stock in supplier.get('item_stock', {}).items():
                # Take into account only numerical inventory quantities.
                if isinstance(stock, (int, float)) and stock >= 0:
                    item_stock_map[item_id] = stock

        for product in products:
            if category.lower() in product['name'].lower():
                for variant_id, variant in product['variants'].items():
                    if available_only and not variant.get('available', False):
                        continue
                    if max_price and variant['price'] > max_price:
                        continue
                    if min_price and variant['price'] < min_price:
                        continue

                    # Verify inventory quantities if stock filters are available.
                    item_id = variant.get('item_id', variant_id)
                    stock_level = item_stock_map.get(item_id, 0)

                    if min_stock is not None and stock_level < min_stock:
                        continue
                    if max_stock is not None and stock_level > max_stock:
                        continue

                    results.append({
                        'product_id': product['product_id'],
                        'name': product['name'],
                        'item_id': variant.get('item_id', variant_id),
                        'price': variant['price'],
                        'stock_level': stock_level,
                        'options': variant['options'],
                        'available': variant['available']
                    })

        results.sort(key=lambda x: x['price'])

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'search_products_by_category',
                'description': 'Search for products by category name with optional price, availability, and stock filters.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'category': {'type': 'string', 'description': 'Product category to search for'},
                        'available_only': {'type': 'boolean', 'description': 'Only return available products', 'default': True},
                        'max_price': {'type': 'number', 'description': 'Maximum price filter'},
                        'min_price': {'type': 'number', 'description': 'Minimum price filter'},
                        'min_stock': {'type': 'integer', 'description': 'Minimum stock level filter'},
                        'max_stock': {'type': 'integer', 'description': 'Maximum stock level filter'}
                    },
                    'required': ['category']
                }
            }
        }
