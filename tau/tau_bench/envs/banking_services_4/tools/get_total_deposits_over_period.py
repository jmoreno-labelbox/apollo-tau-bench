# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalDepositsOverPeriod(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_ids = kwargs.get('account_ids')
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        if not account_ids or not start_date or not end_date:
            return json.dumps({'error': 'account_ids, start_date, and end_date are required'})
        transactions = load_json('transactions.json')
        total = 0.0
        for t in transactions:
            if t['account_id'] in account_ids and t['transaction_type'] == 'Deposit':
                t_date = t['transaction_date'][:10]
                if start_date <= t_date <= end_date:
                    total += t['amount']
        return json.dumps({'total_deposits': total}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_total_deposits_over_period',
                'description': 'Sums all deposit-type transactions for a given date range.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of account IDs'},
                        'start_date': {'type': 'string', 'description': 'Start date (YYYY-MM-DD)'},
                        'end_date': {'type': 'string', 'description': 'End date (YYYY-MM-DD)'}
                    },
                    'required': ['account_ids', 'start_date', 'end_date']
                }
            }
        }
