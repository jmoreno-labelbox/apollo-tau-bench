from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
from . import load_json

class ApplyPartialRefundToTransaction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str = None, refund_amount: float = None) -> str:
        if not transaction_id or refund_amount is None:
            return json.dumps({'error': 'transaction_id and refund_amount are required'})
        transactions = load_json('transactions.json')
        accounts = load_json('accounts.json')
        txn = next((t for t in transactions.values() if t['transaction_id'] == transaction_id), None)
        if not txn or 'account_id' not in txn or 'amount' not in txn or 'status' not in txn:
            return json.dumps({'error': 'Transaction not found or missing required fields.'})
        if txn['status'] != 'Completed' or txn['amount'] >= 0:
            return json.dumps({'error': 'Refund only allowed for completed debit transactions.'})
        acct = next((a for a in accounts.values() if a['account_id'] == txn['account_id'] and 'balance' in a), None)
        if not acct:
            return json.dumps({'error': 'Account not found or missing balance.'})
        if abs(refund_amount) > abs(txn['amount']):
            return json.dumps({'error': 'Refund amount exceeds original transaction.'})
        acct['balance'] += refund_amount
        refund_txn = {
            'transaction_id': f'txn_{generate_unique_id()}',
            'account_id': txn['account_id'],
            'transaction_date': get_current_timestamp(),
            'amount': refund_amount,
            'currency': acct['currency'],
            'transaction_type': 'Refund',
            'description': f'Partial refund for {transaction_id}',
            'merchant_name': None,
            'status': 'Completed',
            'channel': 'Online'
        }
        data["transactions"][transaction_id] = refund_txn
        return json.dumps({'success': True, 'refund_transaction': refund_txn})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'applyPartialRefundToTransaction',
                'description': 'Issues a partial refund to the account for a completed transaction.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'transaction_id': {'type': 'string', 'description': 'Original Transaction ID'},
                        'refund_amount': {'type': 'number', 'description': 'Refund amount'}
                    },
                    'required': ['transaction_id', 'refund_amount']
                }
            }
        }
