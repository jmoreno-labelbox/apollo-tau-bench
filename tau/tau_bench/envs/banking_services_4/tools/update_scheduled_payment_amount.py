# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateScheduledPaymentAmount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        payment_id = kwargs.get('payment_id')
        new_amount = kwargs.get('amount')
        if not payment_id or new_amount is None:
            return json.dumps({'error': 'payment_id and amount are required'})
        payments = load_json('scheduled_payments.json')
        updated = False
        for p in payments:
            if p['payment_id'] == payment_id:
                if 'amount' not in p:
                    return json.dumps({'error': 'Scheduled payment update not supported: no amount field in data.'})
                p['amount'] = new_amount
                updated = True
        if not updated:
            return json.dumps({'error': 'Scheduled payment not found or update not supported.'})
        return json.dumps({'success': True, 'payment_id': payment_id, 'amount': new_amount})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_scheduled_payment_amount',
                'description': 'Modifies the amount of a scheduled payment by ID (only if amount field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'payment_id': {'type': 'string', 'description': 'Scheduled Payment ID'},
                        'amount': {'type': 'number', 'description': 'New payment amount'}
                    },
                    'required': ['payment_id', 'amount']
                }
            }
        }
