# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPendingSupplyOrders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')

        supply_orders = data['supply_orders']
        pending_orders = []

        for order in supply_orders:
            if order['status'] == 'pending':
                if supplier_id and order['supplier_id'] != supplier_id:
                    continue
                pending_orders.append(order)

        return json.dumps(pending_orders, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_pending_supply_orders',
                'description': 'Get all pending supply orders, optionally filtered by supplier.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supplier_id': {'type': 'string', 'description': 'Optional supplier ID to filter by'}
                    }
                }
            }
        }
