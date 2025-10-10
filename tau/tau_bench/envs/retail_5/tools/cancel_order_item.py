# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelOrderItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_id, order_id) -> str:
        if not order_id or not item_id:
            return json.dumps({'error': 'order_id and item_id are required'})

        order = next((o for o in data['orders'] if o['order_id'] == order_id), None)
        if not order:
            return json.dumps({'error': 'Order not found'})

        if order['status'] not in ['pending', 'processing', 'processed']:
            return json.dumps({'error': f"Cannot cancel items from an order with status '{order['status']}'"})

        # Locate the item for cancellation and determine the refund amount.
        cancelled_item = next((item for item in order['items'] if item['item_id'] == item_id), None)
        if not cancelled_item:
            return json.dumps({'error': f'Item {item_id} not found in order {order_id}'})

        refund_amount = cancelled_item['price']

        # Delete the item from the order.
        original_item_count = len(order['items'])
        order['items'] = [item for item in order['items'] if item['item_id'] != item_id]

        if not order['items']:
            order['status'] = 'cancelled'

        # Verify if gift card payments were made for this order and process the refund.
        user = next((u for u in data['users'] if u['user_id'] == order['user_id']), None)
        gift_card_refund_processed = False

        if user and 'payment_history' in order:
            # Search for gift card transactions in the payment records.
            for payment in order['payment_history']:
                if (payment.get('transaction_type') in ['payment', 'partial_payment'] and
                    payment.get('payment_method_id', '').startswith('gift_card')):

                    payment_method_id = payment['payment_method_id']
                    if payment_method_id in user['payment_methods']:
                        # Reinstate refund amount to the gift card balance.
                        gift_card = user['payment_methods'][payment_method_id]
                        current_balance = gift_card.get('balance', 0)
                        gift_card['balance'] = current_balance + refund_amount
                        gift_card_refund_processed = True

                        # Record the refund in the payment history.
                        order['payment_history'].append({
                            'transaction_type': 'refund',
                            'amount': -refund_amount,
                            'payment_method_id': payment_method_id,
                            'reason': f'Item cancellation: {item_id}',
                            'timestamp': get_current_timestamp()
                        })
                        break

        # Log the refund in payment history even if no gift card payment was detected.
        if not gift_card_refund_processed:
            if 'payment_history' not in order:
                order['payment_history'] = []
            order['payment_history'].append({
                'transaction_type': 'refund',
                'amount': -refund_amount,
                'reason': f'Item cancellation: {item_id}',
                'timestamp': get_current_timestamp()
            })

        return json.dumps({
            'success': True,
            'order_id': order_id,
            'new_status': order['status'],
            'refund_amount': refund_amount,
            'gift_card_refund_processed': gift_card_refund_processed
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'cancel_order_item',
                'description': "Remove a specific item from a pending or processing order.",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'string', 'description': 'The ID of the order to modify.'},
                        'item_id': {'type': 'string', 'description': 'The ID of the item to remove.'}
                    },
                    'required': ['order_id', 'item_id']
                }
            }
        }
