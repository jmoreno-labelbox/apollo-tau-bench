# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AdjustOrderPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        payment_method_id = kwargs.get('payment_method_id')

        if not order_id or not payment_method_id:
            return json.dumps({'error': 'order_id and payment_method_id are required'})

        orders = data['orders']
        users = data['users']

        order = next((o for o in orders if o['order_id'] == order_id), None)
        if not order:
            return json.dumps({'error': 'Order not found'})

        # Calculate the current total of items in the order
        current_total = sum(item['price'] for item in order['items'])

        # Calculate the total amount already paid
        paid_amount = 0.0
        if 'payment_history' in order:
            for transaction in order['payment_history']:
                if transaction.get('transaction_type') == 'payment' or transaction.get('transaction_type') == 'partial_payment':
                    paid_amount += transaction.get('amount', 0.0)
                elif transaction.get('transaction_type') == 'refund':
                    paid_amount += transaction.get('amount', 0.0)  # refund amounts are negative
                elif transaction.get('transaction_type') == 'charge':
                    paid_amount += transaction.get('amount', 0.0)

        # Calculate the difference
        payment_difference = current_total - paid_amount

        # Get the user and validate payment method
        user = next((u for u in users if u['user_id'] == order['user_id']), None)
        if not user:
            return json.dumps({'error': 'User not found for this order'})

        if payment_method_id not in user.get('payment_methods', {}):
            return json.dumps({'error': 'Payment method not found for this user'})

        # Initialize payment_history if it doesn't exist
        if 'payment_history' not in order:
            order['payment_history'] = []

        transaction_type = None
        amount = 0.0
        message = ""

        if abs(payment_difference) < 0.01:  # Essentially equal (accounting for floating point precision)
            message = f"Order total ({current_total:.2f}) matches paid amount ({paid_amount:.2f}). No adjustment needed."
            return json.dumps({
                'success': True,
                'order_id': order_id,
                'current_total': current_total,
                'paid_amount': paid_amount,
                'payment_difference': payment_difference,
                'action': 'no_action_needed',
                'message': message
            }, indent=2)

        elif payment_difference < 0:  # Paid more than total, need refund
            refund_amount = abs(payment_difference)
            transaction_type = 'refund'
            amount = -refund_amount  # Negative for refund
            message = f"Refund of ${refund_amount:.2f} processed to payment method {payment_method_id}"

        else:  # payment_difference > 0, need to charge more
            charge_amount = payment_difference
            transaction_type = 'charge'
            amount = charge_amount  # Positive for additional charge
            order['status'] = 'processing'
            message = f"Additional charge of ${charge_amount:.2f} processed to payment method {payment_method_id}"

        # Create the transaction record
        transaction = {
            "transaction_type": transaction_type,
            "amount": amount,
            "payment_method_id": payment_method_id,
            "reason": "Order total adjustment",
            "timestamp": get_current_timestamp()
        }

        # Add the transaction to payment history
        order['payment_history'].append(transaction)

        return json.dumps({
            'success': True,
            'order_id': order_id,
            'current_total': current_total,
            'paid_amount': paid_amount,
            'payment_difference': payment_difference,
            'action': transaction_type,
            'transaction_amount': amount,
            'payment_method_id': payment_method_id,
            'message': message
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'adjust_order_payment',
                'description': 'Automatically adjusts payment for an order by comparing current order total with paid amount. Creates refund if overpaid or charges additional amount if underpaid.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'string', 'description': 'Order ID to adjust payment for'},
                        'payment_method_id': {'type': 'string', 'description': 'Payment method ID to use for refund or additional charge'}
                    },
                    'required': ['order_id', 'payment_method_id']
                }
            }
        }
