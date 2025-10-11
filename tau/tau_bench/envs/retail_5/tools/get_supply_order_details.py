# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplyOrderDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id) -> str:

        if not supply_order_id:
            return json.dumps({'error': 'supply_order_id is required'})

        supply_orders = data['supply_orders']
        order = next((o for o in supply_orders if o['supply_order_id'] == supply_order_id), None)

        if not order:
            return json.dumps({'error': f'Supply order {supply_order_id} not found'})

        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_supply_order_details',
                'description': 'Get detailed information about a specific supply order.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supply_order_id': {'type': 'string', 'description': 'Supply order ID to get details for'}
                    },
                    'required': ['supply_order_id']
                }
            }
        }
