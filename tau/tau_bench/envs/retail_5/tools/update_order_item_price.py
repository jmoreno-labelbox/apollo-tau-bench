# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOrderItemPrice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        item_id = kwargs.get('item_id')
        new_price = kwargs.get('new_price')
        if not all([order_id, item_id, new_price]):
            return json.dumps({'error': 'order_id, item_id, and new_price are required'})

        order = next((o for o in data['orders'] if o['order_id'] == order_id), None)
        if not order:
            return json.dumps({'error': 'Order not found'})

        if order['status'] != 'pending':
            return json.dumps({'error': 'Can only update prices on pending orders.'})

        item_to_update = next((item for item in order['items'] if item['item_id'] == item_id), None)
        if not item_to_update:
            return json.dumps({'error': f'Item {item_id} not in order.'})

        item_to_update['price'] = new_price
        return json.dumps({'success': True, 'order_id': order_id, 'item_id': item_id, 'new_price': new_price}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_order_item_price',
                'description': "Manually update the price of an item in a pending order.",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'string'},
                        'item_id': {'type': 'string'},
                        'new_price': {'type': 'number'}
                    },
                    'required': ['order_id', 'item_id', 'new_price']
                }
            }
        }
