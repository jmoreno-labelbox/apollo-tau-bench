# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSupplyOrderQuantity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supply_order_id = kwargs.get('supply_order_id')
        new_quantity = kwargs.get('new_quantity')

        if not supply_order_id or new_quantity is None:
            return json.dumps({'error': 'supply_order_id and new_quantity are required'})

        if new_quantity < 0:
            return json.dumps({'error': 'Quantity cannot be negative'})

        supply_orders = data['supply_orders']
        order = next((o for o in supply_orders if o['supply_order_id'] == supply_order_id), None)

        if not order:
            return json.dumps({'error': f'Supply order {supply_order_id} not found'})

        if order['status'] not in ['pending']:
            return json.dumps({'error': f'Cannot update quantity for order with status: {order["status"]}'})

        old_quantity = order['quantity']
        old_total_cost = order['total_cost']

        order['quantity'] = new_quantity
        order['total_cost'] = new_quantity * order['unit_cost']

        return json.dumps({
            'success': True,
            'supply_order_id': supply_order_id,
            'old_quantity': old_quantity,
            'new_quantity': new_quantity,
            'old_total_cost': old_total_cost,
            'new_total_cost': order['total_cost'],
            'updated_at': get_current_timestamp()
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_supply_order_quantity',
                'description': 'Update the quantity of a pending supply order and recalculate total cost.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supply_order_id': {'type': 'string', 'description': 'Supply order ID to update'},
                        'new_quantity': {'type': 'integer', 'description': 'New quantity for the order'}
                    },
                    'required': ['supply_order_id', 'new_quantity']
                }
            }
        }
