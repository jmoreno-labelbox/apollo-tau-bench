# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyPaymentToOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id, payment_method_id, shipping_address) -> str:
        if not all([order_id, payment_method_id, shipping_address]):
            return json.dumps({'error': 'order_id, payment_method_id, and shipping_address are required'})

        order = next((o for o in data['orders'] if o['order_id'] == order_id), None)
        if not order: return json.dumps({'error': 'Order not found'})
        if order['status'] != 'pending': return json.dumps({'error': f'Order status is not pending, but {order["status"]}'})

        user = next((u for u in data['users'] if u['user_id'] == order['user_id']), None)
        if not user or payment_method_id not in user['payment_methods']:
            return json.dumps({'error': 'Invalid payment method for user'})

        total_amount = sum(item['price'] for item in order['items'])

        # Process gift card transactions independently.
        if payment_method_id.startswith('gift_card'):
            # Retrieve details for the gift card payment method.
            gift_card = user['payment_methods'][payment_method_id]
            gift_card_balance = gift_card.get('balance', 0)

            if gift_card_balance >= total_amount:
                # Adequate funds - subtract the amount and proceed as usual.
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
                # Not enough funds - utilize the full available balance and maintain the order in a pending state.
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
            # Standard payment method handling
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
