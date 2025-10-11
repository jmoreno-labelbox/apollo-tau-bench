# Copyright Sierra

import json
import os
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool

# Note: DATA_DIR and load_json are no longer used by the invoke methods,
# which is the correct architecture. They are left here in case they are
# used by other parts of the framework not provided.
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')

def get_current_timestamp() -> str:
    # Deterministic timestamp as per requirements
    return "2025-08-12T12:00:00.000000"

def generate_unique_id() -> str:
    # Deterministic ID as per requirements
    return 'fd520c73'


class UpdateSupplyOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, supply_order_id) -> str:

        if not supply_order_id or not new_status:
            return json.dumps({'error': 'supply_order_id and new_status are required'})

        supply_orders = data['supply_orders']
        order = next((o for o in supply_orders if o['supply_order_id'] == supply_order_id), None)

        if not order:
            return json.dumps({'error': 'Supply order not found'})

        old_status = order['status']
        order['status'] = new_status

        # Upon order completion, refresh inventory levels.
        if new_status == 'completed':
            suppliers = data['suppliers']
            supplier = next((s for s in suppliers if s['supplier_id'] == order['supplier_id']), None)

            if supplier and order['item_id'] in supplier['item_stock']:
                current_stock = supplier['item_stock'][order['item_id']]
                if isinstance(current_stock, int):
                    supplier['item_stock'][order['item_id']] = current_stock + order['quantity']

        return json.dumps({
            'success': True,
            'supply_order_id': supply_order_id,
            'old_status': old_status,
            'new_status': new_status,
            'updated_at': get_current_timestamp()
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_supply_order_status',
                'description': 'Update the status of a supply order. Automatically updates inventory when marked as completed.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supply_order_id': {'type': 'string', 'description': 'Supply order ID to update'},
                        'new_status': {'type': 'string', 'description': 'New status for the supply order'}
                    },
                    'required': ['supply_order_id', 'new_status']
                }
            }
        }
