from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
class UpdateScheduledPaymentAmount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str = None, amount: float = None) -> str:
        if not payment_id or amount is None:
            return json.dumps({'error': 'payment_id and amount are required'})
        payments = load_json('scheduled_payments.json')
        payments = _convert_db_to_list(payments)
        updated = False
        for p in payments:
            if p['payment_id'] == payment_id:
                if 'amount' not in p:
                    return json.dumps({'error': 'Scheduled payment update not supported: no amount field in data.'})
                p['amount'] = amount
                updated = True
        if not updated:
            return json.dumps({'error': 'Scheduled payment not found or update not supported.'})
        return json.dumps({'success': True, 'payment_id': payment_id, 'amount': amount})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'updateScheduledPaymentAmount',
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