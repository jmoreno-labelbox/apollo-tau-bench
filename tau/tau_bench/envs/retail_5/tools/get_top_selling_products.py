# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTopSellingProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        limit = kwargs.get('limit', 10)
        category = kwargs.get('category')

        orders = data['orders']
        product_sales = {}

        for order in orders:
            if order['status'] in ['delivered', 'completed', 'processed']:
                for item in order['items']:
                    product_id = item['product_id']
                    product_name = item['name']

                    if category and category.lower() not in product_name.lower():
                        continue

                    if product_id not in product_sales:
                        product_sales[product_id] = {
                            'product_id': product_id,
                            'name': product_name,
                            'total_sold': 0,
                            'revenue': 0
                        }

                    product_sales[product_id]['total_sold'] += 1
                    product_sales[product_id]['revenue'] += item['price']

        sorted_products = sorted(product_sales.values(), key=lambda x: x['total_sold'], reverse=True)

        return json.dumps(sorted_products[:limit], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_top_selling_products',
                'description': 'Get top selling products based on completed orders.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'limit': {'type': 'integer', 'description': 'Number of top products to return', 'default': 10},
                        'category': {'type': 'string', 'description': 'Filter by product category'}
                    }
                }
            }
        }
