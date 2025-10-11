# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetStockLevels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_id, supplier_id, low_stock_threshold = 50) -> str:

        suppliers = data['suppliers']

        if supplier_id:
            supplier = next((s for s in suppliers if s['supplier_id'] == supplier_id), None)
            if not supplier:
                return json.dumps({'error': 'Supplier not found'})

            if item_id:
                stock_level = supplier['item_stock'].get(item_id, 'not_found')
                return json.dumps({
                    'supplier_id': supplier_id,
                    'item_id': item_id,
                    'stock_level': stock_level
                }, indent=2)

            low_stock_items = []
            for item, stock in supplier['item_stock'].items():
                if (isinstance(stock, int) and stock < low_stock_threshold) or (isinstance(stock, str) and stock == 'out_of_stock'):
                    low_stock_items.append({
                        'item_id': item,
                        'stock_level': stock
                    })

            return json.dumps({
                'supplier_id': supplier_id,
                'low_stock_items': low_stock_items,
                'threshold': low_stock_threshold
            }, indent=2)

        # Retrieve low inventory from all suppliers.
        all_low_stock = []
        for supplier in suppliers:
            for item, stock in supplier['item_stock'].items():
                if (isinstance(stock, int) and stock < low_stock_threshold) or (isinstance(stock, str) and stock == 'out_of_stock'):
                    all_low_stock.append({
                        'supplier_id': supplier['supplier_id'],
                        'supplier_name': supplier['name'],
                        'item_id': item,
                        'stock_level': stock
                    })

        return json.dumps(all_low_stock, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_stock_levels',
                'description': 'Get stock levels for items, with options to filter by supplier or check low stock items.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supplier_id': {'type': 'string', 'description': 'Supplier ID to check stock for'},
                        'item_id': {'type': 'string', 'description': 'Specific item ID to check stock for'},
                        'low_stock_threshold': {'type': 'integer', 'description': 'Threshold below which items are considered low stock', 'default': 50}
                    }
                }
            }
        }
