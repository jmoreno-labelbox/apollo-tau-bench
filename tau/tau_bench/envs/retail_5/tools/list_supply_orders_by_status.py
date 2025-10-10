# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListSupplyOrdersByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get('status')
        supplier_id = kwargs.get('supplier_id')
        limit = kwargs.get('limit', 20)

        if not status:
            return json.dumps({'error': 'status is required'})

        supply_orders = data['supply_orders']
        filtered_orders = []

        for order in supply_orders:
            if order['status'] == status:
                if supplier_id and order['supplier_id'] != supplier_id:
                    continue
                filtered_orders.append(order)

        # Sort by order date in descending order.
        filtered_orders.sort(key=lambda x: x['order_date'], reverse=True)

        return json.dumps(filtered_orders[:limit], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'list_supply_orders_by_status',
                'description': 'Get supply orders filtered by status, optionally by supplier.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'status': {'type': 'string', 'description': 'Status to filter by (pending, fulfilled, cancelled)'},
                        'supplier_id': {'type': 'string', 'description': 'Optional supplier ID to filter by'},
                        'limit': {'type': 'integer', 'description': 'Maximum number of orders to return', 'default': 20}
                    },
                    'required': ['status']
                }
            }
        }
