# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BulkOrderProcessing(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_ids = kwargs.get('order_ids')
        new_status = kwargs.get('new_status')

        if not order_ids or not new_status:
            return json.dumps({'error': 'order_ids and new_status are required'})

        orders = data['orders']
        updated_orders = []

        for order_id in order_ids:
            order = next((o for o in orders if o['order_id'] == order_id), None)
            if order:
                old_status = order['status']
                order['status'] = new_status
                updated_orders.append({
                    'order_id': order_id,
                    'old_status': old_status,
                    'new_status': new_status
                })

        return json.dumps({
            'success': True,
            'updated_orders': updated_orders,
            'total_updated': len(updated_orders),
            'updated_at': get_current_timestamp()
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'bulk_order_processing',
                'description': 'Update the status of multiple orders at once.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of order IDs to update'},
                        'new_status': {'type': 'string', 'description': 'New status for all orders'}
                    },
                    'required': ['order_ids', 'new_status']
                }
            }
        }
