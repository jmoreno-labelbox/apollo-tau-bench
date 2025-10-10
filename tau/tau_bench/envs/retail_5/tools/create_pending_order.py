# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import generate_unique_id


class CreatePendingOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_details, user_id) -> str:
        if not user_id or not item_details:
            return json.dumps({'error': 'user_id and item_details are required'})

        user = next((u for u in data['users'] if u['user_id'] == user_id), None)
        if not user: return json.dumps({'error': 'User not found'})

        order_items, total_amount = [], 0.0
        order_string=''
        for detail in item_details:
            item_id, quantity = detail['item_id'], detail.get('quantity', 1)
            found_item = None
            for p in data['products']:
                if item_id in p['variants']:
                    variant = p['variants'][item_id]
                    if variant['available']:
                        price = variant['price'] * quantity
                        found_item = {'name': p['name'], 'product_id': p['product_id'], 'item_id': item_id, 'price': price, 'options': variant['options']}
                        total_amount += price
                        order_string+=f"{item_id}"
                    break
            if not found_item: return json.dumps({'error': f'Item {item_id} is not available'})
            order_items.append(found_item)

        order_id = f"#W{generate_unique_id()}_{order_string}"
        new_order = {
            'order_id': order_id, 'user_id': user_id, 'address': None,
            'items': order_items, 'fulfillments': [], 'status': 'pending',
            'payment_history': [], 'timestamp': get_current_timestamp()
        }

        existing_order_index = next((i for i, o in enumerate(data['orders']) if o['order_id'] == order_id), None)
        if existing_order_index is not None:
            data['orders'][existing_order_index] = new_order
        else:
            data['orders'].append(new_order)
        return json.dumps({'success': True, 'order_id': order_id, 'total_amount': total_amount}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'create_pending_order',
                'description': 'Creates a new order with a "pending" status without payment or shipping.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'user_id': {'type': 'string'},
                        'item_details': {'type': 'array', 'items': {'type': 'object', 'properties': {'item_id': {'type': 'string'}, 'quantity': {'type': 'integer'}}}}
                    },
                    'required': ['user_id', 'item_details']
                }
            }
        }
