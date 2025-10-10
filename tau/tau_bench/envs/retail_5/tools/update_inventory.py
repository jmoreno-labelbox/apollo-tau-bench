# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        item_id = kwargs.get('item_id')
        new_stock = kwargs.get('new_stock')
        adjustment = kwargs.get('adjustment')

        if not supplier_id or not item_id:
            return json.dumps({'error': 'supplier_id and item_id are required'})

        if new_stock is None and adjustment is None:
            return json.dumps({'error': 'Either new_stock or adjustment is required'})

        suppliers = data['suppliers']
        supplier = next((s for s in suppliers if s['supplier_id'] == supplier_id), None)

        if not supplier:
            return json.dumps({'error': 'Supplier not found'})

        current_stock = supplier['item_stock'].get(item_id)

        if isinstance(current_stock, str) and current_stock == 'discontinued':
            return json.dumps({'error': f'Cannot update stock for item with status: {current_stock}'})

        if new_stock is not None:
            supplier['item_stock'][item_id] = new_stock
            updated_stock = new_stock
        else:
            if not isinstance(current_stock, int):
                # Handle cases where stock is not a number, like None or not present
                current_stock = 0
            updated_stock = max(0, current_stock + adjustment)
            supplier['item_stock'][item_id] = updated_stock

        return json.dumps({
            'success': True,
            'supplier_id': supplier_id,
            'item_id': item_id,
            'previous_stock': current_stock,
            'updated_stock': updated_stock,
            'updated_at': get_current_timestamp()
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_inventory',
                'description': 'Update inventory stock levels for a specific item.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supplier_id': {'type': 'string', 'description': 'Supplier ID managing the inventory'},
                        'item_id': {'type': 'string', 'description': 'Item ID to update stock for'},
                        'new_stock': {'type': 'integer', 'description': 'Set to this exact stock level'},
                        'adjustment': {'type': 'integer', 'description': 'Adjust current stock by this amount (positive or negative)'}
                    },
                    'required': ['supplier_id', 'item_id']
                }
            }
        }
