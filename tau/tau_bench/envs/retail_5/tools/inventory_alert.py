# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InventoryAlert(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        threshold = kwargs.get('threshold', 10)
        category_filter = kwargs.get('category_filter')

        suppliers = data['suppliers']
        products = data['products']
        critical_items = []

        for supplier in suppliers:
            for item_id, stock in supplier['item_stock'].items():
                if isinstance(stock, int) and stock <= threshold:
                    product_name = 'Unknown'
                    for product in products:
                        if item_id in product['variants']:
                            product_name = product['name']
                            break

                    if category_filter and category_filter.lower() not in product_name.lower():
                        continue

                    critical_items.append({
                        'item_id': item_id,
                        'product_name': product_name,
                        'supplier_id': supplier['supplier_id'],
                        'supplier_name': supplier['name'],
                        'current_stock': stock,
                        'threshold': threshold
                    })

        return json.dumps({
            'critical_items': critical_items,
            'total_critical': len(critical_items),
            'threshold_used': threshold
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'inventory_alert',
                'description': 'Generate alerts for items that are critically low in stock.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'threshold': {'type': 'integer', 'description': 'Stock threshold for critical alert', 'default': 10},
                        'category_filter': {'type': 'string', 'description': 'Filter alerts by product category'}
                    }
                }
            }
        }
