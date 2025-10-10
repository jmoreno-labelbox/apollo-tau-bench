# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignFulfillmentToOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        courier_id = kwargs.get('courier_id')
        delivery_options = kwargs.get('delivery_options', 'standard')
        if not order_id or not courier_id:
            return json.dumps({'error': 'order_id and courier_id are required'})

        order = next((o for o in data['orders'] if o['order_id'] == order_id), None)
        if not order: return json.dumps({'error': 'Order not found'})
        if order['status'] != 'processing': return json.dumps({'error': f'Order status is not processing, but {order["status"]}'})

        ord_split = order_id.split('_')

        tracking_id = ord_split[1] if len(ord_split) > 1 else f"{generate_unique_id()}"
        item_ids = [item['item_id'] for item in order['items']]

        fulfillment = {'tracking_id': [tracking_id], 'item_ids': item_ids}
        order['fulfillments'].append(fulfillment)

        new_tracking_record = {
            'tracking_id': [tracking_id], 'item_ids': item_ids,
            'address': order['address'], 'delivery_carrier': courier_id, 'delivery_options': delivery_options,
            'order_id': order_id, 'tracking_history': {'received': get_current_timestamp()}
        }
        data['tracking'].append(new_tracking_record)

        courier = next((c for c in data['couriers'] if c['courier_id'] == courier_id), None)
        if courier: courier['tracking_ids'].append(tracking_id)

        order['status'] = 'processed'
        return json.dumps({'success': True, 'order_id': order_id, 'tracking_id': tracking_id, 'new_status': 'processed'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'assign_fulfillment_to_order',
                'description': 'Assigns a courier and creates tracking for a processed order.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'string'},
                        'courier_id': {'type': 'string'},
                        'delivery_options': {'type': 'string'}
                    },
                    'required': ['order_id', 'courier_id']
                }
            }
        }
