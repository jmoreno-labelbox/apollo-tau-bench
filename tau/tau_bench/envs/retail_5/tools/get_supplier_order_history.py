# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierOrderHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        limit = kwargs.get('limit', 10)

        if not supplier_id:
            return json.dumps({'error': 'supplier_id is required'})

        suppliers = data['suppliers']
        supply_orders = data['supply_orders']
        products = data['products']

        supplier = next((s for s in suppliers if s['supplier_id'] == supplier_id), None)
        if not supplier:
            return json.dumps({'error': f'Supplier {supplier_id} not found'})

        # Retrieve all orders associated with this supplier.
        supplier_orders = [o for o in supply_orders if o['supplier_id'] == supplier_id]
        supplier_orders.sort(key=lambda x: x['order_date'], reverse=True)

        # Augment orders by adding product names.
        enriched_orders = []
        for order in supplier_orders[:limit]:
            product = next((p for p in products if p['product_id'] == order['product_id']), None)
            enriched_order = order.copy()
            enriched_order['product_name'] = product['name'] if product else 'Unknown Product'
            enriched_orders.append(enriched_order)

        # Compute summary statistics.
        total_orders = len(supplier_orders)
        total_value = sum(o['total_cost'] for o in supplier_orders)
        pending_orders = len([o for o in supplier_orders if o['status'] == 'pending'])

        return json.dumps({
            'supplier': {
                'supplier_id': supplier['supplier_id'],
                'name': supplier['name'],
                'contact_info': supplier['contact_info']
            },
            'order_summary': {
                'total_orders': total_orders,
                'total_value': total_value,
                'pending_orders': pending_orders
            },
            'recent_orders': enriched_orders
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_supplier_order_history',
                'description': 'Get order history and summary statistics for a supplier.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supplier_id': {'type': 'string', 'description': 'Supplier ID to get order history for'},
                        'limit': {'type': 'integer', 'description': 'Maximum number of recent orders to return', 'default': 10}
                    },
                    'required': ['supplier_id']
                }
            }
        }
