from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class InitiateFundTransferToBeneficiary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_account_id: str = None, beneficiary_id: str = None, amount: float = None, description: str = None) -> str:
        if not source_account_id or not beneficiary_id or amount is None:
            return json.dumps({'error': 'source_account_id, beneficiary_id, and amount are required'})
        accounts = load_json('accounts.json')
        beneficiaries = load_json('beneficiaries.json')
        transactions = load_json('transactions.json')
        # Find source account
        src = next((a for a in accounts if a['account_id'] == source_account_id and a['status'] == 'Active'), None)
        if not src or 'balance' not in src:
            return json.dumps({'error': 'Source account not found or not active, or missing balance field.'})
        # Find beneficiary
        bene = next((b for b in beneficiaries if b['beneficiary_id'] == beneficiary_id), None)
        if not bene or 'account_details' not in bene:
            return json.dumps({'error': 'Beneficiary not found or missing account_details.'})
        if src['balance'] < amount:
            return json.dumps({'error': 'Insufficient funds.'})
        src['balance'] -= amount
        txn = {
            'transaction_id': f'txn_{generate_unique_id()}',
            'account_id': source_account_id,
            'transaction_date': get_current_timestamp(),
            'amount': -amount,
            'currency': src['currency'],
            'transaction_type': 'Transfer',
            'description': f'Transfer to beneficiary {bene["beneficiary_name"]}',
            'merchant_name': None,
            'status': 'Completed',
            'channel': 'Online'
        }
        transactions.append(txn)
        return json.dumps({'success': True, 'transaction': txn})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'initiateFundTransferToBeneficiary',
                'description': 'Starts a one-time transfer to a saved beneficiary from a given account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'source_account_id': {'type': 'string', 'description': 'Source Account ID'},
                        'beneficiary_id': {'type': 'string', 'description': 'Beneficiary ID'},
                        'amount': {'type': 'number', 'description': 'Transfer amount'}
                    },
                    'required': ['source_account_id', 'beneficiary_id', 'amount']
                }
            }
        }
