# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import generate_unique_id


class CreateSupplyOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        product_id = kwargs.get('product_id')
        item_id = kwargs.get('item_id')
        quantity = kwargs.get('quantity')
        unit_cost = kwargs.get('unit_cost')

        if not all([supplier_id, product_id, item_id, quantity, unit_cost]):
            return json.dumps({'error': 'supplier_id, product_id, item_id, quantity, and unit_cost are required'})

        supply_orders = data['supply_orders']

        supply_order_id = f"#SO{generate_unique_id()}-{item_id}"
        total_cost = quantity * unit_cost

        new_order = {
            'supply_order_id': supply_order_id,
            'supplier_id': supplier_id,
            'product_id': product_id,
            'item_id': item_id,
            'quantity': quantity,
            'status': 'pending',
            'order_date': get_current_timestamp(),
            'unit_cost': unit_cost,
            'total_cost': total_cost
        }

        supply_orders.append(new_order)

        return json.dumps({
            'success': True,
            'supply_order_id': supply_order_id,
            'total_cost': total_cost
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'create_supply_order',
                'description': 'Create a new supply order to restock inventory from a supplier.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supplier_id': {'type': 'string', 'description': 'Supplier ID to order from'},
                        'product_id': {'type': 'string', 'description': 'Product ID to order'},
                        'item_id': {'type': 'string', 'description': 'Specific item variant ID'},
                        'quantity': {'type': 'integer', 'description': 'Quantity to order'},
                        'unit_cost': {'type': 'number', 'description': 'Cost per unit'}
                    },
                    'required': ['supplier_id', 'product_id', 'item_id', 'quantity', 'unit_cost']
                }
            }
        }
