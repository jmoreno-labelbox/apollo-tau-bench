# Sierra copyright reserved.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessReturn(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_ids, order_id, reason) -> str:

        if not all([order_id, item_ids, reason]):
            return json.dumps({'error': 'order_id, item_ids, and reason are required'})

        orders = data['orders']
        suppliers = data['suppliers']
        products = data['products']
        order = next((o for o in orders if o['order_id'] == order_id), None)

        if not order:
            return json.dumps({'error': 'Order not found'})

        if order['status'] not in ['delivered', 'completed', 'processed']:
            return json.dumps({'error': f'Returns not allowed for orders with status: {order["status"]}'})

        return_items = []
        refund_amount = 0.0

        for item_to_return_id in item_ids:
            item_in_order = next((i for i in order['items'] if i['item_id'] == item_to_return_id), None)
            if item_in_order:
                return_items.append(item_in_order)
                refund_amount += item_in_order['price']

                # Replenish stock.
                product_for_item = next((p for p in products if p['product_id'] == item_in_order['product_id']), None)
                if product_for_item:
                    supplier_for_product = next((s for s in suppliers if s['supplier_id'] == product_for_item['supplier_id']), None)
                    if supplier_for_product and item_to_return_id in supplier_for_product['item_stock']:
                        current_stock = supplier_for_product['item_stock'][item_to_return_id]
                        if isinstance(current_stock, int):
                            supplier_for_product['item_stock'][item_to_return_id] = current_stock + 1 # Assuming a quantity of one

        if not return_items:
            return json.dumps({'error': 'No matching items found in order for return'})

        # Record the refund transaction.
        refund_transaction = {
            "transaction_type": "refund",
            "amount": -refund_amount,
            "reason": reason,
            "timestamp": get_current_timestamp()
        }
        if 'payment_history' not in order:
            order['payment_history'] = []
        order['payment_history'].append(refund_transaction)

        # Modify the order status to indicate a return.
        order['status'] = 'partially_returned' if len(order['items']) > len(return_items) else 'returned'

        return json.dumps({
            'success': True,
            'order_id': order_id,
            'returned_items_count': len(return_items),
            'refund_amount': refund_amount,
            'new_order_status': order['status']
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'process_return',
                'description': 'Process a return for specific items from an order, logs the refund, and restock inventory.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'string', 'description': 'Order ID to process return for'},
                        'item_ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of item IDs to return'},
                        'reason': {'type': 'string', 'description': 'Reason for return'}
                    },
                    'required': ['order_id', 'item_ids', 'reason']
                }
            }
        }
