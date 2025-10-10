# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        if not order_id:
            return json.dumps({'error': 'order_id is required'})

        orders = data['orders']
        order = next((o for o in orders if o['order_id'] == order_id), None)

        if not order:
            return json.dumps({'error': 'Order not found'})

        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_order_details',
                'description': 'Retrieve complete details for a specific order by order ID.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'string', 'description': 'Order ID to look up'}
                    },
                    'required': ['order_id']
                }
            }
        }
