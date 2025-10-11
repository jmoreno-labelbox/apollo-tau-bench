# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, order_id) -> str:

        if not order_id or not new_status:
            return json.dumps({'error': 'order_id and new_status are required'})

        orders = data['orders']
        order = next((o for o in orders if o['order_id'] == order_id), None)

        if not order:
            return json.dumps({'error': 'Order not found'})

        old_status = order['status']
        order['status'] = new_status

        return json.dumps({
            'success': True,
            'order_id': order_id,
            'old_status': old_status,
            'new_status': new_status,
            'updated_at': get_current_timestamp()
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_order_status',
                'description': 'Update the status of an existing order.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'string', 'description': 'Order ID to update'},
                        'new_status': {'type': 'string', 'description': 'New status for the order'}
                    },
                    'required': ['order_id', 'new_status']
                }
            }
        }
