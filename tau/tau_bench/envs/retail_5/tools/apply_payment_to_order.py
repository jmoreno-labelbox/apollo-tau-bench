# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyPaymentToOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        payment_method_id = kwargs.get('payment_method_id')
        shipping_address = kwargs.get('shipping_address')
        if not all([order_id, payment_method_id, shipping_address]):
            return json.dumps({'error': 'order_id, payment_method_id, and shipping_address are required'})

        order = next((o for o in data['orders'] if o['order_id'] == order_id), None)
        if not order: return json.dumps({'error': 'Order not found'})
        if order['status'] != 'pending': return json.dumps({'error': f'Order status is not pending, but {order["status"]}'})

        user = next((u for u in data['users'] if u['user_id'] == order['user_id']), None)
        if not user or payment_method_id not in user['payment_methods']:
            return json.dumps({'error': 'Invalid payment method for user'})

        total_amount = sum(item['price'] for item in order['items'])

        # Handle gift card payments separately
        if payment_method_id.startswith('gift_card'):
            # Get gift card payment method details
            gift_card = user['payment_methods'][payment_method_id]
            gift_card_balance = gift_card.get('balance', 0)

            if gift_card_balance >= total_amount:
                # Sufficient balance - deduct the amount and process normally
                gift_card['balance'] = gift_card_balance - total_amount
                order['payment_history'].append({
                    'transaction_type': 'payment',
                    'amount': total_amount,
                    'payment_method_id': payment_method_id,
                    'timestamp': get_current_timestamp()
                })
                order['address'] = shipping_address
                order['status'] = 'processing'
                return json.dumps({'success': True, 'order_id': order_id, 'new_status': 'processing'}, indent=2)
            else:
                # Insufficient balance - use all available balance and keep order pending
                if gift_card_balance > 0:
                    order['payment_history'].append({
                        'transaction_type': 'partial_payment',
                        'amount': gift_card_balance,
                        'payment_method_id': payment_method_id,
                        'timestamp': get_current_timestamp()
                    })
                    order['address'] = shipping_address
                    order['status'] = 'pending'
                    gift_card['balance'] = 0

                return json.dumps({
                    'success': False,
                    'reason': 'Insufficient gift card balance',
                    'order_id': order_id,
                    'status': 'pending',
                    'remaining_amount': total_amount - gift_card_balance
                }, indent=2)
        else:
            # Regular payment method processing
            order['payment_history'].append({'transaction_type': 'payment', 'amount': total_amount, 'payment_method_id': payment_method_id, 'timestamp': get_current_timestamp()})
            order['address'] = shipping_address
            order['status'] = 'processing'
            return json.dumps({'success': True, 'order_id': order_id, 'new_status': 'processing'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'apply_payment_to_order',
                'description': 'Applies a payment method and shipping address to a pending order.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'string'},
                        'payment_method_id': {'type': 'string'},
                        'shipping_address': {'type': 'object'}
                    },
                    'required': ['order_id', 'payment_method_id', 'shipping_address']
                }
            }
        }
