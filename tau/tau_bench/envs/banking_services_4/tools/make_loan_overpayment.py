from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class MakeLoanOverpayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, from_account_id: str = None, amount: float = None) -> str:
        if not loan_id or not from_account_id or amount is None:
            return json.dumps({'error': 'loan_id, from_account_id, and amount are required'})
        loans = load_json('loans.json')
        accounts = load_json('accounts.json')
        transactions = load_json('transactions.json')
        loan = next((l for l in loans.values() if l['loan_id'] == loan_id), None)
        acct = next((a for a in accounts.values() if a['account_id'] == from_account_id and a['status'] == 'Active'), None)
        if not loan or 'current_balance' not in loan:
            return json.dumps({'error': 'Loan not found or missing current_balance.'})
        if not acct or 'balance' not in acct:
            return json.dumps({'error': 'Account not found or missing balance.'})
        if acct['balance'] < amount:
            return json.dumps({'error': 'Insufficient funds.'})
        acct['balance'] -= amount
        loan['current_balance'] = max(0, loan['current_balance'] - amount)
        txn = {
            'transaction_id': f'txn_{generate_unique_id()}',
            'account_id': from_account_id,
            'transaction_date': get_current_timestamp(),
            'amount': -amount,
            'currency': acct['currency'],
            'transaction_type': 'Loan Overpayment',
            'description': f'Overpayment to loan {loan_id}',
            'merchant_name': None,
            'status': 'Completed',
            'channel': 'Online'
        }
        transactions.append(txn)
        return json.dumps({'success': True, 'transaction': txn, 'loan_id': loan_id, 'new_balance': loan['current_balance']})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'makeLoanOverpayment',
                'description': 'Applies an additional payment to a loan outside the regular schedule.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'loan_id': {'type': 'string', 'description': 'Loan ID'},
                        'from_account_id': {'type': 'string', 'description': 'Account to debit'},
                        'amount': {'type': 'number', 'description': 'Overpayment amount'}
                    },
                    'required': ['loan_id', 'from_account_id', 'amount']
                }
            }
        }
