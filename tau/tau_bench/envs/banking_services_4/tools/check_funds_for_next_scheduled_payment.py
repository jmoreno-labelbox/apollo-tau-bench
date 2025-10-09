from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class CheckFundsForNextScheduledPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str = None) -> str:
        if not payment_id:
            return json.dumps({'error': 'payment_id is required'})

        payments = load_json('scheduled_payments.json')
        payment = next((p for p in payments.values() if p['payment_id'] == payment_id), None)
        if not payment:
            return json.dumps({'error': 'Scheduled payment not found.'})

        accounts = load_json('accounts.json')
        source_account = next((a for a in accounts.values() if a['account_id'] == payment['source_account_id']), None)
        if not source_account:
            return json.dumps({'error': 'Source account for payment not found.'})

        payment_amount = payment['amount']
        account_balance = source_account['balance']
        sufficient_funds = account_balance >= payment_amount

        return json.dumps({
            'payment_id': payment_id,
            'next_payment_date': payment.get('next_payment_date'),
            'payment_amount': payment_amount,
            'account_balance': account_balance,
            'sufficient_funds': sufficient_funds
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'checkFundsForNextScheduledPayment',
                'description': 'Checks if the source account has enough funds for the next scheduled payment.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'payment_id': {'type': 'string', 'description': 'The ID of the scheduled payment to check.'}
                    },
                    'required': ['payment_id']
                }
            }
        }
